#!/bin/bash
# Plantilla e2e_new.sh para tarea de Performance Optimization (P2p)

echo "=============== INICIANDO PRUEBAS E2E (PO TASK) ==============="

# 1. Construir la imagen Docker
echo "[1/4] Construyendo contenedor de pruebas..."
docker build -t test-env .

# 2. Ejecutar contenedor pre-parche (Evaluando el Bottleneck)
echo "[2/4] Ejecutando evaluación ANTES del parche (Esperando fallo por tiempo)..."
docker run --rm -v $(pwd):/app test-env bash -c "./run_script.sh && python parsing.py report.json before.json"
echo "Contenido generado en before.json"

# 3. Aplicar el Golden Patch (Optimizando el código)
echo "[3/4] Aplicando la optimización (golden.patch)..."
docker run --rm -v $(pwd):/app test-env bash -c "patch -p1 < golden.patch"

# 4. Ejecutar contenedor post-parche (Evaluando la mejora)
echo "[4/4] Ejecutando evaluación DESPUÉS del parche..."
docker run --rm -v $(pwd):/app test-env bash -c "./run_script.sh && python parsing.py report.json after.json"
echo "Contenido generado en after.json"

echo "Comparando resultados..."
# Aquí se puede añadir validación del before.json y after.json
echo "=============== PROCESO FINALIZADO ==============="
echo "- Verifica que before.json tenga estatus FAILED"
echo "- Verifica que after.json tenga estatus PASSED"
