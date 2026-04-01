# Guía 3 — Guía de Auditoría y Especificaciones del Proyecto Real Coder (ID: 697b72cae052640b8db3e22d)

## Resumen Ejecutivo
El proyecto Real Coder tiene como objetivo primordial la generación de soluciones de software de alta calidad, verificadas y creadas desde cero para tareas de estilo freelance. El proceso de auditoría exige la evaluación de cuatro artefactos críticos: el Agent Prompt (instrucciones para la IA), el Golden Patch (implementación de referencia), la Suite de Verificación de Doble Capa (pruebas automatizadas F2P) y una Rúbrica de Expertos multidimensional.

Los puntos críticos de control incluyen:
- **Fidelidad al Prompt:** El prompt debe ser una traducción rigurosa de la tarea original e incluir una sección obligatoria de "Expected Interfaces".
- **Integridad Técnica:** El código debe ejecutarse en un contenedor Docker específico (Ubuntu 22.04) y pasar todas las pruebas y rúbricas internas.
- **Metodología de Calificación:** Se aplica una política de "calificación al nivel más bajo", donde una falla en cualquier dimensión reduce la nota total de la tarea a ese nivel. Un puntaje de 5 requiere perfección absoluta en todas las dimensiones.

---

## 1. Contexto y Objetivos del Proyecto
El proyecto busca crear soluciones funcionales partiendo de una "pizarra en blanco". Los auditores deben asegurar que el contribuyente proporcione:
- **Agent Prompt:** Un punto de entrada estructurado para guiar a un agente de IA.
- **Golden Patch:** Una implementación funcional de "verdad absoluta" (ground truth).
- **Suite de Verificación Dual:** Pruebas automatizadas Fail-to-Pass (F2P).
- **Rúbrica de Expertos:** Un conjunto de al menos 5 criterios para evaluar el Golden Patch cuando las pruebas automatizadas no son prescriptivas.

### Entorno de Ejecución
Todo el código debe ser compatible con un contenedor Docker (Ubuntu 22.04), utilizando los scripts estandarizados `run.sh` y `parsing.py`.

---

## 2. Flujo de Trabajo de Auditoría
El proceso de evaluación se divide en seis pasos lógicos:

| Paso | Acción | Descripción Crítica |
|---|---|---|
| 1 | Revisión de Instrucciones | Consultar las guías actualizadas en la plataforma. |
| 2 | Evaluación del Prompt | Verificar que incluya la sección "Expected Interfaces" y todas las restricciones necesarias. |
| 3 | Evaluación del Golden Patch | Validar la lógica del parche y la precisión técnica del archivo Docker. |
| 4 | Evaluación de Pruebas F2P | Verificar que las pruebas fallen sin el parche y pasen con él usando `real_coder_e2e.sh`. |
| 5 | Evaluación de la Rúbrica | Asegurar que los criterios sean atómicos y verificables (mínimo 20 criterios requeridos según la interfaz). |
| 6 | Cálculo del Puntaje Final | Tally de errores y selección de categorías según las instrucciones de calificación. |

---

## 3. Dimensiones de Evaluación del Golden Response
La calidad del código y la respuesta se mide bajo criterios estrictos:

### Corrección y Ejecución
- **Compilación:** El código debe compilar sin errores. Las advertencias (warnings) pueden penalizar pero no fallar la tarea automáticamente.
- **Fallo de Verificadores (Nuevo 03/25):** Si el Golden Response falla cualquiera de sus propias pruebas F2P o criterios de rúbrica, la tarea se considera un Fallo automático.
- **Salida de Ejecución:** Los errores de tiempo de ejecución (runtime) que impacten la funcionalidad material se consideran fallos. Se exceptúan casos de borde menores (insignificantes).

### Diseño y Rendimiento
- **Eficiencia:** Se penalizan enfoques de fuerza bruta (ej. O(n^3)) cuando existen soluciones optimizadas (ej. O(n \log n)).
- **Diseño de Código:** Debe seguir principios de modularidad, abstracción y separación de preocupaciones.
- **Legibilidad:** Uso de nombres de variables significativos y formato consistente.

---

## 4. Requisitos Críticos del Agent Prompt
El prompt debe ser una herramienta funcional para que un LLM genere la solución.
- **Expected Interfaces (Interfaces Esperadas):** Es obligatorio documentar cada archivo, clase o función con la que interactuará una aplicación externa o la suite de pruebas. Debe incluir:
  - Ruta (Path) exacta.
  - Nombre y Tipo (clase, método, función).
  - Entradas y Salidas (parámetros y tipos de retorno).
  - Descripción de efectos observables.
  - Campos específicos del lenguaje (ej. herencia en Python o implementaciones en Go).
- **Factibilidad:** No debe requerir APIs externas, aunque se permite dependencia de internet para herramientas de diseño.

---

## 5. Especificaciones de la Suite de Pruebas (Test Suite)
Las pruebas deben seguir el prompt reescrito, no el Golden Patch específicamente.
- **Especificidad vs. Amplitud (Actualizado 03/25):** Se permite un margen de hasta 10% de pruebas "Overly Specific" (que prueban requisitos no pedidos) o "Overly Broad" (que permiten implementaciones inválidas). Superar este 10% resulta en fallo.
- **Cobertura de Verificadores:** Los verificadores deben cubrir todos los requisitos explícitos e implícitos. Un fallo mayor ocurre si falta cobertura para más del 5% de los requisitos principales del backend.

---

## 6. Calidad de la Rúbrica y Clasificación de Errores
Las rúbricas se evalúan de forma holística bajo tres umbrales de error:

### Definiciones de Errores Mayores (Major Issues)
- **Criterios no autocontenidos:** El criterio no puede evaluarse sin mirar el prompt u otra información externa (ej. "La respuesta identifica al presidente" vs "La respuesta identifica a George Washington como el presidente").
- **Falta de Atocimidad:** Agrupar restricciones totalmente no relacionadas en un solo criterio.
- **Criterios Incorrectos:** Errores fácticos o requisitos que no están en el prompt.
- **Encuadre (Framing):** Los criterios deben estar redactados para que una buena respuesta sea "Sí" o "Verdadero".

### Umbrales de Fallo en Rúbricas

| Tipo de Error | Umbral de Fallo (Fail) | Umbral No-Fallo (Non-Fail) |
|---|---|---|
| Errores Mayores | > 5% de los criterios | <= 5% de los criterios |
| Errores Moderados | > 15% de los criterios | <= 15% de los criterios |
| Errores Menores | > 25% de los criterios | 5% - 25% de los criterios |

---

## 7. Instrucciones Generales de Calificación (Escala 1-5)
- **Regla de la Dimensión Mínima:** La calificación final de la tarea será igual a la calificación más baja obtenida en cualquiera de las dimensiones evaluadas.
- **Esfuerzo:** Se selecciona un 1 sobre un 2 si el intento muestra poco o ningún esfuerzo.
- **Juicio Profesional:** Entre un 3 y un 4, el auditor debe usar su juicio sobre la seriedad del problema menor detectado.
- **Precedencia:** Las instrucciones del prompt o de la tarea siempre tienen prioridad sobre otras dimensiones generales (ej. si el prompt pide errores ortográficos intencionales, no se penaliza la ortografía).
