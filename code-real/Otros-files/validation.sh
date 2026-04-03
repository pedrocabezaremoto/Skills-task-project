#!/bin/bash
# ==============================================================================
# validation.sh — Outlier Real Coder | F2P Automated Validation Script
# Módulo: code-real | Rol: Genera before.json y after.json
# ==============================================================================
# REGLA G7: Solo se permite editar la variable APP_DIR.
# REGLA G5: Este archivo DEBE usar finales de línea LF (Unix), NO CRLF (Windows).
# ==============================================================================

# ============================================================
# ██████  EDITABLE SECTION — MODIFY ONLY THIS LINE  ██████
# ============================================================
APP_DIR="./app"
# ============================================================
# ██████  END EDITABLE SECTION                       ██████
# ============================================================

# ╔══════════════════════════════════════════════════════════╗
# ║  ██  DO NOT MODIFY ANYTHING BELOW THIS LINE  ██        ║
# ║  Cualquier cambio invalida el proceso de evaluación.    ║
# ║  Ref: G4 §Restricciones Críticas, G7 §3                ║
# ╚══════════════════════════════════════════════════════════╝

set -e

# --- Rutas derivadas de APP_DIR ---
DOCKERFILE="${APP_DIR}/Dockerfile"
TESTS_ZIP="${APP_DIR}/tests.zip"
CODEBASE_ZIP="${APP_DIR}/codebase.zip"
RUN_SCRIPT="${APP_DIR}/run.sh"
PARSE_SCRIPT="${APP_DIR}/parsing.py"

# --- Configuración Docker ---
IMAGE_TAG="agent-evaluator:latest"
MAX_ZIP_DEPTH=3

echo "================================================================"
echo "  Real Coder — F2P Validation Script"
echo "  Ref: G1 §5, G4 §Protocolo, G5 §3"
echo "================================================================"

# --- STEP 1: Validación de estructura de directorio (G7 §1) ---
echo ""
echo "[STEP 1] Validando estructura del directorio ${APP_DIR}..."
echo "────────────────────────────────────────────────────────────"

REQUIRED_FILES=("$DOCKERFILE" "$TESTS_ZIP" "$CODEBASE_ZIP" "$RUN_SCRIPT" "$PARSE_SCRIPT")
MISSING=0

for file in "${REQUIRED_FILES[@]}"; do
    if [ ! -f "$file" ]; then
        echo "  ❌ FALTA: $(basename $file)"
        MISSING=$((MISSING + 1))
    else
        echo "  ✅ OK:    $(basename $file)"
    fi
done

if [ $MISSING -gt 0 ]; then
    echo ""
    echo "🚨 ERROR: Faltan ${MISSING} archivo(s) obligatorio(s) en ${APP_DIR}."
    echo "   Ref: G7 §1 — Se requieren exactamente 5 componentes."
    echo "   Componentes: Dockerfile, tests.zip, codebase.zip, run.sh, parsing.py"
    exit 1
fi

echo "  ✅ Estructura validada: 5/5 archivos presentes."

# --- STEP 2: Validación de profundidad ZIP (G7 §2) ---
echo ""
echo "[STEP 2] Validando estructura de archivos ZIP..."
echo "────────────────────────────────────────────────────────────"

# Validar codebase.zip: NO debe tener carpeta raíz contenedora (G7 §2, G1 §Reglas de Empaquetado)
echo "  Verificando codebase.zip (no debe tener carpeta raíz anidada)..."
NESTED=$(unzip -l "$CODEBASE_ZIP" 2>/dev/null | awk 'NR>3 && !/^-/ && !/Archive/' | head -5)
echo "  Primeros archivos: "
echo "$NESTED" | head -3 | sed 's/^/    /'

# Validar tests.zip: DEBE contener carpeta tests/ como primer nivel (G7 §2)
echo "  Verificando tests.zip (debe contener carpeta tests/)..."
HAS_TESTS_DIR=$(unzip -l "$TESTS_ZIP" 2>/dev/null | grep -c "tests/" || true)
if [ "$HAS_TESTS_DIR" -eq 0 ]; then
    echo "  ⚠️  ADVERTENCIA: tests.zip no contiene carpeta tests/ como primer nivel."
    echo "     Ref: G7 §2 — 'Regla de Oro de Compresión'"
fi

echo "  ✅ Validación ZIP completada."

# --- STEP 3: Construir imagen Docker (G4 §Protocolo) ---
echo ""
echo "[STEP 3] Construyendo imagen Docker..."
echo "────────────────────────────────────────────────────────────"
echo "  Imagen: ${IMAGE_TAG}"
echo "  Base: ubuntu:22.04 (obligatoria por G4/G5)"

docker build -t "$IMAGE_TAG" "$APP_DIR"

echo "  ✅ Imagen construida exitosamente."

# --- STEP 4: BASELINE — Evidence A (G1 §5, G3 §Paso 4) ---
echo ""
echo "[STEP 4] Ejecutando BASELINE (Evidence A — antes del Golden Patch)..."
echo "────────────────────────────────────────────────────────────"
echo "  Expectativa: TODAS las pruebas deben FALLAR (FAILED, no ERROR)"
echo "  Ref: G1 §Paso 2, G2 §3, G8 §4"

# Crear directorio temporal para baseline
BASELINE_DIR=$(mktemp -d)
cp "$RUN_SCRIPT" "$BASELINE_DIR/"
cp "$PARSE_SCRIPT" "$BASELINE_DIR/"
unzip -o "$TESTS_ZIP" -d "$BASELINE_DIR/" > /dev/null 2>&1

# Ejecutar en Docker sin el codebase (baseline vacía)
docker run --rm \
    -v "${BASELINE_DIR}:/app" \
    -w /app \
    "$IMAGE_TAG" \
    bash -c "chmod +x run.sh && bash run.sh > /tmp/stdout.txt 2> /tmp/stderr.txt; python3 parsing.py; cp /tmp/stdout.txt /app/before_stdout.txt; cp /tmp/stderr.txt /app/before_stderr.txt" \
    || true

# Copiar resultados
if [ -f "${BASELINE_DIR}/results.json" ]; then
    cp "${BASELINE_DIR}/results.json" "${APP_DIR}/before.json"
    echo "  ✅ before.json generado."
elif [ -f "${BASELINE_DIR}/output.json" ]; then
    cp "${BASELINE_DIR}/output.json" "${APP_DIR}/before.json"
    echo "  ✅ before.json generado (desde output.json)."
else
    echo "  ❌ ERROR: No se generó results.json ni output.json en baseline."
fi

[ -f "${BASELINE_DIR}/before_stdout.txt" ] && cp "${BASELINE_DIR}/before_stdout.txt" "${APP_DIR}/"
[ -f "${BASELINE_DIR}/before_stderr.txt" ] && cp "${BASELINE_DIR}/before_stderr.txt" "${APP_DIR}/"

rm -rf "$BASELINE_DIR"

echo "  Archivos generados en ${APP_DIR}/:"
echo "    - before.json"
echo "    - before_stdout.txt"
echo "    - before_stderr.txt"

# --- STEP 5: GOLDEN PATCH — Evidence B (G1 §Paso 4-5, G3 §Paso 3) ---
echo ""
echo "[STEP 5] Ejecutando con GOLDEN PATCH (Evidence B — después)..."
echo "────────────────────────────────────────────────────────────"
echo "  Expectativa: TODAS las pruebas deben PASAR (PASSED)"
echo "  Ref: G1 §Paso 4-5, G3 §Paso 3"

# Crear directorio temporal con codebase + tests
SOLUTION_DIR=$(mktemp -d)
cp "$RUN_SCRIPT" "$SOLUTION_DIR/"
cp "$PARSE_SCRIPT" "$SOLUTION_DIR/"
unzip -o "$TESTS_ZIP" -d "$SOLUTION_DIR/" > /dev/null 2>&1
unzip -o "$CODEBASE_ZIP" -d "$SOLUTION_DIR/" > /dev/null 2>&1

# Ejecutar en Docker con el codebase completo
docker run --rm \
    -v "${SOLUTION_DIR}:/app" \
    -w /app \
    "$IMAGE_TAG" \
    bash -c "chmod +x run.sh && bash run.sh > /tmp/stdout.txt 2> /tmp/stderr.txt; python3 parsing.py; cp /tmp/stdout.txt /app/after_stdout.txt; cp /tmp/stderr.txt /app/after_stderr.txt" \
    || true

# Copiar resultados
if [ -f "${SOLUTION_DIR}/results.json" ]; then
    cp "${SOLUTION_DIR}/results.json" "${APP_DIR}/after.json"
    echo "  ✅ after.json generado."
elif [ -f "${SOLUTION_DIR}/output.json" ]; then
    cp "${SOLUTION_DIR}/output.json" "${APP_DIR}/after.json"
    echo "  ✅ after.json generado (desde output.json)."
else
    echo "  ❌ ERROR: No se generó results.json ni output.json con el Golden Patch."
fi

[ -f "${SOLUTION_DIR}/after_stdout.txt" ] && cp "${SOLUTION_DIR}/after_stdout.txt" "${APP_DIR}/"
[ -f "${SOLUTION_DIR}/after_stderr.txt" ] && cp "${SOLUTION_DIR}/after_stderr.txt" "${APP_DIR}/"

rm -rf "$SOLUTION_DIR"

echo "  Archivos generados en ${APP_DIR}/:"
echo "    - after.json"
echo "    - after_stdout.txt"
echo "    - after_stderr.txt"

# --- STEP 6: Resumen Final ---
echo ""
echo "================================================================"
echo "  VALIDACIÓN F2P COMPLETADA"
echo "================================================================"
echo ""
echo "  Archivos generados en ${APP_DIR}/:"
echo "  ┌──────────────────────────────────────────────┐"
echo "  │  before.json       ← Baseline (FAILED)      │"
echo "  │  before_stdout.txt ← Log stdout baseline     │"
echo "  │  before_stderr.txt ← Log stderr baseline     │"
echo "  │  after.json        ← Golden Patch (PASSED)   │"
echo "  │  after_stdout.txt  ← Log stdout golden       │"
echo "  │  after_stderr.txt  ← Log stderr golden       │"
echo "  └──────────────────────────────────────────────┘"
echo ""
echo "  📋 Siguiente paso: Verificar manualmente que:"
echo "     1. before.json muestra TODOS los tests como FAILED"
echo "     2. after.json muestra TODOS los tests como PASSED"
echo "     3. Ref: G1 §5, G3 §Paso 4, G9 §3"
echo ""
echo "================================================================"
