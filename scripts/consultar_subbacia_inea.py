#!/usr/bin/env python3
"""Consulta uma camada ArcGIS por nome e preserva respostas, parâmetros e hashes."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DEFAULT_LAYER_URL = (
    "https://geoportal.inea.rj.gov.br/server/rest/services/"
    "Recursos_Hidricos_Gestao_Costeira/MapServer/4/query"
)
VERSION = "0.3.0"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def normalized(value: object) -> str:
    text = unicodedata.normalize("NFKD", str(value)).encode("ascii", "ignore").decode("ascii")
    return " ".join(text.casefold().split())


def display_url(base_url: str, params: dict[str, str]) -> str:
    return f"{base_url}?{urllib.parse.urlencode(params)}"


def post(
    base_url: str,
    params: dict[str, str],
    timeout: float,
    retries: int,
) -> tuple[bytes, dict[str, str], int, int]:
    body = urllib.parse.urlencode(params).encode("utf-8")
    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        request = urllib.request.Request(
            base_url,
            data=body,
            method="POST",
            headers={
                "User-Agent": "pragmatismo-civico-geodata/0.3",
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept": "application/json, application/geo+json",
            },
        )
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return response.read(), dict(response.headers.items()), int(response.status), attempt
        except (TimeoutError, urllib.error.URLError, urllib.error.HTTPError) as error:
            last_error = error
            if attempt < retries:
                time.sleep(min(2 ** (attempt - 1), 8))
    assert last_error is not None
    raise last_error


def parse_json_object(raw: bytes, label: str) -> dict[str, Any]:
    payload = json.loads(raw.decode("utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"{label}: resposta JSON raiz não é objeto.")
    if "error" in payload:
        raise ValueError(f"{label}: serviço ArcGIS retornou erro: {payload['error']}")
    return payload


def select_matches(payload: dict[str, Any], name: str) -> tuple[list[int], list[str]]:
    features = payload.get("features")
    if not isinstance(features, list):
        raise ValueError("Consulta de atributos sem lista de feições.")
    token = normalized(name)
    ids: list[int] = []
    names: list[str] = []
    for feature in features:
        if not isinstance(feature, dict) or not isinstance(feature.get("attributes"), dict):
            continue
        attributes = feature["attributes"]
        candidate = attributes.get("sub_bacias")
        object_id = attributes.get("objectid")
        if candidate is None or object_id is None:
            continue
        if token in normalized(candidate):
            ids.append(int(object_id))
            names.append(str(candidate))
    return sorted(set(ids)), sorted(set(names))


def validate_geojson(raw: bytes) -> dict[str, Any]:
    payload = parse_json_object(raw, "Consulta de geometria")
    if payload.get("type") != "FeatureCollection" or not isinstance(payload.get("features"), list):
        raise ValueError("Consulta de geometria não retornou FeatureCollection GeoJSON.")
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", default="Itapeba")
    parser.add_argument("--layer-url", default=DEFAULT_LAYER_URL)
    parser.add_argument("--out-sr", type=int, default=4674)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--timeout", type=float, default=90.0)
    parser.add_argument("--retries", type=int, default=3)
    args = parser.parse_args()

    if args.retries < 1:
        parser.error("--retries deve ser maior ou igual a 1")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    index_path = output_dir / "index-response.json"
    raw_path = output_dir / "response.geojson"
    manifest_path = output_dir / "query-manifest.json"
    report_path = output_dir / "query-report.md"
    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()

    index_params = {
        "where": "1=1",
        "outFields": "objectid,sub_bacias",
        "returnGeometry": "false",
        "resultRecordCount": "2000",
        "f": "json",
    }

    try:
        index_raw, index_headers, index_status, index_attempts = post(
            args.layer_url, index_params, args.timeout, args.retries
        )
        index_path.write_bytes(index_raw)
        index_payload = parse_json_object(index_raw, "Consulta de atributos")
        object_ids, names = select_matches(index_payload, args.name)

        geometry_params: dict[str, str] | None = None
        geometry_status: int | None = None
        geometry_attempts = 0
        geometry_headers: dict[str, str] = {}
        if object_ids:
            geometry_params = {
                "objectIds": ",".join(str(value) for value in object_ids),
                "outFields": "*",
                "returnGeometry": "true",
                "outSR": str(args.out_sr),
                "f": "geojson",
            }
            raw, geometry_headers, geometry_status, geometry_attempts = post(
                args.layer_url, geometry_params, args.timeout, args.retries
            )
            payload = validate_geojson(raw)
            if len(payload["features"]) != len(object_ids):
                raise ValueError("Quantidade de geometrias difere dos OBJECTID selecionados.")
            interpretation = "correspondencia_nominal_encontrada_revisao_pendente"
            response_origin = "geoinea"
        else:
            raw = json.dumps(
                {"type": "FeatureCollection", "features": []},
                ensure_ascii=False,
                separators=(",", ":"),
            ).encode("utf-8")
            interpretation = "consulta_sem_correspondencia_nominal"
            response_origin = "gerada_a_partir_de_indice_oficial_sem_correspondencia"
        raw_path.write_bytes(raw)

        manifest = {
            "tool": {"name": "consultar_subbacia_inea.py", "version": VERSION},
            "generated_at_utc": generated_at,
            "name": args.name,
            "layer_url": args.layer_url,
            "out_sr": args.out_sr,
            "index_query": {
                "method": "POST",
                "display_url": display_url(args.layer_url, index_params),
                "parameters": index_params,
                "http_status": index_status,
                "content_type": index_headers.get("Content-Type"),
                "attempts_used": index_attempts,
                "path": index_path.name,
                "sha256": sha256_bytes(index_raw),
                "size_bytes": len(index_raw),
            },
            "selection": {
                "normalization": "NFKD, ASCII, casefold, whitespace",
                "object_ids": object_ids,
                "matched_names": names,
                "match_count": len(object_ids),
            },
            "geometry_query": (
                {
                    "method": "POST",
                    "display_url": display_url(args.layer_url, geometry_params),
                    "parameters": geometry_params,
                    "http_status": geometry_status,
                    "content_type": geometry_headers.get("Content-Type"),
                    "attempts_used": geometry_attempts,
                }
                if geometry_params
                else None
            ),
            "response": {
                "path": raw_path.name,
                "origin": response_origin,
                "sha256": sha256_bytes(raw),
                "size_bytes": len(raw),
                "feature_count": len(object_ids),
                "empty": len(object_ids) == 0,
            },
            "interpretation": interpretation,
            "limitations": [
                "Correspondência nominal não comprova equivalência temática ou oficialidade para o caso.",
                "Resposta vazia não comprova inexistência territorial; comprova apenas o resultado desta consulta.",
                "A geometria encontrada exige validação automática e revisão técnica manual.",
            ],
        }
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        report_path.write_text(
            "\n".join(
                [
                    "# Relatório de consulta ao GeoINEA",
                    "",
                    f"- **Data UTC:** `{generated_at}`",
                    f"- **Nome consultado:** `{args.name}`",
                    f"- **Atributos indexados:** {len(index_payload.get('features', []))}",
                    f"- **Correspondências:** {len(object_ids)}",
                    f"- **Nomes retornados:** {', '.join(names) if names else '—'}",
                    f"- **OBJECTID:** {', '.join(map(str, object_ids)) if object_ids else '—'}",
                    f"- **SHA-256 do índice:** `{manifest['index_query']['sha256']}`",
                    f"- **SHA-256 do GeoJSON:** `{manifest['response']['sha256']}`",
                    f"- **Interpretação:** `{interpretation}`",
                    "",
                    "A resposta deve ser preservada mesmo quando vazia. Qualquer feição encontrada permanece pendente de validação e revisão manual.",
                    "",
                ]
            ),
            encoding="utf-8",
        )
        print(json.dumps(manifest["response"], ensure_ascii=False))
        return 0
    except Exception as error:
        failure = {
            "tool": {"name": "consultar_subbacia_inea.py", "version": VERSION},
            "generated_at_utc": generated_at,
            "name": args.name,
            "layer_url": args.layer_url,
            "index_parameters": index_params,
            "timeout_seconds": args.timeout,
            "max_attempts": args.retries,
            "error": f"{type(error).__name__}: {error}",
        }
        manifest_path.write_text(json.dumps(failure, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        report_path.write_text(f"# Falha na consulta ao GeoINEA\n\n- **Erro:** `{failure['error']}`\n", encoding="utf-8")
        print(f"ERRO: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
