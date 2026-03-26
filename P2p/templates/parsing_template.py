#!/usr/bin/env python3
"""
Hawkins Experiments — Parsing Template
⚠️ REGLA: SOLO modificar la función parse_test_output()
   El resto del archivo NO debe tocarse.

Uso: python3 parsing.py stdout.txt stderr.txt results.json
"""

import json
import sys
from dataclasses import dataclass, asdict
from typing import List


@dataclass
class TestResult:
    name: str
    status: str  # PASSED | FAILED | SKIPPED | ERROR


def parse_test_output(stdout_content: str, stderr_content: str) -> List[TestResult]:
    """
    ============================================
    TODO: Implementar la lógica de parsing aquí.
    ============================================
    
    Adaptar según el framework de pruebas del repo:
    - pytest:     Buscar patrones "PASSED", "FAILED", "ERROR"
    - junit:      Parsear XML de salida
    - go test:    Buscar "--- PASS:", "--- FAIL:"
    - cargo test: Buscar "test result:"
    - mocha/jest: Buscar patrones del runner de JS
    
    Debe retornar una lista de TestResult con:
    - name: nombre de la prueba
    - status: uno de "PASSED", "FAILED", "SKIPPED", "ERROR"
    """
    raise NotImplementedError("Implement the test output parsing logic")


# ============================================
# DO NOT MODIFY — Lógica principal del script
# ============================================
def main():
    if len(sys.argv) != 4:
        print("Usage: python3 parsing.py <stdout_file> <stderr_file> <output_json>")
        sys.exit(1)

    stdout_file = sys.argv[1]
    stderr_file = sys.argv[2]
    output_file = sys.argv[3]

    with open(stdout_file, "r") as f:
        stdout_content = f.read()

    with open(stderr_file, "r") as f:
        stderr_content = f.read()

    results = parse_test_output(stdout_content, stderr_content)
    
    output = {
        "tests": [asdict(r) for r in results]
    }

    with open(output_file, "w") as f:
        json.dump(output, f, indent=2)

    print(f"Results written to {output_file}")


if __name__ == "__main__":
    main()
