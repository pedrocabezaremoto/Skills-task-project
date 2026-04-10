# Rubric Checker — Task 69d691f7
## Church Management Platform | Full Stack | TypeScript / React + Node.js

> Usa este archivo en Cursor Chat para auditar cada criterio del rubric antes de Fase 5.

---

## INSTRUCCIÓN DE USO

Para cada criterio del rubric, verifica los ítems de abajo. Un criterio con cualquier issue MAJOR = FAIL del rubric completo si supera el 5%.

---

## BLOQUE 1 — Reglas Generales del Rubric

| # | Verificación | Estado |
|---|---|---|
| 1.1 | Hay mínimo **5 criterios** y máximo **30 criterios** | ⬜ |
| 1.2 | Todos los pesos son **1, 3 o 5** (nunca 2 ni 4) | ⬜ |
| 1.3 | Los criterios cubren los **top 30 requerimientos no testeables** por unit tests | ⬜ |
| 1.4 | No hay criterios que duplican cobertura de los unit tests | ⬜ |
| 1.5 | El rubric cubre requerimientos **frontend/UI** que los tests no pueden verificar | ⬜ |

---

## BLOQUE 2 — Calidad de Cada Criterio

Para cada criterio, verifica:

| Propiedad | Regla | Tipo de error si falla |
|---|---|---|
| **Atomicidad** | Verifica UNA sola cosa discreta | MAJOR si agrupa cosas sin relación |
| **Self-contained** | Se puede evaluar SIN leer el prompt | MAJOR si requiere contexto externo |
| **Positive framing** | El criterio evalúa a YES/PASS cuando es correcto | MAJOR si está en negativo |
| **No overfitting** | No fuerza implementación específica que el prompt no pidió | MODERATE |
| **No underfitting** | No tan vago que acepta respuestas incorrectas | MODERATE |
| **No subjetivo** | Sin "apropiado", "correcto", "buenas prácticas" sin definir | MODERATE |
| **Peso correcto** | 5=crítico, 3=importante, 1=deseable | MINOR si off by 1 level |
| **Categoría correcta** | Instrucción Seguida / Corrección / Eficiencia / Claridad / Calidad | MINOR |

---

## BLOQUE 3 — Dimensiones Obligatorias

Todo rubric debe tener al menos 1 criterio en cada dimensión:

| Dimensión | Al menos 1 criterio | Estado |
|---|---|---|
| Instruction Following | | ⬜ |
| Code Correctness | | ⬜ |
| Code Quality | | ⬜ |
| Code Clarity | | ⬜ |
| Code Efficiency | | ⬜ |

---

## BLOQUE 4 — Pesos de Referencia para Esta Tarea

| Peso | Descripción |
|---|---|
| **5 — Crítico** | JWT auth con roles, SQLite persistencia, funcionalidad core (grupos, eventos, donaciones) |
| **3 — Importante** | RSVP, volunteer scheduling, conflict detection, reporting |
| **1 — Deseable** | UI profesional, mensajes de error descriptivos, responsive design |

---

## BLOQUE 5 — Conteo de Errores

| Tipo | Cantidad | % del total | ¿FAIL? |
|---|---|---|---|
| MAJOR | | | ⬜ >5% → FAIL |
| MODERATE (incl. major) | | | ⬜ >15% → FAIL |
| MINOR (incl. todos) | | | ⬜ >25% → FAIL |

**Total criterios escritos:** ___
**Umbral MAJOR para FAIL:** ___ criterios (5% de total)
**Umbral MODERATE para FAIL:** ___ criterios (15% de total)

---

## RESULTADO FINAL

| Bloque | Estado |
|---|---|
| Bloque 1 — Reglas generales | ⬜ PASS / ⬜ FAIL |
| Bloque 2 — Calidad por criterio | ⬜ PASS / ⬜ FAIL |
| Bloque 3 — 5 dimensiones cubiertas | ⬜ PASS / ⬜ FAIL |
| Bloque 4 — Pesos correctos | ⬜ PASS / ⬜ FAIL |
| Bloque 5 — Error rate OK | ⬜ PASS / ⬜ FAIL |

### ✅ RUBRIC LISTO — todos los bloques en PASS
### ❌ REGRESA A CORREGIR — uno o más bloques en FAIL

---

## NOTAS / ISSUES ENCONTRADOS

```
(anota aquí cualquier criterio con problema)
```
