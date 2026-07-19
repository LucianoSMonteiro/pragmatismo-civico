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
    payload = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {"sub_bacias": "Itapeba teste"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[-42.9, -22.9], [-42.8, -22.9], [-42.8, -22.8], [-42.9, -22.9]]],
                },
            }
        ],
    }

    def do_POST(self) -> None:  # noqa: N802
        length = int(self.headers.get("Content-Length", "0"))
        query = parse_qs(self.rfile.read(length).decode("utf-8"))
        if query.get("f") != ["geojson"] or query.get("outSR") != ["4674"]:
            self.send_response(400)
            self.end_headers()
            return
        raw = json.dumps(self.payload).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/geo+json")
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def log_message(self, format: str, *args: object) -> None:
        return


class ConsultarSubbaciaIneaTest(unittest.TestCase):
    def test_preserva_resposta_manifesto_e_relatorio(self) -> None:
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
                self.assertEqual(manifest["query"]["method"], "POST")
                self.assertEqual(manifest["query"]["attempts_used"], 1)
                self.assertEqual(manifest["http"]["status"], 200)
                self.assertEqual(manifest["response"]["feature_count"], 1)
                self.assertEqual(manifest["response"]["matched_names"], ["Itapeba teste"])
                self.assertFalse(manifest["response"]["empty"])
                self.assertEqual(len(manifest["response"]["sha256"]), 64)
                self.assertTrue((output / "response.geojson").is_file())
                self.assertIn("correspondencia_nominal", manifest["interpretation"])
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=2)


if __name__ == "__main__":
    unittest.main()
