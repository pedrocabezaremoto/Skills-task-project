#!/usr/bin/env python3
# ==============================================================================
# parsing.py — Outlier Real Coder | JSON Report Translator
# Módulo: code-real | Rol: Convertir report.json de pytest → output.json de Outlier
# ==============================================================================
# Formato de salida requerido por Outlier:
# {
#   "status": "PASSED" | "FAILED",
#   "tests": [
#     {"name": "test_nombre", "status": "passed/failed", "message": "error_log"}
#   ]
# }
# ==============================================================================

import json
import sys
import os

# --- Configuración de rutas ---
INPUT_FILE = "report.json"
OUTPUT_FILE = "output.json"


def translate_report(input_path: str, output_path: str) -> None:
    """
    Lee el report.json generado por pytest-json-report
    y lo transforma al formato output.json de Outlier.
    """
    # 1. Verificar existencia del archivo de entrada
    if not os.path.exists(input_path):
        print(f"[ERROR] No se encontró '{input_path}'. Ejecuta run.sh primero.", file=sys.stderr)
        sys.exit(1)

    # 2. Leer el reporte de pytest
    with open(input_path, "r", encoding="utf-8") as f:
        try:
            pytest_report = json.load(f)
        except json.JSONDecodeError as e:
            print(f"[ERROR] El archivo '{input_path}' no es JSON válido: {e}", file=sys.stderr)
            sys.exit(2)

    # 3. Extraer la lista de tests del reporte de pytest
    raw_tests = pytest_report.get("tests", [])

    # 4. Traducir cada test al formato de Outlier
    outlier_tests = []
    for test in raw_tests:
        # Determinar el estado del test
        outcome = test.get("outcome", "failed").lower()
        status_map = {
            "passed": "passed",
            "failed": "failed",
            "error": "failed",
            "xfailed": "failed",
            "xpassed": "passed",
            "skipped": "failed",  # Skipped se trata como fallo en F2P
        }
        test_status = status_map.get(outcome, "failed")

        # Extraer el mensaje de error si existe
        message = ""
        call_info = test.get("call", {})
        if call_info and "longrepr" in call_info:
            longrepr = call_info["longrepr"]
            # longrepr puede ser un string o una lista; lo normalizamos
            if isinstance(longrepr, list):
                message = " | ".join(str(part) for part in longrepr)
            else:
                message = str(longrepr)

        # Limpiar el nombre del test (eliminar ruta del archivo, dejar solo el nombre de función)
        node_id = test.get("nodeid", "unknown_test")
        test_name = node_id.split("::")[-1] if "::" in node_id else node_id

        outlier_tests.append({
            "name": test_name,
            "status": test_status,
            "message": message,
        })

    # 5. Determinar el estado global
    #    Outlier requiere PASSED solo si el 100% de los tests pasan
    summary = pytest_report.get("summary", {})
    failed_count = summary.get("failed", 0) + summary.get("error", 0)
    total_count = summary.get("total", len(raw_tests))

    # Si no hay tests, se considera FAILED (Estado Evidence A)
    if total_count == 0:
        global_status = "FAILED"
    elif failed_count == 0:
        global_status = "PASSED"
    else:
        global_status = "FAILED"

    # 6. Construir el output.json de Outlier
    outlier_output = {
        "status": global_status,
        "tests": outlier_tests,
    }

    # 7. Escribir el output.json
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(outlier_output, f, indent=2, ensure_ascii=False)

    # 8. Reporte en consola
    print("==============================================")
    print("  Outlier Real Coder — JSON Translator")
    print("==============================================")
    print(f"[INPUT]   {input_path}")
    print(f"[OUTPUT]  {output_path}")
    print(f"[STATUS]  {global_status}")
    print(f"[TESTS]   {total_count} total | {failed_count} fallidos")
    print("----------------------------------------------")

    for t in outlier_tests:
        icon = "✅" if t["status"] == "passed" else "❌"
        print(f"  {icon} {t['name']} → {t['status']}")

    print("==============================================")

    if global_status == "PASSED":
        print("[SUCCESS] Evidence B lista: output.json → PASSED al 100%")
    else:
        print("[INFO]    Evidence A capturada: output.json → FAILED (esperado)")


if __name__ == "__main__":
    translate_report(INPUT_FILE, OUTPUT_FILE)
