#!/usr/bin/env python3
"""Valida um GeoJSON de delimitação de sub-bacia e produz manifesto auditável.

O validador não afirma oficialidade da geometria. Ele verifica integridade do
arquivo, estrutura GeoJSON, anéis, coordenadas, extensão espacial, nome
esperado e proveniência declarada. A oficialidade depende da fonte e da revisão
documental registradas fora deste script.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator, Sequence

EARTH_RADIUS_M = 6_371_008.8
VERSION = "0.1.0"


@dataclass
class Validation:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    feature_count: int = 0
    polygon_count: int = 0
    ring_count: int = 0
    vertex_count: int = 0
    geometry_types: set[str] = field(default_factory=set)
    bbox: list[float] | None = None
    estimated_area_km2: float = 0.0
    expected_name_matches: int = 0

    @property
    def ok(self) -> bool:
        return not self.errors


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(float(value))


def iter_feature_geometries(payload: dict[str, Any]) -> Iterator[tuple[dict[str, Any], dict[str, Any]]]:
    payload_type = payload.get("type")
    if payload_type == "FeatureCollection":
        features = payload.get("features")
        if not isinstance(features, list):
            raise ValueError("FeatureCollection sem lista 'features'.")
        for index, feature in enumerate(features, start=1):
            if not isinstance(feature, dict) or feature.get("type") != "Feature":
                raise ValueError(f"Item {index} não é uma Feature válida.")
            geometry = feature.get("geometry")
            if not isinstance(geometry, dict):
                raise ValueError(f"Feature {index} sem geometria.")
            yield feature, geometry
    elif payload_type == "Feature":
        geometry = payload.get("geometry")
        if not isinstance(geometry, dict):
            raise ValueError("Feature sem geometria.")
        yield payload, geometry
    elif payload_type in {"Polygon", "MultiPolygon"}:
        yield {"type": "Feature", "properties": {}, "geometry": payload}, payload
    else:
        raise ValueError("O arquivo deve ser FeatureCollection, Feature, Polygon ou MultiPolygon.")


def iter_polygons(geometry: dict[str, Any]) -> Iterator[list[list[list[float]]]]:
    geometry_type = geometry.get("type")
    coordinates = geometry.get("coordinates")
    if geometry_type == "Polygon":
        if not isinstance(coordinates, list):
            raise ValueError("Polygon sem coordenadas.")
        yield coordinates
    elif geometry_type == "MultiPolygon":
        if not isinstance(coordinates, list):
            raise ValueError("MultiPolygon sem coordenadas.")
        for polygon in coordinates:
            if not isinstance(polygon, list):
                raise ValueError("MultiPolygon contém polígono inválido.")
            yield polygon
    else:
        raise ValueError(f"Geometria não poligonal: {geometry_type!r}.")


def point_equal(a: Sequence[float], b: Sequence[float], tolerance: float = 1e-12) -> bool:
    return abs(float(a[0]) - float(b[0])) <= tolerance and abs(float(a[1]) - float(b[1])) <= tolerance


def orientation(a: Sequence[float], b: Sequence[float], c: Sequence[float]) -> float:
    return (float(b[0]) - float(a[0])) * (float(c[1]) - float(a[1])) - (
        float(b[1]) - float(a[1])
    ) * (float(c[0]) - float(a[0]))


def on_segment(a: Sequence[float], b: Sequence[float], c: Sequence[float], eps: float = 1e-12) -> bool:
    return (
        min(float(a[0]), float(c[0])) - eps <= float(b[0]) <= max(float(a[0]), float(c[0])) + eps
        and min(float(a[1]), float(c[1])) - eps <= float(b[1]) <= max(float(a[1]), float(c[1])) + eps
        and abs(orientation(a, b, c)) <= eps
    )


def segments_intersect(
    a: Sequence[float], b: Sequence[float], c: Sequence[float], d: Sequence[float], eps: float = 1e-12
) -> bool:
    o1 = orientation(a, b, c)
    o2 = orientation(a, b, d)
    o3 = orientation(c, d, a)
    o4 = orientation(c, d, b)

    if ((o1 > eps and o2 < -eps) or (o1 < -eps and o2 > eps)) and (
        (o3 > eps and o4 < -eps) or (o3 < -eps and o4 > eps)
    ):
        return True

    if abs(o1) <= eps and on_segment(a, c, b):
        return True
    if abs(o2) <= eps and on_segment(a, d, b):
        return True
    if abs(o3) <= eps and on_segment(c, a, d):
        return True
    if abs(o4) <= eps and on_segment(c, b, d):
        return True
    return False


def ring_self_intersections(ring: list[list[float]]) -> int:
    segments = list(zip(ring[:-1], ring[1:]))
    intersections = 0
    for i, (a, b) in enumerate(segments):
        for j in range(i + 1, len(segments)):
            if abs(i - j) <= 1:
                continue
            if i == 0 and j == len(segments) - 1:
                continue
            c, d = segments[j]
            if segments_intersect(a, b, c, d):
                intersections += 1
    return intersections


def approximate_ring_area_m2(ring: list[list[float]]) -> float:
    """Calcula área plana aproximada para polígonos pequenos em longitude/latitude."""
    if len(ring) < 4:
        return 0.0
    lat0 = math.radians(sum(float(point[1]) for point in ring[:-1]) / max(1, len(ring) - 1))

    projected: list[tuple[float, float]] = []
    for point in ring:
        lon = math.radians(float(point[0]))
        lat = math.radians(float(point[1]))
        projected.append((EARTH_RADIUS_M * lon * math.cos(lat0), EARTH_RADIUS_M * lat))

    area = 0.0
    for (x1, y1), (x2, y2) in zip(projected[:-1], projected[1:]):
        area += x1 * y2 - x2 * y1
    return area / 2.0


def feature_text(feature: dict[str, Any]) -> str:
    properties = feature.get("properties") or {}
    if not isinstance(properties, dict):
        return ""
    return " ".join(str(value) for value in properties.values() if value is not None).casefold()


def update_bbox(current: list[float] | None, lon: float, lat: float) -> list[float]:
    if current is None:
        return [lon, lat, lon, lat]
    current[0] = min(current[0], lon)
    current[1] = min(current[1], lat)
    current[2] = max(current[2], lon)
    current[3] = max(current[3], lat)
    return current


def validate_geojson(
    payload: dict[str, Any],
    *,
    expected_name: str | None,
    expected_envelope: list[float] | None,
) -> Validation:
    result = Validation()

    try:
        items = list(iter_feature_geometries(payload))
    except ValueError as error:
        result.errors.append(str(error))
        return result

    result.feature_count = len(items)
    if result.feature_count == 0:
        result.errors.append("O arquivo não contém feições.")
        return result

    expected_token = expected_name.casefold() if expected_name else None

    for feature_index, (feature, geometry) in enumerate(items, start=1):
        geometry_type = geometry.get("type")
        result.geometry_types.add(str(geometry_type))

        if expected_token and expected_token in feature_text(feature):
            result.expected_name_matches += 1

        try:
            polygons = list(iter_polygons(geometry))
        except ValueError as error:
            result.errors.append(f"Feature {feature_index}: {error}")
            continue

        for polygon_index, polygon in enumerate(polygons, start=1):
            result.polygon_count += 1
            if not polygon:
                result.errors.append(f"Feature {feature_index}, polígono {polygon_index}: sem anéis.")
                continue

            polygon_area = 0.0
            for ring_index, ring in enumerate(polygon, start=1):
                result.ring_count += 1
                context = f"Feature {feature_index}, polígono {polygon_index}, anel {ring_index}"
                if not isinstance(ring, list):
                    result.errors.append(f"{context}: anel não é uma lista.")
                    continue
                if len(ring) < 4:
                    result.errors.append(f"{context}: menos de quatro posições.")
                    continue

                normalized_ring: list[list[float]] = []
                invalid_coordinate = False
                for point_index, point in enumerate(ring, start=1):
                    if not isinstance(point, (list, tuple)) or len(point) < 2:
                        result.errors.append(f"{context}, posição {point_index}: coordenada inválida.")
                        invalid_coordinate = True
                        continue
                    lon, lat = point[0], point[1]
                    if not is_number(lon) or not is_number(lat):
                        result.errors.append(f"{context}, posição {point_index}: valor não numérico ou não finito.")
                        invalid_coordinate = True
                        continue
                    lon_f, lat_f = float(lon), float(lat)
                    if not -180 <= lon_f <= 180 or not -90 <= lat_f <= 90:
                        result.errors.append(
                            f"{context}, posição {point_index}: longitude/latitude fora do intervalo válido."
                        )
                        invalid_coordinate = True
                        continue
                    normalized_ring.append([lon_f, lat_f])
                    result.vertex_count += 1
                    result.bbox = update_bbox(result.bbox, lon_f, lat_f)

                if invalid_coordinate or len(normalized_ring) != len(ring):
                    continue
                if not point_equal(normalized_ring[0], normalized_ring[-1]):
                    result.errors.append(f"{context}: anel não fechado.")
                    continue

                unique_points = {(point[0], point[1]) for point in normalized_ring[:-1]}
                if len(unique_points) < 3:
                    result.errors.append(f"{context}: menos de três vértices distintos.")
                    continue

                intersections = ring_self_intersections(normalized_ring)
                if intersections:
                    result.errors.append(f"{context}: {intersections} auto-interseção(ões) detectada(s).")
                    continue

                signed_area = approximate_ring_area_m2(normalized_ring)
                if abs(signed_area) < 1.0:
                    result.errors.append(f"{context}: área nula ou desprezível.")
                    continue

                polygon_area += abs(signed_area) if ring_index == 1 else -abs(signed_area)

            if polygon_area <= 0:
                result.errors.append(
                    f"Feature {feature_index}, polígono {polygon_index}: área exterior não positiva após os furos."
                )
            else:
                result.estimated_area_km2 += polygon_area / 1_000_000.0

    if expected_token and result.expected_name_matches == 0:
        result.errors.append(f"Nenhuma feição contém o nome esperado {expected_name!r} em seus atributos.")

    if expected_envelope and result.bbox:
        min_lon, min_lat, max_lon, max_lat = expected_envelope
        bbox = result.bbox
        if bbox[0] < min_lon or bbox[1] < min_lat or bbox[2] > max_lon or bbox[3] > max_lat:
            result.errors.append(
                "A extensão da geometria está fora do envelope esperado: "
                f"bbox={bbox}, envelope={expected_envelope}."
            )

    if result.estimated_area_km2 > 0:
        result.warnings.append(
            "A área é uma estimativa equiretangular para controle de plausibilidade; "
            "não substitui cálculo geodésico em SIG."
        )

    return result


def build_manifest(
    *,
    input_path: Path,
    validation: Validation,
    source_url: str | None,
    accessed_at: str | None,
    source_srid: str,
    expected_name: str | None,
    expected_envelope: list[float] | None,
) -> dict[str, Any]:
    return {
        "validator": {"name": "validar_geojson_subbacia.py", "version": VERSION},
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "source": {
            "path": input_path.name,
            "sha256": sha256_file(input_path),
            "size_bytes": input_path.stat().st_size,
            "url": source_url,
            "accessed_at": accessed_at,
            "declared_srid": source_srid,
        },
        "expectations": {
            "name": expected_name,
            "envelope": expected_envelope,
        },
        "summary": {
            "ok": validation.ok,
            "feature_count": validation.feature_count,
            "polygon_count": validation.polygon_count,
            "ring_count": validation.ring_count,
            "vertex_count": validation.vertex_count,
            "geometry_types": sorted(validation.geometry_types),
            "bbox": validation.bbox,
            "estimated_area_km2": round(validation.estimated_area_km2, 6),
            "expected_name_matches": validation.expected_name_matches,
        },
        "errors": validation.errors,
        "warnings": validation.warnings,
        "limitations": [
            "Validação estrutural não comprova oficialidade, atualidade, escala, licença ou adequação temática.",
            "GeoJSON não preserva necessariamente todos os metadados do serviço de origem.",
            "A área estimada serve apenas para controle de plausibilidade.",
        ],
    }


def build_report(manifest: dict[str, Any]) -> str:
    source = manifest["source"]
    summary = manifest["summary"]
    lines = [
        "# Relatório de validação geoespacial",
        "",
        f"- **Resultado:** {'APROVADO' if summary['ok'] else 'REPROVADO'}",
        f"- **Arquivo:** `{source['path']}`",
        f"- **SHA-256:** `{source['sha256']}`",
        f"- **SRID declarado:** `{source['declared_srid']}`",
        f"- **Feições:** {summary['feature_count']}",
        f"- **Polígonos:** {summary['polygon_count']}",
        f"- **Anéis:** {summary['ring_count']}",
        f"- **Vértices:** {summary['vertex_count']}",
        f"- **BBox:** `{summary['bbox']}`",
        f"- **Área aproximada:** {summary['estimated_area_km2']:.6f} km²",
        "",
        "## Achados",
        "",
    ]
    if not manifest["errors"] and not manifest["warnings"]:
        lines.append("Nenhum achado.")
    if manifest["errors"]:
        lines.extend(["### Erros", ""])
        lines.extend(f"- {item}" for item in manifest["errors"])
    if manifest["warnings"]:
        lines.extend(["", "### Avisos", ""])
        lines.extend(f"- {item}" for item in manifest["warnings"])
    lines.extend(
        [
            "",
            "## Limites",
            "",
            *[f"- {item}" for item in manifest["limitations"]],
            "",
        ]
    )
    return "\n".join(lines)


def parse_envelope(values: list[str] | None) -> list[float] | None:
    if not values:
        return None
    if len(values) != 4:
        raise ValueError("O envelope deve conter quatro números: min_lon min_lat max_lon max_lat.")
    envelope = [float(value) for value in values]
    if envelope[0] >= envelope[2] or envelope[1] >= envelope[3]:
        raise ValueError("Envelope inválido.")
    return envelope


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--report", required=True)
    parser.add_argument("--source-url")
    parser.add_argument("--accessed-at")
    parser.add_argument("--source-srid", default="EPSG:4674")
    parser.add_argument("--expected-name")
    parser.add_argument("--expected-envelope", nargs=4)
    args = parser.parse_args()

    input_path = Path(args.input)
    manifest_path = Path(args.manifest)
    report_path = Path(args.report)

    if not input_path.is_file():
        print(f"ERRO: arquivo não encontrado: {input_path}", file=sys.stderr)
        return 2

    try:
        payload = json.loads(input_path.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("O JSON raiz deve ser objeto.")
        envelope = parse_envelope(args.expected_envelope)
    except (OSError, json.JSONDecodeError, ValueError) as error:
        print(f"ERRO: {error}", file=sys.stderr)
        return 2

    validation = validate_geojson(
        payload,
        expected_name=args.expected_name,
        expected_envelope=envelope,
    )
    manifest = build_manifest(
        input_path=input_path,
        validation=validation,
        source_url=args.source_url,
        accessed_at=args.accessed_at,
        source_srid=args.source_srid,
        expected_name=args.expected_name,
        expected_envelope=envelope,
    )

    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    report_path.write_text(build_report(manifest), encoding="utf-8")

    print(
        f"Validação {'aprovada' if validation.ok else 'reprovada'}: "
        f"{validation.feature_count} feição(ões), {validation.polygon_count} polígono(s)."
    )
    return 0 if validation.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
