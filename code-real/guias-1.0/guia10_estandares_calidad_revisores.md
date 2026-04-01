# Guía 10 — Guía de Auditoría para Revisores: Estándares de Calidad en el Desarrollo de Software

## Resumen Ejecutivo
Este documento sintetiza los criterios críticos de evaluación establecidos en la "Hoja de Auditoría para Revisores" (Reviewer Audit Sheet). La directriz principal es garantizar la integridad, funcionalidad y precisión de los entregables técnicos a través de una revisión rigurosa de cuatro pilares fundamentales: el Prompt (instrucción), el Golden Patch (solución de referencia), los Tests (pruebas) y las Rúbricas de evaluación.

Los puntos clave incluyen la prohibición de solicitudes imposibles o errores fácticos mayores en los prompts, la exigencia de que el código sea compilable y eficiente, y la necesidad de que las rúbricas sean objetivas y no dependan exclusivamente de una implementación específica. El incumplimiento en áreas críticas, como la compilación del código o la presencia de errores fácticos en las instrucciones, resulta en una falla inmediata del proceso de auditoría.

---

## 1. Análisis del Prompt y la Interfaz
El prompt constituye la base del desarrollo. La auditoría exige que las instrucciones sean claras, realistas y contextualmente coherentes.

### Criterios de Calidad del Prompt
- **Viabilidad:** Se penalizan las solicitudes imposibles, conflictivas o poco prácticas.
- **Exactitud Fáctica:** No se permiten errores factuales mayores; se tolera un máximo de un error menor.
- **Autenticidad:** Las restricciones no deben ser artificiales ni estar excesivamente acumuladas (ej. "explícalo como a un niño" combinado con múltiples limitaciones de brevedad).
- **Dependencias Externas:** Se permiten diseños dependientes de internet, pero el requerimiento de APIs externas resulta en una falla.

### Requisitos de la Interfaz
Toda entrada en la interfaz debe estar documentada exhaustivamente, incluyendo:
- Ruta (Path), Nombre, Tipo, Entrada (Input), Salida (Output) y Descripción.
- Documentación de cada archivo, función o clase llamada por las pruebas.
- Exclusión de funciones auxiliares o campos de librerías de terceros en la lista de interfaces.

---

## 2. Estándares del "Golden Patch" (Solución de Referencia)
El Golden Patch es la implementación de referencia que debe demostrar la viabilidad de la solución propuesta.
- **Cumplimiento de Instrucciones:** Debe seguir cada instrucción explícita del prompt; omitir una sola instrucción conlleva a la falla.
- **Integridad Técnica:** El código debe ser compilable y no presentar errores de ejecución materiales. Se permiten errores menores en casos de borde que no afecten la funcionalidad principal.
- **Calidad del Código:**
  - **Legibilidad:** No debe presentar problemas de legibilidad en más de dos áreas.
  - **Nomenclatura:** Se prohíbe el uso de nombres de variables engañosos (ej. llamar `even_array` a una lista de números impares).
  - **Eficiencia:** El diseño no debe ser tosco o ineficiente, manteniendo principios básicos de modularidad y abstracción.
- **Restricciones de Contenido:** Prohibición absoluta de uso de Unsplash, activos con derechos de autor, llaves de API externas o contenido dañino.

---

## 3. Evaluación de Pruebas (Tests) y Cobertura
Las pruebas deben validar los requisitos del prompt de manera objetiva, sin sesgarse por la implementación específica del Golden Patch.
- **Validación de Requisitos:** Los tests deben verificar lo solicitado en el prompt, no los detalles internos de la implementación del revisor.
- **Especificidad:** Se limita a un máximo del 5% las pruebas excesivamente específicas que verifiquen elementos no solicitados explícitamente (como nombres de métodos internos o mensajes de error exactos).
- **Cobertura del Verificador:** Menos del 5% de los requisitos principales del backend deben quedar sin cobertura tanto por las pruebas como por las rúbricas.
- **Casos de Falla:** Un código base vacío debe fallar todas las pruebas (marcado como FAILED, no como ERROR). Un error de importación o la falta de dependencias en Dockerfile se clasifica como ERROR.

---

## 4. Estructura y Rigor de las Rúbricas
Las rúbricas deben ser instrumentos de medición precisos y objetivos.

| Error Común a Evitar | Descripción del Estándar |
|---|---|
| **Falta de autonomía** | La rúbrica debe ser clara por sí misma. *Ejemplo malo:* "Maneja el caso de borde del prompt". *Ejemplo bueno:* "Maneja entradas de cantidad negativa devolviendo un error 400". |
| **Sobreajuste (Overfitting)** | No debe rechazar alternativas válidas basándose en nombres de archivos o variables específicos no requeridos. |
| **Subjetividad** | Se deben evitar términos como "apropiado" o "mejores prácticas" sin criterios de medición definidos. |
| **Encuadre Negativo** | Las rúbricas deben redactarse para que una respuesta correcta evalúe como "Sí" o "Verdadero". |
| **Redundancia** | No se permiten pares de rúbricas que verifiquen exactamente lo mismo. |

---

## 5. Validación Técnica y Entrega de Archivos
El proceso de auditoría finaliza con una validación técnica de los archivos entregados para asegurar que el entorno sea reproducible.
- **Estructura de Archivos:** El archivo `codebase.zip` debe contener los archivos en la raíz, sin carpetas envolventes. El archivo `tests.zip` debe tener la carpeta `tests/` en el nivel superior.
- **Scripts de Ejecución:** Las secciones etiquetadas como "DO NOT MODIFY" en `run.sh` o `parsing.py` deben permanecer intactas.
- **Resultados de Pruebas:** Se debe verificar que en el archivo `before.json` todos los tests fallen, y en `after.json` todos pasen tras aplicar el Golden Patch.
- **Docker:** No se permite el uso del comando `COPY` en el Dockerfile ni en el script `run.sh`.
