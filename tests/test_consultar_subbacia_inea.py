from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "consultar_subbacia_inea.py"


class Handler(BaseHTTPRequestHandler):
    def do_POST(self) -> None:  # noqa: N802
        length = int(self.headers.get("Content-Length", "0"))
        query = parse_qs(self.rfile.read(length).decode("utf-8"))
        if query.get("f") == ["json"] and query.get("returnGeometry") == ["false"]:
            payload = {
                "features": [
                    {"attributes": {"objectid": 7, "sub_bacias": "Itapeba teste"}},
                    {"attributes": {"objectid": 8, "sub_bacias": "Outra bacia"}},
                ]
            }
            content_type = "application/json"
        elif query.get("f") == ["geojson"] and query.get("objectIds") == ["7"]:
            payload = {
                "type": "FeatureCollection",
                "features": [
                    {
                        "type": "Feature",
                        "properties": {"objectid": 7, "sub_bacias": "Itapeba teste"},
                        "geometry": {
                            "type": "Polygon",
                            "coordinates": [[[-42.9, -22.9], [-42.8, -22.9], [-42.8, -22.8], [-42.9, -22.9]]],
                        },
                    }
                ],
            }
            content_type = "application/geo+json"
        else:
            self.send_response(400)
            self.end_headers()
            return

        raw = json.dumps(payload).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def log_message(self, format: str, *args: object) -> None:
        return


class ConsultarSubbaciaIneaTest(unittest.TestCase):
    def test_preserva_indice_resposta_manifesto_e_relatorio(self) -> None:
        server = HTTPServer(("127.0.0.1", 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            with tempfile.TemporaryDirectory() as temporary:
                output = Path(temporary) / "out"
                result = subprocess.run(
                    [
                        sys.executable,
                        str(SCRIPT),
                        "--name",
                        "Itapeba",
                        "--layer-url",
                        f"http://127.0.0.1:{server.server_port}/query",
                        "--output-dir",
                        str(output),
                        "--timeout",
                        "5",
                        "--retries",
                        "2",
                    ],
                    cwd=ROOT,
                    capture_output=True,
                    text=True,
                    check=False,
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                manifest = json.loads((output / "query-manifest.json").read_text(encoding="utf-8"))
                self.assertEqual(manifest["index_query"]["method"], "POST")
                self.assertEqual(manifest["index_query"]["attempts_used"], 1)
                self.assertEqual(manifest["selection"]["object_ids"], [7])
                self.assertEqual(manifest["selection"]["matched_names"], ["Itapeba teste"])
                self.assertEqual(manifest["response"]["feature_count"], 1)
                self.assertFalse(manifest["response"]["empty"])
                self.assertEqual(manifest["response"]["origin"], "geoinea")
                self.assertEqual(len(manifest["response"]["sha256"]), 64)
                self.assertTrue((output / "index-response.json").is_file())
                self.assertTrue((output / "response.geojson").is_file())
                self.assertIn("correspondencia_nominal", manifest["interpretation"])
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=2)


if __name__ == "__main__":
    unittest.main()
