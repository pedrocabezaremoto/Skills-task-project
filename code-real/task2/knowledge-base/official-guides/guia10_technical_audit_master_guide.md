# Guía Maestra de Auditoría Técnica para Agentes de Programación

## 1. Introducción al Marco de Auditoría y Control de Calidad

En el ciclo de vida del desarrollo de software moderno, la auditoría técnica constituye el eje fundamental que garantiza la transición de un prototipo experimental a un sistema de grado productivo. Un marco de evaluación riguroso no es opcional; es la única metodología capaz de salvaguardar la integridad de las respuestas generadas por agentes de Inteligencia Artificial (IA), mitigando errores lógicos y vulnerabilidades antes de su despliegue.

El propósito de esta guía es establecer un protocolo estandarizado y mandatorio para la validación de prompts, interfaces de desarrollo, código fuente (Golden Patch) y entornos de ejecución. Este documento dicta los estándares técnicos de aceptación que todo auditor debe aplicar para asegurar la excelencia técnica. La ejecución exitosa de este flujo de control comienza con una inspección implacable del punto de entrada: el Prompt.

---

## 2. Protocolo de Análisis y Validación de Prompts

El prompt es el cimiento estratégico del proyecto; cualquier ambigüedad, contradicción o restricción técnica inviable en esta etapa desencadenará errores en cascada que invalidan el trabajo posterior. El auditor debe rechazar cualquier prompt que comprometa la viabilidad del desarrollo o que imponga limitaciones artificiales que no aporten valor técnico.

### Prompt Acceptance Criteria:

1.  **No impossible, conflicting, or impractical requests**: Any logical contradiction results in an immediate failure (1 miss = fail).
2.  **Factual precision**: The prompt must be technically accurate. A maximum of two minor errors is permitted; two or more minor errors, or any major factual error, will result in failure.
3.  **Avoidance of "stacked constraints"**: Reject prompts that are over-constrained (3+ overlapping constraints, e.g., "keep it brief" + "explain to a child" + "no using the letter 'e'").
4.  **Preservation of context**: If a prompt is rewritten for clarity, it must not fundamentally alter the original task’s context or scope.
5.  **External dependencies**: Internet-dependent designs are permitted, but requirements for specific external APIs that cannot be simulated or accessed are grounds for failure.

> [!NOTE]
> Tras validar el prompt, el auditor debe asegurar que la estructura de comunicación sea consistente y esté plenamente documentada.

---

## 3. Especificación Técnica de la Interfaz de Desarrollo

La interoperabilidad del sistema depende de interfaces normalizadas. El auditor debe exigir una definición contractual clara que sirva de puente entre el requisito y la implementación, eliminando cualquier ambigüedad en los puntos de entrada y salida del sistema.

| Campo | Descripción |
| :--- | :--- |
| **Path** | Ruta exacta del archivo dentro de la estructura del proyecto. |
| **Name** | Identificador único de la función, clase o componente. |
| **Type** | Clasificación técnica (ej. Clase, Método, Endpoint, Interfaz). |
| **Input** | Especificación completa de parámetros y tipos de datos aceptados. |
| **Output** | Definición del formato y tipo de dato del valor de retorno. |
| **Description** | Explicación funcional de la responsabilidad del componente. |

### Protocolo de Verificación de Interfaz: 

El auditor deberá realizar un cross-check obligatorio de las importaciones de las pruebas contra la lista de interfaces. 

> [!WARNING]
> Si una prueba invoca una función o archivo no documentado en la interfaz, se considera un fallo de auditoría. Asimismo, el agente tiene prohibido listar funciones de ayuda (helpers) o librerías de terceros como interfaces principales.

Una vez blindada la interfaz, el proceso se centra en la ejecución de la lógica central: el Golden Patch.

---

## 4. Lógica de Implementación y Requisitos del "Golden Patch"

El "Golden Patch" es la solución técnica definitiva y debe representar el estándar más alto de ingeniería. No basta con que el código "funcione"; debe ser modular, eficiente y estrictamente fiel a las instrucciones originales. Bajo este protocolo, existe una política de tolerancia cero ante desviaciones de requisitos.

### Technical Evaluation Checklist:

*   **Instruction Adherence**: Every single explicit prompt instruction must be implemented. One single miss results in an automatic "Fail."
*   **Operational Integrity**: The code must compile and run. Minor edge-case errors that do not impact core functionality are acceptable, but any material runtime error is a failure.
*   **Nomenclature and Readability**: Variable names must be descriptive and semantically correct. Misleading names (e.g., using `even_list` to store odd numbers) result in immediate failure. Readability issues must be limited to ≤2 areas.
*   **Efficiency**: The implementation shall not be grossly inefficient and must adhere to basic abstraction principles.
*   **Compliance**: Absolute prohibition of copyrighted assets (e.g., Unsplash), external API keys, or harmful content.

La calidad del código debe ser confirmada mediante un marco de pruebas que valide el cumplimiento de los requisitos del usuario.

---

## 5. Marco de Pruebas (Testing Framework) y Cobertura de Verificación

El auditor debe distinguir críticamente entre pruebas de implementación y pruebas de cumplimiento. El foco debe ser siempre la validación de los requisitos del usuario y no los detalles internos del código del agente.

### Flujo de Trabajo de Verificación:

1.  **Validación de Código Base Vacío**: El auditor ejecutará las pruebas sobre el código original. Se debe obtener un estado de `ALL FAILED`. Si el sistema devuelve un "ERROR", el auditor debe identificar dependencias rotas o fallos en el Dockerfile.
2.  **Validación del Golden Patch**: Tras aplicar el parche, el estado obligatorio debe ser `ALL PASSED`.
3.  **Límite de Especificidad**: Las pruebas no deben evaluar detalles que el prompt no exigió (mensajes de error exactos o nombres de métodos internos). El límite para estas pruebas sobre-específicas es del ≤5%.

### Criterios de Flagging:

*   **No marcar (Don't flag)**: Elementos subjetivos de UI ("elegante", "bonito"), detalles triviales o instrucciones marcadas explícitamente como opcionales.
*   **Marcar (Do flag)**: Funcionalidades obligatorias incluso si su uso es opcional para el usuario final (ej. "el usuario puede opcionalmente agregar una nota" implica que la capacidad de agregar la nota debe existir).

---

## 6. Taxonomía de Rúbricas y Métricas de Evaluación de Calidad

Las rúbricas transforman criterios cualitativos en métricas técnicas medibles. Deben ser "autocontenidas", permitiendo su evaluación sin necesidad de consultar el prompt original.

**Métricas de Cobertura (Verifier Coverage)**: Es un requisito arquitectónico que ≤5% de los requisitos principales del backend queden sin cobertura simultánea por parte de pruebas y rúbricas.

### Common Errors to Catch:

*   **Negative Framing**: Las rúbricas deben redactarse para que una respuesta correcta siempre evalúe a "Sí" o "Verdadero".
*   **Redundant Pairs**: No se permiten dos rúbricas que evalúen el mismo criterio técnico.
*   **Weighting Logic**:
    *   **Major Error**: Peso desviado por 2 niveles (ej. 1 vs 5).
    *   **Minor Error**: Peso desviado por 1 nivel (ej. 1 vs 3, o 3 vs 5) o dimensiones mal categorizadas.
*   **Overfitting**: Rechazar rúbricas que exijan nombres de variables o archivos específicos que el prompt original no mandataba.

El proceso concluye con la validación de la integridad del paquete y el entorno Docker.

---

## 7. Protocolo de Validación de Archivos y Entorno Docker

La reproducibilidad absoluta en entornos aislados es el pilar final de la garantía de calidad. El auditor debe verificar que el paquete de entrega cumpla con las especificaciones de estructura de archivos necesarias para la automatización.

### Final Technical Checklist:

*   **Package Structure**:
    *   `codebase.zip` debe contener los archivos directamente en el nivel raíz (sin una carpeta contenedora padre).
    *   `tests.zip` debe contener la carpeta `tests/` en el nivel superior.
*   **Immutable Sections**: Las secciones marcadas como "DO NOT MODIFY" en `run.sh` o `parsing.py` deben permanecer intactas. Cualquier alteración por parte del agente invalida la entrega.
*   **Execution State**: Validación de marcas de tiempo actuales y consistencia en los archivos `before.json` (todos fallidos) y `after.json` (todos pasados).
*   **Docker Constraints**: Restricción absoluta del comando `COPY` dentro del `Dockerfile` o del script `run.sh`.

> [!IMPORTANT]
> La adherencia estricta a este protocolo de auditoría técnica es el único camino hacia la excelencia operativa y la confiabilidad en el desarrollo de software asistido por IA. El auditor que ignore estas directrices compromete la integridad del sistema completo.
