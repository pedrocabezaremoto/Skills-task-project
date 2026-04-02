# Step 1 — Plan the Task

> Tu primer objetivo es proponer una tarea que sea realista, suficientemente compleja para separar modelos, y totalmente evaluable.

---

## 1. Check your task type

Se te asignará uno de estos formatos:

| Formato | Descripción |
|---------|-------------|
| **Multi-turn** | Construye una conversación back-and-forth natural (no un script rígido). El modelo debe descubrir Skills, usar memoria y encontrar fricción orgánicamente entre turnos. |
| **Single-turn** | Escribe un prompt único, largo y complejo desde el inicio. No se permiten turnos de seguimiento. El prompt debe ser auto-contenido mientras fuerza Skills + memoria + coordinación de herramientas. |
| **Long context** | Primero crea una conversación previa larga que exceda 64,000 tokens. Solo después de establecer ese contexto comienzas la tarea real. La query final debe requerir explícitamente usar información del contexto previo mientras sigue usando Skills + memoria + herramientas. |

---

## 2. Pick a domain and find inspiration

La idea de la tarea debe estar inspirada en un post/discusión real online, luego elevada con complejidad arquitectónica y restricciones.

Dominios disponibles:

| Dominio | Ejemplos |
|---------|----------|
| **Health** | medical care, fitness, mental health, nutrition, sleep |
| **Exploration** | learning, creativity, hobbies, DIY, cooking |
| **Advice** | finance, career, legal, planning, decision-making |
| **Relationships** | family, dating, communication, workplace dynamics |
| **Time** | scheduling, task management, automation, travel, logistics |

---

## 3a — Write Agent Objective

Escribe el diseño del agente.

| Section | Minimum Bar | Strong Objective |
|---------|-------------|-----------------|
| **Agent Objective** | - Define una persona real con stakes operacionales. | - Crea presión de decisión natural (restricciones competitivas, ambigüedad, información incompleta). |
| | - Describe un problema concreto con restricciones reales (budget, tiempo, riesgo, umbrales, políticas, etc.). | - Tiene criterios de éxito explícitos (ej. "top 5 rankeados con justificación", "señalar violaciones sobre umbral", "comparar contra baseline de política"). |
| | - Requiere un artefacto estructurado orientado a decisión (no solo un resumen). | - Introduce contexto que luego fuerce complejidad de razonamiento (datos inciertos, estado cambiante, contradicciones entre fuentes). |
| | - Implica tradeoffs o presión de priorización. | - Importaría de forma realista en un contexto de negocio, política, financiero, operacional o personal. |

---

## 3b — Write Core Functionalities

| Section | Minimum Bar | Strong Objective |
|---------|-------------|-----------------|
| **Core Functionalities** | - Ingiere inputs estructurados o desordenados. | - Integra sistemas heterogéneos (ej. API + scraping + archivo local). |
| | - Coordina entre al menos dos sistemas/fuentes de datos significativos. | - Normaliza o fusiona datos de esquemas inconsistentes. |
| | - Realiza ≥ 3 etapas (Acquire → Process → Decide → Output). | - Implementa lógica de scoring multi-factor (≥3 variables ponderadas o balanceadas). |
| | - Implementa lógica de decisión explícita (ranking, scoring, thresholding, comparación de reglas). | - Realiza comparaciones de políticas o aplicación de restricciones. |
| | - Produce un artefacto estructurado y testeable. | - Registra acciones tomadas y las referencia después. |
| | - Mantiene alguna forma de estado (log, perfil, historial, dataset). | - Produce un artefacto exportable o reutilizable (JSON, CSV, board, reporte estructurado). |

---

## 3c — Build Complexity

| Section | Minimum Bar | Strong Objective |
|---------|-------------|-----------------|
| **Build Complexity** | - Al menos una separación modular de responsabilidades. | - Un refactor arquitectónico visible (ej. división en módulos) + al menos un momento de backtracking significativo. |
| | - Coordinación multi-etapa con dependencias visibles. | - Fricción real que fuerce cambio de estrategia (datos faltantes, unidades inconsistentes, paywall, login, rate limits…). |
| | - Al menos un punto de fricción realista. | - Lógica de scoring multi-factor implementada y revisada si es necesario. |
| | - Estado persistente creado y reutilizado. | - Estado persistente consultado antes de actuar. |
| | - Lógica de decisión explícita implementada. | - Al menos un fallo realista + recuperación + stress-testing del agente bajo restricciones. |
| | - Las mismas restricciones probadas en todos los modelos. | - Pushing comparable en los seis modelos. |

---

## 4. Validate your idea

Usa este checklist para detectar tareas "demasiado simples" temprano.

### Minimum bar checklist ✅
- [ ] Una persona real y un objetivo claro
- [ ] Inputs explícitos (archivo, sheet, API, email, dataset, etc.)
- [ ] Coordinación multi-etapa donde cada etapa depende de la anterior
- [ ] Coordinación entre al menos dos sistemas/herramientas/fuentes significativas
- [ ] Al menos un punto de fricción real que fuerce adaptación
- [ ] Un artefacto/output definido (no solo texto exploratorio)
- [ ] Estado persistente que importe después

### Not acceptable — Red flags ❌
- Workflows de un solo paso
- Summarización simple
- Queries de búsqueda básica sin lógica de decisión
- Razonamiento estático sin coordinación esencial de herramientas
- Tareas donde los modelos probablemente se desempeñarían casi idénticamente
