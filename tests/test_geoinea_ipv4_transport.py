from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from coletar_geoinea_subbacia import CollectionError
from geoinea_ipv4_transport import curl_ipv4_fetch


class GeoIneaIpv4TransportTest(unittest.TestCase):
    @patch("geoinea_ipv4_transport.subprocess.run")
    def test_preserva_corpo_e_metadados_http(self, run_mock) -> None:
        run_mock.return_value = subprocess.CompletedProcess(
            args=["curl"],
            returncode=0,
            stdout=(
                b'{"name":"GPL_SUBBACIAS_ERJ_50"}'
                b"\n200\napplication/json; charset=utf-8\n"
                b"https://geoportal.inea.rj.gov.br/server/rest/services/teste"
            ),
            stderr=b"",
        )

        record = curl_ipv4_fetch("https://example.invalid/layer?f=pjson", 60)

        self.assertEqual(record.status, 200)
        self.assertEqual(record.body, b'{"name":"GPL_SUBBACIAS_ERJ_50"}')
        self.assertEqual(record.content_type, "application/json; charset=utf-8")
        self.assertEqual(
            record.url,
            "https://geoportal.inea.rj.gov.br/server/rest/services/teste",
        )
        command = run_mock.call_args.args[0]
        self.assertIn("--ipv4", command)
        self.assertIn("--fail-with-body", command)
        self.assertIn("https://example.invalid/layer?f=pjson", command)
        self.assertEqual(run_mock.call_args.kwargs["timeout"], 70)

    @patch("geoinea_ipv4_transport.subprocess.run")
    def test_rejeita_falha_de_conexao(self, run_mock) -> None:
        run_mock.return_value = subprocess.CompletedProcess(
            args=["curl"],
            returncode=28,
            stdout=b"",
            stderr=b"curl: (28) Failed to connect",
        )

        with self.assertRaisesRegex(CollectionError, "código 28"):
            curl_ipv4_fetch("https://example.invalid/layer?f=pjson", 30)

    @patch("geoinea_ipv4_transport.subprocess.run")
    def test_rejeita_status_http_fora_de_2xx(self, run_mock) -> None:
        run_mock.return_value = subprocess.CompletedProcess(
            args=["curl"],
            returncode=0,
            stdout=b'{"error":"indisponivel"}\n503\napplication/json\nhttps://example.invalid',
            stderr=b"",
        )

        with self.assertRaisesRegex(CollectionError, "HTTP 503"):
            curl_ipv4_fetch("https://example.invalid/layer?f=pjson", 30)


if __name__ == "__main__":
    unittest.main()
