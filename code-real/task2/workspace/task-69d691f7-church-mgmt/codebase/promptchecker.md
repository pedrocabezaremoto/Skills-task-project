# Prompt Checker — Task 69d691f7
## Church Management Platform | Full Stack | TypeScript / React + Node.js

> QA Protocol v2.0 — Basado en: guia1 (Determinism Rule), guia2 (ATQAV-P), guia3 (Audit Protocol), guia6 (SWE Validation), guia9 (Task Review), guia10 (Master Audit Guide)
>
> **Regla de uso:** Ejecuta los bloques en orden. Un FAIL en cualquier bloque es condición suficiente para rechazar el prompt. Todos deben estar en ✅ PASS antes de avanzar a Fase 2.

---

## BLOQUE 0 — Pre-Validación: Scope & Feasibility

> Ejecutar primero. Si falla aquí, no continuar con los bloques siguientes.

| # | Verificación | Estado |
|---|---|---|
| 0.1 | El tipo de tarea es identificable (ej: Full Stack API + React Dashboard) | ⬜ |
| 0.2 | No hay requests imposibles ni instrucciones mutuamente excluyentes — **1 miss = FAIL automático** | ⬜ |
| 0.3 | No se requieren API keys externas, datasets descargables ni servicios live | ⬜ |
| 0.4 | No hay "stacked constraints": máximo 2 restricciones solapadas sobre el mismo elemento (ej: "brief" + "explain to a child" + "no letter e" = FAIL) | ⬜ |
| 0.5 | La tarea exige razonamiento de ingeniería de nivel senior — no es lookup trivial ni tarea de traducción directa (Reasoning Requirement) | ⬜ |

**Resultado Bloque 0:** ⬜ PASS / ⬜ FAIL

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
| 2.7 | Todas las versiones declaradas son factualmente correctas y compatibles entre sí — **cualquier error mayor = FAIL; máx 2 errores menores permitidos** | ⬜ |
| 2.8 | No se listan librerías de terceros que requieran setup externo (ej: API keys, licencias, servicios cloud) | ⬜ |

**Resultado Bloque 2:** ⬜ PASS / ⬜ FAIL

---

## BLOQUE 3 — Expected Interface

> Cada componente público debe tener los 6 campos obligatorios + validaciones adicionales para TypeScript.

### Campos requeridos por componente:

| Campo | Requerido | Descripción |
|---|---|---|
| **Path** | ✅ | Ruta exacta del archivo dentro de la estructura del repositorio |
| **Name** | ✅ | Nombre de clase/función/método sin ambigüedad |
| **Type** | ✅ | `class` / `function` / `method` / `interface` / `React component` / `Express Router` |
| **Input** | ✅ | Parámetros con tipos TypeScript explícitos |
| **Output** | ✅ | Tipo de retorno con descripción del comportamiento observable |
| **Description** | ✅ | Qué hace en 1-2 oraciones, enfocado en comportamiento externo |

### Checklist de validación:

| # | Verificación | Estado |
|---|---|---|
| 3.1 | Cada componente listado tiene los 6 campos completos | ⬜ |
| 3.2 | No se documentan helper functions internas (solo interfaces públicas que los tests importarán) | ⬜ |
| 3.3 | No se documentan campos de librerías de terceros como si fueran interfaces propias | ⬜ |
| 3.4 | Todos los componentes que los tests van a importar están documentados | ⬜ |
| 3.5 | **TypeScript-específico:** componentes que usan herencia o implementan interfaces tienen documentado `extends` / `implements` donde aplica | ⬜ |
| 3.6 | **Implementation Agnosticism:** las descripciones NO filtran lógica interna, estructura de helpers, ni decisiones de modularización — solo comportamiento observable desde fuera | ⬜ |
| 3.7 | **Minimal Surface Area:** solo se documenta el entry point primario de cada módulo; no se listan sub-rutas internas ni detalles de implementación como interfaces públicas | ⬜ |

**Resultado Bloque 3:** ⬜ PASS / ⬜ FAIL

---

## BLOQUE 4 — Linguistic Determinism Audit

> Audit obligatorio basado en la Determinism Rule (guia1). El prompt debe funcionar como una máquina de estados: un solo camino de ejecución predecible.

### 4A — Términos prohibidos (presencia de cualquiera = FAIL)

Escanear el prompt completo por estos términos:

| Término prohibido | Motivo | Presente |
|---|---|---|
| `"or"` (como alternativa de implementación) | Introduce bifurcación no-determinística | ⬜ |
| `"alternatively"` | Bifurcación explícita | ⬜ |
| `"either X or Y"` | Alternativa de diseño | ⬜ |
| `"recommended"` | Sugerencia, no mandato | ⬜ |
| `"should"` (sin ser "MUST") | Modal débil | ⬜ |
| `"you can"` | Opción discrecional | ⬜ |
| `"you may"` | Permiso, no instrucción | ⬜ |
| `"etc."` | Lista abierta, ambigua | ⬜ |
| `"something like"` | Vaguedad intencional | ⬜ |
| `"relevant technologies"` | Tech stack no especificado | ⬜ |
| `"If you want"` | Condicional discrecional | ⬜ |

> **Criterio:** 0 ocurrencias en contexto de decisión de implementación. Ocurrencias en ejemplos o nombres de campos propios del dominio son aceptables.

### 4B — Verificación de phrasing imperativo

| # | Verificación | Estado |
|---|---|---|
| 4.1 | Los requerimientos usan verbos imperativos: `MUST`, `SHALL`, `Implement`, `Create`, `Generate`, `Return` | ⬜ |
| 4.2 | No aparecen frases como "You should", "It's recommended", "If you want", "Feel free to" en los Requirements | ⬜ |
| 4.3 | Las restricciones de seguridad/acceso usan `MUST NOT` o `is strictly forbidden` — no "avoid" ni "try not to" | ⬜ |

**Resultado Bloque 4:** ⬜ PASS / ⬜ FAIL

---

## BLOQUE 5 — Requirements Coverage

> Cada requerimiento del task description original debe estar en el prompt reescrito.
>
> **Umbral de aprobación:** ≥ 95% cubiertos y testeables (máx 1 requerimiento faltante de 17). Más de 1 faltante = FAIL.

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

> **Regla del 5%:** Un gap de cobertura > 5% en requerimientos principales de backend = **Major Insufficient Coverage** = FAIL automático.
> Para 17 requerimientos: faltar ≥ 1 testeable = borde de FAIL; faltar ≥ 2 = FAIL definitivo.

**Resultado Bloque 5:** ⬜ PASS / ⬜ FAIL

---

## BLOQUE 6 — Validaciones Críticas

| # | Verificación | Estado |
|---|---|---|
| 6.1 | No hay instrucciones contradictorias en el prompt — **1 contradicción = FAIL** | ⬜ |
| 6.2 | No se menciona descarga de datasets externos ni live API | ⬜ |
| 6.3 | El prompt NO incluye instrucciones de unit tests ni rubrics (son artefactos separados) | ⬜ |
| 6.4 | Current State dice claramente que es greenfield (desde cero) | ⬜ |
| 6.5 | No hay lógica imposible de implementar dentro de un entorno Ubuntu 22.04 + Docker | ⬜ |
| 6.6 | **Factual Precision:** versiones de librerías, nombres de paquetes npm y comportamientos técnicos declarados son verificablemente correctos — máx 2 errores menores; 0 errores mayores | ⬜ |
| 6.7 | La solución completa corre en entorno local sin dependencias de red externas (backend solo en `127.0.0.1`) | ⬜ |

**Resultado Bloque 6:** ⬜ PASS / ⬜ FAIL

---

## RESULTADO FINAL

| Bloque | Descripción | Estado |
|---|---|---|
| Bloque 0 — Pre-Validación | Feasibility, Reasoning Req, Stacked Constraints | ⬜ PASS / ⬜ FAIL |
| Bloque 1 — Estructura | Pattern A/B, campos obligatorios | ⬜ PASS / ⬜ FAIL |
| Bloque 2 — Tech Stack | Versiones, compatibilidad, factual precision | ⬜ PASS / ⬜ FAIL |
| Bloque 3 — Expected Interface | 6 campos + TS-specific + impl agnosticism | ⬜ PASS / ⬜ FAIL |
| Bloque 4 — Linguistic Determinism | Términos prohibidos + phrasing imperativo | ⬜ PASS / ⬜ FAIL |
| Bloque 5 — Coverage | 17/17 requerimientos + umbral 95% | ⬜ PASS / ⬜ FAIL |
| Bloque 6 — Validaciones Críticas | Contradicciones, factual, greenfield, local | ⬜ PASS / ⬜ FAIL |

### ✅ LISTO PARA FASE 2 — todos los bloques en PASS
### ❌ REGRESA A REVISAR — uno o más bloques en FAIL

---

## SEVERITY REFERENCE

| Tipo | Condición | Impacto |
|---|---|---|
| **FAIL automático** | Instrucción imposible, contradicción, término prohibido en contexto de implementación, gap de cobertura >5%, error factual mayor | Rechazar prompt completo |
| **FAIL acumulativo** | 2+ errores menores en Tech Stack, 2+ requerimientos sin cubrir | Rechazar prompt |
| **WARNING** | 1 error menor de factual precision, 1 ítem de interfaz sin campo TS-específico | Corregir antes de avanzar |

---

## NOTAS / ISSUES ENCONTRADOS

```
(anota aquí el bloque, número de ítem y descripción del problema)

Ejemplo:
[BLOQUE 4] 4A — "or" detectado en Req 5: "weekly or biweekly" → reescribir como enum explícito
[BLOQUE 3] 3.5 — AuthRouter no documenta si implementa alguna interfaz de Express
```
