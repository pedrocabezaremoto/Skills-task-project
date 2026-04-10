# Prompt Checker — Task 69d691f7
## Church Management Platform | Full Stack | TypeScript / React + Node.js

> Usa este archivo en Cursor Chat con el system prompt activo para auditar el prompt antes de avanzar.

---

## INSTRUCCIÓN DE USO

Pega el contenido de `prompt.md` y ejecuta este checklist. Cada ítem debe estar en ✅ antes de pasar a Fase 2.

---

## BLOQUE 1 — Estructura del Prompt (Pattern A / B)

| # | Verificación | Estado |
|---|---|---|
| 1.1 | El prompt usa **Pattern A** (Current State en posición 3) o **Pattern B** (Current State en posición 6) | ⬜ |
| 1.2 | El campo **Title** está presente y describe claramente la tarea | ⬜ |
| 1.3 | El campo **Context** explica el problema y quién lo usa | ⬜ |
| 1.4 | El campo **Tech Stack** define lenguaje/framework con versiones exactas | ⬜ |
| 1.5 | El campo **Requirements** lista requerimientos numerados, determinísticos y testeables | ⬜ |
| 1.6 | El campo **Expected Interface** está presente con todos los componentes públicos | ⬜ |
| 1.7 | El campo **Current State** está en la posición correcta según el patrón elegido | ⬜ |

**Resultado Bloque 1:** ⬜ PASS / ⬜ FAIL

---

## BLOQUE 2 — Tech Stack

| # | Verificación | Estado |
|---|---|---|
| 2.1 | El Tech Stack NO dice "Any" ni "your choice" — es específico | ⬜ |
| 2.2 | Se especifica TypeScript + React (frontend) | ⬜ |
| 2.3 | Se especifica Node.js (backend) con versión | ⬜ |
| 2.4 | Se especifica SQLite como base de datos | ⬜ |
| 2.5 | Se especifica JWT para autenticación | ⬜ |
| 2.6 | Las versiones de dependencias son explícitas (no "latest") | ⬜ |

**Resultado Bloque 2:** ⬜ PASS / ⬜ FAIL

---

## BLOQUE 3 — Expected Interface

> Cada componente público debe tener los 6 campos obligatorios.

| Campo | Requerido | Descripción |
|---|---|---|
| **Path** | ✅ | Ruta exacta del archivo |
| **Name** | ✅ | Nombre de clase/función/método |
| **Type** | ✅ | class / function / method / interface |
| **Input** | ✅ | Parámetros con tipos TypeScript |
| **Output** | ✅ | Tipo de retorno con descripción |
| **Description** | ✅ | Qué hace en 1-2 oraciones |

| # | Verificación | Estado |
|---|---|---|
| 3.1 | Cada componente listado tiene los 6 campos completos | ⬜ |
| 3.2 | No se documentan helper functions internas (solo interfaces públicas) | ⬜ |
| 3.3 | No se documentan campos de librerías de terceros | ⬜ |
| 3.4 | Todos los componentes que los tests van a importar están documentados | ⬜ |

**Resultado Bloque 3:** ⬜ PASS / ⬜ FAIL

---

## BLOQUE 4 — Requerimientos (Coverage Check)

> Cada requerimiento del task description original debe estar en el prompt reescrito.

### Checklist de requerimientos clave de esta tarea:

| # | Requerimiento | En prompt | Testeable |
|---|---|---|---|
| R01 | Registro de organización (nombre, misión, staff admin) | ⬜ | ⬜ |
| R02 | Perfil de miembro (nombre, contacto, familia, fecha membresía, áreas) | ⬜ | ⬜ |
| R03 | Lista de áreas de involucramiento configurable | ⬜ | ⬜ |
| R04 | Creación de grupos pequeños (nombre, descripción, frecuencia, líder, categoría) | ⬜ | ⬜ |
| R05 | Solicitud de unión a grupo + aprobación por líder | ⬜ | ⬜ |
| R06 | Roster del grupo + tracker de asistencia por reunión | ⬜ | ⬜ |
| R07 | Tablero de discusión por grupo | ⬜ | ⬜ |
| R08 | Lista de peticiones de oración (solo visible para miembros del grupo) | ⬜ | ⬜ |
| R09 | Calendario de eventos con RSVP | ⬜ | ⬜ |
| R10 | Sistema de voluntarios con slots semanales, asignación y conflictos | ⬜ | ⬜ |
| R11 | Detección de conflicto (doble bookeo) y alerta de posición vacante | ⬜ | ⬜ |
| R12 | Sistema de check-in para eventos (búsqueda por nombre + botón) | ⬜ | ⬜ |
| R13 | Tracker de donaciones (monto, fecha, fondo, resumen anual) | ⬜ | ⬜ |
| R14 | Herramienta de comunicación (anuncios a todos o por área) | ⬜ | ⬜ |
| R15 | Reportes: métricas de salud de grupos, tendencias de asistencia, puntaje de engagement | ⬜ | ⬜ |
| R16 | Persistencia en SQLite | ⬜ | ⬜ |
| R17 | JWT auth con 3 roles: staff, group leader, member | ⬜ | ⬜ |

**Total cubiertos: ___ / 17**

---

## BLOQUE 5 — Validaciones Críticas

| # | Verificación | Estado |
|---|---|---|
| 5.1 | No hay instrucciones contradictorias en el prompt | ⬜ |
| 5.2 | No se menciona descarga de datasets externos ni live API | ⬜ |
| 5.3 | El prompt NO incluye instrucciones de unit tests ni rubrics | ⬜ |
| 5.4 | Current State dice claramente que es greenfield (desde cero) | ⬜ |
| 5.5 | No hay lógica imposible de implementar | ⬜ |
| 5.6 | El prompt puede ser resuelto por un LLM en un solo response | ⬜ |

**Resultado Bloque 5:** ⬜ PASS / ⬜ FAIL

---

## RESULTADO FINAL

| Bloque | Estado |
|---|---|
| Bloque 1 — Estructura | ⬜ PASS / ⬜ FAIL |
| Bloque 2 — Tech Stack | ⬜ PASS / ⬜ FAIL |
| Bloque 3 — Expected Interface | ⬜ PASS / ⬜ FAIL |
| Bloque 4 — Coverage | ⬜ PASS / ⬜ FAIL |
| Bloque 5 — Validaciones | ⬜ PASS / ⬜ FAIL |

### ✅ LISTO PARA FASE 2 — todos los bloques en PASS
### ❌ REGRESA A REVISAR — uno o más bloques en FAIL

---

## NOTAS / ISSUES ENCONTRADOS

```
(anota aquí cualquier problema encontrado durante la revisión)
```
