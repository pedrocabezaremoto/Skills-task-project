#!/bin/bash
### COMMON SETUP; DO NOT MODIFY ###
set -e

# --- CONFIGURE THIS SECTION ---
# Replace this with your command to run all tests
run_all_tests() {
  echo "Running all tests..."
  
  # Cambiamos al directorio de los tests
  cd /app/tests
  
  # Ejecutamos la suite completa de pytest
  pytest test_main.py -v --tb=short
}
# --- END CONFIGURATION SECTION ---

### COMMON EXECUTION; DO NOT MODIFY ###
run_all_tests
