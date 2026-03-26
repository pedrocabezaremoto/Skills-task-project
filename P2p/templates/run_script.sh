#!/bin/bash
# ============================================
# Hawkins Experiments — Run Script Template
# ============================================
# REGLA: Solo ejecutar pruebas que YA PASABAN
#        antes de aplicar el Golden Patch.
#
# Propósito: Verificar que el Golden Patch
#            no introduce regresiones.
# ============================================

set -e  # Salir ante cualquier error

echo "=== Starting Run Script ==="

# ============================================
# TODO: Build/Compile (si aplica)
# ============================================
# Descomentar según el lenguaje:
# npm run build
# cargo build
# go build ./...
# python setup.py build

# ============================================
# TODO: Linting (si aplica)
# ============================================
# Descomentar según el framework:
# npm run lint
# flake8 src/
# cargo clippy

# ============================================
# TODO: Ejecutar pruebas unitarias
# ============================================
# SOLO las pruebas que ya pasaban antes del parche.
#
# Ejemplos:
# pytest tests/ -v
# npm test
# go test ./...
# cargo test
# python -m unittest discover tests/

echo "=== Run Script Completed ==="
