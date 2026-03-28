# Guía de Estandarización de Dockerfiles y Gestión de Dependencias

## Resumen Ejecutivo

El presente documento detalla los requisitos técnicos y procedimentales para la configuración de contenedores Docker, basándose en las directrices de integración técnica (onboarding). Los pilares fundamentales de esta estrategia incluyen la paridad absoluta entre los archivos Docker situados en distintas ubicaciones del proyecto y la eliminación del uso de scripts externos para la instalación de dependencias del sistema. El objetivo principal es garantizar que el entorno de ejecución sea consistente y funcional, independientemente de si la ejecución es realizada por el equipo de control de calidad (QC) desde la raíz del código fuente o desde el directorio de la aplicación.

---

## 1. Duplicidad y Consistencia de los Dockerfiles

Se ha identificado la coexistencia de dos archivos Docker dentro de la estructura del proyecto. Para asegurar la integridad del despliegue, es imperativo que ambos mantengan una paridad total.

* **Ubicaciones de los Archivos:**
    1. Directorio de la aplicación (`/app`).
    2. Raíz del archivo comprimido del código fuente (`codebase.zip`).
* **Requisito de Uniformidad:** Ambos Dockerfiles deben ser idénticos. Cualquier configuración o dependencia añadida en uno debe verse reflejada exactamente en el otro.
* **Directorio de Trabajo:** Se establece como estándar que el directorio de trabajo (**WORKDIR**) en ambos archivos sea `/app`.

---

## 2. Gestión de Dependencias del Sistema

El protocolo de configuración exige un cambio en la forma en que se gestionan las librerías y dependencias necesarias para el funcionamiento del software.

* **Codificación Directa (Hardcoding):** Todas las dependencias del sistema deben ser integradas manualmente y de forma explícita dentro del Dockerfile.
* **Prohibición de Scripts Externos:** Queda estrictamente prohibido el uso de comandos dentro del Dockerfile que invoquen archivos externos, específicamente `run.sh` (o `run.ssh`), para realizar la instalación de dependencias.
* **Justificación Técnica:** La instalación debe ocurrir directamente a través de las instrucciones del Dockerfile para asegurar la transparencia y la trazabilidad del entorno de construcción.

---

## 3. Flexibilidad de Ejecución y Casos de Uso

La configuración del Dockerfile debe ser lo suficientemente robusta para soportar diferentes contextos de ejecución, especialmente aquellos relacionados con las pruebas de calidad.

* **Compatibilidad de Directorios:** El diseño del Dockerfile debe permitir que el proceso de ejecución sea exitoso tanto si se inicia desde el directorio `/app` como si se ejecuta directamente desde la raíz del codebase.
* **Interoperabilidad con QC:** Se enfatiza que el equipo de Control de Calidad (QC) debe poder ejecutar el Dockerfile desde la raíz sin encontrar errores de rutas o dependencias faltantes.

---

## 4. Directrices Técnicas Consolidadas

| Requisito | Acción Requerida |
| :--- | :--- |
| **Sincronización** | Asegurar que el Dockerfile en `/app` y en la raíz sean idénticos. |
| **Instalación de Dependencias** | Declarar manualmente cada dependencia del sistema en el Dockerfile. |
| **Scripts de Instalación** | Eliminar cualquier referencia a `run.sh` para la gestión de librerías. |
| **Rutas de Trabajo** | Mantener `/app` como el directorio de trabajo estándar. |
| **Versatilidad** | Validar que el contenedor se construye correctamente desde múltiples niveles de directorio. |

---

## Conclusión

La estandarización de los Dockerfiles busca eliminar la ambigüedad en la configuración del entorno. Al centralizar todas las dependencias dentro del propio archivo Docker y mantener una simetría total entre las ubicaciones del código, se garantiza un proceso de ejecución predecible y eficiente para todos los equipos involucrados en el ciclo de vida del desarrollo.
