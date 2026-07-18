"""Normaliza e audita arquivos mensais de chuva do Cemaden.

O portal do Cemaden exige confirmação humana para baixar cada arquivo mensal.
Este script não automatiza nem contorna essa etapa. Ele processa arquivos já
obtidos, preserva proveniência e produz saídas reproduzíveis.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
import unicodedata
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from statistics import median
from zoneinfo import ZoneInfo

VERSION = "0.1.0"
LOCAL_TZ = ZoneInfo("America/Sao_Paulo")
DELIMITERS = ";,\t|"
ALIASES = {
    "timestamp": {
        "datahora", "data_hora", "data", "datetime", "timestamp", "horario",
        "datahorautc", "data_hora_utc", "dataobservacao", "data_medicao",
    },
    "rainfall": {
        "valor", "valormedida", "valor_medida", "chuva", "precipitacao",
        "precipitacaomm", "precipitacao_mm", "mm", "registro", "medida",
    },
    "station_name": {
        "nomeestacao", "nome_estacao", "estacao", "nome", "station",
        "station_name", "pcd",
    },
    "station_id": {
        "idestacao", "id_estacao", "idpcd", "id_pcd", "codigo",
        "codestacao", "cod_estacao", "station_id",
    },
    "municipality": {"cidade", "municipio", "municipality"},
    "state": {"uf", "estado", "state"},
}
DATE_FORMATS = (
    "%d/%m/%Y %H:%M:%S",
    "%d/%m/%Y %H:%M",
    "%Y-%m-%d %H:%M:%S",
    "%Y-%m-%d %H:%M",
    "%Y-%m-%dT%H:%M:%S",
    "%Y-%m-%dT%H:%M",
)


def token(value: str) -> str:
    text = unicodedata.normalize("NFKD", value or "")
    text = "".join(char for char in text if not unicodedata.combining(char))
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def decode(path: Path) -> tuple[str, str]:
    raw = path.read_bytes()
    for encoding in ("utf-8-sig", "utf-8", "latin-1"):
        try:
            return raw.decode(encoding), encoding
        except UnicodeDecodeError:
            pass
    raise ValueError(f"Não foi possível decodificar {path}")


def delimiter(text: str) -> str:
    try:
        return csv.Sniffer().sniff(text[:8192], delimiters=DELIMITERS).delimiter
    except csv.Error:
        return ";"


def column(fieldnames: list[str], semantic: str) -> str | None:
    normalized = {token(name): name for name in fieldnames if name}
    return next((normalized[alias] for alias in ALIASES[semantic] if alias in normalized), None)


def timestamp_utc(value: str) -> datetime:
    text = (value or "").strip()
    if not text:
        raise ValueError("data vazia")
    try:
        parsed = datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError:
        parsed = None
    if parsed is None:
        for fmt in DATE_FORMATS:
            try:
                parsed = datetime.strptime(text, fmt)
                break
            except ValueError:
                continue
    if parsed is None:
        raise ValueError(f"data inválida: {text}")
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def number(value: str) -> float:
    text = (value or "").strip().replace("\u00a0", "")
    if not text or token(text) in {"na", "n_a", "nd", "s_d", "nan", "null", "none", "sem_dado"}:
        raise ValueError("valor ausente")
    if "," in text and "." in text:
        text = text.replace(".", "").replace(",", ".") if text.rfind(",") > text.rfind(".") else text.replace(",", "")
    elif "," in text:
        text = text.replace(",", ".")
    return float(text)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def same(value: str, expected: str | None) -> bool:
    return expected is None or token(value) == token(expected)


def read_file(path: Path, args: argparse.Namespace) -> tuple[list[dict], dict, Counter]:
    text, encoding = decode(path)
    sep = delimiter(text)
    reader = csv.DictReader(text.splitlines(), delimiter=sep)
    fields = reader.fieldnames or []
    cols = {name: column(fields, name) for name in ALIASES}

    missing = []
    if not cols["timestamp"]:
        missing.append("data/hora")
    if not cols["rainfall"]:
        missing.append("precipitação")
    if args.station_name and not args.station_id and not cols["station_name"]:
        missing.append("nome da estação")
    if args.station_id and not args.station_name and not cols["station_id"]:
        missing.append("ID da estação")
    if args.station_name and args.station_id and not (cols["station_name"] or cols["station_id"]):
        missing.append("estação")
    if missing:
        raise ValueError(f"Colunas não reconhecidas em {path}: {', '.join(missing)}")

    summary = {
        "path": path.name,
        "sha256": sha256(path),
        "size_bytes": path.stat().st_size,
        "rows_read": 0,
        "rows_matched": 0,
        "encoding": encoding,
        "delimiter": sep,
    }
    counts = Counter()
    records: list[dict] = []

    for row_number, row in enumerate(reader, start=2):
        summary["rows_read"] += 1
        station_name = (row.get(cols["station_name"], "") if cols["station_name"] else "").strip()
        station_id = (row.get(cols["station_id"], "") if cols["station_id"] else "").strip()
        municipality = (row.get(cols["municipality"], "") if cols["municipality"] else "").strip()
        state = (row.get(cols["state"], "") if cols["state"] else "").strip()

        station_ok = True
        if args.station_name and args.station_id:
            station_ok = (
                (cols["station_name"] and same(station_name, args.station_name))
                or (cols["station_id"] and same(station_id, args.station_id))
            )
        elif args.station_name:
            station_ok = bool(cols["station_name"] and same(station_name, args.station_name))
        elif args.station_id:
            station_ok = bool(cols["station_id"] and same(station_id, args.station_id))

        municipality_ok = not cols["municipality"] or same(municipality, args.municipality)
        state_ok = not cols["state"] or same(state, args.state)
        if not (station_ok and municipality_ok and state_ok):
            counts["filtered_out"] += 1
            continue

        summary["rows_matched"] += 1
        try:
            instant = timestamp_utc(row.get(cols["timestamp"], ""))
        except ValueError:
            counts["invalid_timestamp"] += 1
            continue
        try:
            rainfall = number(row.get(cols["rainfall"], ""))
        except (ValueError, TypeError):
            counts["invalid_rainfall"] += 1
            continue

        flags: set[str] = set()
        if rainfall < 0:
            flags.add("negative_value")
            counts["negative_values"] += 1
        records.append({
            "timestamp": instant,
            "rainfall_mm": rainfall,
            "station_name": station_name or args.station_name or "",
            "station_id": station_id or args.station_id or "",
            "municipality": municipality or args.municipality or "",
            "state": state or args.state or "",
            "source_file": path.name,
            "source_row": row_number,
            "flags": flags,
        })
    return records, summary, counts


def quality_flags(records: list[dict], counts: Counter) -> None:
    grouped: dict[datetime, list[dict]] = {}
    for record in records:
        grouped.setdefault(record["timestamp"], []).append(record)
    for group in grouped.values():
        if len(group) > 1:
            counts["duplicate_rows"] += len(group)
            for record in group:
                record["flags"].add("duplicate_timestamp")

    times = sorted(grouped)
    intervals = [int((right - left).total_seconds()) for left, right in zip(times, times[1:]) if right > left]
    if not intervals:
        return
    frequencies = Counter(intervals)
    top = max(frequencies.values())
    expected = int(median(sorted(value for value, count in frequencies.items() if count == top)))
    if expected <= 0:
        return
    for left, right in zip(times, times[1:]):
        if int((right - left).total_seconds()) > expected * 3:
            counts["gaps_gt_3x_interval"] += 1
            for record in grouped[right]:
                record["flags"].add("gap_after_previous")


def write_normalized(path: Path, records: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "timestamp_utc", "timestamp_america_sao_paulo", "rainfall_mm",
        "station_name", "station_id", "municipality", "state",
        "source_file", "source_row", "qc_flags",
    ]
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        for record in sorted(records, key=lambda item: (item["timestamp"], item["source_file"], item["source_row"])):
            writer.writerow({
                "timestamp_utc": record["timestamp"].isoformat().replace("+00:00", "Z"),
                "timestamp_america_sao_paulo": record["timestamp"].astimezone(LOCAL_TZ).isoformat(),
                "rainfall_mm": f"{record['rainfall_mm']:.3f}".rstrip("0").rstrip("."),
                "station_name": record["station_name"],
                "station_id": record["station_id"],
                "municipality": record["municipality"],
                "state": record["state"],
                "source_file": record["source_file"],
                "source_row": record["source_row"],
                "qc_flags": ";".join(sorted(record["flags"])),
            })


def build_manifest(sources: list[dict], records: list[dict], counts: Counter, args: argparse.Namespace) -> dict:
    instants = sorted(record["timestamp"] for record in records)
    return {
        "schema_version": "1.0",
        "processor": {"script": "scripts/processar_chuva_cemaden.py", "version": VERSION},
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "filters": {
            "station_name": args.station_name,
            "station_id": args.station_id,
            "municipality": args.municipality,
            "state": args.state,
        },
        "timezone": {
            "source_assumption": "UTC quando o arquivo não informa fuso",
            "local_output": "America/Sao_Paulo",
        },
        "sources": sources,
        "counts": {
            "source_files": len(sources),
            "rows_read": sum(source["rows_read"] for source in sources),
            "rows_matched": sum(source["rows_matched"] for source in sources),
            "records_normalized": len(records),
            **dict(sorted(counts.items())),
        },
        "coverage": {
            "first_timestamp_utc": instants[0].isoformat() if instants else None,
            "last_timestamp_utc": instants[-1].isoformat() if instants else None,
        },
        "limitations": [
            "Os arquivos são dados brutos e podem conter inconsistências.",
            "O script não valida causalidade, representatividade espacial ou desempenho de política pública.",
            "Lacunas são sinalizadas pelo intervalo modal observado, não por especificação oficial da estação.",
        ],
    }


def write_report(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    counts = data["counts"]
    coverage = data["coverage"]
    lines = [
        "# Relatório de qualidade — chuva Cemaden", "",
        f"- Processador: `{data['processor']['script']}` v{data['processor']['version']}",
        f"- Gerado em UTC: `{data['generated_at_utc']}`",
        f"- Arquivos: {counts['source_files']}",
        f"- Linhas lidas: {counts['rows_read']}",
        f"- Linhas da estação: {counts['rows_matched']}",
        f"- Registros normalizados: {counts['records_normalized']}",
        f"- Primeiro registro UTC: `{coverage['first_timestamp_utc']}`",
        f"- Último registro UTC: `{coverage['last_timestamp_utc']}`",
        "", "## Achados automáticos", "",
        "| Achado | Quantidade |", "|---|---:|",
    ]
    for key in ("filtered_out", "invalid_timestamp", "invalid_rainfall", "negative_values", "duplicate_rows", "gaps_gt_3x_interval"):
        lines.append(f"| `{key}` | {counts.get(key, 0)} |")
    lines.extend(["", "## Arquivos de origem", "", "| Arquivo | SHA-256 | Linhas | Correspondentes |", "|---|---|---:|---:|"])
    for source in data["sources"]:
        lines.append(f"| `{source['path']}` | `{source['sha256']}` | {source['rows_read']} | {source['rows_matched']} |")
    lines.extend(["", "## Interpretação", "", "Flags automáticas não removem registros nem demonstram erro instrumental. Elas indicam pontos que exigem inspeção antes de qualquer análise.", ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--pattern", action="append")
    parser.add_argument("--station-name", default="Itapeba")
    parser.add_argument("--station-id")
    parser.add_argument("--municipality", default="Maricá")
    parser.add_argument("--state", default="RJ")
    args = parser.parse_args()

    patterns = args.pattern or ["*.csv", "*.txt"]
    files = sorted({path for pattern in patterns for path in args.input_dir.glob(pattern) if path.is_file()})
    if not files:
        print(f"ERRO: nenhum arquivo encontrado em {args.input_dir}", file=sys.stderr)
        return 1

    records: list[dict] = []
    sources: list[dict] = []
    counts = Counter()
    for path in files:
        source_records, source, source_counts = read_file(path, args)
        records.extend(source_records)
        sources.append(source)
        counts.update(source_counts)

    quality_flags(records, counts)
    write_normalized(args.output, records)
    data = build_manifest(sources, records, counts, args)
    args.manifest.parent.mkdir(parents=True, exist_ok=True)
    args.manifest.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_report(args.report, data)
    print(f"{len(records)} registro(s) normalizado(s) de {sum(source['rows_read'] for source in sources)} linha(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
