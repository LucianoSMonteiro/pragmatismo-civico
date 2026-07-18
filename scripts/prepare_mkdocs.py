"""Prepara uma árvore temporária para o build do portal MkDocs.

Os documentos canônicos permanecem nos caminhos atuais do repositório. O MkDocs,
porém, exige que ``docs_dir`` seja um diretório filho do arquivo de configuração.
Este script copia somente os documentos declarados na navegação e os ativos
públicos, preservando os caminhos relativos usados por links e URLs de edição.
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path
from typing import Iterator

import yaml


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "mkdocs.yml"


def iter_nav_paths(node: object) -> Iterator[str]:
    """Percorre recursivamente a configuração ``nav`` e retorna caminhos."""
    if isinstance(node, str):
        yield node
        return

    if isinstance(node, list):
        for item in node:
            yield from iter_nav_paths(item)
        return

    if isinstance(node, dict):
        for value in node.values():
            yield from iter_nav_paths(value)


def copy_path(relative_path: str, destination_root: Path) -> None:
    """Copia um arquivo do repositório preservando seu caminho relativo."""
    source = ROOT / relative_path
    if not source.is_file():
        raise FileNotFoundError(
            f"Arquivo declarado na publicação não encontrado: {relative_path}"
        )

    destination = destination_root / relative_path
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def main() -> int:
    with CONFIG_PATH.open("r", encoding="utf-8") as config_file:
        config = yaml.safe_load(config_file) or {}

    docs_dir_value = config.get("docs_dir")
    if not isinstance(docs_dir_value, str) or not docs_dir_value.strip():
        raise ValueError("mkdocs.yml deve declarar um docs_dir temporário.")

    staging_dir = (ROOT / docs_dir_value).resolve()
    if ROOT not in staging_dir.parents:
        raise ValueError("docs_dir temporário deve permanecer dentro do repositório.")

    if staging_dir.exists():
        shutil.rmtree(staging_dir)
    staging_dir.mkdir(parents=True)

    nav_paths = sorted(set(iter_nav_paths(config.get("nav", []))))
    markdown_paths = [path for path in nav_paths if path.lower().endswith(".md")]

    if not markdown_paths:
        raise ValueError("Nenhum documento Markdown foi encontrado em nav.")

    for relative_path in markdown_paths:
        copy_path(relative_path, staging_dir)

    # Ativos públicos podem ser referenciados por CSS, HTML ou Markdown.
    assets_source = ROOT / "docs" / "assets"
    if assets_source.is_dir():
        shutil.copytree(
            assets_source,
            staging_dir / "docs" / "assets",
            dirs_exist_ok=True,
        )

    # Garante que recursos explicitamente declarados também existam na árvore.
    for key in ("extra_css", "extra_javascript"):
        values = config.get(key, []) or []
        if not isinstance(values, list):
            raise TypeError(f"{key} deve ser uma lista em mkdocs.yml.")
        for relative_path in values:
            if not isinstance(relative_path, str):
                raise TypeError(f"Entrada inválida em {key}: {relative_path!r}")
            copy_path(relative_path, staging_dir)

    print(
        f"Árvore MkDocs preparada em {staging_dir.relative_to(ROOT)} "
        f"com {len(markdown_paths)} documentos navegáveis."
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (FileNotFoundError, TypeError, ValueError, yaml.YAMLError) as error:
        print(f"Erro ao preparar o portal: {error}", file=sys.stderr)
        raise SystemExit(1) from error
