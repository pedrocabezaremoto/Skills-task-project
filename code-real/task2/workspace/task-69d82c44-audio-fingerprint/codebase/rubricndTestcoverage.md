# Rubric & Test Coverage Matrix — Task 69d82c44
## Audio Fingerprinting Library | Data Science | Python 3.11

> Este archivo mapea CADA requerimiento del prompt contra su método de verificación (unit test y/o rubric). Ningún requerimiento puede quedar sin cubrir.

---

## REGLA DE COBERTURA

```
Lógica funcional (Math/DB) → Unit Test (F2P) — obligatorio
Formatos de salida / CLI   → Rubric / Test — obligatorio
Arquitectura / Tech Stack  → Rubric
Lo que tests no cubren     → Rubric — sin excepciones
```

---

## MATRIZ DE COBERTURA (Audio Fingerprint)

| # | Requerimiento | Cubierto por Test | Cubierto por Rubric | Cobertura Total |
|---|---|---|---|---|
| R01 | `fingerprint` load (scipy), mono, float64, STFT params | ⬜ | ⬜ | ⬜ |
| R02 | Detección de picos (multiplicativo threshold & mean) | ⬜ | ⬜ | ⬜ |
| R03 | Máximos locales (excluyendo bordes 0 y N) | ⬜ | ⬜ | ⬜ |
| R04 | Fórmula exacta de hash (bit-shifting formula) | ⬜ | ⬜ | ⬜ |
| R05 | Retorno de `fingerprint` (lista de tuplas o vacío) | ⬜ | ⬜ | ⬜ |
| R06 | `build_database` iteración y limpieza previa (DELETE) | ⬜ | ⬜ | ⬜ |
| R07 | Sentencia SQL CREATE TABLE + Index `idx_fingerprints_hash` | ⬜ | ⬜ | ⬜ |
| R08 | `query` con búsqueda por índice y alineación temporal | ⬜ | ⬜ | ⬜ |
| R09 | Casos exactos de `no_match` (casos a y b) | ⬜ | ⬜ | ⬜ |
| R10 | `test_mode` seed 42, 20dB SNR y uso de `tempfile` | ⬜ | ⬜ | ⬜ |
| R11 | Lógica de `song_name` (sin ruta ni extensión) | ⬜ | ⬜ | ⬜ |
| R12 | CLI: 3 subcomandos y mensajes stdout exactos | ⬜ | ⬜ | ⬜ |
| R13 | `generate_samples` 2 archivos, 30s, chirps (200 hashes min) | ⬜ | ⬜ | ⬜ |
| R14 | Parámetros configurables (keyword args en firmas) | ⬜ | ⬜ | ⬜ |
| R15 | Tech Stack compliance (versiones y no forbidden imports) | ⬜ | ⬜ | ⬜ |

**Total requerimientos: 15**
**Cubiertos: ___ / 15**
**Sin cubrir: ___** ← debe ser 0 antes de submit

---

## GAPS DETECTADOS

```
(lista aquí requerimientos sin cobertura y qué vas a hacer)
```

---

## RESUMEN DE TESTS (F2P Baseline)

| Tipo | Cantidad |
|---|---|
| Tests totales escritos | ___ |
| Tests que fallan en codebase vacío (before.json) | ___ / ___ ← debe ser 100% |
| Tests que pasan con Golden Patch (after.json) | ___ / ___ ← debe ser 100% |
| Tests overfitted (>5% = FAIL) | ___ |

---

## RESUMEN DE RUBRICS

| Tipo | Cantidad |
|---|---|
| Criterios totales | ___ |
| Peso 5 (críticos) | ___ |
| Peso 3 (importantes) | ___ |
| Peso 1 (deseables) | ___ |

---

## VEREDICTO FINAL DE COBERTURA

| Check | Estado |
|---|---|
| 100% requerimientos cubiertos (test o rubric) | ⬜ |
| before.json = 100% FAILED | ⬜ |
| after.json = 100% PASSED | ⬜ |

### ✅ LISTO PARA SUBMIT
### ❌ FALTA CORREGIR
