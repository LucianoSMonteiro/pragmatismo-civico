#!/usr/bin/env python3
"""Consulta a camada de sub-bacias do GeoINEA e preserva a resposta auditável.

A coleta separa quatro fatos:

1. disponibilidade e metadados do serviço;
2. universo de identificadores da camada;
3. atributos consultados e correspondências nominais;
4. geometria retornada, quando houver correspondência.

Uma consulta concluída sem correspondência é um resultado válido. O script não
amplia o filtro, não digitaliza limites e não afirma adequação temática.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import unicodedata
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

SERVICE_ROOT = (
    "https://geoportal.inea.rj.gov.br/server/rest/services/"
    "Recursos_Hidricos_Gestao_Costeira/MapServer/4"
)
VERSION = "0.1.0"
USER_AGENT = "Pragmatismo-Civico-GeoINEA/0.1 (+https://github.com/LucianoSMonteiro/pragmatismo-civico)"


@dataclass(frozen=True)
class ResponseRecord:
    url: str
    body: bytes
    content_type: str | None
    status: int


class CollectionError(RuntimeError):
    """Falha controlada de consulta ou resposta."""


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def normalize_text(value: Any) -> str:
    text = unicodedata.normalize("NFKD", str(value or ""))
    return "".join(character for character in text if not unicodedata.combining(character)).casefold().strip()


def select_matches(features: Iterable[dict[str, Any]], search_term: str) -> list[dict[str, Any]]:
    token = normalize_text(search_term)
    if not token:
        raise ValueError("O termo de busca não pode ser vazio.")

    matches: list[dict[str, Any]] = []
    for feature in features:
        attributes = feature.get("attributes") or {}
        if not isinstance(attributes, dict):
            continue
        if token in normalize_text(attributes.get("sub_bacias")):
            matches.append(feature)
    return matches


def build_url(base_url: str, params: dict[str, Any]) -> str:
    return f"{base_url}?{urlencode(params, doseq=True)}"


def default_fetch(url: str, timeout: int) -> ResponseRecord:
    request = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json, application/geo+json"})
    try:
        with urlopen(request, timeout=timeout) as response:
            return ResponseRecord(
                url=response.geturl(),
                body=response.read(),
                content_type=response.headers.get("Content-Type"),
                status=int(response.status),
            )
    except HTTPError as error:
        body = error.read() if hasattr(error, "read") else b""
        raise CollectionError(f"HTTP {error.code} em {url}: {body[:500]!r}") from error
    except URLError as error:
        raise CollectionError(f"Falha de rede em {url}: {error.reason}") from error


def decode_json(record: ResponseRecord, label: str) -> dict[str, Any]:
    try:
        payload = json.loads(record.body.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise CollectionError(f"Resposta inválida em {label}: não é JSON UTF-8.") from error
    if not isinstance(payload, dict):
        raise CollectionError(f"Resposta inválida em {label}: raiz não é objeto.")
    if "error" in payload:
        raise CollectionError(f"Erro ArcGIS em {label}: {payload['error']}")
    return payload


def write_bytes(path: Path, body: bytes) -> dict[str, Any]:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(body)
    return {
        "path": path.name,
        "size_bytes": len(body),
        "sha256": sha256_bytes(body),
    }


def write_json(path: Path, payload: Any) -> dict[str, Any]:
    body = (json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")
    return write_bytes(path, body)


def chunked(values: list[int], size: int) -> Iterable[list[int]]:
    for start in range(0, len(values), size):
        yield values[start : start + size]


def collect(
    *,
    output_dir: Path,
    search_term: str,
    timeout: int,
    fetch: Callable[[str, int], ResponseRecord] = default_fetch,
) -> dict[str, Any]:
    output_dir.mkdir(parents=True, exist_ok=True)
    started_at = utc_now()
    requests_log: list[dict[str, Any]] = []
    files: dict[str, dict[str, Any]] = {}

    def request_json(label: str, url: str, filename: str) -> dict[str, Any]:
        record = fetch(url, timeout)
        payload = decode_json(record, label)
        file_info = write_bytes(output_dir / filename, record.body)
        files[label] = file_info
        requests_log.append(
            {
                "label": label,
                "url": record.url,
                "status": record.status,
                "content_type": record.content_type,
                **file_info,
            }
        )
        return payload

    metadata_url = build_url(SERVICE_ROOT, {"f": "pjson"})
    metadata = request_json("layer_metadata", metadata_url, "layer-metadata.raw.json")

    geometry_type = metadata.get("geometryType")
    spatial_reference = (metadata.get("extent") or {}).get("spatialReference") or {}
    wkid = spatial_reference.get("latestWkid") or spatial_reference.get("wkid")
    if geometry_type != "esriGeometryPolygon":
        raise CollectionError(f"Tipo geométrico inesperado: {geometry_type!r}.")
    if int(wkid or 0) != 4674:
        raise CollectionError(f"Referência espacial inesperada: {wkid!r}.")

    ids_url = build_url(
        f"{SERVICE_ROOT}/query",
        {"where": "1=1", "returnIdsOnly": "true", "f": "pjson"},
    )
    ids_payload = request_json("object_ids", ids_url, "object-ids.raw.json")
    object_ids_raw = ids_payload.get("objectIds") or []
    if not isinstance(object_ids_raw, list):
        raise CollectionError("A resposta de IDs não contém lista válida.")
    object_ids = sorted({int(value) for value in object_ids_raw})

    all_features: list[dict[str, Any]] = []
    attribute_requests: list[str] = []
    for index, identifiers in enumerate(chunked(object_ids, 500), start=1):
        attributes_url = build_url(
            f"{SERVICE_ROOT}/query",
            {
                "objectIds": ",".join(str(value) for value in identifiers),
                "outFields": "objectid,sub_bacias,rh",
                "returnGeometry": "false",
                "orderByFields": "sub_bacias",
                "f": "pjson",
            },
        )
        label = f"attributes_{index:03d}"
        payload = request_json(label, attributes_url, f"attributes-{index:03d}.raw.json")
        attribute_requests.append(attributes_url)
        features = payload.get("features") or []
        if not isinstance(features, list):
            raise CollectionError(f"Lote {index} sem lista válida de feições.")
        all_features.extend(feature for feature in features if isinstance(feature, dict))

    files["attributes_combined"] = write_json(
        output_dir / "attributes-combined.json",
        {
            "objectIdFieldName": ids_payload.get("objectIdFieldName"),
            "features": all_features,
        },
    )

    matches = select_matches(all_features, search_term)
    match_attributes = [feature.get("attributes") or {} for feature in matches]
    files["matches"] = write_json(
        output_dir / "matches.json",
        {
            "search_term": search_term,
            "normalized_search_term": normalize_text(search_term),
            "match_count": len(matches),
            "features": match_attributes,
        },
    )

    geometry_file: dict[str, Any] | None = None
    geometry_url: str | None = None
    matched_ids = sorted(
        {
            int((feature.get("attributes") or {}).get("objectid"))
            for feature in matches
            if (feature.get("attributes") or {}).get("objectid") is not None
        }
    )

    if matched_ids:
        geometry_url = build_url(
            f"{SERVICE_ROOT}/query",
            {
                "objectIds": ",".join(str(value) for value in matched_ids),
                "outFields": "*",
                "returnGeometry": "true",
                "outSR": "4674",
                "f": "geojson",
            },
        )
        record = fetch(geometry_url, timeout)
        geojson = decode_json(record, "matched_geometry")
        if geojson.get("type") != "FeatureCollection":
            raise CollectionError("A resposta geométrica não é FeatureCollection GeoJSON.")
        geometry_file = write_bytes(output_dir / "matched-geometry.geojson", record.body)
        files["matched_geometry"] = geometry_file
        requests_log.append(
            {
                "label": "matched_geometry",
                "url": record.url,
                "status": record.status,
                "content_type": record.content_type,
                **geometry_file,
            }
        )

    completed_at = utc_now()
    manifest = {
        "collector": {"name": "coletar_geoinea_subbacia.py", "version": VERSION},
        "started_at_utc": started_at,
        "completed_at_utc": completed_at,
        "service": {
            "layer_url": SERVICE_ROOT,
            "service_item_id": metadata.get("serviceItemId"),
            "layer_name": metadata.get("name"),
            "display_field": metadata.get("displayField"),
            "geometry_type": geometry_type,
            "spatial_reference_wkid": wkid,
            "max_record_count": metadata.get("maxRecordCount"),
        },
        "query": {
            "search_term": search_term,
            "normalized_search_term": normalize_text(search_term),
            "strategy": "listar todos os objectIds, consultar atributos em lotes e filtrar localmente",
            "metadata_url": metadata_url,
            "ids_url": ids_url,
            "attribute_urls": attribute_requests,
            "geometry_url": geometry_url,
        },
        "result": {
            "query_completed": True,
            "object_id_count": len(object_ids),
            "attribute_feature_count": len(all_features),
            "match_count": len(matches),
            "matched_object_ids": matched_ids,
            "geometry_downloaded": geometry_file is not None,
        },
        "requests": requests_log,
        "files": files,
        "limitations": [
            "Correspondência nominal não comprova equivalência temática com o recorte municipal.",
            "Ausência de correspondência nominal não comprova ausência física da sub-bacia.",
            "A coleta não amplia o filtro, não deriva divisor hidrográfico e não substitui revisão técnica.",
            "A oficialidade e as condições de uso dependem dos metadados e do órgão produtor.",
        ],
    }
    write_json(output_dir / "query-manifest.json", manifest)

    report_lines = [
        "# Consulta GeoINEA — sub-bacia de Itapeba",
        "",
        f"- **Resultado técnico:** consulta concluída",
        f"- **Termo:** `{search_term}`",
        f"- **Objetos na camada:** {len(object_ids)}",
        f"- **Feições com atributos:** {len(all_features)}",
        f"- **Correspondências nominais:** {len(matches)}",
        f"- **Geometria baixada:** {'sim' if geometry_file else 'não'}",
        f"- **Referência espacial publicada:** EPSG:{wkid}",
        "",
    ]
    if matches:
        report_lines.extend(["## Correspondências", ""])
        for attributes in match_attributes:
            report_lines.append(
                f"- objectid `{attributes.get('objectid')}` — "
                f"`{attributes.get('sub_bacias')}` — RH `{attributes.get('rh')}`"
            )
    else:
        report_lines.extend(
            [
                "## Resultado nominal",
                "",
                "Nenhuma feição contém o termo normalizado `itapeba` no campo `sub_bacias`.",
                "",
                "Isso não autoriza concluir que a sub-bacia não exista. Pode haver diferença de nomenclatura, escala ou classificação institucional.",
            ]
        )
    report_lines.extend(
        [
            "",
            "## Limites",
            "",
            *[f"- {item}" for item in manifest["limitations"]],
            "",
        ]
    )
    (output_dir / "query-report.md").write_text("\n".join(report_lines), encoding="utf-8")
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default="geoinea-result")
    parser.add_argument("--search-term", default="Itapeba")
    parser.add_argument("--timeout", type=int, default=60)
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    try:
        manifest = collect(
            output_dir=output_dir,
            search_term=args.search_term,
            timeout=args.timeout,
        )
    except (CollectionError, OSError, ValueError) as error:
        output_dir.mkdir(parents=True, exist_ok=True)
        failure = {
            "collector": {"name": "coletar_geoinea_subbacia.py", "version": VERSION},
            "completed_at_utc": utc_now(),
            "query_completed": False,
            "error": str(error),
        }
        write_json(output_dir / "query-failure.json", failure)
        print(f"ERRO: {error}", file=sys.stderr)
        return 1

    result = manifest["result"]
    print(
        "Consulta concluída: "
        f"{result['object_id_count']} objeto(s), "
        f"{result['match_count']} correspondência(s) nominal(is), "
        f"geometria={'sim' if result['geometry_downloaded'] else 'não'}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
