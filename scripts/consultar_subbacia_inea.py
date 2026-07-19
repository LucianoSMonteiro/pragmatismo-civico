#!/usr/bin/env python3
"""Consulta uma camada ArcGIS por nome e preserva resposta, parâmetros e hash."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
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
VERSION = "0.2.0"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def build_query_params(name: str, out_sr: int) -> dict[str, str]:
    escaped_name = name.upper().replace("'", "''")
    return {
        "where": f"UPPER(sub_bacias) LIKE '%{escaped_name}%'",
        "outFields": "*",
        "returnGeometry": "true",
        "outSR": str(out_sr),
        "f": "geojson",
    }


def build_query_url(base_url: str, params: dict[str, str]) -> str:
    return f"{base_url}?{urllib.parse.urlencode(params)}"


def fetch(
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
                "User-Agent": "pragmatismo-civico-geodata/0.2",
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept": "application/geo+json, application/json",
            },
        )
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return (
                    response.read(),
                    dict(response.headers.items()),
                    int(response.status),
                    attempt,
                )
        except (TimeoutError, urllib.error.URLError, urllib.error.HTTPError) as error:
            last_error = error
            if attempt < retries:
                time.sleep(min(2 ** (attempt - 1), 8))
    assert last_error is not None
    raise last_error


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
    parser.add_argument("--timeout", type=float, default=120.0)
    parser.add_argument("--retries", type=int, default=3)
    args = parser.parse_args()

    if args.retries < 1:
        parser.error("--retries deve ser maior ou igual a 1")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    raw_path = output_dir / "response.geojson"
    manifest_path = output_dir / "query-manifest.json"
    report_path = output_dir / "query-report.md"

    params = build_query_params(args.name, args.out_sr)
    query_url = build_query_url(args.layer_url, params)
    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()

    try:
        raw, headers, status, attempts = fetch(
            args.layer_url,
            params,
            args.timeout,
            args.retries,
        )
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
                "method": "POST",
                "layer_url": args.layer_url,
                "display_url": query_url,
                "parameters": params,
                "name": args.name,
                "out_sr": args.out_sr,
                "timeout_seconds": args.timeout,
                "max_attempts": args.retries,
                "attempts_used": attempts,
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
                    f"- **Método:** `POST`",
                    f"- **Tentativas usadas:** {attempts}",
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
            "query": {
                "method": "POST",
                "layer_url": args.layer_url,
                "display_url": query_url,
                "parameters": params,
                "name": args.name,
                "out_sr": args.out_sr,
                "timeout_seconds": args.timeout,
                "max_attempts": args.retries,
            },
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
