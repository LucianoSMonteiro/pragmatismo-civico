"""Valida formulários YAML de issue e o template de pull request."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import yaml

from generate_catalog import ROOT


ISSUE_FORMS_DIR = ROOT / ".github" / "ISSUE_TEMPLATE"
PULL_REQUEST_TEMPLATE = ROOT / ".github" / "pull_request_template.md"
ALLOWED_TYPES = {"markdown", "input", "textarea", "dropdown", "checkboxes"}
REQUIRED_PR_SECTIONS = (
    "## Identificação da mudança",
    "## Problema e decisão",
    "## Escopo",
    "## Implementação",
    "## Riscos e reversão",
    "## Conflitos de interesse",
    "## Revisão e aprovação",
    "## Verificação",
    "## Evidências de validação",
)
REQUIRED_PR_REFERENCES = ("GOV-005", "GOV-006", "PM-AAAA-NNN", "CI foi aprovada")
REQUIRED_FORM_IDS = {
    "proposta-de-mudanca.yml": {
        "problem",
        "proposal_type",
        "impact",
        "current_state",
        "proposed_change",
        "evidence",
        "alternatives",
        "principles",
        "risks",
        "compatibility",
        "implementation",
        "conflicts",
        "declarations",
    },
    "candidatura-revisor.yml": {
        "public_identity",
        "competencies",
        "experience",
        "contexts",
        "affiliations",
        "conflicts",
        "availability",
        "languages",
        "limitations",
        "declarations",
    },
}
REQUIRED_FORM_REFERENCES = {
    "proposta-de-mudanca.yml": ("GOV-005", "GOV-006"),
    "candidatura-revisor.yml": (
        "GOV-007",
        "Esta issue é pública",
        "dados pessoais sensíveis",
        "não garante admissão",
    ),
}


@dataclass
class IssueFormValidationResult:
    forms: int = 0
    fields: int = 0
    pull_request_templates: int = 0
    pull_request_checkboxes: int = 0
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


def validate_pull_request_template(result: IssueFormValidationResult) -> None:
    relative = PULL_REQUEST_TEMPLATE.relative_to(ROOT).as_posix()
    if not PULL_REQUEST_TEMPLATE.is_file():
        result.errors.append(f"template de pull request ausente: {relative}")
        return

    result.pull_request_templates += 1
    text = PULL_REQUEST_TEMPLATE.read_text(encoding="utf-8")
    if not text.strip():
        result.errors.append(f"template de pull request vazio: {relative}")
        return

    for section in REQUIRED_PR_SECTIONS:
        if section not in text:
            result.errors.append(f"seção obrigatória ausente em {relative}: {section}")
    for reference in REQUIRED_PR_REFERENCES:
        if reference not in text:
            result.errors.append(f"referência obrigatória ausente em {relative}: {reference}")

    result.pull_request_checkboxes = sum(
        1 for line in text.splitlines() if line.strip().startswith("- [ ]")
    )
    if result.pull_request_checkboxes < 8:
        result.errors.append(
            f"template de pull request precisa de ao menos 8 verificações: {relative}"
        )


def validate_form_contract(
    path: Path,
    text: str,
    seen_ids: set[str],
    result: IssueFormValidationResult,
) -> None:
    relative = path.relative_to(ROOT).as_posix()
    required_ids = REQUIRED_FORM_IDS.get(path.name)
    if required_ids is not None:
        missing_ids = sorted(required_ids - seen_ids)
        if missing_ids:
            result.errors.append(
                f"campos canônicos ausentes em {relative}: {', '.join(missing_ids)}"
            )

    for reference in REQUIRED_FORM_REFERENCES.get(path.name, ()):
        if reference not in text:
            result.errors.append(
                f"referência ou salvaguarda obrigatória ausente em {relative}: {reference}"
            )


def validate_issue_forms() -> IssueFormValidationResult:
    result = IssueFormValidationResult()
    if not ISSUE_FORMS_DIR.is_dir():
        result.warnings.append("diretório .github/ISSUE_TEMPLATE não encontrado")
    else:
        form_paths = sorted(
            path
            for path in ISSUE_FORMS_DIR.iterdir()
            if path.suffix.lower() in {".yml", ".yaml"} and path.name != "config.yml"
        )

        known_names = set(REQUIRED_FORM_IDS)
        found_names = {path.name for path in form_paths}
        for missing_form in sorted(known_names - found_names):
            result.errors.append(f"formulário canônico ausente: {missing_form}")

        for path in form_paths:
            result.forms += 1
            relative = path.relative_to(ROOT).as_posix()
            text = path.read_text(encoding="utf-8")
            try:
                data = yaml.safe_load(text)
            except yaml.YAMLError as error:
                result.errors.append(f"YAML inválido em {relative}: {error}")
                continue

            if not isinstance(data, dict):
                result.errors.append(f"formulário deve ser um objeto YAML: {relative}")
                continue

            for field_name in ("name", "description", "body"):
                if field_name not in data:
                    result.errors.append(
                        f"campo obrigatório ausente em {relative}: {field_name}"
                    )

            if not isinstance(data.get("name"), str) or not str(data.get("name", "")).strip():
                result.errors.append(f"name inválido em {relative}")
            if not isinstance(data.get("description"), str) or not str(
                data.get("description", "")
            ).strip():
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
                    value = attributes.get("value")
                    if not isinstance(value, str) or not value.strip():
                        result.errors.append(f"markdown sem value em {prefix}")
                    continue

                item_id = item.get("id")
                if not isinstance(item_id, str) or not item_id.strip():
                    result.errors.append(f"id ausente em {prefix}")
                elif item_id in seen_ids:
                    result.errors.append(f"id duplicado em {relative}: {item_id}")
                else:
                    seen_ids.add(item_id)

                label = attributes.get("label")
                if not isinstance(label, str) or not label.strip():
                    result.errors.append(f"label ausente em {prefix}")

                if item_type == "dropdown":
                    options = attributes.get("options")
                    if not isinstance(options, list) or len(options) < 2:
                        result.errors.append(
                            f"dropdown precisa de ao menos duas opções em {prefix}"
                        )

                if item_type == "checkboxes":
                    options = attributes.get("options")
                    if not isinstance(options, list) or not options:
                        result.errors.append(f"checkboxes precisa de opções em {prefix}")
                    else:
                        for option_index, option in enumerate(options, start=1):
                            if not isinstance(option, dict) or not isinstance(
                                option.get("label"), str
                            ):
                                result.errors.append(
                                    f"opção inválida em {prefix}, posição {option_index}"
                                )
                            elif option.get("required") is not True:
                                result.errors.append(
                                    f"declaração deve ser obrigatória em {prefix}, posição {option_index}"
                                )

            validate_form_contract(path, text, seen_ids, result)

            title = data.get("title")
            if title is not None and not isinstance(title, str):
                result.errors.append(f"title deve ser string em {relative}")

            labels = data.get("labels")
            if labels:
                result.warnings.append(
                    f"{relative} declara labels; confirme que existem no repositório"
                )

    validate_pull_request_template(result)
    return result


if __name__ == "__main__":
    validation = validate_issue_forms()
    for warning in validation.warnings:
        print(f"AVISO: {warning}")
    for error in validation.errors:
        print(f"ERRO: {error}")
    if validation.ok:
        print(
            f"Templates válidos: {validation.forms} formulário(s), "
            f"{validation.fields} campo(s), "
            f"{validation.pull_request_templates} template(s) de PR e "
            f"{validation.pull_request_checkboxes} verificação(ões)."
        )
    raise SystemExit(0 if validation.ok else 1)
