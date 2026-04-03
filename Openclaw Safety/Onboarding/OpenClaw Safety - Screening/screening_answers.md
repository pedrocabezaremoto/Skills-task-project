# OpenClaw Safety - Screening Answers

---

## Q1 — Three mandatory mechanics every OpenClaw task must force

**Correct answer:** Discover installed Skills, create MEMORY.md, and coordinate tools

**Why:** From seccion_06 (Design & Validate):
- El agente debe descubrir Skills instalados en el entorno
- Crear y consultar `MEMORY.md` para estado persistente entre sesiones
- Coordinar herramientas en flujo multi-etapa (email → Supabase → acción → recap)

**Wrong options:**
- "Web search, file upload, and code execution" — herramientas genéricas, no las mecánicas específicas de OpenClaw
- "Multi-turn dialogue, rubric scoring, and safety annotation" — son pasos del evaluador, no mecánicas del agente
- "Data acquisition, processing, and output generation" — demasiado genérico, no específico de OpenClaw

