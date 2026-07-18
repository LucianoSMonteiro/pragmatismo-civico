from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from validar_registro_documentos_tecnicos import validate_registry


REGISTRY = ROOT / "casos" / "CASO-001_REGISTRO_DOCUMENTOS_TECNICOS.json"


class ValidarRegistroDocumentosTecnicosTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = json.loads(REGISTRY.read_text(encoding="utf-8"))

    def test_registro_canonico_e_valido(self) -> None:
        result = validate_registry(copy.deepcopy(self.payload))
        self.assertTrue(result.ok, result.errors)
        self.assertEqual(result.records, 8)
        self.assertEqual(result.claims, 20)
        self.assertEqual(result.inconsistencies, 3)
        self.assertEqual(result.required_documents, 7)

    def test_comunicacao_nao_pode_ser_evidencia_financeira_primaria(self) -> None:
        payload = copy.deepcopy(self.payload)
        payload["records"][0]["evidence_level"] = "primario_financiamento"

        result = validate_registry(payload)

        self.assertFalse(result.ok)
        self.assertTrue(
            any("comunicação institucional" in error for error in result.errors),
            result.errors,
        )

    def test_fonte_obtida_exige_caminho_e_hash(self) -> None:
        payload = copy.deepcopy(self.payload)
        payload["records"][0]["state"] = "obtida"

        result = validate_registry(payload)

        self.assertFalse(result.ok)
        self.assertTrue(any("exige `local_path`" in error for error in result.errors))
        self.assertTrue(any("exige SHA-256" in error for error in result.errors))

    def test_inconsistencia_deve_referenciar_alegacoes_existentes(self) -> None:
        payload = copy.deepcopy(self.payload)
        payload["known_inconsistencies"][0]["claim_ids"] = ["C-010", "C-999"]

        result = validate_registry(payload)

        self.assertFalse(result.ok)
        self.assertTrue(any("alegação inexistente `C-999`" in error for error in result.errors))


if __name__ == "__main__":
    unittest.main()
