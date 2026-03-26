#!/bin/bash
# ==============================================================================
# run.sh — Outlier Real Coder | F2P Test Executor
# Módulo: code-real | Rol: Ejecutor de pytest con reporte JSON
# ==============================================================================
# Regla: Nunca revela la lógica interna. Solo ejecuta tests y genera report.json
# ==============================================================================

set -e  # Salir inmediatamente si un comando falla

# --- Configuración ---
REPORT_FILE="report.json"
TEST_DIR="tests/"       # Directorio donde viven los tests del proyecto

echo "=============================================="
echo "  Outlier Real Coder — F2P Test Runner"
echo "=============================================="

# --- Verificación de existencia del directorio de tests ---
if [ ! -d "$TEST_DIR" ]; then
    echo "[ERROR] El directorio de tests '$TEST_DIR' no existe."
    echo "[INFO]  Esto es esperado para la Evidence A (Estado: FALLO CONTROLADO)."
    # Generamos un report.json de fallo manual para que parsing.py funcione
    cat > "$REPORT_FILE" << 'EOF'
{
  "created": 0,
  "duration": 0,
  "exitcode": 1,
  "root": "/workspace",
  "environment": {},
  "summary": {"failed": 1, "total": 1},
  "tests": [
    {
      "nodeid": "setup::environment_check",
      "outcome": "failed",
      "call": {"longrepr": "Test directory not found. Solution file is empty (Evidence A state)."}
    }
  ]
}
EOF
    echo "[RESULT] report.json generado con fallo controlado (Evidence A)."
    exit 1  # Salida con error — requerido para la Evidence A
fi

# --- Verificación de existencia de archivos de solución ---
# El archivo de solución debe existir aunque esté vacío
SOLUTION_FILE=$(find /workspace -maxdepth 2 -name "solution.py" 2>/dev/null | head -n 1)
if [ -z "$SOLUTION_FILE" ]; then
    echo "[WARN]  No se encontró solution.py. Los tests fallarán por importación."
fi

# --- Ejecución de pytest con reporte JSON ---
echo "[INFO]  Ejecutando pytest..."
echo "[CMD]   pytest $TEST_DIR --json-report --json-report-file=$REPORT_FILE -v"
echo "----------------------------------------------"

# pytest retorna código de salida != 0 si hay tests fallidos (comportamiento esperado en Evidence A)
pytest "$TEST_DIR" \
    --json-report \
    --json-report-file="$REPORT_FILE" \
    -v \
    --tb=short \
    || EXIT_CODE=$?

echo "----------------------------------------------"
echo "[INFO]  Pytest finalizado. Código de salida: ${EXIT_CODE:-0}"

# --- Verificar que el reporte fue generado ---
if [ ! -f "$REPORT_FILE" ]; then
    echo "[ERROR] No se generó $REPORT_FILE. Verifica la instalación de pytest-json-report."
    exit 2
fi

echo "[OK]    $REPORT_FILE generado correctamente."
echo "[NEXT]  Ejecuta: python3 parsing.py para generar output.json"

# Salimos con el código de pytest para que validation.sh pueda detectar el estado
exit ${EXIT_CODE:-0}
