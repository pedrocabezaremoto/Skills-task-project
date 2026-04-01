# Guía 8 — Informe de Directrices: Errores Comunes y Guía de Corrección – Real Coder

## Resumen Ejecutivo
Este documento sintetiza las directrices críticas y el análisis de fallas de control de calidad (QC) recopilados durante un periodo de cuatro semanas en el proyecto Real Coder. El objetivo central es proporcionar un marco de trabajo riguroso para la implementación de parches, la reescritura de prompts y la creación de suites de pruebas automatizadas.

Los hallazgos más críticos subrayan la necesidad de una fidelidad absoluta a las instrucciones del prompt, la eliminación de la sobre-especificidad en las pruebas (testear comportamiento, no implementación) y la documentación exhaustiva de las interfaces. Se enfatiza que cualquier requisito no cubierto por una prueba automatizada debe ser evaluado mediante una rúbrica atómica y objetiva. El cumplimiento de la configuración del entorno Docker (base Ubuntu 22.04 y finales de línea Unix) es obligatorio para garantizar la reproducibilidad de los resultados.

---

## 1. Calidad del Parche Dorado (Golden Patch)
El "Golden Patch" representa la implementación final que debe satisfacer todos los requisitos del prompt. Las fallas en esta área suelen derivar de omisiones en las instrucciones explícitas o errores de lógica en casos de borde.

### Fallas Comunes y Mejores Prácticas
| Tipo de Falla | Ejemplos de Error | Mejores Prácticas |
|---|---|---|
| Omisión de Instrucciones | No instalar dependencias de clientes cuando se solicita; funciones de filtrado que solo funcionan por URL y no por UI. | Leer el prompt línea por línea como una lista de verificación. Cada requisito debe ser rastreable en el código. |
| Incumplimiento de Contratos | Códigos de salida incorrectos (ej. devolver 2 en vez de 1); uso de librerías prohibidas o internet en runtime. | Verificar contratos de inicio, códigos de error HTTP/salida y patrones prohibidos (scripts inline, fetching en vivo). |
| Errores de Salida/Lógica | Rutas CRUD que devuelven 302 en vez de 401; re-sembrado de base de datos que borra datos del usuario al reiniciar. | Ejecutar flujos de usuario de extremo a extremo, no solo el "camino feliz". Probar estados de persistencia y concurrencia. |
| Documentación Deficiente | Archivos fuente sin comentarios; falta de explicación en fórmulas matemáticas complejas o transiciones de estado. | Añadir docstrings a cada clase y función pública. Los comentarios deben explicar el "por qué" de la lógica no obvia. |

---

## 2. Calidad de la Reescritura del Prompt
La transformación de una tarea cruda en un prompt estructurado es fundamental. El documento advierte contra la herencia de ambigüedades y la creación de requisitos físicamente imposibles.
- **Evitar Contradicciones:** No solicitar "sin acceso a internet" y usar librerías como NLTK que descargan datos en su primer uso, a menos que se gestione previamente.
- **Alineación con el Brief Original:** Si la tarea original ofrece flexibilidad (ej. "SQLite o JSON"), la reescritura no debe restringirlo a una sola opción sin justificación.
- **Estilo de Redacción:** El prompt debe redactarse con un estilo de "brief de freelance" (ej. "Necesito una herramienta...") en lugar de un estilo imperativo directo.
- **Limpieza de Metadatos:** Se deben eliminar todas las referencias internas, como números de tarea o notas de revisores previos.

---

## 3. Interfaz Esperada (Expected Interface)
Esta sección es el componente más crítico para que una suite de pruebas externa interactúe con el código. La ausencia o error en esta sección garantiza una falla de QC.

### Requisitos Obligatorios por Entrada
Cada entrada de interfaz debe contener exactamente seis campos:
1. **Path:** Ruta del archivo.
2. **Name:** Nombre de la función, clase o endpoint.
3. **Type:** Tipo de componente.
4. **Input:** Parámetros con sus tipos (ej. `filepath: str`). Usar "N/A" si no aplica.
5. **Output:** Tipo de retorno o código de respuesta HTTP. Usar "N/A" si no aplica.
6. **Description:** Detalle exhaustivo de lo que la prueba validará (selectores DOM, encabezados CSV, etc.).

**Puntos Clave:**
- Cualquier componente importado o llamado por el verificador debe estar documentado.
- Las descripciones deben ser literales; si una prueba busca un encabezado específico, la descripción de la interfaz debe mencionarlo.

---

## 4. Suite de Pruebas F2P: El Riesgo de la Sobre-Especificidad
Las pruebas deben validar que se cumplan los requisitos del prompt sin obligar al desarrollador a adoptar una implementación específica.
- **Comportamiento vs. Implementación:** Una prueba falla si rechaza una solución válida que satisface el prompt pero usa una estructura distinta (ej. nombres de flags de CLI diferentes a los sugeridos pero no exigidos).
- **Mocks Neutrales:** Se debe realizar el patching a nivel de librería (ej. `mock.patch("paramiko.SSHClient")`) y no sobre la ruta de importación específica del módulo, para evitar romper pruebas ante diferentes estilos de importación.
- **Validación de Código Vacío:** Antes de la solución, todas las pruebas deben fallar en un entorno de código vacío. Si una prueba pasa por error (ej. capturando una excepción genérica), debe corregirse para ser más específica.

---

## 5. Cobertura del Verificador y Rúbricas
La combinación de pruebas automatizadas y criterios de rúbrica debe cubrir el 100% de los requisitos del prompt.
- **Gaps de Cobertura:** Requisitos como "responsividad móvil" o "validación W3C" a menudo se omiten. Si no se puede testear automáticamente, debe estar en la rúbrica.
- **Restricciones de Librerías:** Las prohibiciones de uso de ciertas librerías deben validarse mediante rúbricas, ya que las pruebas unitarias rara vez detectan importaciones prohibidas de forma efectiva.
- **Rúbricas Atómicas:** Cada criterio debe ser evaluable como un "Sí" o "No" objetivo. Evitar adjetivos vagos como "apropiado" o "limpio" sin definir los parámetros específicos.

### Pesos de la Rúbrica
- **Peso 5 (Mandatorio):** Requisitos sin los cuales la solución es inaceptable.
- **Peso 3:** Mejoran sustancialmente la calidad.
- **Peso 1:** Atributos deseables pero no críticos.

---

## 6. Entorno y Configuración Docker
La reproducibilidad depende estrictamente del entorno Docker. El uso de la imagen base `ubuntu:22.04` es innegociable.
- **Dependencias del Sistema:** Cualquier librería de sistema necesaria (ej. libheif) debe incluirse en la sección de SYSTEM DEPENDENCIES del Dockerfile.
- **Finales de Línea:** El archivo `run.sh` debe guardarse obligatoriamente con finales de línea Unix (LF). Los finales de línea de Windows (CRLF) causarán el colapso inmediato del script en Docker.
- **Inyección de Código:** No se debe usar el comando `COPY` para el código de la aplicación; este se inyecta en tiempo de ejecución. El Dockerfile solo debe preparar el entorno y las dependencias.

---

## Lista de Verificación Final para el Envío
- [ ] El parche dorado pasa todos los criterios de la rúbrica en autoevaluación.
- [ ] Todas las pruebas FALLAN en un código vacío dentro de Docker.
- [ ] Todas las pruebas PASAN con el parche dorado dentro de Docker.
- [ ] Cada requisito del prompt está cubierto por una prueba o una rúbrica.
- [ ] La interfaz documenta todos los componentes externos con sus 6 campos obligatorios.
- [ ] El archivo `run.sh` utiliza finales de línea LF.
- [ ] La imagen base del Dockerfile es `ubuntu:22.04`.
- [ ] No hay pruebas que penalicen detalles de implementación no solicitados.
