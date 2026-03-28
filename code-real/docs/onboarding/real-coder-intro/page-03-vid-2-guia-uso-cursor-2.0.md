# Cursor 2.0: Editor de Código con IA Agéntica

## Resumen Ejecutivo

Cursor 2.0 representa una evolución significativa en el desarrollo de software asistido por inteligencia artificial. Al ser un "fork" de Visual Studio Code (VS Code), mantiene la familiaridad de las funciones principales de este editor, pero integra capacidades agénticas avanzadas que permiten generar archivos, proyectos y lógica de programación de forma masiva. Los pilares de esta versión incluyen el modelo propio Composer, que ofrece una velocidad hasta cuatro veces superior a otros modelos líderes, y la capacidad de ejecutar múltiples agentes en paralelo. El flujo de trabajo se centra en tres modos operativos: Plan (planificación), Agent (ejecución) y Ask (consulta), permitiendo una transición fluida desde la idea inicial hasta el código funcional, con herramientas integradas de revisión, control de versiones y personalización mediante reglas específicas del proyecto.

---

## 1. Naturaleza y Arquitectura de Cursor 2.0

Cursor se define como un editor de código agéntico basado en IA, diseñado para aumentar la eficiencia del desarrollador mediante la automatización de tareas complejas.

* **Base Tecnológica:** Es una bifurcación (fork) de VS Code, lo que garantiza compatibilidad con sus funciones principales y extensiones.
* **Modelos de IA:** Aunque permite el uso de modelos como GPT, Gemini y Claude, la versión 2.0 introduce Composer, un modelo nativo optimizado para ser significativamente más rápido en la generación de código.
* **Capacidad Agéntica:** La herramienta no solo sugiere texto, sino que puede actuar como un agente capaz de crear estructuras de archivos completas y ejecutar planes de desarrollo de manera autónoma.

---

## 2. Modos Operativos del Editor

El centro de la interfaz es el panel de chat agéntico, que ofrece tres modos distintos para interactuar con la IA:

| Modo | Función Principal | Impacto en el Proyecto |
| :--- | :--- | :--- |
| **Plan** | Genera una hoja de ruta detallada en formato Markdown (.md) basada en el prompt del usuario. | No modifica archivos; crea una lista de tareas pendientes (to-do list). |
| **Agent** | Ejecuta las tareas del plan o instrucciones directas, escribiendo y modificando código. | Realiza cambios directos en los archivos del sistema. |
| **Ask** | Responde preguntas sobre el código, explica funciones o da instrucciones de configuración. | Modo seguro: no altera ningún archivo, solo proporciona respuestas de texto. |

---

## 3. Flujo de Trabajo y Generación de Proyectos

Para obtener resultados óptimos, se recomienda seguir un proceso estructurado que minimice errores y código innecesario.

### Planificación y Contexto

* **Especificidad:** Es crítico definir claramente el objetivo (ej. sitio web, juego, herramienta de backend) antes de iniciar. Cuanto más específico sea el prompt, menor será la probabilidad de que la IA genere código erróneo.
* **Aportación de Contexto:** El usuario puede usar el símbolo `@` para referenciar archivos específicos, carpetas o documentación. También es posible subir imágenes (como mockups) para que la IA las use como base visual.
* **Navegación Web:** Cursor incluye una función de navegador que permite a la IA probar aplicaciones y buscar información en tiempo real.

### Ejecución y Construcción

Una vez aprobado el plan, el botón Build activa un agente para ejecutar los pasos. Cursor permite la ejecución de múltiples agentes simultáneos, lo que aumenta la velocidad de desarrollo en tareas paralelas.

### Revisión de Código (Diff View)

Tras la generación de código, el sistema entra en un estado de "espera de revisión" (awaiting review):

* **Vista de Diferencias (Diff):** Muestra los cambios realizados línea por línea.
* **Persistencia del Código:** Es vital comprender que el código generado ya existe en los archivos incluso antes de presionar "Aceptar todo". Si el usuario cierra el proyecto sin aceptar o deshacer, los cambios permanecerán.
* **Acciones:** El usuario puede seleccionar "Keep All" (Conservar todo), "Undo All" (Deshacer todo) o revisar archivos de forma individual.

---

## 4. Herramientas de Edición de Precisión

Además de la generación masiva de código, Cursor ofrece herramientas para ajustes granulares:

* **Quick Edit (Control/Command + K):** Permite resaltar un bloque de código y solicitar cambios específicos (ej. "limpiar este código" o "añadir comentarios"). Es ideal para cambios dirigidos y precisos.
* **Autocomplete:** Predicción de la siguiente línea de código en tiempo real. Se acepta presionando la tecla Tab.
* **Terminal Integrada:** Cursor puede sugerir y ejecutar comandos en la terminal, previa aprobación del usuario, para instalar dependencias o inicializar repositorios.

---

## 5. Personalización y Reglas del Proyecto

Cursor permite definir comportamientos específicos mediante reglas para asegurar la consistencia del código.

* **Cursor Rules (.cursorrules):** Archivos en formato Markdown que almacenan reglas globales o por proyecto.
* **Aplicación de Reglas:** Se pueden configurar para que se apliquen siempre, de forma inteligente o a archivos específicos (ej. "siempre generar docstrings para funciones" o "no tocar archivos .tsx").
* **Configuración de Interfaz:** A través del menú de ajustes o el "Command Palette" (Ctrl/Cmd + Shift + P), el usuario puede cambiar temas (ej. Monokai), redimensionar paneles y anclar pestañas.

---

## 6. Control de Versiones y Conectividad Externa

### Integración con Git

El editor enfatiza la importancia de utilizar control de versiones para proteger el proyecto contra cambios no deseados de la IA.

* **Puntos de Control:** Se recomienda pedir al agente que realice "commits" después de cambios importantes para crear puntos de restauración.
* **Automatización:** El agente puede inicializar repositorios Git y ejecutar comandos de guardado automáticamente si se le solicita.

### Protocolo de Contexto de Modelo (MCP)

Cursor soporta servidores MCP, lo que expande las capacidades de los agentes:

* **Conectividad:** Permite a los agentes interactuar con herramientas externas, bases de datos (como Tiger Data) y APIs de terceros.
* **Arcade MCP:** Se menciona como una plataforma de llamada a herramientas que gestiona la autenticación y seguridad, permitiendo que los agentes ejecuten flujos de trabajo reales más allá de simples demostraciones.
