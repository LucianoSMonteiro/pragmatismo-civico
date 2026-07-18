#!/usr/bin/env python3
"""Transporte HTTP IPv4 para consultas ao GeoINEA em runners de CI.

O módulo existe porque a tentativa com a pilha padrão do Python expirou três
vezes em runner hospedado. Ele não altera filtros, respostas ou critérios de
validação; apenas força IPv4 e preserva os bytes recebidos.
"""

from __future__ import annotations

import subprocess

from coletar_geoinea_subbacia import CollectionError, ResponseRecord, USER_AGENT


def curl_ipv4_fetch(url: str, timeout: int) -> ResponseRecord:
    command = [
        "curl",
        "--ipv4",
        "--silent",
        "--show-error",
        "--fail-with-body",
        "--location",
        "--connect-timeout",
        str(min(30, timeout)),
        "--max-time",
        str(timeout),
        "--header",
        "Accept: application/json, application/geo+json",
        "--user-agent",
        USER_AGENT,
        "--write-out",
        "\n%{http_code}\n%{content_type}\n%{url_effective}",
        url,
    ]
    try:
        completed = subprocess.run(
            command,
            capture_output=True,
            check=False,
            timeout=timeout + 10,
        )
    except FileNotFoundError as error:
        raise CollectionError("curl não está disponível no ambiente.") from error
    except subprocess.TimeoutExpired as error:
        raise CollectionError(f"curl excedeu o tempo limite em {url}.") from error

    if completed.returncode != 0:
        stderr = completed.stderr.decode("utf-8", errors="replace").strip()
        body = completed.stdout[:500]
        raise CollectionError(
            f"curl falhou com código {completed.returncode} em {url}: {stderr}; corpo={body!r}"
        )

    marker = b"\n"
    parts = completed.stdout.rsplit(marker, 3)
    if len(parts) != 4:
        raise CollectionError("Não foi possível separar corpo e metadados da resposta curl.")

    body, status_raw, content_type_raw, effective_url_raw = parts
    try:
        status = int(status_raw.decode("ascii"))
    except ValueError as error:
        raise CollectionError(f"Status HTTP inválido retornado pelo curl: {status_raw!r}.") from error

    if status < 200 or status >= 300:
        raise CollectionError(f"HTTP {status} em {url}: {body[:500]!r}")

    return ResponseRecord(
        url=effective_url_raw.decode("utf-8", errors="replace"),
        body=body,
        content_type=content_type_raw.decode("utf-8", errors="replace") or None,
        status=status,
    )
