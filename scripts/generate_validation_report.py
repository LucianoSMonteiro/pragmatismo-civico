"""Executa a validação documental e produz relatório Markdown consolidado."""

from __future__ import annotations

import argparse
import base64
import hashlib
import os
import shutil
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from generate_catalog import ROOT, load_documents
from validate_issue_forms import IssueFormValidationResult, validate_issue_forms
from validate_links import LinkValidationResult, validate_links
from validate_metadata_graph import ValidationResult, validate_documents


MANUAL_DEBT = (
    "GitHub Pages ainda exige ativação inicial pelo proprietário na issue #1.",
    "O CASO-001 existe apenas em preparação e ainda não possui diagnóstico, revisão independente ou resultado empírico.",
    "Nenhuma feição oficial de Itapeba, série pluviométrica real ou documento técnico integral foi incorporado ao caso.",
    "A adequação da licença para documentação, ferramentas e eventual software permanece pendente.",
    "O cadastro público de revisores existe, mas ainda não possui pessoa elegível ou ativa.",
    "A instância plural permanente de revisão e aprovação ainda não foi constituída.",
)
GEOINEA_MARKER = ROOT / ".github" / "geoinea-query-once"


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
            f"| Templates de contribuição | {status_label(issue_forms.ok)} | "
            f"{issue_forms.forms} formulário(s) de issue; "
            f"{issue_forms.fields} campo(s); "
            f"{issue_forms.pull_request_templates} template(s) de PR; "
            f"{issue_forms.pull_request_checkboxes} verificação(ões) de PR |"
        ),
        "",
    ]

    add_findings(lines, "Achados de metadados e grafo", metadata.errors, metadata.warnings)
    add_findings(lines, "Achados de links e âncoras", links.errors, links.warnings)
    add_findings(
        lines,
        "Achados de templates de contribuição",
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
            "A execução documental verifica campos obrigatórios, versões semânticas, estados, idioma, datas, compatibilidade, listas sem duplicidade, histórico da versão corrente, referências, reciprocidade de saídas e substituições, ciclos de dependência, destinos internos, âncoras Markdown, os formulários canônicos de proposta e candidatura, salvaguardas públicas de privacidade e o template de pull request.",
            "",
            "Os pipelines `data/pipeline` e `geodata/pipeline` são executados separadamente com fixtures sintéticos. Eles verificam o funcionamento do código, não a oficialidade, representatividade, suficiência ou qualidade de fontes reais.",
            "",
            "A automação não substitui revisão humana de mérito, avaliação real de competência, aprovação metodológica, validação empírica, transições formais de estado ou avaliação da qualidade das evidências.",
            "",
        ]
    )
    return "\n".join(lines)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def wrap_base64(data: bytes, width: int = 88) -> list[str]:
    encoded = base64.b64encode(data).decode("ascii")
    return [encoded[index : index + width] for index in range(0, len(encoded), width)]


def build_geoinea_appendix() -> str:
    """Executa uma coleta externa somente quando o marcador explícito existe.

    Todos os arquivos produzidos são incorporados ao relatório em Base64, com
    tamanho e SHA-256. Assim o artefato padrão da CI preserva os bytes exatos sem
    transformar uma dependência externa em requisito permanente do build.
    """
    if not GEOINEA_MARKER.is_file():
        return ""

    from coletar_geoinea_subbacia import CollectionError, collect

    search_term = GEOINEA_MARKER.read_text(encoding="utf-8").strip() or "Itapeba"
    output_dir = ROOT / "geoinea-result"
    last_error: str | None = None
    manifest = None

    for attempt in range(1, 4):
        if output_dir.exists():
            shutil.rmtree(output_dir)
        try:
            manifest = collect(
                output_dir=output_dir,
                search_term=search_term,
                timeout=120,
            )
            last_error = None
            break
        except (CollectionError, OSError, ValueError) as error:
            last_error = f"tentativa {attempt}: {error}"
            if attempt < 3:
                time.sleep(attempt * 10)

    lines = [
        "# Anexo temporário — consulta oficial ao GeoINEA",
        "",
        f"- **Marcador:** `{GEOINEA_MARKER.relative_to(ROOT)}`",
        f"- **Termo nominal:** `{search_term}`",
        "- **Natureza:** coleta externa temporária; não altera o resultado da validação documental",
        "",
    ]

    if manifest is None:
        lines.extend(
            [
                "## Falha de coleta",
                "",
                f"A consulta não foi concluída após três tentativas. Último erro: `{last_error}`.",
                "",
            ]
        )
        print(f"GEOINEA_QUERY_FAILURE: {last_error}")
        return "\n".join(lines)

    result = manifest["result"]
    lines.extend(
        [
            "## Resultado",
            "",
            f"- objetos informados pela camada: **{result['object_id_count']}**;",
            f"- feições de atributos consultadas: **{result['attribute_feature_count']}**;",
            f"- correspondências nominais: **{result['match_count']}**;",
            f"- geometria baixada: **{'sim' if result['geometry_downloaded'] else 'não'}**.",
            "",
            "Correspondência nominal não comprova equivalência temática. Ausência nominal não comprova inexistência física.",
            "",
            "## Arquivos preservados no artefato",
            "",
        ]
    )

    for path in sorted(item for item in output_dir.rglob("*") if item.is_file()):
        data = path.read_bytes()
        relative = path.relative_to(output_dir).as_posix()
        lines.extend(
            [
                f"### `{relative}`",
                "",
                f"- tamanho: `{len(data)}` bytes;",
                f"- SHA-256: `{sha256_bytes(data)}`.",
                "",
                "```base64",
                *wrap_base64(data),
                "```",
                "",
            ]
        )

    print(
        "GEOINEA_QUERY_SUCCESS: "
        f"objects={result['object_id_count']} "
        f"matches={result['match_count']} "
        f"geometry={result['geometry_downloaded']}"
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

    report = build_report(metadata_result, link_result, issue_form_result)
    appendix = build_geoinea_appendix()
    if appendix:
        report = f"{report}\n\n{appendix}\n"

    output_path = Path(args.output)
    if not output_path.is_absolute():
        output_path = ROOT / output_path
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")

    print(f"Relatório gerado em {output_path}")
    return 0 if metadata_result.ok and link_result.ok and issue_form_result.ok else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (FileNotFoundError, TypeError, ValueError) as error:
        print(f"ERRO: {error}", file=sys.stderr)
        raise SystemExit(1) from error
