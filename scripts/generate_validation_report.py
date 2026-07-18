"""Executa a validação documental e produz relatório Markdown consolidado."""

from __future__ import annotations

import argparse
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

from generate_catalog import ROOT, load_documents
from validate_issue_forms import IssueFormValidationResult, validate_issue_forms
from validate_links import LinkValidationResult, validate_links
from validate_metadata_graph import ValidationResult, validate_documents


MANUAL_DEBT = (
    "GitHub Pages ainda exige ativação inicial pelo proprietário na issue #1.",
    "A camada de aplicações e evidências ainda não possui estudo de caso oficial.",
    "A adequação da licença para documentação, ferramentas e eventual software permanece pendente.",
    "A política de revisão e aprovação e a instância plural permanente ainda não foram constituídas.",
)


def status_label(ok: bool) -> str:
    return "APROVADO" if ok else "REPROVADO"


def add_findings(lines: list[str], title: str, errors: list[str], warnings: list[str]) -> None:
    lines.extend([f"## {title}", ""])
    if not errors and not warnings:
        lines.extend(["Nenhum achado.", ""])
        return
    if errors:
        lines.extend(["### Erros", ""])
        lines.extend(f"- {item}" for item in errors)
        lines.append("")
    if warnings:
        lines.extend(["### Avisos", ""])
        lines.extend(f"- {item}" for item in warnings)
        lines.append("")


def build_report(
    metadata: ValidationResult,
    links: LinkValidationResult,
    issue_forms: IssueFormValidationResult,
) -> str:
    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    commit = os.environ.get("GITHUB_SHA", "execução local")
    overall_ok = metadata.ok and links.ok and issue_forms.ok

    lines = [
        "# Relatório de Validação Documental",
        "",
        f"- **Resultado:** {status_label(overall_ok)}",
        f"- **Gerado em:** `{generated_at}`",
        f"- **Commit:** `{commit}`",
        f"- **Documentos avaliados:** {metadata.documents}",
        "",
        "## Resumo",
        "",
        "| Verificação | Resultado | Medidas |",
        "|---|---|---|",
        (
            f"| Metadados e grafo | {status_label(metadata.ok)} | "
            f"{metadata.dependencies} dependências; {metadata.outputs} saídas; "
            f"{metadata.complementary_relations} relações complementares; "
            f"{metadata.substitutions} substituições |"
        ),
        (
            f"| Links e âncoras | {status_label(links.ok)} | "
            f"{links.links} destinos; {links.internal_links} internos; "
            f"{links.anchors_checked} âncoras |"
        ),
        (
            f"| Formulários de issue | {status_label(issue_forms.ok)} | "
            f"{issue_forms.forms} formulário(s); {issue_forms.fields} campo(s) |"
        ),
        "",
    ]

    add_findings(lines, "Achados de metadados e grafo", metadata.errors, metadata.warnings)
    add_findings(lines, "Achados de links e âncoras", links.errors, links.warnings)
    add_findings(
        lines,
        "Achados de formulários de issue",
        issue_forms.errors,
        issue_forms.warnings,
    )

    lines.extend(["## Dívida manual conhecida", ""])
    lines.extend(f"- {item}" for item in MANUAL_DEBT)
    lines.extend(
        [
            "",
            "## Escopo da automação",
            "",
            "A execução verifica campos obrigatórios, versões semânticas, estados, idioma, datas, compatibilidade, listas sem duplicidade, histórico da versão corrente, referências, reciprocidade de saídas e substituições, ciclos de dependência, destinos internos, âncoras Markdown e estrutura mínima dos formulários YAML de issue.",
            "",
            "Ela não substitui revisão humana de mérito, aprovação metodológica, validação empírica, transições formais de estado ou avaliação da qualidade das evidências.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="validation-report.md")
    args = parser.parse_args()

    documents = load_documents(include_catalog=True)
    metadata_result = validate_documents(documents)
    link_result = validate_links(documents)
    issue_form_result = validate_issue_forms()

    output_path = Path(args.output)
    if not output_path.is_absolute():
        output_path = ROOT / output_path
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        build_report(metadata_result, link_result, issue_form_result),
        encoding="utf-8",
    )

    print(f"Relatório gerado em {output_path}")
    return 0 if metadata_result.ok and link_result.ok and issue_form_result.ok else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (FileNotFoundError, TypeError, ValueError) as error:
        print(f"ERRO: {error}", file=sys.stderr)
        raise SystemExit(1) from error
