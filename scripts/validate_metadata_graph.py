"""Valida identificadores, dependências e reciprocidade do grafo documental."""

from __future__ import annotations

import sys

from generate_catalog import load_documents


ALLOWED_EXTERNAL_OUTPUTS = {"VALIDACAO-AUTOMATICA-DE-METADADOS"}
ALLOWED_STATUSES = {"rascunho", "piloto", "revisao-publica", "estavel", "obsoleto", "arquivado"}


def as_string_list(value: object, field: str, document_id: str) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise TypeError(f"{field} deve ser lista de strings em {document_id}")
    return value


def main() -> int:
    documents = load_documents(include_catalog=True)
    by_id = {str(document.metadata["id"]): document for document in documents}
    errors: list[str] = []

    for document_id, document in sorted(by_id.items()):
        metadata = document.metadata
        status = str(metadata.get("status"))
        if status not in ALLOWED_STATUSES:
            errors.append(f"estado não canônico em {document_id}: {status}")

        dependencies = as_string_list(metadata.get("depende_de"), "depende_de", document_id)
        outputs = as_string_list(
            metadata.get("produz_entrada_para"),
            "produz_entrada_para",
            document_id,
        )

        for dependency in dependencies:
            if dependency not in by_id:
                errors.append(f"dependência inexistente: {document_id} depende de {dependency}")

        for target_id in outputs:
            if target_id in ALLOWED_EXTERNAL_OUTPUTS:
                continue
            target = by_id.get(target_id)
            if target is None:
                errors.append(f"saída aponta para identificador inexistente: {document_id} → {target_id}")
                continue
            target_dependencies = as_string_list(
                target.metadata.get("depende_de"),
                "depende_de",
                target_id,
            )
            if document_id not in target_dependencies:
                errors.append(
                    "saída obrigatória sem dependência recíproca: "
                    f"{document_id} → {target_id}"
                )

    if errors:
        for error in errors:
            print(f"ERRO: {error}", file=sys.stderr)
        return 1

    print(
        f"Grafo documental válido: {len(documents)} documentos, "
        "identificadores únicos e saídas obrigatórias recíprocas."
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (FileNotFoundError, TypeError, ValueError) as error:
        print(f"ERRO: {error}", file=sys.stderr)
        raise SystemExit(1) from error
