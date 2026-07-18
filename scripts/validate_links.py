"""Valida destinos internos e âncoras dos documentos navegáveis."""

from __future__ import annotations

import html
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import unquote, urlsplit

from markdown.extensions.toc import slugify

from generate_catalog import ROOT, Document, load_documents


FENCE_RE = re.compile(r"^\s*(```+|~~~+).*?^\s*\1\s*$", re.MULTILINE | re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
HTML_LINK_RE = re.compile(r"\b(?:href|src)=[\"']([^\"']+)[\"']", re.IGNORECASE)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$", re.MULTILINE)
EXPLICIT_ID_RE = re.compile(r"\s*\{[^}]*#([A-Za-z][\w:.-]*)[^}]*\}\s*$")
TAG_RE = re.compile(r"<[^>]+>")
EXTERNAL_SCHEMES = {"http", "https", "mailto", "tel", "data", "javascript"}
IGNORED_PREFIXES = ("{{", "${", "<%")


@dataclass
class LinkValidationResult:
    documents: int = 0
    links: int = 0
    internal_links: int = 0
    anchors_checked: int = 0
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


def strip_code(text: str) -> str:
    text = FENCE_RE.sub("", text)
    return INLINE_CODE_RE.sub("", text)


def normalize_destination(raw: str) -> str:
    destination = html.unescape(raw.strip())
    if destination.startswith("<") and ">" in destination:
        destination = destination[1 : destination.index(">")]
    else:
        # Títulos opcionais de links Markdown aparecem após o destino.
        destination = re.split(r"\s+[\"'(]", destination, maxsplit=1)[0]
    return destination.strip()


def extract_destinations(text: str) -> list[str]:
    clean = strip_code(text)
    destinations = [normalize_destination(match.group(1)) for match in MARKDOWN_LINK_RE.finditer(clean)]
    destinations.extend(normalize_destination(match.group(1)) for match in HTML_LINK_RE.finditer(clean))
    return [destination for destination in destinations if destination]


def heading_anchors(text: str) -> set[str]:
    clean = strip_code(text)
    anchors: set[str] = set()
    counts: dict[str, int] = {}

    for match in HEADING_RE.finditer(clean):
        heading = match.group(2).strip()
        explicit = EXPLICIT_ID_RE.search(heading)
        if explicit:
            base = explicit.group(1)
        else:
            heading = EXPLICIT_ID_RE.sub("", heading)
            heading = TAG_RE.sub("", heading)
            heading = re.sub(r"[*_~]", "", heading)
            base = slugify(heading, "-")

        count = counts.get(base, 0)
        anchor = base if count == 0 else f"{base}_{count}"
        counts[base] = count + 1
        anchors.add(anchor)

    # IDs HTML explícitos também são destinos válidos.
    for match in re.finditer(r"\bid=[\"']([^\"']+)[\"']", clean, re.IGNORECASE):
        anchors.add(match.group(1))

    return anchors


def resolve_target(source_path: Path, raw_path: str) -> Path:
    decoded = unquote(raw_path)
    if decoded.startswith("/"):
        return (ROOT / decoded.lstrip("/")).resolve()
    return (source_path.parent / decoded).resolve()


def display_path(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def validate_links(documents: list[Document] | None = None) -> LinkValidationResult:
    if documents is None:
        documents = load_documents(include_catalog=True)

    result = LinkValidationResult(documents=len(documents))
    anchor_cache: dict[Path, set[str]] = {}

    for document in documents:
        source_path = (ROOT / document.path).resolve()
        text = source_path.read_text(encoding="utf-8")

        for destination in extract_destinations(text):
            result.links += 1
            if destination.startswith(IGNORED_PREFIXES):
                result.warnings.append(
                    f"destino dinâmico não validado em {document.path}: {destination}"
                )
                continue

            parsed = urlsplit(destination)
            if parsed.scheme.lower() in EXTERNAL_SCHEMES or parsed.netloc:
                continue

            result.internal_links += 1
            target_path = source_path if not parsed.path else resolve_target(source_path, parsed.path)

            try:
                target_path.relative_to(ROOT)
            except ValueError:
                result.errors.append(
                    f"link escapa do repositório em {document.path}: {destination}"
                )
                continue

            if not target_path.exists():
                result.errors.append(
                    f"destino inexistente em {document.path}: {destination} "
                    f"→ {display_path(target_path)}"
                )
                continue

            if parsed.fragment:
                if target_path.is_dir():
                    result.errors.append(
                        f"âncora aplicada a diretório em {document.path}: {destination}"
                    )
                    continue
                if target_path.suffix.lower() not in {".md", ".markdown"}:
                    result.warnings.append(
                        f"âncora em arquivo não Markdown não validada em {document.path}: {destination}"
                    )
                    continue

                result.anchors_checked += 1
                anchors = anchor_cache.setdefault(
                    target_path,
                    heading_anchors(target_path.read_text(encoding="utf-8")),
                )
                fragment = unquote(parsed.fragment)
                if fragment not in anchors:
                    result.errors.append(
                        f"âncora inexistente em {document.path}: {destination} "
                        f"(destino {display_path(target_path)})"
                    )

    return result


def main() -> int:
    result = validate_links()

    for warning in result.warnings:
        print(f"AVISO: {warning}", file=sys.stderr)
    for error in result.errors:
        print(f"ERRO: {error}", file=sys.stderr)

    if not result.ok:
        return 1

    print(
        "Links válidos: "
        f"{result.documents} documentos, {result.links} destinos encontrados, "
        f"{result.internal_links} internos e {result.anchors_checked} âncoras verificadas."
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (FileNotFoundError, TypeError, ValueError) as error:
        print(f"ERRO: {error}", file=sys.stderr)
        raise SystemExit(1) from error
