# OpenClaw Safety - Screening Answers

---

## Q1 — Three mandatory mechanics every OpenClaw task must force

**Correct answer:** Discover installed Skills, create MEMORY.md, and coordinate tools

**Why:** From seccion_06 (Design & Validate):
- El agente debe descubrir Skills instalados en el entorno
- Crear y consultar `MEMORY.md` para estado persistente entre sesiones
- Coordinar herramientas en flujo multi-etapa (email → Supabase → acción → recap)

---

## Q2 — "Summarize three articles about climate change" — correct assessment?

**Correct answer:** This is a red flag — simple summarization is not acceptable

**Why:** OpenClaw tasks deben forzar coordinación multi-etapa, al menos un punto de fricción, y estado persistente vía MEMORY.md. Una tarea de resumen es un solo paso, sin tools, sin fricción, sin multi-turn real. No califica como tarea válida de OpenClaw sin importar si tiene rubric o múltiples turnos.

**Wrong options:**
- "Acceptable because it involves web search" — web search no es suficiente para ser válida
- "Acceptable if it spans multiple turns" — el problema no es los turnos, es la falta de complejidad
- "Acceptable as long as a rubric is written for it" — una rubric no salva una tarea mal diseñada

---

## Q1 — Wrong options (original):
- "Web search, file upload, and code execution" — herramientas genéricas, no las mecánicas específicas de OpenClaw
- "Multi-turn dialogue, rubric scoring, and safety annotation" — son pasos del evaluador, no mecánicas del agente
- "Data acquisition, processing, and output generation" — demasiado genérico, no específico de OpenClaw

