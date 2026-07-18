#!/usr/bin/env python3
"""Valida o registro estruturado de documentos técnicos do CASO-001."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REGISTRY = ROOT / "casos" / "CASO-001_REGISTRO_DOCUMENTOS_TECNICOS.json"
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")
RECORD_ID = re.compile(r"^DT-\d{3}$")
CLAIM_ID = re.compile(r"^C-\d{3}$")
REQUIRED_ID = re.compile(r"^REQ-\d{3}$")
INCONSISTENCY_ID = re.compile(r"^INC-\d{3}$")

ALLOWED_SOURCE_TYPES = {
    "comunicacao_institucional",
    "registro_financiamento",
    "orientacao_selecao",
    "portal_transparencia",
    "registro_historico",
}
ALLOWED_EVIDENCE_LEVELS = {
    "contextual",
    "primario_financiamento",
    "requisito_procedimental",
    "indice_contratacao",
    "contextual_historico",
}
ALLOWED_STATES = {"localizada", "consultada", "obtida", "tratada", "pendente"}
ALLOWED_REQUIRED_STATES = {"pendente", "obtido", "revisado", "nao_aplicavel"}
ALLOWED_INCONSISTENCY_STATES = {"aberta", "explicacao_provisoria", "resolvida"}


@dataclass
class ValidationResult:
    records: int = 0
    claims: int = 0
    required_documents: int = 0
    inconsistencies: int = 0
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


def is_iso_date(value: Any) -> bool:
    if value is None:
        return True
    if not isinstance(value, str):
        return False
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return True


def require_string(mapping: dict[str, Any], field_name: str, context: str, result: ValidationResult) -> str:
    value = mapping.get(field_name)
    if not isinstance(value, str) or not value.strip():
        result.errors.append(f"{context}: `{field_name}` deve ser texto não vazio.")
        return ""
    return value.strip()


def validate_https_url(value: Any, context: str, result: ValidationResult) -> None:
    if not isinstance(value, str):
        result.errors.append(f"{context}: `url` deve ser texto.")
        return
    parsed = urlparse(value)
    if parsed.scheme != "https" or not parsed.netloc:
        result.errors.append(f"{context}: URL deve usar HTTPS e possuir host: {value!r}.")


def validate_registry(payload: dict[str, Any]) -> ValidationResult:
    result = ValidationResult()

    schema_version = payload.get("schema_version")
    if not isinstance(schema_version, str) or not SEMVER.fullmatch(schema_version):
        result.errors.append("`schema_version` deve seguir SemVer X.Y.Z.")
    if payload.get("case_id") != "CASO-001":
        result.errors.append("`case_id` deve ser `CASO-001`.")
    if payload.get("issue") != 7:
        result.errors.append("`issue` deve ser 7.")
    if not is_iso_date(payload.get("updated_at")):
        result.errors.append("`updated_at` deve ser data ISO YYYY-MM-DD.")

    records = payload.get("records")
    if not isinstance(records, list) or not records:
        result.errors.append("`records` deve ser lista não vazia.")
        records = []

    record_ids: set[str] = set()
    claim_ids: set[str] = set()

    for index, record in enumerate(records, start=1):
        context = f"registro {index}"
        if not isinstance(record, dict):
            result.errors.append(f"{context}: deve ser objeto.")
            continue
        result.records += 1

        record_id = require_string(record, "id", context, result)
        if record_id and not RECORD_ID.fullmatch(record_id):
            result.errors.append(f"{context}: identificador inválido `{record_id}`.")
        if record_id in record_ids:
            result.errors.append(f"{context}: identificador duplicado `{record_id}`.")
        record_ids.add(record_id)
        context = record_id or context

        for field_name in ("title", "organization", "scope"):
            require_string(record, field_name, context, result)

        source_type = record.get("source_type")
        if source_type not in ALLOWED_SOURCE_TYPES:
            result.errors.append(f"{context}: `source_type` inválido: {source_type!r}.")
        evidence_level = record.get("evidence_level")
        if evidence_level not in ALLOWED_EVIDENCE_LEVELS:
            result.errors.append(f"{context}: `evidence_level` inválido: {evidence_level!r}.")
        state = record.get("state")
        if state not in ALLOWED_STATES:
            result.errors.append(f"{context}: estado inválido: {state!r}.")

        if source_type == "comunicacao_institucional" and evidence_level not in {"contextual"}:
            result.errors.append(
                f"{context}: comunicação institucional não pode ser classificada como evidência contratual ou financeira primária."
            )
        if source_type == "registro_historico" and evidence_level != "contextual_historico":
            result.errors.append(f"{context}: registro histórico deve usar `contextual_historico`.")
        if source_type == "registro_financiamento" and evidence_level != "primario_financiamento":
            result.errors.append(f"{context}: registro financeiro deve usar `primario_financiamento`.")

        validate_https_url(record.get("url"), context, result)
        for date_field in ("published_at", "accessed_at"):
            if not is_iso_date(record.get(date_field)):
                result.errors.append(f"{context}: `{date_field}` deve ser data ISO ou null.")
        if record.get("accessed_at") is None:
            result.errors.append(f"{context}: `accessed_at` é obrigatório.")

        local_path = record.get("local_path")
        sha256 = record.get("sha256")
        if state in {"obtida", "tratada"}:
            if not isinstance(local_path, str) or not local_path.strip():
                result.errors.append(f"{context}: fonte `{state}` exige `local_path`.")
            if not isinstance(sha256, str) or not SHA256.fullmatch(sha256):
                result.errors.append(f"{context}: fonte `{state}` exige SHA-256 minúsculo válido.")
        else:
            if local_path is not None or sha256 is not None:
                result.warnings.append(
                    f"{context}: fonte não obtida possui caminho ou hash; confirme se o estado deveria ser `obtida`."
                )

        identifiers = record.get("identifiers")
        if not isinstance(identifiers, dict):
            result.errors.append(f"{context}: `identifiers` deve ser objeto.")

        limitations = record.get("limitations")
        if not isinstance(limitations, list) or not limitations:
            result.errors.append(f"{context}: `limitations` deve ser lista não vazia.")
        elif any(not isinstance(item, str) or not item.strip() for item in limitations):
            result.errors.append(f"{context}: limitações devem ser textos não vazios.")

        claims = record.get("claims")
        if not isinstance(claims, list) or not claims:
            result.errors.append(f"{context}: `claims` deve ser lista não vazia.")
            continue

        for claim_index, claim in enumerate(claims, start=1):
            claim_context = f"{context}, alegação {claim_index}"
            if not isinstance(claim, dict):
                result.errors.append(f"{claim_context}: deve ser objeto.")
                continue
            result.claims += 1
            claim_id = require_string(claim, "id", claim_context, result)
            if claim_id and not CLAIM_ID.fullmatch(claim_id):
                result.errors.append(f"{claim_context}: identificador inválido `{claim_id}`.")
            if claim_id in claim_ids:
                result.errors.append(f"{claim_context}: identificador duplicado `{claim_id}`.")
            claim_ids.add(claim_id)
            for field_name in ("topic", "scope", "statement"):
                require_string(claim, field_name, claim_id or claim_context, result)
            value = claim.get("value")
            unit = claim.get("unit")
            if value is not None and not isinstance(value, (int, float)):
                result.errors.append(f"{claim_id}: `value` deve ser número ou null.")
            if value is not None and (not isinstance(unit, str) or not unit.strip()):
                result.errors.append(f"{claim_id}: valor numérico exige unidade.")
            if value is None and unit is not None:
                result.errors.append(f"{claim_id}: unidade deve ser null quando valor é null.")

    inconsistencies = payload.get("known_inconsistencies")
    if not isinstance(inconsistencies, list):
        result.errors.append("`known_inconsistencies` deve ser lista.")
        inconsistencies = []
    inconsistency_ids: set[str] = set()
    for index, inconsistency in enumerate(inconsistencies, start=1):
        context = f"inconsistência {index}"
        if not isinstance(inconsistency, dict):
            result.errors.append(f"{context}: deve ser objeto.")
            continue
        result.inconsistencies += 1
        identifier = require_string(inconsistency, "id", context, result)
        if identifier and not INCONSISTENCY_ID.fullmatch(identifier):
            result.errors.append(f"{context}: identificador inválido `{identifier}`.")
        if identifier in inconsistency_ids:
            result.errors.append(f"{context}: identificador duplicado `{identifier}`.")
        inconsistency_ids.add(identifier)
        context = identifier or context
        require_string(inconsistency, "topic", context, result)
        require_string(inconsistency, "description", context, result)
        status = inconsistency.get("status")
        if status not in ALLOWED_INCONSISTENCY_STATES:
            result.errors.append(f"{context}: estado inválido `{status}`.")
        references = inconsistency.get("claim_ids")
        if not isinstance(references, list) or len(references) < 2:
            result.errors.append(f"{context}: deve referenciar ao menos duas alegações.")
        else:
            for claim_id in references:
                if claim_id not in claim_ids:
                    result.errors.append(f"{context}: alegação inexistente `{claim_id}`.")

    required_documents = payload.get("required_documents")
    if not isinstance(required_documents, list) or not required_documents:
        result.errors.append("`required_documents` deve ser lista não vazia.")
        required_documents = []
    required_ids: set[str] = set()
    for index, required in enumerate(required_documents, start=1):
        context = f"documento requerido {index}"
        if not isinstance(required, dict):
            result.errors.append(f"{context}: deve ser objeto.")
            continue
        result.required_documents += 1
        identifier = require_string(required, "id", context, result)
        if identifier and not REQUIRED_ID.fullmatch(identifier):
            result.errors.append(f"{context}: identificador inválido `{identifier}`.")
        if identifier in required_ids:
            result.errors.append(f"{context}: identificador duplicado `{identifier}`.")
        required_ids.add(identifier)
        require_string(required, "document", identifier or context, result)
        if required.get("state") not in ALLOWED_REQUIRED_STATES:
            result.errors.append(f"{identifier}: estado de documento requerido inválido.")

    if result.records and result.claims < result.records:
        result.errors.append("Cada registro deve possuir ao menos uma alegação verificável.")
    return result


def build_report(result: ValidationResult, registry_path: Path) -> str:
    lines = [
        "# Validação do registro de documentos técnicos",
        "",
        f"- **Resultado:** {'APROVADO' if result.ok else 'REPROVADO'}",
        f"- **Arquivo:** `{registry_path.name}`",
        f"- **Fontes:** {result.records}",
        f"- **Alegações:** {result.claims}",
        f"- **Inconsistências:** {result.inconsistencies}",
        f"- **Documentos requeridos:** {result.required_documents}",
        "",
    ]
    if result.errors:
        lines.extend(["## Erros", ""])
        lines.extend(f"- {item}" for item in result.errors)
        lines.append("")
    if result.warnings:
        lines.extend(["## Avisos", ""])
        lines.extend(f"- {item}" for item in result.warnings)
        lines.append("")
    if not result.errors and not result.warnings:
        lines.extend(["Nenhum achado.", ""])
    lines.extend(
        [
            "## Limite",
            "",
            "A validação confirma estrutura, rastreabilidade e coerência classificatória. Ela não confirma autenticidade, completude ou mérito técnico das fontes.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--registry", default=str(DEFAULT_REGISTRY))
    parser.add_argument("--report")
    args = parser.parse_args()

    registry_path = Path(args.registry)
    try:
        payload = json.loads(registry_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        print(f"ERRO: {error}", file=sys.stderr)
        return 2
    if not isinstance(payload, dict):
        print("ERRO: a raiz do registro deve ser objeto.", file=sys.stderr)
        return 2

    result = validate_registry(payload)
    if args.report:
        report_path = Path(args.report)
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(build_report(result, registry_path), encoding="utf-8")

    print(
        f"Registro {'aprovado' if result.ok else 'reprovado'}: "
        f"{result.records} fonte(s), {result.claims} alegação(ões), "
        f"{result.inconsistencies} inconsistência(s)."
    )
    for error in result.errors:
        print(f"ERRO: {error}", file=sys.stderr)
    for warning in result.warnings:
        print(f"AVISO: {warning}", file=sys.stderr)
    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
