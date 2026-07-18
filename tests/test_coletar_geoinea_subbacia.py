from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import sys

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from coletar_geoinea_subbacia import ResponseRecord, collect, normalize_text, select_matches


class FakeGeoInea:
    def __init__(self) -> None:
        self.urls: list[str] = []

    @staticmethod
    def response(url: str, payload: object, content_type: str = "application/json") -> ResponseRecord:
        return ResponseRecord(
            url=url,
            body=(json.dumps(payload, ensure_ascii=False) + "\n").encode("utf-8"),
            content_type=content_type,
            status=200,
        )

    def __call__(self, url: str, timeout: int) -> ResponseRecord:
        self.urls.append(url)
        parsed = urlparse(url)
        params = parse_qs(parsed.query)

        if parsed.path.endswith("/MapServer/4"):
            return self.response(
                url,
                {
                    "name": "banco_geoinea.gerget.GPL_SUBBACIAS_ERJ_50",
                    "displayField": "sub_bacias",
                    "geometryType": "esriGeometryPolygon",
                    "serviceItemId": "e20f5ed7320d45e7a2d0fa2f0e84cf54",
                    "maxRecordCount": 2000,
                    "extent": {"spatialReference": {"wkid": 4674}},
                },
            )

        if params.get("returnIdsOnly") == ["true"]:
            return self.response(
                url,
                {"objectIdFieldName": "objectid", "objectIds": [2, 1]},
            )

        if params.get("returnGeometry") == ["false"]:
            return self.response(
                url,
                {
                    "features": [
                        {"attributes": {"objectid": 1, "sub_bacias": "Itapeba", "rh": "RH-V"}},
                        {"attributes": {"objectid": 2, "sub_bacias": "Inoã", "rh": "RH-V"}},
                    ]
                },
            )

        if params.get("f") == ["geojson"]:
            return self.response(
                url,
                {
                    "type": "FeatureCollection",
                    "features": [
                        {
                            "type": "Feature",
                            "properties": {"objectid": 1, "sub_bacias": "Itapeba", "rh": "RH-V"},
                            "geometry": {
                                "type": "Polygon",
                                "coordinates": [
                                    [
                                        [-42.9, -22.95],
                                        [-42.8, -22.95],
                                        [-42.8, -22.85],
                                        [-42.9, -22.85],
                                        [-42.9, -22.95],
                                    ]
                                ],
                            },
                        }
                    ],
                },
                "application/geo+json",
            )

        raise AssertionError(f"URL não prevista: {url}")


class ColetarGeoIneaSubbaciaTest(unittest.TestCase):
    def test_normalizacao_e_correspondencia(self) -> None:
        self.assertEqual(normalize_text("  ITAPÉBA  "), "itapeba")
        features = [
            {"attributes": {"sub_bacias": "Sub-bacia de Itapéba"}},
            {"attributes": {"sub_bacias": "Inoã"}},
        ]
        matches = select_matches(features, "Itapeba")
        self.assertEqual(len(matches), 1)

    def test_coleta_com_correspondencia_preserva_geometria(self) -> None:
        fake = FakeGeoInea()
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary)
            manifest = collect(
                output_dir=output,
                search_term="Itapeba",
                timeout=5,
                fetch=fake,
            )

            result = manifest["result"]
            self.assertTrue(result["query_completed"])
            self.assertEqual(result["object_id_count"], 2)
            self.assertEqual(result["attribute_feature_count"], 2)
            self.assertEqual(result["match_count"], 1)
            self.assertEqual(result["matched_object_ids"], [1])
            self.assertTrue(result["geometry_downloaded"])

            self.assertTrue((output / "layer-metadata.raw.json").is_file())
            self.assertTrue((output / "object-ids.raw.json").is_file())
            self.assertTrue((output / "attributes-001.raw.json").is_file())
            self.assertTrue((output / "attributes-combined.json").is_file())
            self.assertTrue((output / "matches.json").is_file())
            self.assertTrue((output / "matched-geometry.geojson").is_file())
            self.assertTrue((output / "query-manifest.json").is_file())
            self.assertTrue((output / "query-report.md").is_file())

            persisted = json.loads((output / "query-manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(persisted["result"]["match_count"], 1)
            self.assertEqual(persisted["service"]["spatial_reference_wkid"], 4674)
            self.assertEqual(len(persisted["files"]["matched_geometry"]["sha256"]), 64)

    def test_consulta_sem_correspondencia_e_resultado_valido(self) -> None:
        fake = FakeGeoInea()
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary)
            manifest = collect(
                output_dir=output,
                search_term="Nome inexistente",
                timeout=5,
                fetch=fake,
            )

            self.assertTrue(manifest["result"]["query_completed"])
            self.assertEqual(manifest["result"]["match_count"], 0)
            self.assertFalse(manifest["result"]["geometry_downloaded"])
            self.assertFalse((output / "matched-geometry.geojson").exists())
            report = (output / "query-report.md").read_text(encoding="utf-8")
            self.assertIn("Nenhuma feição contém", report)
            self.assertIn("não autoriza concluir", report)


if __name__ == "__main__":
    unittest.main()
