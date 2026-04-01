# Guía 7 — Guía de Validación y Estructura para la Evaluación de Agentes

## Resumen Ejecutivo
Este documento detalla los protocolos críticos y los requisitos de configuración necesarios para asegurar la integridad de la carpeta raíz y el correcto funcionamiento del entorno de evaluación. La precisión en la estructura de archivos, los métodos específicos de compresión ZIP y la vigilancia sobre las herramientas de edición automatizada son fundamentales para evitar errores comunes. El cumplimiento estricto de estas directrices garantiza que el entorno `/app` contenga exclusivamente el código base del agente, manteniendo una separación absoluta con la suite de pruebas.

---

## 1. Estructura Obligatoria del Directorio (`/app`)
Para un despliegue exitoso, el directorio raíz debe contener exactamente cinco elementos. No se permite la inclusión de archivos o carpetas adicionales fuera de esta lista:
- `codebase.zip`: El código fuente del agente comprimido.
- `tests.zip`: La suite de pruebas comprimida.
- `Dockerfile`: Archivo de configuración de la imagen Docker.
- `parsing.py`: Script de procesamiento de datos.
- `run.sh`: Script de ejecución principal.

### Restricciones de Contenido
El entorno `/app` tiene una función específica y restrictiva:
- **Exclusividad:** Solo debe contener el código base del agente.
- **Aislamiento de Pruebas:** Bajo ninguna circunstancia se debe colocar contenido de la suite de pruebas dentro de `/app`.

---

## 2. Protocolos de Compresión ZIP
La metodología de compresión es diferenciada y crítica según el tipo de archivo. El incumplimiento de estas "Reglas de Oro" invalidará la estructura interna.

| Archivo | Estructura Interna (Al abrir el ZIP) | Método de Compresión |
|---|---|---|
| `tests.zip` | Debe contener la carpeta `tests/` en el primer nivel. | Se debe comprimir la carpeta completa. |
| `codebase.zip` | Debe contener directamente los archivos (sin carpeta raíz). | Se deben comprimir los archivos desde el interior de la carpeta. |

> **Advertencia Crítica:** Se prohíbe el anidamiento en `codebase.zip` (ejemplo de error: `codebase.zip → codebase/ → archivos`). La estructura debe ser directa: `codebase.zip → archivos`.

---

## 3. Gestión de Integridad y Herramientas de Edición (Cursor)
El uso de herramientas como Cursor, específicamente sus funciones de "Auto-edit" o "Agent", requiere una supervisión extrema para evitar modificaciones no autorizadas.

### Monitoreo de Archivos Sensibles
Los archivos `run.sh` y `parsing.py` deben ser monitoreados de cerca. Existe una prohibición absoluta de modificar las secciones etiquetadas explícitamente como "DO NOT MODIFY".

### Reglas para `verification.sh`
En el archivo `verification.sh`, las facultades de edición están estrictamente limitadas:
- **Acción Permitida:** El usuario solo tiene permiso para editar la sección de la Ruta (Path).
- **Restricción:** No se debe actualizar ningún otro elemento. Es imperativo evitar que los agentes de IA "alucinen" mejoras o realicen cambios en otras líneas del archivo.

---

## 4. Especificaciones Técnicas y Configuración
Basado en la configuración del entorno, se deben observar los siguientes parámetros técnicos:
- **Ruta del Directorio (Host):** La ubicación estándar definida es `/home/abhisek007/mattock_code/task1_nabid_review_copy/app`.
- **Etiqueta de Imagen Docker:** La imagen generada debe utilizar el tag `agent-evaluator:latest`.
- **Protección contra Anidamiento (Zip Nesting Guard):**
  - Se ha definido una variable `MAX_ZIP_DEPTH=3`.
  - El sistema generará un error si los archivos dentro de un ZIP están enterrados a una profundidad mayor a la permitida (ejemplo: se permite `dir/sub/archivo.py`, pero no niveles superiores).
- **Requisito de Existencia de Archivos de Entrada:** Todos los archivos de entrada definidos (`Dockerfile`, `tests.zip`, `codebase.zip`, `run.sh`, `parsing.py`) deben existir obligatoriamente en el directorio definido por la variable `APP_DIR`.
