# Reporte de Mejoras — rubricChecker.md v2.0
## Task 69d691f7 | Church Management Platform

**Fecha:** 2026-04-11
**Archivo mejorado:** `workspace/task-69d691f7-church-mgmt/codebase/rubricChecker.md`

---

## Contexto

Se realizó una auditoría del `rubricChecker.md` comparándolo contra las 10 guías oficiales en `knowledge-base/official-guides/`. Se identificaron 3 gaps que podían causar falsos positivos al validar un rubric.

---

## Cambios Realizados en Bloque 2

### 1. Nueva fila — Reframing correcto (MODERATE)

**Antes:** No existía.

**Después:**
```
| Reframing correcto | "Does not use X" → debe decir "Successfully avoids X" | MODERATE si usa "no / does not / evita que" directo |
```

**Por qué:** Guia9 (Task Review & Validation) exige explícitamente que criterios con negativo implícito sean reescritos en positivo activo. El checker anterior dejaba pasar esta forma incorrecta.

---

### 2. Nueva fila — No redundancia (MODERATE)

**Antes:** No existía.

**Después:**
```
| No redundancia | No hay otro criterio verificando el mismo requisito | MODERATE si hay par duplicado |
```

**Por qué:** Guia2 (ATQAV) y Guia10 (Master Guide) prohíben explícitamente criterios duplicados. Sin este check, un rubric con pares redundantes pasaba la validación.

---

### 3. Fila modificada — Peso correcto dividida en 2

**Antes:**
```
| Peso correcto | 5=crítico, 3=importante, 1=deseable | MINOR si off by 1 level |
```

**Después:**
```
| Peso correcto (gap 1) | 5=crítico, 3=importante, 1=deseable — off by 1 nivel | MINOR |
| Peso correcto (gap 2) | Desviación de 2 niveles (ej: puso 1, debía ser 5)    | MAJOR |
```

**Por qué:** Guia3 (Technical Audit) y Guia10 (Master Guide) distinguen claramente los dos casos. Un gap de 2 niveles es MAJOR, no MINOR. El checker anterior clasificaba ambos como MINOR.

---

## Guías que respaldan estos cambios

| Cambio | Guía de respaldo |
|---|---|
| Reframing correcto | Guia9 — Task Review & Validation (sección 4) |
| No redundancia | Guia2 — ATQAV Protocol (sección 6), Guia10 — Master Guide (sección 6) |
| Weight gap 2 niveles = MAJOR | Guia3 — Technical Audit (sección 5), Guia10 — Master Guide (sección 6) |

---

## Estado

- Versión anterior: v1.0 (sin estos 3 checks)
- Versión actual: v2.0 (11 filas en Bloque 2, alineado con guías oficiales)
