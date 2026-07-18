"""Gera o catálogo público a partir da navegação e dos metadados canônicos."""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator

import yaml


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "mkdocs.yml"
CATALOG_PATH = "CATALOGO_DOCUMENTAL.md"

CATALOG_METADATA: dict[str, object] = {
    "id": "CATALOGO-DOCUMENTAL",
    "titulo": "Catálogo Documental do Pragmatismo Cívico",
    "versao": "0.1.0",
    "status": "rascunho",
    "tipo": "publicacao",
    "idioma": "pt-BR",
    "data_criacao": None,
    "data_versao": "2026-07-18",
    "responsaveis": ["Projeto Pragmatismo Cívico"],
    "aprovadores": [],
    "depende_de": ["ARQ-001", "ARQ-002", "PPC-META-001"],
    "produz_entrada_para": [],
    "relaciona_se_com": ["PORTAL-INICIO", "GUIA-COMECAR"],
    "substitui": [],
    "substituido_por": None,
    "compatibilidade": "inicial",
    "proxima_revisao": None,
}

LAYER_ORDER = [
    "Publicação e acesso",
    "Princípios e fundamentos",
    "Governança e arquitetura",
    "Método",
    "Ferramentas",
]

LAYER_BY_PATH = {
    "README.md": "Publicação e acesso",
    "docs/COMECAR.md": "Publicação e acesso",
    CATALOG_PATH: "Publicação e acesso",
    "FRAMEWORK_DE_REFERENCIA.md": "Princípios e fundamentos",
    "TEORIA_DO_PRAGMATISMO_CIVICO.md": "Princípios e fundamentos",
    "MANIFESTO.md": "Princípios e fundamentos",
    "CARTA_DE_PRINCIPIOS.md": "Princípios e fundamentos",
    "SPECIFICATION.md": "Princípios e fundamentos",
    "GLOSSARIO.md": "Princípios e fundamentos",
    "PPC-000_ESPECIFICACAO_DO_ECOSSISTEMA_PPC.md": "Governança e arquitetura",
    "MODELO_DE_GOVERNANCA.md": "Governança e arquitetura",
    "PPC-META-001_METADADOS_E_VERSIONAMENTO.md": "Governança e arquitetura",
    "PPC-000A_CICLO_DE_VIDA_DOS_PADROES.md": "Governança e arquitetura",
    "ARQ-001_ARQUITETURA_DOCUMENTAL_DO_FRAMEWORK.md": "Governança e arquitetura",
    "ARQ-002_INVENTARIO_E_PLANO_DE_MIGRACAO_DOCUMENTAL.md": "Governança e arquitetura",
    "ARQ-003_DECISAO_SOBRE_A_ESTRUTURA_FISICA_DO_REPOSITORIO.md": "Governança e arquitetura",
    "GOV-005_PROCESSO_DE_PROPOSTAS_DE_MUDANCA.md": "Governança e arquitetura",
    "CONTRIBUTING.md": "Governança e arquitetura",
    "CODE_OF_CONDUCT.md": "Governança e arquitetura",
    "ROADMAP.md": "Governança e arquitetura",
    "CICLO_DO_PRAGMATISMO_CIVICO.md": "Método",
    "PPC-001_DIAGNOSTICO_DE_PROBLEMAS_PUBLICOS.md": "Método",
    "PPC-002_FORMULACAO_E_COMPARACAO_DE_ALTERNATIVAS.md": "Método",
    "PPC-003_AVALIACAO_TECNICA_DE_ALTERNATIVAS.md": "Método",
    "PPC-004_DECISAO_E_JUSTIFICATIVA.md": "Método",
    "MODELO_DE_TEORIA_DA_MUDANCA.md": "Método",
    "PPC-005_IMPLEMENTACAO_E_GESTAO_ADAPTATIVA.md": "Método",
    "PPC-006_MONITORAMENTO_E_AVALIACAO_CONTINUA.md": "Método",
    "PPC-007_AVALIACAO_DE_RESULTADOS_E_IMPACTOS.md": "Método",
    "PPC-008_APRENDIZAGEM_INSTITUCIONAL_E_MELHORIA_CONTINUA.md": "Método",
    "FICHA_PPC-001_DIAGNOSTICO_DE_PROBLEMA_PUBLICO.md": "Ferramentas",
    "FICHA_PPC-002_FORMULACAO_E_COMPARACAO_DE_ALTERNATIVAS.md": "Ferramentas",
    "FICHA_PPC-003_AVALIACAO_TECNICA_DE_ALTERNATIVAS.md": "Ferramentas",
    "FICHA_PPC-004_DECISAO_E_JUSTIFICATIVA.md": "Ferramentas",
    "FICHA_TEORIA_DA_MUDANCA.md": "Ferramentas",
    "FICHA_PPC-005_IMPLEMENTACAO_E_GESTAO_ADAPTATIVA.md": "Ferramentas",
    "FICHA_PPC-006_MONITORAMENTO_E_AVALIACAO_CONTINUA.md": "Ferramentas",
    "FICHA_PPC-007_AVALIACAO_DE_RESULTADOS_E_IMPACTOS.md": "Ferramentas",
    "FICHA_PPC-008_APRENDIZAGEM_INSTITUCIONAL_E_MELHORIA_CONTINUA.md": "Ferramentas",
    "FICHA_GOV-005_PROPOSTA_DE_MUDANCA.md": "Ferramentas",
    "MATRIZ_DE_AVALIACAO_DE_POLITICAS_PUBLICAS.md": "Ferramentas",
    "INDICADORES.md": "Ferramentas",
}

REQUIRED_FIELDS = ("id", "titulo", "versao", "status", "tipo", "responsaveis")


@dataclass(frozen=True)
class Document:
    label: str
    path: str
    layer: str
    metadata: dict[str, object]


def iter_nav_entries(node: object) -> Iterator[tuple[str, str]]:
    if isinstance(node, list):
        for item in node:
            yield from iter_nav_entries(item)
    elif isinstance(node, dict):
        for label, value in node.items():
            if isinstance(value, str):
                yield str(label), value
            else:
                yield from iter_nav_entries(value)


def extract_metadata(text: str, path: str) -> dict[str, object]:
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end < 0:
            raise ValueError(f"Front matter sem fechamento: {path}")
        raw = text[4:end]
    else:
        match = re.match(r"<!--\s*\n---\n(.*?)\n---\s*\n-->", text, re.DOTALL)
        if match is None:
            raise ValueError(f"Metadados estruturados não encontrados: {path}")
        raw = match.group(1)

    metadata = yaml.safe_load(raw)
    if not isinstance(metadata, dict):
        raise ValueError(f"Metadados inválidos: {path}")
    return metadata


def validate_metadata(metadata: dict[str, object], path: str) -> None:
    missing = [field for field in REQUIRED_FIELDS if field not in metadata]
    if missing:
        raise ValueError(f"Campos ausentes em {path}: {', '.join(missing)}")
    for field in ("depende_de", "produz_entrada_para", "relaciona_se_com"):
        value = metadata.get(field, [])
        if value is not None and not isinstance(value, list):
            raise TypeError(f"{field} deve ser lista em {path}")


def load_documents(include_catalog: bool = True) -> list[Document]:
    with CONFIG_PATH.open("r", encoding="utf-8") as config_file:
        config = yaml.safe_load(config_file) or {}

    documents: list[Document] = []
    seen_paths: set[str] = set()
    for label, path in iter_nav_entries(config.get("nav", [])):
        if not path.lower().endswith(".md") or path in seen_paths:
            continue
        seen_paths.add(path)
        source = ROOT / path
        if not source.is_file():
            raise FileNotFoundError(f"Documento da navegação não encontrado: {path}")
        metadata = extract_metadata(source.read_text(encoding="utf-8"), path)
        validate_metadata(metadata, path)
        layer = LAYER_BY_PATH.get(path)
        if layer is None:
            raise ValueError(f"Camada não definida para {path}")
        documents.append(Document(label, path, layer, metadata))

    if include_catalog and CATALOG_PATH not in seen_paths:
        documents.append(
            Document(
                "Catálogo documental",
                CATALOG_PATH,
                LAYER_BY_PATH[CATALOG_PATH],
                CATALOG_METADATA,
            )
        )

    identifiers = [str(document.metadata["id"]) for document in documents]
    duplicates = sorted(
        identifier
        for identifier, count in Counter(identifiers).items()
        if count > 1
    )
    if duplicates:
        raise ValueError(f"Identificadores duplicados: {', '.join(duplicates)}")
    return documents


def format_list(value: object) -> str:
    if not value:
        return "—"
    if not isinstance(value, list):
        return str(value)
    return ", ".join(f"`{item}`" for item in value)


def yaml_front_matter(metadata: dict[str, object]) -> str:
    body = yaml.safe_dump(
        metadata,
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
    ).rstrip()
    return f"---\n{body}\n---\n"


def append_document_tables(lines: list[str], documents: list[Document]) -> None:
    for layer in LAYER_ORDER:
        lines.extend(
            [
                f"## {layer}",
                "",
                "| Identificador | Documento | Versão | Estado | Tipo | Caminho |",
                "|---|---|---:|---|---|---|",
            ]
        )
        for document in sorted(
            (item for item in documents if item.layer == layer),
            key=lambda item: (str(item.metadata["id"]), item.path),
        ):
            metadata = document.metadata
            title = str(metadata["titulo"]).replace("|", "\\|")
            lines.append(
                f"| `{metadata['id']}` | [{title}]({document.path}) | "
                f"`{metadata['versao']}` | `{metadata['status']}` | "
                f"`{metadata['tipo']}` | `{document.path}` |"
            )
        lines.append("")


def generate_catalog(documents: list[Document]) -> str:
    counts = Counter(document.layer for document in documents)
    lines = [
        yaml_front_matter(CATALOG_METADATA),
        "# Catálogo Documental do Pragmatismo Cívico",
        "",
        "Este catálogo apresenta a fonte canônica dos documentos públicos, seus identificadores, versões, estados e relações principais.",
        "",
        "Ele é gerado a partir do `mkdocs.yml` e dos metadados de cada documento. A presença no catálogo não significa aprovação, estabilidade ou validação empírica; essas propriedades são determinadas pelo campo `status` e pelo histórico correspondente.",
        "",
        "## Visão geral",
        "",
        "| Camada | Documentos |",
        "|---|---:|",
    ]
    lines.extend(f"| {layer} | {counts[layer]} |" for layer in LAYER_ORDER)
    lines.extend([f"| **Total** | **{len(documents)}** |", ""])

    append_document_tables(lines, documents)

    lines.extend(
        [
            "## Mapa de dependências obrigatórias",
            "",
            "A tabela registra apenas `depende_de`. Relações complementares aparecem na seção seguinte.",
            "",
            "| Documento | Depende de | Produz entrada para |",
            "|---|---|---|",
        ]
    )
    for document in sorted(documents, key=lambda item: str(item.metadata["id"])):
        metadata = document.metadata
        lines.append(
            f"| `{metadata['id']}` | {format_list(metadata.get('depende_de'))} | "
            f"{format_list(metadata.get('produz_entrada_para'))} |"
        )

    lines.extend(
        [
            "",
            "## Relações complementares",
            "",
            "| Documento | Relaciona-se com |",
            "|---|---|",
        ]
    )
    for document in sorted(documents, key=lambda item: str(item.metadata["id"])):
        related = document.metadata.get("relaciona_se_com")
        if related:
            lines.append(f"| `{document.metadata['id']}` | {format_list(related)} |")

    lines.extend(
        [
            "",
            "## Rotas recomendadas",
            "",
            "### Conhecer o framework",
            "",
            "`PORTAL-INICIO` → `GUIA-COMECAR` → `CARTA-DE-PRINCIPIOS` → `SPECIFICATION` → `FRAMEWORK-DE-REFERENCIA` → `TEORIA-DO-PRAGMATISMO-CIVICO` → `GLOSSARIO`.",
            "",
            "### Aplicar o método",
            "",
            "`CICLO-PC-001` → `PPC-001` → `PPC-002` → `PPC-003` → `PPC-004` → `MODELO-TDM-001` → `PPC-005` → `PPC-006` → `PPC-007` → `PPC-008`.",
            "",
            "### Compreender e propor mudanças",
            "",
            "`PPC-000` → `PPC-000A` → `PPC-META-001` → `GOV-005` → `FICHA-GOV-005` → `ARQ-001` → `ARQ-002` → `ARQ-003` → `CATALOGO-DOCUMENTAL`.",
            "",
            "## Limites e manutenção",
            "",
            "- a branch padrão do repositório é a fonte canônica;",
            "- o catálogo deve ser regenerado quando a navegação ou os metadados mudarem;",
            "- aplicações concluídas devem preservar a versão efetivamente utilizada;",
            "- documentos em `rascunho` ou `piloto` não devem ser apresentados como estáveis;",
            "- a ausência de estudos de caso oficiais permanece uma limitação do framework.",
            "",
            "## Histórico de alterações",
            "",
            "| Versão | Data | Tipo | Alteração | Responsável |",
            "|---|---|---|---|---|",
            "| 0.1.0 | 2026-07-18 | inicial | Criação do catálogo público, agrupamento por camada e mapa das relações documentais | Projeto Pragmatismo Cívico |",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default=CATALOG_PATH)
    args = parser.parse_args()

    documents = load_documents(include_catalog=True)
    output_path = Path(args.output)
    if not output_path.is_absolute():
        output_path = ROOT / output_path
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(generate_catalog(documents), encoding="utf-8")
    print(f"Catálogo gerado em {output_path} com {len(documents)} documentos.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (FileNotFoundError, TypeError, ValueError, yaml.YAMLError) as error:
        print(f"Erro ao gerar catálogo: {error}", file=sys.stderr)
        raise SystemExit(1) from error
