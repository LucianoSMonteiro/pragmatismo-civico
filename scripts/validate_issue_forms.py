"""Valida a estrutura mínima dos formulários YAML de issue."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import yaml

from generate_catalog import ROOT


ISSUE_FORMS_DIR = ROOT / ".github" / "ISSUE_TEMPLATE"
ALLOWED_TYPES = {"markdown", "input", "textarea", "dropdown", "checkboxes"}


@dataclass
class IssueFormValidationResult:
    forms: int = 0
    fields: int = 0
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


def validate_issue_forms() -> IssueFormValidationResult:
    result = IssueFormValidationResult()
    if not ISSUE_FORMS_DIR.is_dir():
        result.warnings.append("diretório .github/ISSUE_TEMPLATE não encontrado")
        return result

    form_paths = sorted(
        path
        for path in ISSUE_FORMS_DIR.iterdir()
        if path.suffix.lower() in {".yml", ".yaml"} and path.name != "config.yml"
    )

    for path in form_paths:
        result.forms += 1
        relative = path.relative_to(ROOT).as_posix()
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
        except yaml.YAMLError as error:
            result.errors.append(f"YAML inválido em {relative}: {error}")
            continue

        if not isinstance(data, dict):
            result.errors.append(f"formulário deve ser um objeto YAML: {relative}")
            continue

        for field_name in ("name", "description", "body"):
            if field_name not in data:
                result.errors.append(f"campo obrigatório ausente em {relative}: {field_name}")

        if not isinstance(data.get("name"), str) or not str(data.get("name", "")).strip():
            result.errors.append(f"name inválido em {relative}")
        if not isinstance(data.get("description"), str) or not str(data.get("description", "")).strip():
            result.errors.append(f"description inválida em {relative}")

        body = data.get("body")
        if not isinstance(body, list) or not body:
            result.errors.append(f"body deve ser lista não vazia em {relative}")
            continue

        seen_ids: set[str] = set()
        for index, item in enumerate(body, start=1):
            result.fields += 1
            prefix = f"{relative} item {index}"
            if not isinstance(item, dict):
                result.errors.append(f"item inválido em {prefix}")
                continue

            item_type = item.get("type")
            if item_type not in ALLOWED_TYPES:
                result.errors.append(f"tipo não suportado em {prefix}: {item_type}")
                continue

            attributes = item.get("attributes")
            if not isinstance(attributes, dict):
                result.errors.append(f"attributes ausente ou inválido em {prefix}")
                continue

            if item_type == "markdown":
                if not isinstance(attributes.get("value"), str) or not attributes["value"].strip():
                    result.errors.append(f"markdown sem value em {prefix}")
                continue

            item_id = item.get("id")
            if not isinstance(item_id, str) or not item_id.strip():
                result.errors.append(f"id ausente em {prefix}")
            elif item_id in seen_ids:
                result.errors.append(f"id duplicado em {relative}: {item_id}")
            else:
                seen_ids.add(item_id)

            if not isinstance(attributes.get("label"), str) or not attributes["label"].strip():
                result.errors.append(f"label ausente em {prefix}")

            if item_type == "dropdown":
                options = attributes.get("options")
                if not isinstance(options, list) or len(options) < 2:
                    result.errors.append(f"dropdown precisa de ao menos duas opções em {prefix}")

            if item_type == "checkboxes":
                options = attributes.get("options")
                if not isinstance(options, list) or not options:
                    result.errors.append(f"checkboxes precisa de opções em {prefix}")
                else:
                    for option_index, option in enumerate(options, start=1):
                        if not isinstance(option, dict) or not isinstance(option.get("label"), str):
                            result.errors.append(
                                f"opção inválida em {prefix}, posição {option_index}"
                            )

        title = data.get("title")
        if title is not None and not isinstance(title, str):
            result.errors.append(f"title deve ser string em {relative}")

        labels = data.get("labels")
        if labels:
            result.warnings.append(
                f"{relative} declara labels; confirme que existem no repositório"
            )

    return result


if __name__ == "__main__":
    validation = validate_issue_forms()
    for warning in validation.warnings:
        print(f"AVISO: {warning}")
    for error in validation.errors:
        print(f"ERRO: {error}")
    if validation.ok:
        print(
            f"Formulários válidos: {validation.forms} arquivo(s), "
            f"{validation.fields} campo(s)."
        )
    raise SystemExit(0 if validation.ok else 1)
