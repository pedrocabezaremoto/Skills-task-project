# Guía 9 — Guía de Directrices para Revisores de Real Coder (mattock_name)

## Resumen Ejecutivo
Este documento detalla los protocolos y estándares de calidad exigidos para el equipo de revisores en el proyecto Real Coder. Los revisores actúan como la primera línea de defensa para garantizar que cada tarea (task) cumpla con las expectativas técnicas y de instrucción. El proceso se fundamenta en un flujo de trabajo riguroso que incluye la configuración de entornos locales, el uso de herramientas de evaluación automatizada (como Tara Eval), la reparación manual de errores en prompts, pruebas unitarias y soluciones (Golden Patches), y una validación final determinista. La excelencia en este rol depende de una atención minuciosa al detalle y la aplicación estricta de una rúbrica de calificación donde el puntaje final es dictado por la dimensión de menor desempeño (Lowest Dimension Rule).

### Perfil y Habilidades del Revisor Éxitoso
Para garantizar la integridad del proceso de revisión, se han identificado cuatro competencias nucleares:
- **Atención al detalle:** Capacidad para detectar errores sutiles en el código, la lógica, las pruebas y las rúbricas.
- **Comunicación escrita efectiva:** Provisión de correcciones y retroalimentación de manera clara, estructurada y constructiva.
- **Juicio objetivo:** Evaluación del trabajo basada exclusivamente en los requisitos del proyecto, evitando sesgos personales.
- **Dominio de la rúbrica de puntuación:** Conocimiento profundo de los criterios de calificación para asegurar consistencia y justicia.

---

## Flujo de Trabajo Estandarizado
El proceso de revisión sigue una secuencia lógica de pasos diseñados para eliminar errores antes de la entrega final.

### 1. Configuración del Entorno
El revisor debe crear un entorno de trabajo local con una estructura de directorios específica para garantizar la reproducibilidad.

| Directorio / Archivo | Descripción |
|---|---|
| `/app` | Contiene los archivos obligatorios: Dockerfile, tests.zip, codebase.zip, run.sh, parsing.sh (o parsing.py). |
| `without_solution/` | Carpeta para ejecución de línea base; todas las pruebas deben fallar aquí. |
| `with_solution/` | Carpeta para ejecución de verificación; todas las pruebas deben pasar tras aplicar el Golden Patch. |

### 2. Ejecución de Tara Eval
El uso de la herramienta Tara Eval es obligatorio para obtener un informe de calidad inicial.
- **Secciones de Tara Eval:**
  - **Task Info:** Metadatos, ID del intento, prompt reescrito, rúbricas y resultados de pruebas unitarias.
  - **Eval Section:** Análisis de ejecución en sandbox, comparación de archivos JSON (antes/después) y puntuación de satisfacción de requisitos.
  - **Verification & Coverage:** Evalúa si las pruebas y rúbricas son suficientes para validar los requisitos del prompt.
*Advertencia: Tara Eval es una guía, no la fuente absoluta de verdad; el revisor es el responsable final.*

### 3. Reparación de la Tarea (Fix Task)
Si se encuentran deficiencias, el revisor debe intervenir en cuatro áreas críticas:

#### 3.1 Revisión del Prompt Reescrito
Se debe asegurar que el prompt sea claro, específico y técnicamente correcto.
- **Alcance de la reparación:** Si hay errores mayores (requisitos faltantes, contradicciones o interfaces imposibles), el revisor debe arreglar el prompt y actualizar todos los componentes derivados (pruebas, Golden Patch y rúbricas).
- **Herramientas:** Se recomienda el uso de linters de prompts externos para detectar inconsistencias.

#### 3.2 Revisión de Pruebas Unitarias (F2P Validation)
Se debe garantizar el principio Fail-to-Pass (F2P):
- Las pruebas deben fallar en el entorno `without_solution`.
- Las pruebas deben pasar en el entorno `with_solution`.
- Se deben evitar pruebas frágiles o excesivamente específicas que dependan de detalles de implementación no solicitados.

#### 3.3 Revisión de Rúbricas
Las rúbricas deben cubrir los 30 requisitos más importantes que no pueden ser verificados mediante código.
- **Atomicidad:** Cada criterio debe evaluar una sola idea.
- **Neutralidad de implementación:** No deben forzar nombres de archivos internos específicos a menos que el prompt lo exija.
- **Ponderación:** Los pesos deben ser estrictamente 1 (Deseable), 3 (Importante) o 5 (Mandatorio).

#### 3.4 Golden Patch e Integridad Técnica
El Golden Patch debe ser la "verdad absoluta" de la implementación.
- **Entorno:** Debe ejecutarse perfectamente en un contenedor Docker con Ubuntu 22.04.
- **Cumplimiento de Activos:** Se prohíbe estrictamente el uso de contenido de Unsplash; todos los activos visuales deben ser 100% libres para uso comercial.
- **Auditoría de Cobertura:** Se debe realizar un mapeo del 100% de los requisitos del prompt contra la suite de verificación (pruebas + rúbricas).

### 4. Validación Final y Envío
Antes de la sumisión, es imperativo ejecutar el script `validation.sh` para confirmar que las correcciones manuales son deterministas.
- El archivo `before.json` debe mostrar un 100% de fallas en las pruebas.
- El archivo `after.json` debe mostrar un 100% de éxito.
- Se debe verificar que el archivo `codebase.zip` no contenga carpetas anidadas y que los archivos estén en la raíz.

### 5. Calificación y Retroalimentación
La calificación final no es un promedio, sino que se rige por principios de rigor extremo:
- **Regla de la Dimensión Más Baja:** El grado final de la tarea es igual al puntaje más bajo obtenido en cualquier dimensión individual (instrucción, corrección de código, calidad, claridad o eficiencia).
- **Retroalimentación Constructiva:** Los comentarios deben guiar al autor de la tarea (attempter) hacia la mejora, explicando no solo el error, sino cómo corregirlo.
- **Adherencia Estricta:** Las decisiones de calificación deben basarse únicamente en la Especificación de Control de Calidad (QC Spec) oficial, eliminando intuiciones personales del proceso.
