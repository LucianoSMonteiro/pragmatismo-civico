#!/usr/bin/env python3
"""Consulta uma camada ArcGIS por nome e preserva resposta, parâmetros e hash."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DEFAULT_LAYER_URL = (
    "https://geoportal.inea.rj.gov.br/server/rest/services/"
    "Recursos_Hidricos_Gestao_Costeira/MapServer/4/query"
)
VERSION = "0.1.0"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def build_query_url(base_url: str, name: str, out_sr: int) -> str:
    params = {
        "where": f"UPPER(sub_bacias) LIKE '%{name.upper().replace("'", "''")}%'",
        "outFields": "*",
        "returnGeometry": "true",
        "outSR": str(out_sr),
        "f": "geojson",
    }
    return f"{base_url}?{urllib.parse.urlencode(params)}"


def fetch(url: str, timeout: float) -> tuple[bytes, dict[str, str], int]:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "pragmatismo-civico-geodata/0.1"},
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read(), dict(response.headers.items()), int(response.status)


def validate_payload(raw: bytes) -> dict[str, Any]:
    payload = json.loads(raw.decode("utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("Resposta JSON raiz não é objeto.")
    if "error" in payload:
        raise ValueError(f"Serviço ArcGIS retornou erro: {payload['error']}")
    if payload.get("type") != "FeatureCollection":
        raise ValueError("Resposta não é FeatureCollection GeoJSON.")
    features = payload.get("features")
    if not isinstance(features, list):
        raise ValueError("FeatureCollection sem lista de feições.")
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", default="Itapeba")
    parser.add_argument("--layer-url", default=DEFAULT_LAYER_URL)
    parser.add_argument("--out-sr", type=int, default=4674)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--timeout", type=float, default=45.0)
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    raw_path = output_dir / "response.geojson"
    manifest_path = output_dir / "query-manifest.json"
    report_path = output_dir / "query-report.md"

    query_url = build_query_url(args.layer_url, args.name, args.out_sr)
    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()

    try:
        raw, headers, status = fetch(query_url, args.timeout)
        raw_path.write_bytes(raw)
        payload = validate_payload(raw)
        features = payload["features"]
        names = sorted(
            {
                str(feature.get("properties", {}).get("sub_bacias"))
                for feature in features
                if isinstance(feature, dict)
                and isinstance(feature.get("properties"), dict)
                and feature["properties"].get("sub_bacias") is not None
            }
        )
        manifest = {
            "tool": {"name": "consultar_subbacia_inea.py", "version": VERSION},
            "generated_at_utc": generated_at,
            "query": {
                "layer_url": args.layer_url,
                "url": query_url,
                "name": args.name,
                "out_sr": args.out_sr,
            },
            "http": {
                "status": status,
                "content_type": headers.get("Content-Type"),
                "etag": headers.get("ETag"),
                "last_modified": headers.get("Last-Modified"),
            },
            "response": {
                "path": raw_path.name,
                "sha256": sha256_bytes(raw),
                "size_bytes": len(raw),
                "feature_count": len(features),
                "matched_names": names,
                "empty": len(features) == 0,
            },
            "interpretation": (
                "consulta_sem_correspondencia_nominal"
                if not features
                else "correspondencia_nominal_encontrada_revisao_pendente"
            ),
            "limitations": [
                "Correspondência nominal não comprova equivalência temática ou oficialidade para o caso.",
                "Resposta vazia não comprova inexistência territorial; comprova apenas o resultado desta consulta.",
                "A geometria encontrada exige validação automática e revisão técnica manual.",
            ],
        }
        manifest_path.write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        report_path.write_text(
            "\n".join(
                [
                    "# Relatório de consulta ao GeoINEA",
                    "",
                    f"- **Data UTC:** `{generated_at}`",
                    f"- **Nome consultado:** `{args.name}`",
                    f"- **HTTP:** `{status}`",
                    f"- **Feições:** {len(features)}",
                    f"- **Nomes retornados:** {', '.join(names) if names else '—'}",
                    f"- **SHA-256:** `{manifest['response']['sha256']}`",
                    f"- **Interpretação:** `{manifest['interpretation']}`",
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
            "query": {"url": query_url, "name": args.name, "out_sr": args.out_sr},
            "error": f"{type(error).__name__}: {error}",
        }
        manifest_path.write_text(
            json.dumps(failure, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        report_path.write_text(
            f"# Falha na consulta ao GeoINEA\n\n- **Erro:** `{failure['error']}`\n",
            encoding="utf-8",
        )
        print(f"ERRO: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
