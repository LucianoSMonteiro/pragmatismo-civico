from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "validar_geojson_subbacia.py"
FIXTURE = ROOT / "tests" / "fixtures" / "itapeba_subbacia_sintetica.geojson"


class ValidarGeojsonSubbaciaTest(unittest.TestCase):
    def executar(self, input_path: Path, base: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--input",
                str(input_path),
                "--manifest",
                str(base / "manifest.json"),
                "--report",
                str(base / "report.md"),
                "--source-url",
                "synthetic://fixture",
                "--accessed-at",
                "2026-07-18",
                "--source-srid",
                "EPSG:4674",
                "--expected-name",
                "Itapeba",
                "--expected-envelope",
                "-43.1",
                "-23.1",
                "-42.5",
                "-22.5",
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_geojson_sintetico_valido(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            result = self.executar(FIXTURE, base)

            self.assertEqual(result.returncode, 0, result.stderr)
            manifest_path = base / "manifest.json"
            report_path = base / "report.md"
            self.assertTrue(manifest_path.is_file())
            self.assertTrue(report_path.is_file())

            data = json.loads(manifest_path.read_text(encoding="utf-8"))
            summary = data["summary"]
            self.assertTrue(summary["ok"])
            self.assertEqual(summary["feature_count"], 1)
            self.assertEqual(summary["polygon_count"], 1)
            self.assertEqual(summary["ring_count"], 1)
            self.assertEqual(summary["vertex_count"], 5)
            self.assertEqual(summary["geometry_types"], ["Polygon"])
            self.assertEqual(summary["expected_name_matches"], 1)
            self.assertGreater(summary["estimated_area_km2"], 0)
            self.assertEqual(len(data["source"]["sha256"]), 64)
            self.assertEqual(data["source"]["declared_srid"], "EPSG:4674")
            self.assertEqual(data["errors"], [])
            self.assertIn("APROVADO", report_path.read_text(encoding="utf-8"))

    def test_rejeita_anel_aberto(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            payload = json.loads(FIXTURE.read_text(encoding="utf-8"))
            payload["features"][0]["geometry"]["coordinates"][0][-1] = [-42.85, -22.90]
            invalid_path = base / "invalido.geojson"
            invalid_path.write_text(
                json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )

            result = self.executar(invalid_path, base)

            self.assertEqual(result.returncode, 1)
            data = json.loads((base / "manifest.json").read_text(encoding="utf-8"))
            self.assertFalse(data["summary"]["ok"])
            self.assertTrue(any("anel não fechado" in item for item in data["errors"]))
            self.assertIn("REPROVADO", (base / "report.md").read_text(encoding="utf-8"))


def load_module_from_tests(name: str):
    path = ROOT / "tests" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Não foi possível carregar {path}.")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def load_tests(loader, standard_tests, pattern):
    """Mantém um ponto de entrada para geometria, coleta e evidências do caso."""
    suite = unittest.TestSuite()
    suite.addTests(standard_tests)
    for module_name in (
        "test_coletar_geoinea_subbacia",
        "test_geoinea_ipv4_transport",
        "test_validar_registro_documentos_tecnicos",
    ):
        suite.addTests(loader.loadTestsFromModule(load_module_from_tests(module_name)))
    return suite


if __name__ == "__main__":
    unittest.main()
