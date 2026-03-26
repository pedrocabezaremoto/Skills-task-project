# Módulo 2: Flujo de Trabajo Técnico y TDD (Video 2)

> **Documento de Entrenamiento (training1)**
> Basado en: *Guía de Onboarding para el Desarrollo de Soluciones y Verificación de Casos de Prueba.*

---

## 🛠️ Fase 1: Ingeniería y Estructuración del Prompt

El objetivo principal es eliminar la ambigüedad y entregar toda la información para que el agente de IA sepa exactamente qué generar. El *prompt* es el documento maestro y tiene componentes obligatorios:

1. **Título y Contexto:** Descripción estilo "freelance" sobre las necesidades del cliente.
2. **Tech Stack (Pila Tecnológica):** Especificación estricta de lenguajes y herramientas para frontend y backend.
3. **Estado Actual:** Generalmente, se inicia con un repositorio vacío (solo con archivos de prueba).
4. **Implementación Requerida:** Detalles profundos sobre características, funcionalidades y modelos de datos.
5. **Expected Interfaces (Interfaces Esperadas):** Un contrato vital y exhaustivo. Debe documentar:
   - Ruta (Path) y nombre del archivo.
   - Tipo de componente (clase, función, API Endpoint).
   - Inputs (Entradas) y Outputs (Salidas).
   - Descripción de su propósito técnico.
6. **Entregables Finales:** Confirmación de que se espera un código fuente integrado, completo y listo para producción.

---

## 🚦 Fase 2: Metodología TDD y Verificación F2P (Fail-to-Pass)

El proyecto exige escribir las pruebas unitarias **antes** de codificar el software final (*Test-Driven Development*). Todas las pruebas deben alinearse estrictamente al *prompt*.

### El Ciclo F2P (Fail-to-Pass)
1. **Fase de Falla (Fail):** Ejecutar pruebas sobre código vacío. Todas deben fallar. Se genera automáticamente un archivo `before.json`.
2. **Desarrollo del Golden Patch:** El agente de IA crea la solución perfecta para cumplir con el código.
3. **Fase de Éxito (Pass):** Ejecutar pruebas sobre el nuevo código. Todas deben pasar en verde. Se genera un `after.json`.

### ⚠️ Regla de Oro: Evitar Pruebas "Excesivamente Específicas"
No se debe penalizar a la IA por tomar soluciones lógicas y válidas.
- **Ejemplo negativo:** Forzar un `ModuleNotFoundError` en una prueba, si el sistema podría retornar un error manejado diferente de manera válida. 
- Las pruebas deben permitir diferentes acercamientos lógicos mientras cumplan la solicitud principal.

---

## 📝 Fase 3: Rúbricas de Evaluación Experta

Para aspectos subjetivos o aquellos que son imposibles de cubrir mediante scripts F2P, entra el evaluador humano.

**Reglas de Redacción:**
- **Atómicas:** Cada regla evalúa un solo punto.
- **Verificables:** Deben ser objetivamente comprobables.
- **Encuadre Positivo:** Se leen como la presencia de una cualidad ("*El código incluye...*").

**Sistema de Pesos:**
- **5 (Obligatorio):** Requisito explícito y demandado por el prompt.
- **3 (Importante):** Implícitamente necesario; mejora de forma drástica la calidad.
- **1 (Deseable):** La solución funciona sin esto, pero hacerlo la vuelve más robusta (Nice to have).
- *(Estrictamente prohibido usar valores 2 o 4).*

---

## 🐳 Fase 4: Configuración del Entorno y Ejecución (Docker)

Se requiere una infraestructura estandarizada para garantizar la reproducibilidad; por ende, todo funciona contenerizado.

### Archivos Fundamentales del Entorno:
- `Dockerfile`: Obligatorio. Todas las dependencias deben estar **"hardcodeadas"** aquí. Cero excusas.
- `run.sh`: Ejecuta las pruebas automatizadas y produce los logs.
- `parsing.py`: Limpia los resultados de la prueba volcándolos en archivos JSON claros.
- `verification.sh` (o `validation.sh`): Script maestro de orquestación.

### Infraestructura Local
- **Windows:** Obligatorio el uso de **WSL (Windows Subsystem for Linux)** e instalando Ubuntu. Se abre Cursor conectándose directamente al sistema WSL.
- **Mac:** Docker Desktop nativo funciona de fábrica.
- **Cursor IDE:** Recomendado para apertura directa dentro de los volúmenes del sistema y edición transparente.

---

## 🚨 Protocolo y Soporte Final

1. **Entorno de Trabajo:** Todo debe estar metido dentro de una carpeta raíz designada como `app/`.
2. **Validación Definitiva:** La tarea solo es Correcta si el script final automatizado documenta **"Falla Total"** *(before.json)* y luego **"Éxito Total"** *(after.json)*.
3. **War Room 24/7:** Hay disponibilidad constante de asistencia liderada por Quality Managers (QM).
