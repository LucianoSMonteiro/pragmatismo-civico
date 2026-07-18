"""Valida metadados, identificadores e relações do acervo documental."""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from datetime import date

from generate_catalog import ROOT, Document, load_documents


VERSION_RE = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")
LANGUAGE_RE = re.compile(r"^[a-z]{2,3}(?:-[A-Z]{2})?$")
ALLOWED_STATUSES = {
    "ideia",
    "proposta",
    "rascunho",
    "revisao-publica",
    "piloto",
    "estavel",
    "em-revisao",
    "substituido",
    "obsoleto",
    "arquivado",
}
ALLOWED_COMPATIBILITY = {"inicial", "compativel", "parcial", "incompativel"}
ALLOWED_EXTERNAL_REFERENCES = {"MKDOCS", "VALIDACAO-AUTOMATICA-DE-METADADOS"}
LIST_FIELDS = (
    "responsaveis",
    "aprovadores",
    "depende_de",
    "produz_entrada_para",
    "relaciona_se_com",
    "substitui",
)
REQUIRED_FIELDS = (
    "id",
    "titulo",
    "versao",
    "status",
    "tipo",
    "idioma",
    "data_criacao",
    "data_versao",
    "responsaveis",
    "aprovadores",
    "depende_de",
    "produz_entrada_para",
    "relaciona_se_com",
    "substitui",
    "substituido_por",
    "compatibilidade",
    "proxima_revisao",
)


@dataclass
class ValidationResult:
    documents: int = 0
    dependencies: int = 0
    outputs: int = 0
    complementary_relations: int = 0
    substitutions: int = 0
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


def as_string_list(value: object, field_name: str, document_id: str) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise TypeError(f"{field_name} deve ser lista de strings em {document_id}")
    return value


def parse_date(value: object, field_name: str, document_id: str, *, nullable: bool) -> date | None:
    if value is None:
        if nullable:
            return None
        raise ValueError(f"{field_name} não pode ser nulo em {document_id}")
    if isinstance(value, date):
        return value
    if isinstance(value, str):
        try:
            return date.fromisoformat(value)
        except ValueError as error:
            raise ValueError(
                f"{field_name} deve usar AAAA-MM-DD em {document_id}: {value}"
            ) from error
    raise TypeError(f"{field_name} possui tipo inválido em {document_id}")


def has_current_version_in_history(document: Document) -> bool:
    source = (ROOT / document.path).read_text(encoding="utf-8")
    version = re.escape(str(document.metadata["versao"]))
    history_match = re.search(
        r"^##+\s+(?:\d+(?:\.\d+)*\s*[-—.]?\s*)?"
        r"Hist[oó]rico de (?:altera[cç][oõ]es|vers[oõ]es)\s*$",
        source,
        flags=re.MULTILINE | re.IGNORECASE,
    )
    if history_match is None:
        return False
    history = source[history_match.end() :]
    return (
        re.search(
            rf"^\|\s*(?:`|\*\*)?{version}(?:`|\*\*)?\s*\|",
            history,
            flags=re.MULTILINE,
        )
        is not None
    )


def detect_dependency_cycles(by_id: dict[str, Document]) -> list[str]:
    graph: dict[str, list[str]] = {}
    for document_id, document in by_id.items():
        graph[document_id] = [
            target
            for target in as_string_list(
                document.metadata.get("depende_de"), "depende_de", document_id
            )
            if target in by_id
        ]

    cycles: set[tuple[str, ...]] = set()
    visiting: list[str] = []
    visited: set[str] = set()

    def walk(node: str) -> None:
        if node in visiting:
            start = visiting.index(node)
            cycle = visiting[start:] + [node]
            rotations = [
                tuple(cycle[index:-1] + cycle[:index] + [cycle[index]])
                for index in range(len(cycle) - 1)
            ]
            cycles.add(min(rotations))
            return
        if node in visited:
            return
        visiting.append(node)
        for target in graph[node]:
            walk(target)
        visiting.pop()
        visited.add(node)

    for document_id in sorted(graph):
        walk(document_id)

    return [" → ".join(cycle) for cycle in sorted(cycles)]


def validate_documents(documents: list[Document] | None = None) -> ValidationResult:
    if documents is None:
        documents = load_documents(include_catalog=True)

    result = ValidationResult(documents=len(documents))
    by_id = {str(document.metadata["id"]): document for document in documents}

    for document_id, document in sorted(by_id.items()):
        metadata = document.metadata

        missing = [field_name for field_name in REQUIRED_FIELDS if field_name not in metadata]
        if missing:
            result.errors.append(
                f"campos obrigatórios ausentes em {document_id}: {', '.join(missing)}"
            )
            continue

        version = str(metadata.get("versao"))
        if VERSION_RE.fullmatch(version) is None:
            result.errors.append(f"versão inválida em {document_id}: {version}")

        status = str(metadata.get("status"))
        if status not in ALLOWED_STATUSES:
            result.errors.append(f"estado não canônico em {document_id}: {status}")

        compatibility = str(metadata.get("compatibilidade"))
        if compatibility not in ALLOWED_COMPATIBILITY:
            result.errors.append(
                f"compatibilidade inválida em {document_id}: {compatibility}"
            )

        language = str(metadata.get("idioma"))
        if LANGUAGE_RE.fullmatch(language) is None:
            result.errors.append(f"idioma inválido em {document_id}: {language}")

        try:
            creation_date = parse_date(
                metadata.get("data_criacao"), "data_criacao", document_id, nullable=True
            )
            version_date = parse_date(
                metadata.get("data_versao"), "data_versao", document_id, nullable=False
            )
            review_date = parse_date(
                metadata.get("proxima_revisao"),
                "proxima_revisao",
                document_id,
                nullable=True,
            )
            if creation_date and version_date and creation_date > version_date:
                result.errors.append(
                    f"data de criação posterior à versão em {document_id}"
                )
            if version_date and version_date > date.today():
                result.errors.append(f"data de versão futura em {document_id}: {version_date}")
            if review_date and version_date and review_date < version_date:
                result.errors.append(
                    f"próxima revisão anterior à versão em {document_id}"
                )
        except (TypeError, ValueError) as error:
            result.errors.append(str(error))

        for field_name in LIST_FIELDS:
            try:
                values = as_string_list(metadata.get(field_name), field_name, document_id)
            except TypeError as error:
                result.errors.append(str(error))
                continue
            if len(values) != len(set(values)):
                result.errors.append(f"itens duplicados em {field_name} de {document_id}")
            if document_id in values:
                result.errors.append(f"autorreferência em {field_name} de {document_id}")

        try:
            responsibles = as_string_list(
                metadata.get("responsaveis"), "responsaveis", document_id
            )
            if not responsibles:
                result.errors.append(f"responsáveis ausentes em {document_id}")

            dependencies = as_string_list(
                metadata.get("depende_de"), "depende_de", document_id
            )
            outputs = as_string_list(
                metadata.get("produz_entrada_para"),
                "produz_entrada_para",
                document_id,
            )
            related = as_string_list(
                metadata.get("relaciona_se_com"), "relaciona_se_com", document_id
            )
            replacements = as_string_list(
                metadata.get("substitui"), "substitui", document_id
            )
        except TypeError:
            continue

        result.dependencies += len(dependencies)
        result.outputs += len(outputs)
        result.complementary_relations += len(related)
        result.substitutions += len(replacements)

        for field_name, targets in (
            ("depende_de", dependencies),
            ("produz_entrada_para", outputs),
            ("relaciona_se_com", related),
            ("substitui", replacements),
        ):
            for target_id in targets:
                if target_id not in by_id and target_id not in ALLOWED_EXTERNAL_REFERENCES:
                    result.errors.append(
                        f"referência inexistente em {field_name}: {document_id} → {target_id}"
                    )

        for target_id in outputs:
            if target_id not in by_id:
                continue
            target_dependencies = as_string_list(
                by_id[target_id].metadata.get("depende_de"),
                "depende_de",
                target_id,
            )
            if document_id not in target_dependencies:
                result.errors.append(
                    f"saída obrigatória sem dependência recíproca: {document_id} → {target_id}"
                )

        for replaced_id in replacements:
            if replaced_id not in by_id:
                continue
            reciprocal = by_id[replaced_id].metadata.get("substituido_por")
            if reciprocal != document_id:
                result.errors.append(
                    f"substituição sem reciprocidade: {document_id} substitui {replaced_id}, "
                    f"mas o documento substituído declara {reciprocal!r}"
                )

        replacement_id = metadata.get("substituido_por")
        if replacement_id is not None:
            if not isinstance(replacement_id, str):
                result.errors.append(
                    f"substituido_por deve ser string ou nulo em {document_id}"
                )
            elif replacement_id not in by_id:
                result.errors.append(
                    f"substituto inexistente: {document_id} → {replacement_id}"
                )
            else:
                reciprocal = as_string_list(
                    by_id[replacement_id].metadata.get("substitui"),
                    "substitui",
                    replacement_id,
                )
                if document_id not in reciprocal:
                    result.errors.append(
                        f"substituição sem reciprocidade: {document_id} é substituído por "
                        f"{replacement_id}, mas não consta em substitui"
                    )

        if status == "substituido" and metadata.get("substituido_por") is None:
            result.errors.append(
                f"documento com estado substituído sem substituido_por: {document_id}"
            )
        if metadata.get("substituido_por") is not None and status not in {
            "substituido",
            "obsoleto",
            "arquivado",
        }:
            result.errors.append(
                f"documento vigente declara substituido_por sem estado compatível: {document_id}"
            )

        if compatibility == "inicial" and version != "0.1.0":
            result.warnings.append(
                f"compatibilidade inicial em versão diferente de 0.1.0: {document_id} {version}"
            )

        if not has_current_version_in_history(document):
            result.errors.append(
                f"histórico não contém a versão corrente {version}: {document_id}"
            )

    for cycle in detect_dependency_cycles(by_id):
        result.errors.append(f"ciclo de dependências obrigatórias: {cycle}")

    return result


def main() -> int:
    result = validate_documents()

    for warning in result.warnings:
        print(f"AVISO: {warning}", file=sys.stderr)
    for error in result.errors:
        print(f"ERRO: {error}", file=sys.stderr)

    if not result.ok:
        return 1

    print(
        "Metadados válidos: "
        f"{result.documents} documentos, {result.dependencies} dependências, "
        f"{result.outputs} saídas, {result.complementary_relations} relações "
        f"complementares e {result.substitutions} substituições."
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (FileNotFoundError, TypeError, ValueError) as error:
        print(f"ERRO: {error}", file=sys.stderr)
        raise SystemExit(1) from error
