# Guía 5 — Guía de Instrucciones de Docker y Validación para Real Coder

## Resumen Ejecutivo
Este documento sintetiza las directrices críticas y los procedimientos operativos para la modificación de archivos Docker, el uso de scripts de ejecución y el proceso de validación en entornos Mac y Windows dentro del proyecto Real Coder.

El objetivo primordial de este marco de trabajo es garantizar un proceso de evaluación consistente y automatizado. La integridad del sistema de validación depende del cumplimiento estricto de una estructura de archivos predefinida y de limitaciones severas en la modificación de los componentes del entorno. Los puntos más críticos incluyen la **prohibición del comando COPY** en el Dockerfile para el código del proyecto, la obligatoriedad de instalar todas las dependencias durante la construcción de la imagen y la generación exitosa de resultados comparativos ("antes" y "después") mediante archivos JSON. Cualquier desviación de estas instrucciones rompe el proceso de evaluación y resulta en fallos técnicos.

---

## 1. Reglas Fundamentales y Advertencias Críticas
El proceso de validación se rige por un conjunto de reglas innegociables diseñadas para mantener la fidelidad del entorno de prueba.
- **Fidelidad de la Estructura:** El script de validación depende de una estructura de directorios y archivos extremadamente rigurosa.
- **Gestión de Código:** Está terminantemente prohibido usar el comando `COPY` o `ADD` en el Dockerfile para incluir el código de la solución. El código se monta mediante volúmenes en tiempo de ejecución.
- **Instalación de Dependencias:** Todas las librerías necesarias (vía apt, pip, etc.) deben declararse en el Dockerfile. No se permite la instalación de dependencias en tiempo de ejecución dentro de `run.sh`.
- **Integridad de Scripts:** No se deben modificar los bloques protegidos en `run.sh` o `parsing.py` (marcados comúnmente como `### DO NOT MODIFY ###`).

---

## 2. Configuración y Requisitos del Sistema
Tanto para usuarios de Mac como de Windows, el software central es Docker Desktop.

### Requisitos por Plataforma
| Componente | Especificaciones para Mac | Especificaciones para Windows |
|---|---|---|
| Software Base | Docker Desktop (Apple Silicon o Intel) | Docker Desktop con backend WSL2 habilitado |
| Terminales Recomendadas | Terminal de Mac (Applications -> Utilities) | PowerShell, Git Bash o terminal de WSL Ubuntu |
| Verificación | `docker --version` | `docker --version` |

---

## 3. Gestión del Dockerfile: Modificaciones Permitidas y Prohibidas
El Dockerfile debe utilizarse exclusivamente para configurar el entorno, las herramientas y las dependencias.

### Análisis de Modificaciones
| Tipo de Cambio | Acciones Permitidas | Acciones Prohibidas |
|---|---|---|
| Dependencias del Sistema | Agregar paquetes mediante `apt-get install` en la sección de dependencias del sistema. | Cambiar la imagen base (ej. `FROM ubuntu:22.04` o `24.04`). |
| Dependencias de Python | Instalar paquetes mediante `pip install` (ej. requests, pytest, numpy). | Eliminar líneas o instrucciones existentes en la plantilla. |
| Estructura del Archivo | Añadir paquetes necesarios para que los tests se importen correctamente. | Alterar el orden de las secciones, comentarios o el `WORKDIR /app`. |
| Comandos de Código | N/A | Usar `COPY` o `ADD` para mover archivos del proyecto a la imagen. |
| Configuración de Ejecución | N/A | Cambiar el `ENTRYPOINT` o el comando por defecto (`CMD`). |

---

## 4. Flujo de Trabajo de Validación
La validación se divide en dos fases críticas: la línea base (código vacío) y la verificación (con el parche de código aplicado).

### Estructura de la Carpeta del Proyecto
Para ejecutar `validation.sh`, se debe organizar el directorio de la siguiente manera:
- **Raíz del Proyecto:** Contiene el script `validation.sh`.
- **Subcarpeta `app/` (Obligatoria):** Debe contener exactamente estos 5 archivos:
  - `Dockerfile` (modificado solo con dependencias).
  - `tests.zip` (suite de pruebas oculta).
  - `codebase.zip` (el código del agente o "Golden Patch").
  - `run.sh` (ejecutor de pruebas).
  - `parsing.py` (analizador de resultados).

### Ejecución del Proceso
1. **Preparación:** Asegurar que Docker Desktop esté en ejecución.
2. **Configuración de Ruta:** Actualizar la variable `APP_DIR` en `validation.sh` con la ruta absoluta de la carpeta `app/`.
3. **Ejecución:** Iniciar el script mediante `bash validation.sh`.
4. **Fases Automáticas:**
   - **Construcción** de la imagen Docker.
   - **Línea Base:** Ejecuta pruebas en un `/app` vacío. Los resultados deben marcarse como FAILED en `before.json`.
   - **Inyección de Código:** Descomprime `codebase.zip`.
   - **Verificación Final:** Ejecuta las pruebas nuevamente. Los resultados deben marcarse como PASSED en `after.json`.

---

## 5. Uso de Scripts Auxiliares
### `run.sh` y `parsing.py`
Estos scripts se utilizan para la ejecución manual y el análisis de resultados dentro del contenedor.
- **Objetivo de `run.sh`:** Ejecutar la suite de pruebas (usualmente pytest).
- **Objetivo de `parsing.py`:** Procesar las salidas de texto y generar un reporte estructurado en JSON.
- **Comando Típico de Contenedor:** `docker run -it --rm -v $(pwd):/app real-coder-env bash` seguido de `./run.sh`.

---

## 6. Resolución de Problemas (Troubleshooting)
El documento identifica varios puntos de falla comunes y sus soluciones:
- **Errores de Construcción (Build):** Generalmente causados por errores de sintaxis al añadir paquetes en el Dockerfile o falta de permisos en Docker Desktop.
- **Fallo de Validación:** Si los archivos JSON no muestran el cambio esperado de FAILED a PASSED, se debe revisar si el archivo `codebase.zip` tiene niveles de anidación excesivos (el máximo permitido suele ser 3).
- **Problemas de Daemon:** Si el comando docker no es reconocido o falla, es necesario reiniciar Docker Desktop o verificar que los permisos de administrador fueron aceptados.
- **Rendimiento en Mac (M1/M2/M3/M4):** La primera construcción de la imagen puede ser lenta debido a la emulación o carga inicial de caché; las construcciones subsiguientes son más rápidas.
