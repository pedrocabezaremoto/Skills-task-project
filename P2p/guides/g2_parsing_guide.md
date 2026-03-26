# G2 — Guía del Analizador de Resultados (parsing.py)

> Cómo implementar, configurar y desplegar el sistema de análisis de resultados de pruebas.

---

## 1. Arquitectura del Analizador

### Entradas y Salidas
| Elemento | Detalle |
|----------|---------|
| **Entrada 1** | `stdout.txt` — Salida estándar de la ejecución de pruebas |
| **Entrada 2** | `stderr.txt` — Salida de errores de la ejecución |
| **Salida** | `results.json` — Informe estructurado en JSON |

### Estructura JSON Obligatoria

```json
{
  "tests": [
    {
      "name": "nombre de la prueba",
      "status": "PASSED|FAILED|SKIPPED|ERROR"
    }
  ]
}
```

> ⚠️ Solo estos 4 estados son válidos: `PASSED`, `FAILED`, `SKIPPED`, `ERROR`

---

## 2. Generación de Registros

### Opción A: Mediante `run.sh`
El archivo `run.sh` ejecuta la suite completa de pruebas.
- **Acción requerida:** Editar `run_all_tests()` con los comandos reales de ejecución de pruebas.
- El script base solo imprime un placeholder que debe reemplazarse.

### Opción B: Ejecución Directa
Si ya tienes el comando de pruebas:
```bash
<comando-de-tests> > stdout.txt 2> stderr.txt
# Ejemplo con pytest:
pytest -q > stdout.txt 2> stderr.txt
```

---

## 3. Implementación de `parse_test_output()`

### Estado Inicial
La función lanza `NotImplementedError('Implement the test output parsing logic')` por defecto.

### Especificaciones
```python
def parse_test_output(stdout_content: str, stderr_content: str) -> List[TestResult]:
    # Adaptar según el framework:
    # - pytest     → buscar patrones "PASSED", "FAILED", "ERROR"
    # - junit      → parsear XML de salida
    # - go test    → buscar "--- PASS:", "--- FAIL:"
    # - cargo test → buscar "test result:"
    # - mocha/jest → buscar patrones del runner
    pass
```

### Regla Crítica
> **SOLO** tienes permitido modificar la función `parse_test_output()`. El resto del archivo `parsing.py` NO se toca.

---

## 4. Ejecución

### Directa
```bash
python3 parsing.py stdout.txt stderr.txt results.json
```

### Via Docker
```bash
docker run --rm -it -v "$PWD:/app" test-parser bash -lc \
  "./run.sh > stdout.txt 2> stderr.txt && python3 parsing.py stdout.txt stderr.txt results.json"
```

---

## 5. Checklist de Despliegue

- [ ] `run.sh` ejecuta pruebas reales (no placeholder `echo`)
- [ ] `stdout.txt` y `stderr.txt` generados correctamente
- [ ] `parse_test_output()` implementada para el framework del repo
- [ ] `python3 parsing.py` se ejecuta sin errores
- [ ] `results.json` contiene la clave `"tests"` con su lista de resultados
