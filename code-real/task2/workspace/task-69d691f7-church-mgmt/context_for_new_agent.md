# Contexto para el Agente Asistente - Real Coder (Task 2)

¡Hola! Eres un agente experto en desarrollo "Full Stack" (TypeScript, React, Node.js, SQLite) y tienes excelente conocimiento del flujo de Outlier "Real Coder". Estás asistiéndome paso a paso en "modo bebé" para completar una tarea.

## Resumen del Proyecto actual
Estamos construyendo una **Plataforma de gestión para iglesias y comunidades** con Node.js, Express, React y SQLite.

## Lo que se ha hecho hasta ahora (Fase 1 completada)
1.  Se inicializó el entorno de trabajo en `/root/skills-task-project/code-real/task2/workspace/task-69d691f7-church-mgmt`.
2.  Ya tengo el **Prompt Estructurado** definitivo (documentado en `fase-1-prompt/outputs/structured_prompt.md`). Este prompt incluye todos los requisitos detallados y la sección de **Expected Interface** que define exactamente las rutas, inputs y outputs que nuestro código debe tener.

## En qué etapa estamos: Fase 2 (TDD / Pruebas F2P)
Acabamos de empezar la **Fase 2**. Esto significa que necesitamos construir una suite de pruebas automatizadas que falle al 100% en un código en blanco (`before.json`).

### Tu primera tarea:
Quiero que me guíes paso a paso para completar la Fase 2 de Outlier:
1.  Necesitamos crear la suite de pruebas (basada en el `Expected Interface` del prompt). ¿Deberíamos usar `pytest` (python) para testear la API como es común en Outlier, o preferimos `Vitest/Jest` (Node)? El prompt anterior sugiere `pytest` en las plantillas. Dime qué recomiendas.
2.  Debes desglozar los requisitos para planificar las pruebas (guardaremos esto en `fase-2-tdd/outputs/requirements-decomposition.md`).
3.  Desarrollar el script de pruebas (ej. `test_main.py`) que pruebe toda la interfaz esperada.
4.  Ejecutar el script en el codebase vacío para generar el `before.json` que demuestre que el 100% de los tests fallan de forma determinista y coherente (F2P).

Por favor, actúa de forma proactiva utilizando comandos de bash/archivos si tienes los permisos dentro de la ruta `/root/skills-task-project/code-real/task2/workspace/task-69d691f7-church-mgmt` para crear los archivos necesarios. ¡Iniciemos!
