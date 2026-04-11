#!/bin/bash
### COMMON SETUP; DO NOT MODIFY ###
set -e

# --- CONFIGURE THIS SECTION ---
# Replace this with your command to run all tests
run_all_tests() {
  echo "Running all tests..."
  # The tests are contained in the 'tests' directory which will be populated 
  # inside the codebase directory during the evaluation step.
  # We should run pytest directly from the app scope aiming at the root of the structure
  python3 -m pytest tests/test_f2p.py -v --tb=short
}
# --- END CONFIGURATION SECTION ---

### COMMON EXECUTION; DO NOT MODIFY ###
run_all_tests
