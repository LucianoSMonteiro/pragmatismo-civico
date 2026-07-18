"""Analisa o impacto de uma possível migração física por camadas.

O script não move arquivos. Ele compara a estrutura vigente com uma hipótese de
organização por diretórios, calcula o alcance da migração e gera um relatório
para apoiar uma decisão arquitetural explícita.
"""

from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit

from generate_catalog import ROOT, Document, load_documents


LAYER_DIRECTORIES = {
    "Publicação e acesso": "publicacao",
    "Princípios e fundamentos": "fundamentos",
    "Governança e arquitetura": "governanca",
    "Método": "metodo",
    "Ferramentas": "ferramentas",
}

# O README precisa permanecer na raiz para continuar funcionando como página de
# apresentação do repositório. O guia já possui caminho próprio em docs/.
PRESERVED_PATHS = {"README.md", "docs/COMECAR.md"}
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")


def proposed_path(document: Document) -> str:
    """Retorna o caminho hipotético do documento em uma estrutura por camada."""
    if document.path in PRESERVED_PATHS:
        return document.path
    directory = LAYER_DIRECTORIES[document.layer]
    return str(PurePosixPath(directory) / PurePosixPath(document.path).name)


def internal_target(source_path: str, raw_target: str) -> str | None:
    """Resolve um link Markdown local para um caminho relativo ao repositório."""
    target = raw_target.strip()
    if target.startswith("<") and target.endswith(")"):
        target = target[1:-1].strip()
    if not target:
        return None

    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc or target.startswith(("mailto:", "tel:")):
        return None
    decoded = unquote(parsed.path)
    if not decoded:
        return None

    source_parent = PurePosixPath(source_path).parent
    parts: list[str] = []
    for part in (source_parent / decoded).parts:
        if part in ("", "."):
            continue
        if part == "..":
            if parts:
                parts.pop()
            continue
        parts.append(part)
    return str(PurePosixPath(*parts))


def count_links(documents: list[Document], proposed: dict[str, str]) -> tuple[int, int, Counter[str]]:
    """Conta links locais e referências que exigiriam reescrita."""
    public_paths = {document.path for document in documents}
    total = 0
    affected = 0
    affected_by_source: Counter[str] = Counter()

    for document in documents:
        source = (ROOT / document.path).read_text(encoding="utf-8")
        for match in LINK_RE.finditer(source):
            target = internal_target(document.path, match.group(1))
            if target not in public_paths:
                continue
            total += 1
            if proposed[document.path] != document.path or proposed[target] != target:
                affected += 1
                affected_by_source[document.path] += 1

    return total, affected, affected_by_source


def generate_report(documents: list[Document]) -> str:
    proposed = {document.path: proposed_path(document) for document in documents}
    moved = [document for document in documents if proposed[document.path] != document.path]
    root_documents = [document for document in documents if PurePosixPath(document.path).parent == PurePosixPath(".")]
    total_links, affected_links, affected_by_source = count_links(documents, proposed)
    layer_counts = Counter(document.layer for document in documents)
    destination_counts = Counter(PurePosixPath(proposed[document.path]).parent.as_posix() for document in moved)

    lines = [
        "# Análise da estrutura física do repositório",
        "",
        "Relatório gerado automaticamente. Nenhum arquivo foi movido.",
        "",
        "## Linha de base",
        "",
        "| Medida | Resultado |",
        "|---|---:|",
        f"| Documentos navegáveis | {len(documents)} |",
        f"| Documentos Markdown na raiz | {len(root_documents)} |",
        f"| Caminhos preservados por função pública | {len(PRESERVED_PATHS)} |",
        f"| Links Markdown entre documentos públicos | {total_links} |",
        "",
        "## Hipótese de organização por camada",
        "",
        "| Medida | Resultado |",
        "|---|---:|",
        f"| Documentos que mudariam de caminho | {len(moved)} |",
        f"| Referências internas potencialmente afetadas | {affected_links} |",
        f"| Entradas de navegação a revisar | {len(moved)} |",
        f"| Diretórios de destino | {len(destination_counts)} |",
        "",
        "### Distribuição atual por camada",
        "",
        "| Camada | Documentos |",
        "|---|---:|",
    ]
    for layer in LAYER_DIRECTORIES:
        lines.append(f"| {layer} | {layer_counts[layer]} |")

    lines.extend(["", "### Destinos hipotéticos", "", "| Diretório | Documentos movidos |", "|---|---:|"])
    for directory, count in sorted(destination_counts.items()):
        lines.append(f"| `{directory}/` | {count} |")

    lines.extend(
        [
            "",
            "## Arquivos com mais referências afetadas",
            "",
            "| Documento de origem | Referências a revisar |",
            "|---|---:|",
        ]
    )
    if affected_by_source:
        for path, count in affected_by_source.most_common(10):
            lines.append(f"| `{path}` | {count} |")
    else:
        lines.append("| — | 0 |")

    lines.extend(
        [
            "",
            "## Avaliação",
            "",
            "A organização por diretórios tornaria a estrutura física mais semelhante às camadas lógicas, mas não alteraria a navegação pública, que já é definida pelo `mkdocs.yml` e pelo catálogo.",
            "",
            "A migração exigiria alterar caminhos canônicos, referências internas, navegação, catálogo, URLs de edição e possíveis referências externas. O ganho é predominantemente de manutenção visual no repositório, enquanto o custo recai sobre compatibilidade, histórico e manutenção de redirecionamentos.",
            "",
            "## Critério recomendado",
            "",
            "Manter a estrutura atual enquanto o benefício líquido de mover arquivos não superar os riscos e custos calculados. Reavaliar quando ao menos uma das condições ocorrer:",
            "",
            "- crescimento que torne a localização no repositório materialmente difícil;",
            "- inclusão recorrente de estudos de caso, relatórios ou anexos;",
            "- necessidade de permissões ou automações específicas por diretório;",
            "- disponibilidade de redirecionamentos confiáveis para URLs publicadas;",
            "- evidência de que a estrutura atual causa erros, duplicação ou custo de manutenção relevante.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="structure-analysis.md")
    args = parser.parse_args()

    documents = load_documents(include_catalog=True)
    output_path = Path(args.output)
    if not output_path.is_absolute():
        output_path = ROOT / output_path
    output_path.write_text(generate_report(documents), encoding="utf-8")
    print(f"Análise estrutural gerada para {len(documents)} documentos em {output_path}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
