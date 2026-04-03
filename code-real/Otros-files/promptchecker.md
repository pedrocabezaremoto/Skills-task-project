# 🔍 Prompt Checker — Checklist de Revisión de Prompts Reescritos

> **Uso:** Revisar cada prompt reescrito antes de la entrega contra estas reglas.
> Ref: G1 §Paso 1, G2 §6, G3 §Paso 2, G6 §1, G8 §2-3, G9 §4.1

---

## 1. Estructura Obligatoria del Prompt

Cada prompt reescrito **DEBE** contener estas secciones:

| Sección | Status | Descripción |
|---|---|---|
| `Título y Contexto` | `[ ]` | Nombre del proyecto + objetivos claros |
| `Tech Stack` | `[ ]` | Lenguajes y frameworks explícitos (prohibido "Any") |
| `Key Requirements` | `[ ]` | Lista detallada de funcionalidades y comportamientos |
| `Expected Interface` | `[ ]` | **CRÍTICO** — Cada archivo/función/clase/endpoint documentado |

---

## 2. Expected Interface — Los 6 Campos Obligatorios (G3 §Paso 2, G8 §3)

> ⚠️ **FALLO CRÍTICO** si falta cualquiera de estos campos en cualquier entrada.

Cada componente público en la interfaz debe documentar:

| # | Campo | Descripción | Ejemplo |
|---|---|---|---|
| 1 | **Path** | Ruta del archivo | `src/calculator.py` |
| 2 | **Name** | Nombre de la función/clase/endpoint | `calculate_total` |
| 3 | **Type** | Tipo de componente | `function`, `class`, `API endpoint` |
| 4 | **Input** | Parámetros con tipos | `items: list[dict], tax_rate: float` |
| 5 | **Output** | Tipo de retorno o respuesta | `float` o `200 OK con JSON body` |
| 6 | **Description** | Qué validará la prueba | `Retorna el total con impuesto aplicado` |

### Campos Específicos por Lenguaje (si aplica)

| Lenguaje | Campo Adicional |
|---|---|
| Java/TypeScript | `extends`/`implements` |
| Go | `embedding` |
| Python | `Bases`/`Overrides` |
| Java/Kotlin | `Annotations`/`Decorators` |

> **Regla G8:** Si Input u Output no aplican, usar `N/A` explícitamente.

---

## 3. Validación de Contenido del Prompt

### 3.1 Instrucciones No Conflictivas (G8 §2)

- `[ ]` ¿Todos los requisitos son compatibles simultáneamente con el stack?
  - ❌ Error: Pedir "sin acceso a internet" pero incluir NLTK/spaCy que descargan datos
  - ❌ Error: Pedir "SQLite" cuando el original decía "SQLite o JSON"

### 3.2 Fidelidad al Prompt Original (G8 §2)

- `[ ]` ¿Se preserva la flexibilidad del brief original?
- `[ ]` ¿Cada adición es rastreable al informe inicial del cliente?
- `[ ]` ¿No se eliminaron opciones que el cliente dejó abiertas?

### 3.3 Estilo de Redacción (G2 §6, G8 §2)

- `[ ]` ¿Usa estilo de solicitud de cliente profesional? ("Necesito...", no "Construye...")
- `[ ]` ¿El prompt es de naturaleza cerrada (close-ended)?
- `[ ]` ¿No contiene números de tarea ni notas internas?
- `[ ]` ¿No incluye meta-datos como presupuesto o cronograma?

### 3.4 Contenido Prohibido (G1 §2, G2 §6)

- `[ ]` ¿No requiere claves de API externas?
- `[ ]` ¿No usa iconos con derechos de autor?
- `[ ]` ¿No clona interfaces de sitios web existentes?
- `[ ]` ¿No usa contenido de Unsplash?
- `[ ]` ¿Los activos son 100% comerciales? (Google Fonts, Lucide/Heroicons, Pexels)

---

## 4. Criterios de Evaluación del Prompt (G3 §3)

| Sub-dimensión | Criterio de Fallo (1-2) | No-Fallo (3-4) |
|---|---|---|
| **Requisito de Razonamiento** | Solo búsqueda de hechos | Razonamiento trivial del dominio |
| **Restricciones** | Poco realistas o apiladas (3+) | Básicas pero creíbles |
| **Veracidad** | 1+ error factual mayor o 2+ menores | 1 error factual menor |
| **Factibilidad** | Impráctica o instrucciones en conflicto | Concesiones menores en requisitos secundarios |
| **Interfaces Esperadas** | Ausentes, incompletas o engañosas | Todos los campos y tipos presentes |

---

## 5. Flujo de Verificación Rápida

```
┌─────────────────────────────────────────────────┐
│  1. ¿Tiene las 4 secciones obligatorias?        │  → Si NO → FALLO
│  2. ¿Expected Interface tiene 6 campos/entrada? │  → Si NO → FALLO CRÍTICO
│  3. ¿Instrucciones son compatibles entre sí?    │  → Si NO → Corregir
│  4. ¿Preserva la flexibilidad del original?     │  → Si NO → Corregir
│  5. ¿Estilo "solicitud de cliente"?             │  → Si NO → Reescribir
│  6. ¿Sin contenido prohibido?                   │  → Si NO → FALLO
│  7. ¿Stack tecnológico explícito?               │  → Si NO → Definir
└─────────────────────────────────────────────────┘
```

---

## 6. Errores Más Comunes en Prompts (G8 §2)

| # | Error | Impacto | Solución |
|---|---|---|---|
| 1 | Omitir Expected Interface | Las pruebas externas no pueden ejecutarse | Documentar CADA componente público |
| 2 | Escribir en estilo imperativo | No simula un brief freelance real | Usar "Necesito un sistema que..." |
| 3 | Dejar notas internas visibles | Contamina el prompt | Limpiar antes de entrega |
| 4 | Exigir stack no solicitado | Restricción artificial | Preservar opciones del cliente |
| 5 | Descripciones engañosas en Interface | El desarrollador construye algo distinto | Detallar selectores DOM, headers, campos |
| 6 | Conflictos entre requisitos | Imposibilidad técnica | Verificar compatibilidad de todo el stack |
