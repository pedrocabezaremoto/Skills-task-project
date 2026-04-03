# OpenClaw Safety - Screening
## Pregunta 1

**Pregunta:** What are the three mandatory mechanics every OpenClaw task must force?
**Respuesta:** Multi-turn dialogue, rubric scoring, and safety annotation.

**Contexto:**
- **Multi-turn:** El evaluador simula una conversación real de varios turnos con el agente para probar su capacidad de razonamiento y uso de herramientas en pasos sucesivos.
- **Rubric scoring:** La evaluación de cada modelo (los 5 iniciales + la trayectoria Silver) se rige por rúbricas de criterios positivos y negativos.
- **Safety annotation:** Es obligatorio anotar cualquier violación de seguridad usando los códigos F1-F8 (como F3 para fugas de privacidad o F6 para alucinaciones).

---
*Notas extraídas del Onboarding de OpenClaw Safety.*
