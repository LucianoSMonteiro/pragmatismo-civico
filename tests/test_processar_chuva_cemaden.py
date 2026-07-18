from __future__ import annotations

import csv
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "processar_chuva_cemaden.py"
FIXTURE = ROOT / "tests" / "fixtures" / "cemaden_itapeba_sintetico.csv"


class ProcessarChuvaCemadenTest(unittest.TestCase):
    def test_processamento_sintetico(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            raw = base / "raw"
            raw.mkdir()
            shutil.copy2(FIXTURE, raw / "2022-04.csv")

            output = base / "processed" / "itapeba.csv"
            manifest = base / "manifest" / "manifest.json"
            report = base / "reports" / "quality.md"
            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--input-dir",
                    str(raw),
                    "--output",
                    str(output),
                    "--manifest",
                    str(manifest),
                    "--report",
                    str(report),
                    "--station-id",
                    "3717",
                ],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue(output.is_file())
            self.assertTrue(manifest.is_file())
            self.assertTrue(report.is_file())

            data = json.loads(manifest.read_text(encoding="utf-8"))
            counts = data["counts"]
            self.assertEqual(counts["rows_read"], 8)
            self.assertEqual(counts["rows_matched"], 7)
            self.assertEqual(counts["records_normalized"], 5)
            self.assertEqual(counts["filtered_out"], 1)
            self.assertEqual(counts["invalid_timestamp"], 1)
            self.assertEqual(counts["invalid_rainfall"], 1)
            self.assertEqual(counts["negative_values"], 1)
            self.assertEqual(counts["duplicate_rows"], 2)
            self.assertEqual(counts["gaps_gt_3x_interval"], 1)
            self.assertEqual(data["sources"][0]["path"], "2022-04.csv")
            self.assertEqual(len(data["sources"][0]["sha256"]), 64)

            with output.open(encoding="utf-8", newline="") as stream:
                rows = list(csv.DictReader(stream))
            self.assertEqual(len(rows), 5)
            self.assertEqual(rows[0]["timestamp_utc"], "2022-04-01T00:00:00Z")
            self.assertTrue(rows[0]["timestamp_america_sao_paulo"].endswith("-03:00"))
            self.assertIn("duplicate_timestamp", rows[2]["qc_flags"])
            self.assertIn("gap_after_previous", rows[-1]["qc_flags"])
            self.assertIn("negative_value", rows[-1]["qc_flags"])


if __name__ == "__main__":
    unittest.main()
