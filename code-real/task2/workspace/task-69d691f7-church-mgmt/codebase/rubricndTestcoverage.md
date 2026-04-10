# Rubric & Test Coverage Matrix — Task 69d691f7
## Church Management Platform | Full Stack | TypeScript / React + Node.js

> Este archivo mapea CADA requerimiento del prompt contra su método de verificación (unit test y/o rubric). Ningún requerimiento puede quedar sin cubrir.

---

## REGLA DE COBERTURA

```
Backend funcional  → Unit Test (F2P) — obligatorio
Frontend / UI      → Rubric — obligatorio
Arquitectura       → Rubric
Lo que tests no cubren → Rubric — sin excepciones
```

---

## MATRIZ DE COBERTURA

| # | Requerimiento | Cubierto por Test | Cubierto por Rubric | Cobertura Total |
|---|---|---|---|---|
| R01 | Registro de organización (nombre, misión, staff) | ⬜ Test # ___ | ⬜ Rubric # ___ | ⬜ |
| R02 | Perfil de miembro (nombre, contacto, familia, fecha, áreas) | ⬜ Test # ___ | ⬜ Rubric # ___ | ⬜ |
| R03 | Lista de áreas configurable | ⬜ Test # ___ | ⬜ | ⬜ |
| R04 | Creación de grupos pequeños (nombre, desc, frecuencia, día/hora, ubicación, líder, categoría) | ⬜ Test # ___ | ⬜ Rubric # ___ | ⬜ |
| R05 | Solicitud de unión a grupo | ⬜ Test # ___ | ⬜ | ⬜ |
| R06 | Aprobación de solicitud por líder | ⬜ Test # ___ | ⬜ | ⬜ |
| R07 | Roster del grupo | ⬜ Test # ___ | ⬜ | ⬜ |
| R08 | Tracker de asistencia por reunión | ⬜ Test # ___ | ⬜ Rubric # ___ | ⬜ |
| R09 | Tablero de discusión por grupo | ⬜ Test # ___ | ⬜ Rubric # ___ | ⬜ |
| R10 | Lista de peticiones de oración (visible solo para miembros del grupo) | ⬜ Test # ___ | ⬜ Rubric # ___ | ⬜ |
| R11 | Calendario de eventos (fecha, hora, lugar, descripción) | ⬜ Test # ___ | ⬜ Rubric # ___ | ⬜ |
| R12 | RSVP en eventos | ⬜ Test # ___ | ⬜ | ⬜ |
| R13 | Sistema de voluntarios — slots semanales, posiciones | ⬜ Test # ___ | ⬜ Rubric # ___ | ⬜ |
| R14 | Sign-up o asignación de voluntarios | ⬜ Test # ___ | ⬜ | ⬜ |
| R15 | Detección de conflicto (doble bookeo) | ⬜ Test # ___ | ⬜ | ⬜ |
| R16 | Alerta de posición vacante (gap alert) | ⬜ Test # ___ | ⬜ | ⬜ |
| R17 | Check-in para eventos (búsqueda por nombre + botón) | ⬜ Test # ___ | ⬜ Rubric # ___ | ⬜ |
| R18 | Tracker de donaciones (monto, fecha, fondo) | ⬜ Test # ___ | ⬜ | ⬜ |
| R19 | Resumen anual por miembro y totales org | ⬜ Test # ___ | ⬜ Rubric # ___ | ⬜ |
| R20 | Herramienta de comunicación / anuncios (todos o por área) | ⬜ Test # ___ | ⬜ Rubric # ___ | ⬜ |
| R21 | Reportes: tendencias de asistencia de grupos | ⬜ Test # ___ | ⬜ Rubric # ___ | ⬜ |
| R22 | Puntaje de engagement por miembro (eventos + grupos) | ⬜ Test # ___ | ⬜ Rubric # ___ | ⬜ |
| R23 | Persistencia en SQLite | ⬜ Test # ___ | ⬜ Rubric # ___ | ⬜ |
| R24 | JWT auth — rol staff | ⬜ Test # ___ | ⬜ | ⬜ |
| R25 | JWT auth — rol group leader | ⬜ Test # ___ | ⬜ | ⬜ |
| R26 | JWT auth — rol member | ⬜ Test # ___ | ⬜ | ⬜ |
| R27 | Perfiles de familia (spouse, children como perfiles separados vinculados) | ⬜ Test # ___ | ⬜ Rubric # ___ | ⬜ |

**Total requerimientos: 27**
**Cubiertos: ___ / 27**
**Sin cubrir: ___** ← debe ser 0 antes de submit

---

## GAPS DETECTADOS

```
(lista aquí requerimientos sin cobertura y qué vas a hacer)
```

---

## RESUMEN DE TESTS

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
| Con errores MAJOR | ___ |
| Con errores MODERATE | ___ |
| Con errores MINOR | ___ |

---

## VEREDICTO FINAL DE COBERTURA

| Check | Estado |
|---|---|
| 100% requerimientos cubiertos (test o rubric) | ⬜ |
| 0% tests overfitted (o <5%) | ⬜ |
| 0% rubrics con error MAJOR (o <5%) | ⬜ |
| before.json = 100% FAILED | ⬜ |
| after.json = 100% PASSED | ⬜ |

### ✅ LISTO PARA SUBMIT
### ❌ FALTA CORREGIR
