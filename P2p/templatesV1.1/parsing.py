#!/usr/bin/env python3
import json
import sys
import os

def parse_test_output(input_file="report.json", output_file="after.json"):
    """
    Simula la transformación de la salida de pruebas (pytest o similar)
    al formato JSON estricto requerido por Outlier.
    """
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        sys.exit(1)

    try:
        with open(input_file, "r") as f:
            data = json.load(f)
        
        outlier_tests = []
        all_passed = True
        
        for test in data.get("tests", []):
            status = "passed" if test.get("outcome") == "passed" else "failed"
            if status == "failed":
                all_passed = False
            
            outlier_tests.append({
                "name": test.get("nodeid", "unknown").split("::")[-1],
                "status": status,
                "message": test.get("call", {}).get("longrepr", "") if status == "failed" else ""
            })
            
        result = {
            "status": "PASSED" if all_passed and outlier_tests else "FAILED",
            "tests": outlier_tests
        }
        
        with open(output_file, "w") as f:
            json.dump(result, f, indent=2)
            
        print(f"Successfully generated {output_file} format.")
            
    except Exception as e:
        print(f"Error parsing: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parse_test_output()
