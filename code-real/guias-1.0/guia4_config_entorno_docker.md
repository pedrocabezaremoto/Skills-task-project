# Guía 4 — Informe Técnico: Configuración y Ejecución del Entorno Docker - Proyecto Real Coder

## Resumen Ejecutivo
Este documento sintetiza las directrices críticas para la configuración, ejecución y validación del entorno Docker dentro del proyecto Real Coder. La integridad del proceso de evaluación depende estrictamente del cumplimiento de las estructuras de archivos y plantillas proporcionadas. Las conclusiones clave incluyen:
- **Fidelidad Absoluta a las Plantillas:** Es imperativo no alterar la estructura básica de los archivos `Dockerfile`, `run.sh` y `parsing.py`, ya que el script de validación externa depende de una arquitectura específica.
- **Entorno Controlado:** Se utiliza una base de Ubuntu 22.04 con dependencias de sistema predefinidas (Git, Python 3, Pip) y una estructura de directorios de trabajo estricta (`/app` y `/eval_assets`).
- **Lógica de Evaluación:** La validación de las tareas se realiza mediante la ejecución de un conjunto de pruebas a través de `run.sh` y el posterior procesamiento de resultados mediante `parsing.py`.
- **Proceso de Ejecución de Tres Pasos:** El flujo de trabajo estándar consiste en la construcción de la imagen, la ejecución del contenedor en modo interactivo y la activación manual del script de pruebas.

---

## Análisis de Temas Principales y Requerimientos

### 1. Estructura y Restricciones del Dockerfile
El Dockerfile actúa como el cimiento del entorno de ejecución. El documento establece reglas estrictas para su manipulación:
- **Uso de Plantilla Obligatorio:** Solo se permite la modificación del archivo para instalar dependencias necesarias para la solución y las pruebas.
- **Prohibiciones Específicas:**
  - No modificar la estructura del archivo.
  - No eliminar instrucciones existentes.
  - No añadir capas de pasos no relacionados.
  - No cambiar los puntos de entrada (entry points) o comandos por defecto.
- **Configuración del Sistema:**
  - **Imagen Base:** `ubuntu:22.04`.
  - **Variables de Entorno:** `DEBIAN_FRONTEND=noninteractive`.
  - **Dependencias Incluidas:** git, python3, python3-pip, python3-setuptools, python-is-python3, y unzip.
- **Configuración de Git:** Se inicializa un repositorio en el directorio `/app` con credenciales genéricas (agent@example.com).
- **Activos de Evaluación:** El directorio `/eval_assets` se crea en el paso de construcción, pero es poblado en tiempo de ejecución por el script de evaluación.

### 2. Gestión de Scripts de Ejecución y Procesamiento
El sistema de evaluación se apoya en dos archivos fundamentales que deben seguir plantillas preestablecidas.

#### A. Script de Ejecución (`run.sh`)
Este archivo de Bash coordina la ejecución de las pruebas unitarias.
- **Sección Configurable:** Los desarrolladores deben implementar la función `run_all_tests()`. El documento sugiere como ejemplo comandos como `cargo test` o similares, dependiendo del lenguaje.
- **Integridad:** Las secciones marcadas como COMMON SETUP y COMMON EXECUTION no deben ser modificadas bajo ninguna circunstancia.

#### B. Script de Parseo (`parsing.py`)
Este script de Python es el encargado de transformar la salida de las pruebas en un formato estandarizado (JSON).
- **Clases de Datos:** Define `TestStatus` (PASSED, FAILED, SKIPPED, ERROR) y la clase `TestResult`.
- **Misión del Desarrollador:** Implementar la lógica dentro de la función `parse_test_output(stdout_content: str, stderr_content: str)`.
- **Salida de Datos:** El script exporta los resultados a un archivo JSON con una lista de objetos que contienen el nombre y el estatus de cada prueba.

---

## Flujo de Trabajo y Comandos de Ejecución
El proceso para validar una tarea sigue una secuencia lógica de comandos en la terminal, los cuales deben ejecutarse desde la raíz del proyecto:

| Paso | Comando | Propósito |
|---|---|---|
| 1 | `docker build -t <nombre_imagen> .` | Construye la imagen Docker. Se recomienda mantener una nomenclatura organizada (ej. real-coder-task-1). |
| 2 | `docker run -it <nombre_imagen>:latest /bin/bash` | Inicia el contenedor y abre una shell interactiva en `/app`. |
| 3 | `bash run.sh` | Ejecuta la suite completa de pruebas dentro del contenedor. |

*Nota:* El comando `docker images` se identifica como una herramienta útil para listar y verificar las imágenes disponibles si se pierde el rastro de la versión actual.

---

## Evidencia de Resultados de Prueba
Basado en el contexto visual de la ejecución del entorno, se identifican los siguientes puntos de referencia sobre el estado exitoso del sistema:
- **Construcción Exitosa:** La construcción de la imagen (vía `docker build`) se completa correctamente en 13 pasos, confirmando la instalación de librerías adicionales como numpy y opencv.
- **Entorno de Pruebas Activo:** La ejecución de `bash run.sh` dentro del contenedor utiliza pytest-9.0.2 sobre Python 3.10.12.
- **Validación de Funcionalidades:** Las pruebas abarcan múltiples módulos críticos, incluyendo:
  - `test_clustering.py`: Verificación de contratos de clustering y casos de borde.
  - `test_duplicate_detection.py`: Detección de fotos duplicadas.
  - `test_edge_cases.py`: Manejo de imágenes pequeñas, borrosas o con múltiples rostros.

---

## Conclusiones Críticas del Documento de Origen
> "Es extremadamente importante que todas las instrucciones en este documento se sigan con precisión. El script de validación depende de una estructura estricta y cualquier cambio involuntario puede romper el proceso de evaluación."

El éxito en el proyecto Real Coder no solo depende de la calidad de la solución técnica, sino de la adhesión rigurosa al protocolo de contenedores Docker. Cualquier desviación en las secciones de "No Modificar" de las plantillas de Python o Bash invalidará automáticamente los resultados de la evaluación, independientemente de la corrección del código de la solución.
