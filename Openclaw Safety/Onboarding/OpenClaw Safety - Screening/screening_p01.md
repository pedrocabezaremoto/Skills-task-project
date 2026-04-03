# OpenClaw Safety - Screening
## Pregunta 1

**Pregunta:** What are the three mandatory mechanics every OpenClaw task must force?
**Respuesta:** Discover installed Skills, create MEMORY.md, and coordinate tools

**Contexto:**
- Estas son las mecánicas que el prompt de la tarea debe forzar en el **agente**.
- **Discover installed Skills:** El agente debe descubrir qué herramientas tiene instaladas en el entorno (ej. buscando en el sistema de archivos o ejecutando comandos exploratorios, leyendo README/HEARTBEAT).
- **create MEMORY.md:** Es un requerimiento directo (como se vio en la Sección 6: "Pide explícitamente al agente que cree el archivo MEMORY.md") para mantener estado persistente entre sesiones.
- **coordinate tools:** El agente debe completar un flujo multi-etapa usando múltiples herramientas en secuencia (ej. leer email → chequear Supabase → actuar).
- Nota: *Multi-turn dialogue, rubric scoring, and safety annotation* son tareas del evaluador, no mecánicas que ejecuta el agente.

---
*Notas extraídas del Onboarding de OpenClaw Safety.*
