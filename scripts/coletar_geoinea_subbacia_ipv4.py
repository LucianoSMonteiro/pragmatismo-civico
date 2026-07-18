#!/usr/bin/env python3
"""Executa o coletor GeoINEA forçando transporte IPv4 via curl."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from coletar_geoinea_subbacia import CollectionError, collect
from geoinea_ipv4_transport import curl_ipv4_fetch


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
            fetch=curl_ipv4_fetch,
        )
    except (CollectionError, OSError, ValueError) as error:
        print(f"ERRO: {error}", file=sys.stderr)
        return 1

    result = manifest["result"]
    print(
        "Consulta IPv4 concluída: "
        f"{result['object_id_count']} objeto(s), "
        f"{result['match_count']} correspondência(s) nominal(is), "
        f"geometria={'sim' if result['geometry_downloaded'] else 'não'}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
