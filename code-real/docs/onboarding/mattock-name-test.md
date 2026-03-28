# Curso Mattock Name Test

Aquí tienes las dos tareas solicitadas:

## Tarea 1: Informe Técnico de Validación (Post-Examen)

Este reporte resume los criterios técnicos que validamos con éxito para tu repositorio personal de habilidades.

### Resumen de Criterios Mattock - Onboarding Fase 1

*   **Estándares de Rúbrica:** Se confirmó que solo se permiten pesos de **1, 3 y 5**. Los criterios deben ser **Atómicos** (una sola validación) y redactados con **Fraseo Positivo** (ej. "The code handles..." en lugar de "The code doesn't crash").
*   **Protocolo F2P (Evidence A):** El Baseline Execution siempre debe reportar **FAILED** en el JSON. Incluso si el runner tiene un error fatal (como un `ModuleNotFoundError` por falta de archivos), el script `parsing.py` debe interceptar el error y mapear los tests como fallidos. Reportar `ERROR` o una lista vacía invalida la tarea.
*   **Alineación Golden Patch:** El Prompt es la fuente de verdad. Si un test exige algo que el prompt no pide (Overfitting), se debe corregir el test y regenerar ambos JSONs (Evidence A y B) para mantener la consistencia.
*   **Aislamiento Docker:** Prohibición absoluta del comando `COPY` o `ADD` en el `Dockerfile`. El código se inyecta por volúmenes. La imagen base mandatoria es `ubuntu:22.04`. Cambiar a alpine o usar `COPY` rompe el entorno de validación dinámica.
*   **Mocks y Acoplamiento:** Se identificó que mockear rutas de importación específicas (ej. `src.file_sync.paramiko`) es una violación crítica. Los tests deben ser agnósticos a la implementación (usar mocks que no dependan del estilo de import del dev).
*   **Orquestación de Scripts:** En `validation.sh`, solo es editable la variable `APP_DIR`. Modificar la lógica del script de validación fuera de esa variable se considera manipulación de infraestructura.
