# Step 2 — Execute the Agents

> Una vez que escribes tu diseño, corres la misma tarea en todos los modelos para producir trayectorias comparables.

---

## Execution steps (per model)

1. Abre OpenClaw en una nueva pestaña y selecciona un modelo.
2. Realiza una interacción normal (construye el agente; no "scriptees" toda la corrida).
3. Cuando termines, **cierra la pestaña sin forzar el fin de sesión**.
4. Si necesitas continuar, reabre y reanuda la conversación.
5. Cuando estés completamente listo, haz clic en **"Collect Traces & Continue"** en la tarea.
6. Después de todas las corridas, rankearás las respuestas de los modelos arrastrando de mejor a peor.

---

## Make trajectories comparable

> Debes mantener el mismo objetivo, inputs y restricciones en todos los modelos.

### Reglas críticas ❌
- **No "coaches" a un modelo más que a otro.** Si aclaras algo, asegúrate de que todos los modelos reciban la misma aclaración o contexto.
- **Rastrea desviaciones mayores** (acceso faltante, fallas de herramientas, ambigüedad) para poder puntuar de forma justa después.
- **Asegúrate de que cada corrida realmente use** los Skills/tools requeridos y escriba estado significativo en MEMORY.md.
