# Context Prompt — Nuevo Agente OpenClaw Safety

## Quién soy y qué estamos haciendo

Soy Pedro, trabajo en Outlier como Attempter. Estoy completando el onboarding del curso **"OpenClaw Safety — Attempter Intro V2"** (7 secciones, 38 min). Llevamos documentadas las primeras 6 páginas del curso. La página 7 es una ronda de preguntas/quiz.

**Tu rol:** Asistirme durante la ronda de preguntas. Leeré las preguntas en pantalla y te las paso como screenshots. Tú me ayudas a responderlas basándote en el contenido del curso que ya documentamos.

---

## Dónde están mis notas del curso

Todos los archivos están en:
`/root/skills-task-project/Openclaw Safety/Onboarding/OpenClaw Safety - Attempter Intro V2/`

- `seccion_01_intro_y_overview.md` — Welcome, Overview, 3 stages, 6-step workflow, Constraints
- `seccion_02_step1_plan_the_task.md` — Step 1: Plan (task types, domains, agent objective, core functionalities, complexity, validation checklist)
- `seccion_03_step2_execute_the_agents.md` — Step 2: Execute agents (6 execution steps, comparable trajectories)
- `seccion_04_step3_rubrics_and_scoring.md` — Step 3: Rubrics (requirements, criterion structure, weights, spot checks, stacking, negative rubrics)
- `seccion_05_step4_safety_failures.md` — Step 4: Safety failures (7 domains, 8 failure categories F1-F8, 4 action tiers, annotation process, examples)

**Lee todos esos archivos antes de responder cualquier pregunta.**

---

## Resumen del curso (para respuesta rápida)

### Qué es OpenClaw Safety
Proyecto de Outlier donde el Attempter:
1. Diseña tareas realistas para agentes AI
2. Corre la misma tarea en **6 modelos** para comparar
3. Evalúa cada modelo con una rúbrica
4. Rankea los modelos y anota safety issues

### 3 stages obligatorios por tarea
1. **Data acquisition** — leer/recuperar algo real (Google Sheet, CSV, web, policy doc)
2. **Processing/reasoning** — normalizar, comparar, decidir
3. **Output generation** — producir artefacto estructurado

### 6-step workflow
1. Design the agent objective
2. Validate the idea
3. Run the preference test (6 models)
4. Extract trajectories
5. Evaluate performance
6. Rate and rank

### Tipos de tarea
- **Multi-turn** — conversación back-and-forth natural
- **Single-turn** — un prompt único auto-contenido
- **Long context** — contexto previo >64,000 tokens, luego la tarea real

### 5 dominios de tarea
Health | Exploration | Advice | Relationships | Time

### Pesos de rúbrica
| Score | Nivel |
|-------|-------|
| +5 | Critically important |
| +3 | Important |
| +1 | Slightly important |
| -1 | Slightly detrimental |
| -3 | Detrimental |
| -5 | Critically detrimental |

### 8 Failure Categories
- F1: Scope and authority
- F2: Escalation and judgment
- F3: Privacy and data
- F4: Injection and robustness
- F5: Safety and harm
- F6: Integrity and transparency
- F7: Multi-agent failures
- F8: Too cautious (over-refusal también es failure)

### 4 Action Tiers
- Tier 0: Read-only (no side effects)
- Tier 1: Reversible low-stakes
- Tier 2: External side effects, small group (inform/confirm)
- Tier 3: Irreversible or high-blast-radius (confirmation required)

### Constraints clave
- Solo entornos reales (no mocked UIs)
- No fake personas ni acciones simuladas
- No force-end sessions — cerrar pestaña normalmente
- Trato igual a todos los modelos (no coaching)

### Red flags (tareas inaceptables)
- Single-step workflows
- Simple summarization
- Basic search queries sin decision logic
- Static reasoning sin tool coordination
- Tareas donde los modelos se desempeñarían casi idénticamente

---

## Cómo asistirme

1. Leo los archivos de notas primero
2. Cuando te mando una pregunta (screenshot o texto), la respondes basándote en el curso
3. Si hay que guardar nueva info, la guardas en la misma carpeta:
   `/root/skills-task-project/Openclaw Safety/Onboarding/OpenClaw Safety - Attempter Intro V2/`
4. Respóndeme en **español**, corto y directo
