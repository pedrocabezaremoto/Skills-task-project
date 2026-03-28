# Open Code: Guía de Inicio y Configuración

## Resumen Ejecutivo

Open Code se define como un agente de programación de inteligencia artificial (IA) de código abierto, diseñado para operar a través de una interfaz de terminal, una aplicación de escritorio o como una extensión de entorno de desarrollo integrado (IDE). Este ecosistema destaca por su arquitectura modular, permitiendo a los desarrolladores no solo utilizar flujos de trabajo predeterminados (Planificación y Construcción), sino también crear agentes personalizados y "habilidades" (skills) para tareas específicas. La plataforma ofrece flexibilidad en la selección de modelos, permitiendo el uso de opciones gratuitas como Grok o la integración de suscripciones pagas como ChatGPT Pro mediante protocolos OAuth o credenciales de API.

---

## 1. Fundamentos de Open Code

Open Code es una herramienta orientada a la automatización del desarrollo de software mediante agentes de IA. Su versatilidad radica en su disponibilidad multiplataforma y su capacidad para integrarse directamente en el flujo de trabajo del desarrollador.

### Instalación y Lanzamiento

* **Método de Instalación:** En sistemas macOS, la instalación se realiza de forma simplificada mediante el gestor de paquetes Homebrew con el comando `brew install`.
* **Inicio del Entorno:** Para ejecutar Open Code en un proyecto específico, se debe navegar a la carpeta del proyecto en la terminal y ejecutar el comando `open code`.
* **Interfaz:** La interfaz por defecto presenta un entorno limpio donde el usuario puede interactuar con diferentes agentes.

### Gestión de Modelos y Proveedores

El sistema no está limitado a un único modelo de lenguaje. Permite una transición fluida entre diversos proveedores:

* **Modelos Gratuitos:** Incluye acceso de fábrica a modelos como Mini Max M2 y Grok Code Fast.
* **Integración de OpenAI:** Los usuarios pueden vincular su suscripción de ChatGPT Pro Plus ejecutando `open code login`, lo que permite la autenticación vía OAuth o API.
* **Comandos de Control:**
  * `/models`: Muestra la lista de modelos disponibles.
  * `Ctrl + F`: Marca un modelo como favorito.
  * `Ctrl + A`: Abre el menú para conectar nuevos proveedores.

---

## 2. Agentes Predeterminados y Flujo de Trabajo

Open Code opera bajo una lógica de división de responsabilidades mediante dos agentes principales incluidos de fábrica:

| Agente | Función Principal |
| :--- | :--- |
| **Plan (Planificación)** | Escanea la base de código o el repositorio actual para generar un plan de ejecución detallado basado en los requerimientos del usuario. |
| **Build (Construcción)** | Toma el plan generado y ejecuta la escritura de código o la creación de archivos necesarios. |

**Dinámica de uso:** Se recomienda iniciar con el agente de Plan para establecer la estructura y luego alternar (usando la tecla Tab) al agente de Build para la implementación física del proyecto.

---

## 3. Personalización: Agentes Propios y Sub-agentes

Una de las capacidades más avanzadas de Open Code es la creación de agentes personalizados para flujos de trabajo específicos, como procesos de revisión y pruebas.

### Estructura de Archivos

Los agentes personalizados se definen mediante archivos Markdown (.md) dentro de una estructura de carpetas específica en el proyecto: `./.open-code/agent/[nombre_del_agente].md`

### Tipos de Agentes

* **Agente Primario:** Es seleccionable manualmente por el usuario en la interfaz.
* **Sub-agente:** No aparece en la lista de selección directa, pero puede ser invocado por un Agente Primario para delegar tareas.

### Configuración de Permisos y Herramientas

En la definición del agente, es crucial configurar los permisos de acceso a las herramientas del sistema:

* `write`: Permiso para escribir archivos.
* `edit`: Permiso para modificar código existente.
* `bash`: Capacidad para ejecutar comandos de terminal.

### Ejemplo de Flujo Multi-agente

Es posible configurar un sistema donde un Agente Principal coordina a otros:

1. El Agente Principal desarrolla una función (ej. una app en Next.js).
2. Delega la tarea a un sub-agente Revisor (con permisos de lectura pero no de edición) para control de calidad.
3. Delega a un sub-agente Tester para ejecutar pruebas de integración.
4. El Agente Principal itera sobre el código basándose en la retroalimentación de los sub-agentes.

---

## 4. Sistema de Habilidades (Skills)

Las "Habilidades" son archivos de contexto que el agente puede cargar bajo demanda, una técnica denominada *lazy loading* (carga perezosa).

* **Propósito:** Proporcionar al agente conocimientos específicos o scripts de ejecución (como configuraciones de diseño UI o scripts de despliegue) sin sobrecargar la memoria global.
* **Ubicación:** Se almacenan en `./.open-code/skill/[nombre_de_habilidad]/skill.md`.
* **Activación:** Aunque son globales por defecto, se pueden restringir o permitir individualmente en la configuración de permisos de cada agente utilizando la sintaxis `permission skill [nombre] allow`.
* **Importancia de la Descripción:** La descripción dentro del archivo `skill.md` debe ser clara y "atractiva" para la IA, facilitando que el modelo identifique cuándo es apropiado invocar dicha habilidad de forma automática.

---

## 5. Personalización y Herramientas Adicionales

* **Temas Visuales:** El entorno es altamente personalizable. Se pueden cambiar los temas visuales (ej. "One Dark Nord") mediante comandos de configuración.
* **Atajos de Agentes:** Es posible iniciar Open Code directamente en un agente específico usando el comando `open code --agent [nombre]`.
* **Repositorios de Comunidad:** Existen configuraciones optimizadas, como el repositorio "Open Agents Control", que automatizan la instalación y configuran agentes especializados (ej. "Open Coder") diseñados para el uso diario intensivo.
