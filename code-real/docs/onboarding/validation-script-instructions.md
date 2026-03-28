# Validation Script Instructions (Curso Real Coder)

## Guía de Revisión y Validación de Proyectos de Desarrollo Asistido

### Resumen Ejecutivo
El presente documento detalla el flujo de trabajo técnico y los estándares de calidad requeridos para la revisión, validación y auditoría de proyectos de desarrollo. El proceso se fundamenta en un ciclo riguroso que comienza con la validación del prompt inicial y culmina en una verificación automatizada mediante contenedores Docker. Los pilares críticos identificados incluyen la adherencia estricta a patrones de formato (**Markdown**), la metodología **Fail-to-Pass (F2P)** —donde todas las pruebas deben fallar en un entorno vacío antes de ser ejecutadas con éxito en la solución— y la cobertura total de los requisitos mediante una combinación de pruebas unitarias y rúbricas manuales. La automatización, facilitada por herramientas de verificación sistémica y scripts de validación, es esencial para garantizar la integridad de los resultados y la concordancia entre la solicitud original y la implementación final.

---

### 1. Configuración Inicial y Estructura del Entorno
El proceso de revisión comienza con una organización estructurada del entorno de trabajo para asegurar la trazabilidad de los archivos.
*   **Creación de Directorios:** Se establece una carpeta de trabajo principal siguiendo una nomenclatura secuencial (ej. v16, v17). Dentro de esta, se deben crear dos subcarpetas esenciales:
    *   **app:** Contendrá los scripts de validación y archivos de configuración.
    *   **codebase:** Destinada a albergar la solución técnica y el código fuente.
*   **Herramientas de Edición:** Se utiliza el editor Cursor para gestionar el proyecto, permitiendo la integración de archivos Markdown (`prompt.md`) y la interacción con modelos para verificar la validez de las instrucciones.

---

### 2. Validación de Prompts y Cumplimiento de Directrices
La calidad del prompt es el factor determinante para el éxito del proyecto. Se utiliza un "Prompt Checker" que integra todas las reglas y directrices del sistema.
#### Elementos Críticos del Prompt
Para evitar fallas mayores en la auditoría, el prompt debe cumplir con:
*   **Patrones A o B:** El contenido debe seguir una estructura predefinida que incluya título y descripción.
*   **Estado Actual (Current State):** Es obligatorio que el prompt mencione el estado inicial del proyecto. La ausencia de este elemento se considera una falla que requiere actualización inmediata.
*   **Formato Markdown:** Los errores de formato (como texto fuera de los bloques de código o etiquetas rotas) son motivos de rechazo.

---

### 3. Metodología Fail-to-Pass (F2P) y Pruebas Unitarias
El sistema de validación se basa en el desarrollo guiado por pruebas (TDD) bajo el esquema F2P, asegurando que las pruebas sean lo suficientemente estrictas.

| Fase de Prueba | Estado Esperado | Propósito |
| :--- | :--- | :--- |
| **Antes (Before)** | 100% Fallidas | Verificar que las pruebas no sean "indulgentes" y que realmente busquen una solución inexistente en un código base vacío. |
| **Después (After)** | 100% Exitosas | Confirmar que la implementación en el codebase cumple con todos los criterios técnicos. |

*   **Ejecución de Pruebas:** Los archivos JSON (`before.json` y `after.json`) deben coincidir en el número de pruebas y ser consistentes.
*   **Evidencia:** El contribuyente debe proporcionar evidencia visual de que todas las pruebas están pasando tras la implementación.

---

### 4. Validación Técnica y Automatización con Docker
La verificación final no depende únicamente de la revisión visual, sino de la ejecución técnica en un entorno controlado.
*   **Scripts de Validación:**
    *   `validation.sh`: Script principal que construye la imagen de Docker, descomprime los archivos de prueba y ejecuta el ciclo F2P.
    *   `run.sh`: Configurado para ejecutar todas las pruebas dentro del contenedor.
    *   `parsing.py`: Recolecta la salida de `run.sh` y la convierte a un formato JSON estandarizado (`test_results.json`).
*   **Estructura de la carpeta /app:** Debe contener `codebase.zip`, `test.zip`, `Dockerfile`, `parsing.py` y `run.sh`.

---

### 5. Rúbricas y Cobertura de Requerimientos
Cuando los aspectos de un prompt no pueden ser evaluados mediante pruebas automatizadas, se recurre a las rúbricas para garantizar una cobertura del 100%. Las rúbricas deben capturar los "pasos perdidos" o *gaps* menores identificados durante la revisión.

---

## Informe Técnico: Validation Script Instructions

### 1. Resumen Ejecutivo
La sección "Validation Script Instructions" define el protocolo oficial de validación end-to-end del proyecto Real Coder. Su núcleo es el script `real_coder_validation_03_03.sh`, que orquesta automáticamente el ciclo F2P (Fail-to-Pass) dentro de un contenedor Docker.

### 2. El Script Oficial: real_coder_validation_03_03.sh
*   **Única Línea Editable:** `APP_DIR="/app"` (solo el path es personalizable). Todo lo demás es **intocable**.
*   **Directorio de Ejecución:** El script se corre desde dentro de `/app`.
*   **Flujo Interno - 7 Pasos:** Verifica archivos, construye imagen, inicia contenedor, inyecta `tests.zip`, corre tests (Before), inyecta `codebase.zip`, corre tests (After) y genera reportes.

### 3. Reglas de Validación Automática
*   **Origen de tests:** Los tests deben venir de `/eval_assets`, **NUNCA** de `/app`.
*   **Sin regresiones:** Tests que pasaban antes no pueden fallar después.
*   **Sin pass-to-pass:** Ningún test puede estar en PASSED tanto en *before* como en *after*.
*   **Al menos 1 F2P:** Debe existir mínimo un test que pasó de FAILED a PASSED.

### 4. Estructura Obligatoria de /app
Exactamente 5 archivos:
1. `Dockerfile`
2. `tests.zip` (carpeta `tests/` como primer nivel)
3. `codebase.zip` (archivos directamente en raíz, sin carpeta padre)
4. `run.sh`
5. `parsing.py`

### 5. La Regla de Oro de los ZIPs
*   **tests.zip:** Primera cosa visible: carpeta `tests/` ✅
*   **codebase.zip:** Primera cosa visible: archivos `.py`, `src/`, etc. directamente ✅

### 6. Sistema de Prompts y Evaluadores (Quality Folder)
Incluye recursos como `promptchecker.md`, `rubrics_instructions.md`, `eval_quality.py`, y el `Coverage System Prompt` para auditar que el 100% de los requisitos estén cubiertos.

---

> [!CAUTION]
> **ADVERTENCIA CRÍTICA:** "Do NOT attempt your first task without consulting a PT in the war room please! Failure in doing so will result in being immediately disabled from the project."
