# 📘 Guía 1 — Flujo Principal del Proyecto Real Coder
> **Traducción oficial al español** | Fuente: `g1instructions` | Fecha original: 26/03/2026
> 
> ⚠️ **Diferencias con tu proyecto actual** están marcadas con `[⚡ DIFERENTE]`

---

## 📂 Registro de Cambios (Changelog)

| Fecha | Descripción |
|---|---|
| 18/03/2026 | **Regla de Determinismo Obligatoria agregada (Paso 1a).** Prohíbe el uso de lenguaje no determinista como "o", "recomendado", "debería" y "etc." para garantizar que el prompt funcione como una máquina de estados estricta con un único camino de ejecución. `[⚡ DIFERENTE]` |
| 18/03/2026 | **Actualizado Paso 1b: Filosofía de Requisitos.** Se estableció una jerarquía clara para "Demasiado Específico" (Fallo Crítico) vs. "Deseable" (Solo Rúbrica) para prevenir sobreajuste de tareas y asegurar verificación agnóstica a la implementación. |
| 18/03/2026 | **Introducido 🧪 PASO 1c: Verificación del Prompt Reescrito.** Protocolos de auditoría obligatorios para Determinismo Lingüístico y Cumplimiento Estructural. `[⚡ DIFERENTE — paso nuevo]` |
| 13/03/2026 | Cualquier tipo de agente de código es válido. Se recomienda OpenCode sobre Cursor por costo-efectividad. |
| 11/03/2026 | Al construir tu sitio web, asegúrate de que la UI cumpla estándares freelance profesionales y todos los flujos de usuario sean funcionales. |
| 10/03/2026 | **Cumplimiento de Activos Visuales:** Los activos deben ser 100% de uso comercial libre. No usar contenido de Unsplash. Usar Google Fonts, Lucide/Heroicons o Pexels. |
| 03/03/2026 | Para tareas frontend/fullstack, usar rúbricas de Seguimiento de Instrucciones (IF) para cubrir requisitos de diseño UI. |
| 01/03/2026 | El Golden Patch debe responder cada requisito del prompt reescrito y pasar todos los criterios de la rúbrica. |
| 27/02/2026 | Se agregó carpeta de System Prompts adicional. |
| 25/02/2026 | Las pruebas unitarias NO deben ser excesivamente específicas. Enfoque TDD. |
| 18/02/2026 | Dockerfile actualizado, script de validación agregado. |
| 02/02/2026 | Se agregó "Expected Interface" (Interfaz Esperada) al prompt reescrito. |

---

## 🎯 Objetivo del Proyecto

Generar soluciones de software de alta calidad y verificadas para tareas de estilo freelance partiendo desde cero. Transformarás una descripción de tarea en bruto en un prompt estructurado, desarrollarás una solución funcional desde cero (Golden Patch) y proporcionarás una suite de verificación de doble capa (pruebas F2P automáticas + rúbrica experta).

---

## ✅ Agentes de Código Permitidos

### OpenCode
- Sitio web: https://opencode.ai/
- Gratuito y recomendado como primera opción.
- Se puede vincular a tu cuenta LLM Pro preferida.

### Cursor (Política de Reembolso)
- El costo de Cursor se reembolsa solo después de completar exitosamente tu primera tarea (puntaje QC no sea 1/5 o 2/5).
- Comenzar con el plan de $20.
- Reembolso de $200+: ≥30 tareas, promedio QC ≥3/5, dentro de 30 días.
- Reembolso de $60–$70: ≥15 tareas, promedio QC ≥3/5, dentro de 30 días.

---

## 🔄 Flujo de Trabajo de la Tarea (16 Pasos Oficiales)

> ⚠️ **[⚡ DIFERENTE]** — Tu proyecto actual usa 6 pasos. La guía oficial usa 16 pasos detallados que expanden ese flujo.

1. Revisar la descripción de la tarea (usualmente un aviso de trabajo freelance) y anotar requisitos, restricciones, lenguaje y salida esperada.
2. Construir un prompt que incluya toda la funcionalidad de extremo a extremo y el diseño del sistema de software para cumplir todos los requisitos.
3. Asegurarse de que el prompt incluya la sección de Expected Interface, cubriendo cada nuevo archivo, función o clase que una aplicación externa o suite de pruebas interactuará (solo interfaces públicas, no funciones auxiliares).
4. Usar Desarrollo Guiado por Pruebas (TDD) con agente Cursor + Claude para construir el conjunto de pruebas unitarias que cubran todos los requisitos sin ser excesivamente específicas.
5. Escribir `run.sh` configurando el comando del ejecutor de pruebas dentro de la plantilla.
6. Escribir `parsing.py` implementando `parse_test_output` dentro de la plantilla.
7. Agregar las dependencias requeridas en el Dockerfile siguiendo la plantilla estrictamente, sin usar el comando `COPY`.
8. **Ejecución Base (Antes):** Construir la imagen Docker y ejecutar la línea base sobre una base de código vacía. Objetivo: el JSON resultante debe mostrar cada prueba unitaria como FAILED (no ERRORED).
9. Escribir las rúbricas cubriendo los 30 requisitos más importantes no evaluados por pruebas unitarias.
10. Pedir al agente que construya la solución completa del prompt y corregir la solución para crear el Golden Patch.
11. **Ejecución de Verificación (Después):** Aplicar el Golden Patch y re-ejecutar ambos scripts. Objetivo: el JSON debe mostrar esas mismas pruebas como PASSED.
12. Calificar las rúbricas contra el Golden Patch evaluando cada criterio, y corregir el Golden Patch o las rúbricas si es necesario.
13. Ejecutar el script de validación para confirmar que `before.json` muestra todos FAIL y `after.json` muestra todos PASS.
14. Verificar la estructura de carpetas y la salida, y corregir cualquier problema.
15. Subir los archivos finalizados: Golden Patch (`codebase.zip`), Dockerfile, `run.sh`, `parsing.py` y `tests.zip`.
16. ¡ENVIAR! 🎉

---

## 📚 Recursos

- Video de Onboarding
- Onboarding General
- Qué modificar en el Dockerfile
- **Linter Fuera de Plataforma:** Para verificar Golden Patch, Pruebas Unitarias y Rúbricas (02/27)

> 💡 **Consejo:** No tengas miedo de alimentar la copia descargada del documento QC Spec al agente Cursor para que te ayude a verificar tu prompt, rúbricas, solución dorada y pruebas.
> 
> ⚠️ **Advertencia:** Estos prompts de sistema (linters fuera de plataforma) deben usarse solo como guía y no tratarse como fuente de verdad. Eres responsable de la corrección de tu solución.

---

## ✏️ PASO 0: Comprender los Requisitos de la Tarea

Antes de reescribir el prompt, revisa cuidadosamente el **Tipo de Tarea**, **Lenguaje de Codificación**, **Descripción Corta** y **Descripción de la Tarea** proporcionados. Esto asegura que entiendas claramente el alcance, las restricciones y los objetivos.

### Secciones Clave a Revisar

**Tipo de Tarea**
Define la categoría general de la aplicación (ej. herramienta de operaciones, plataforma web, pipeline de datos, app móvil).

**Lenguaje de Codificación de la Tarea**
Especifica si la implementación debe usar un lenguaje específico o si cualquier lenguaje está permitido. Si no hay restricción, puedes definir un stack apropiado en tu prompt reescrito.

**Descripción Corta**
Define restricciones globales que aplican a todas las tareas:
- Mantener estándares de desarrollo freelance profesional.
- Si la tarea incluye UI, debe ser limpia, usable y funcional.
- Todos los flujos de usuario principales deben funcionar correctamente.
- No se permite obtener datos en vivo ni descargar datasets externos.
- Cualquier dataset requerido debe incluirse localmente en el repositorio.
- Las pruebas unitarias deben cubrir requisitos funcionales; las rúbricas deben cubrir aspectos de UI/diseño (límite: los 30 criterios más importantes).

**Descripción de la Tarea**
Es el input más importante. Generalmente escrito como un brief de cliente de alto nivel. Tu responsabilidad es transformar esto en un prompt claro, estructurado y listo para implementar:
- Hacer los requisitos específicos e inequívocos.
- Expandir descripciones vagas en funcionalidad concreta.
- Asegurar consistencia lógica en todos los requisitos.
- Eliminar o resolver contradicciones.
- Completar detalles técnicos razonables cuando sea necesario.

### Cumplimiento de Activos Visuales
- **Activos de Uso Comercial Libre:** Google Fonts, Lucide/Heroicons, Pexels.
- **Verificación de Licencias:** No incluir activos que requieran licencia paga.
- **Si no estás seguro:** Usa solo un placeholder de imagen en tu código.
- ‼️ **NO uses contenido de Unsplash** ‼️

---

## 📝 PASO 1a: Generación del Prompt

> 💡 **Consejo Importante:** DEBES incluir la sección completa de Expected Interface en tu prompt reescrito. No hacerlo resultará directamente en una tarea de mala calidad.

El primer paso es transformar una descripción de tarea en bruto en un prompt estructurado. Este prompt funciona como un Brief de Trabajo Freelance que un agente de IA usará para crear una solución.

- **Claridad:** Asegurar que el objetivo y el stack tecnológico sean inequívocos.
- **Contexto:** Incluir toda la información necesaria para crear las pruebas y la solución correctas.
- **Expected Interface:** Definir cada nuevo archivo, función o clase que una aplicación externa o suite de pruebas interactuará. Solo interfaces públicas, no funciones auxiliares.

### Formato de Cada Entrada en la Expected Interface

```
- Path: [Ruta exacta del archivo]
- Name: [Clase.método o nombre de función]
- Type: [class | function | method | API Endpoint | React Component | ...]
- Input: [Parámetros y tipos]
- Output: [Tipo de retorno o respuesta HTTP]
- Description: [Qué hace y qué verifican las pruebas]
```

**Campos Específicos por Lenguaje (cuando aplica):**
- TypeScript/Java: `Inheritance: extends <Base>; implements <IfaceA, IfaceB>`
- Go: `Embedding / Implements: embeds <TypeA>; implements <IfaceA, IfaceB>`
- Python: `Bases / Overrides: bases: <BaseA, BaseB>; overrides: <Base.method>`
- Anotaciones/Decoradores: `@Override`, `@Inject`, `@dataclass`, `@cached_property`

### 🧩 Patrón Común de Estructura del Prompt

**Patrón A** (más común — 12/20 tareas):
```
# Título
## Descripción / Contexto
## Tech Stack
## Key Requirements (con subsecciones ###)
## Expected Interface (con ### por función/clase/endpoint)
## Estado Actual
```

**Patrón B** (para tareas más grandes — 8/20 tareas):
```
# Título
## Descripción
## Estado Actual
## Implementación Requerida
## Expected Interface (con agrupaciones ## y ###)
## Entregables / Criterios de Aceptación
```

### Observaciones Clave
- La Expected Interface siempre está embebida dentro del prompt — no es una columna separada. Representa el 30-70% del contenido total.
- La granularidad varía por complejidad: tareas simples tienen 4-6 entradas; tareas complejas tienen 20-40+.
- "Estado Actual" es casi siempre "Repositorio vacío con archivos de prueba solamente" — establece que es una construcción desde cero.

---

## 🔴 La Regla de Determinismo (Obligatoria) `[⚡ DIFERENTE — REGLA NUEVA]`

> Esta regla no está documentada explícitamente en tu proyecto actual. Es una actualización crítica del 18/03/2026.

Para asegurar que el Golden Patch sea reproducible y verificable, tu prompt reescrito DEBE actuar como una máquina de estados estricta. Debe forzar un único camino de ejecución predecible.

### ⚠️ Zona de Peligro
**Cualquier prompt que contenga opcionalidad, restricciones suaves o alcances abiertos será desactivado inmediatamente.**

- **Frases Obligatorias:** Usar comandos directos e imperativos como "DEBES", "Implementa" o "Crea".
- **Lenguaje Prohibido:** No usar "o", "alternativamente", "ya sea X o Y", "recomendado", "debería", "etc." o "puedes" — a menos que la Descripción de la Tarea lo especifique.
- **Límites Estrictos:** No usar "algo como" o "tecnologías relevantes". Definir una lista exhaustiva y finita de cada herramienta y tecnología requerida.

---

## 🧪 PASO 1b: Requisitos del Prompt

Los requisitos de tu prompt deben separarse en 2 categorías principales:

1. **Requisitos testeables con pruebas unitarias** que NO sean excesivamente específicas.
2. **Requisitos que solo pueden verificarse con rúbricas**, ya sea porque son demasiado específicos para pruebas unitarias o porque solo pueden cubrirse cualitativamente.

Para los requisitos en la categoría 2, solo necesitas cubrir hasta los **TOP 30 CRITERIOS MÁS IMPORTANTES** mencionados explícitamente en las rúbricas.

### Filosofía de Requisitos: Especificidad vs. "Deseable"

| Categoría | Definición | Permitido En |
|---|---|---|
| **Excesivamente Específico** | Verificar un detalle que nunca se menciona explícita o implícitamente en el prompt (ej. forzar un nombre de carpeta interna o nombre de método privado). | **NINGUNO** (Fallo Crítico) |
| **Deseable (Implícito)** | Verificar una expectativa estándar que se menciona implícitamente (ej. una "UI profesional" implica padding de botones consistente). | Solo Rúbricas (Peso 1) |
| **Deseable (Explícito)** | Verificar una característica que el prompt etiquetó explícitamente como "Opcional", "Recomendado" o "Deseable". | Solo Rúbricas (Peso 1) |

---

## 🧪 PASO 1c: Verificación del Prompt Reescrito `[⚡ DIFERENTE — PASO NUEVO]`

> Este paso completo es nuevo respecto a tu proyecto actual. Es un proceso de auditoría obligatorio antes de crear pruebas o el Golden Patch.

Antes de proceder a la creación de pruebas unitarias o construir el Golden Patch, debes validar que tu prompt reescrito actúa como una máquina de estados estricta.

### Verificación 1: No-Determinismo Lingüístico (Linter)

Alimenta el siguiente system prompt a Cursor para auditar tu prompt en busca de "Trampas Lógicas":

**Objetivo:** Tu prompt debe alcanzar estado PASS. Si se encuentran trampas de "Opcionalidad" o "Restricción Suave", debes reemplazar el lenguaje permisivo (ej. "puedes") con comandos directos imperativos (ej. "DEBES").

```
Eres un Arquitecto de Prompts Principal. Tu único objetivo es auditar 
prompts de Contribuidores (CB) en busca de NO-DETERMINISMO LINGÜÍSTICO.

Un prompt de alta calidad debe actuar como una máquina de estados estricta. 
Debe forzar un único camino de ejecución predecible. Fallarás cualquier 
prompt que contenga opcionalidad, restricciones suaves, frases basadas en 
permisos o alcances abiertos.

1. DIMENSIÓN DE AUDITORÍA: TRAMPA DE OPCIONALIDAD
   [Fallo - Múltiples opciones]: El prompt da una elección sin condición estricta.
   * Disparadores: "o", "alternativamente", "ya sea X o Y", "puedes elegir".
   * Regla: El prompt debe dictar UN camino exacto.

2. DIMENSIÓN DE AUDITORÍA: TRAMPA DE RESTRICCIÓN SUAVE
   [Fallo - Sugerencia sobre Comando]: Lenguaje que hace un requisito opcional.
   * Disparadores: "debería", "preferiblemente", "idealmente", "si es posible", 
     "recomendado", "deseable", "intenta".
   * Regla: Un requisito es "DEBE/SHALL" o debe eliminarse completamente.

3. DIMENSIÓN DE AUDITORÍA: TRAMPA DE ALCANCE ABIERTO
   [Fallo - Listas Sin Límite]: El prompt pide extrapolación más allá de un conjunto.
   * Disparadores: "etc.", "herramientas similares", "algo como", 
     "tecnologías relevantes", "y otros".
   * Regla: El prompt debe definir una lista exhaustiva y finita.

4. DIMENSIÓN DE AUDITORÍA: TRAMPA DE PERMISO
   [Fallo - Voz Pasiva]: Declarar lo que la IA está *permitida* a hacer.
   * Disparadores: "puedes", "tienes la opción de".
   * Regla: Reemplazar con comandos directos imperativos.

OUTPUT (SOLO JSON):
{
  "status": "PASS" | "FAIL",
  "determinism_score": "0-100",
  "violations": [...]
}
```

### Verificación 2: Cumplimiento Estructural y de Directrices

Verificar que el prompt sigue el Patrón A o B requerido y contiene una Expected Interface completa para cada caso de prueba.

**Objetivo:** Asegurar 100% de alineación con el esquema de Expected Interface (Path, Name, Type, Input, Output, Description) y verificar que el Tech Stack sea inequívoco.

---

## 💎 PASO 2a: Verificación de Casos de Prueba F2P (Fail-to-Pass)

> 💡 **Consejo:** Las pruebas unitarias NO deben ser excesivamente específicas a tu solución dorada. Si hay algo imposible de cubrir con el prompt, usa una rúbrica en su lugar.

Las pruebas F2P son obligatorias. Este proyecto fomenta un enfoque TDD, lo que significa que debes pre-construir las pruebas unitarias antes de crear el Golden Patch.

### Principios Fundamentales del Testing

**1. Pruebas Estáticas vs. Funcionales**
- **Pruebas Estáticas (FALLO):** Usar scripts que hacen "grep" o buscan palabras específicas en archivos fuente.
- **Pruebas Funcionales (PASS):** Usar un ejecutor de pruebas (como pytest) para ejecutar el código, enviar entradas reales y verificar que las salidas sean correctas.

**2. La "Trampa del Comentario"**
Una debilidad importante del testing estático es que no puede distinguir entre lógica funcional y texto muerto. Una prueba funcional detectaría inmediatamente si el código está roto al intentar filtrar datos y recibir un resultado incorrecto.

**3. El Principio de Caja Negra**
Las pruebas deben tratar tu Golden Patch como una "Caja Negra":
- Solo interactúan con la solución a través de la Expected Interface.
- No mockear ni parchear funciones auxiliares internas.

**4. Resultados Deterministas**
- La misma suite de pruebas DEBE fallar en una base de código vacía y DEBE pasar una vez aplicado el Golden Patch.
- Una prueba debe pasar para cualquier solución válida del prompt, independientemente de nombres de variables o estructuras de archivo internas no especificadas.

### 🎯 La "Zona Dorada" del Testing

| Característica | Demasiado Amplio (FALLO) | Demasiado Específico (FALLO) | La Zona Dorada (PASS) |
|---|---|---|---|
| Método de Verificación | Coincidencia de strings / "Grepping" | Imponer nombres de métodos privados | Testing Funcional: Solicitudes HTTP reales o llamadas a la interfaz pública |
| Cobertura | Solo verificar que los archivos existen | Testear "Mejores Prácticas" no mencionadas | Mapeo de Requisitos: Cada requisito backend tiene una prueba funcional |

### Proceso F2P

1. Usar agente Cursor + Claude para construir el conjunto de pruebas unitarias.
2. Verificar cobertura de las pruebas.
3. **Ejecución Base (Antes):** Ejecutar `run.sh` y `parsing.py` sobre base de código vacía. Objetivo: el JSON debe mostrar tests como FAILED.
4. Pedir al agente que construya la solución completa.
5. Corregir la solución del agente para crear el Golden Patch.
6. **Ejecución de Verificación (Después):** Aplicar el Golden Patch y re-ejecutar ambos scripts. Objetivo: el JSON debe mostrar esas mismas pruebas como PASSED.
7. Escribir las rúbricas para cubrir los 30 requisitos más importantes que las pruebas unitarias no pueden cubrir.

---

## 🛠️ Plantilla Oficial del Dockerfile `[⚡ DIFERENTE]`

> **DIFERENCIA CRÍTICA:** El Dockerfile oficial usa `WORKDIR /app` (no `/workspace` como tu proyecto actual) y agrega `git init` + `mkdir -p /eval_assets`.

```dockerfile
###############################################
# BASE IMAGE
###############################################
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

###############################################
# SYSTEM DEPENDENCIES
###############################################
RUN apt-get update && apt-get install -y \
    git \
    python3 \
    python3-pip \
    python3-setuptools \
    python-is-python3 \
    unzip \
    && rm -rf /var/lib/apt/lists/*

###############################################
# WORKING DIRECTORY + GIT SETUP
###############################################
WORKDIR /app

RUN git init \
    && git config --global user.email "agent@example.com" \
    && git config --global user.name "Agent" \
    && echo "# Workspace" > README.md \
    && git add README.md \
    && git commit -m "Initial commit"

###############################################
# EVALUATION ASSETS DIRECTORY
###############################################
# Poblado en RUNTIME por el script de evaluación.
RUN mkdir -p /eval_assets

CMD ["/bin/bash"]
```

**Reglas del Dockerfile:**
- NO modificar la estructura del archivo.
- NO eliminar instrucciones existentes.
- NO agregar capas de pasos no relacionados.
- NO cambiar puntos de entrada o comandos por defecto.
- SÍ puedes agregar dependencias específicas en la sección de System Dependencies.

---

## 📋 Plantilla Oficial de `run.sh` `[⚡ DIFERENTE]`

> **DIFERENCIA CRÍTICA:** La plantilla oficial es más simple y solo expone la función `run_all_tests()`. Solo editar dentro de los comentarios delimitadores.

```bash
#!/bin/bash
### COMMON SETUP; DO NOT MODIFY ###
set -e

# --- CONFIGURE THIS SECTION ---
# Reemplaza esto con tu comando para ejecutar todas las pruebas
run_all_tests() {
    echo "Running all tests..."
    # TODO: Ejecutar la suite de pruebas completa
    # Ejemplo: cargo test --workspace --lib --no-fail-fast
}
# --- END CONFIGURATION SECTION ---

### COMMON EXECUTION; DO NOT MODIFY ###
run_all_tests
```

---

## 🐍 Plantilla Oficial de `parsing.py` `[⚡ DIFERENTE — ESTRUCTURA COMPLETAMENTE DIFERENTE]`

> **DIFERENCIA CRÍTICA:** La plantilla oficial de `parsing.py` lee archivos `stdout` y `stderr` como entrada (no un `report.json`). La función a implementar es `parse_test_output(stdout_content, stderr_content)`. El formato de salida es diferente al de tu proyecto actual.

```python
import dataclasses
import json
import sys
from enum import Enum
from pathlib import Path
from typing import List

class TestStatus(Enum):
    """Enum de estado de prueba."""
    PASSED = 1
    FAILED = 2
    SKIPPED = 3
    ERROR = 4

@dataclasses.dataclass
class TestResult:
    """Dataclass de resultado de prueba."""
    name: str
    status: TestStatus

### DO NOT MODIFY THE CODE ABOVE ###
### Implementa la lógica de parsing abajo ###

def parse_test_output(stdout_content: str, stderr_content: str) -> List[TestResult]:
    """
    Parsear el contenido de salida de la prueba y extraer resultados.
    """
    raise NotImplementedError('Implementa la lógica de parsing de salida de pruebas')

### Implementa la lógica de parsing arriba ###
### DO NOT MODIFY THE CODE BELOW ###

def export_to_json(results: List[TestResult], output_path: Path) -> None:
    json_results = {
        'tests': [
            {'name': result.name, 'status': result.status.name}
            for result in results
        ]
    }
    with open(output_path, 'w') as f:
        json.dump(json_results, f, indent=2)

def main(stdout_path: Path, stderr_path: Path, output_path: Path) -> None:
    with open(stdout_path) as f:
        stdout_content = f.read()
    with open(stderr_path) as f:
        stderr_content = f.read()
    results = parse_test_output(stdout_content, stderr_content)
    export_to_json(results, output_path)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: python parsing.py <stdout_file> <stderr_file> <output_json>')
        sys.exit(1)
    main(Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]))
```

> ⚠️ **Advertencia:** El archivo solo puede cambiarse dentro de los comentarios delimitadores. Modificar otras secciones restringidas puede fallar tu tarea.

---

## 🐳 Guía de Ejecución del Entorno Docker

**IMPORTANTE:** Es extremadamente importante que todas las instrucciones se sigan con precisión. El script de validación depende de una estructura estricta.

### Comandos de Ejecución

```bash
# 1. Construir la imagen Docker
docker build -t real-coder-task-1 .

# 2. Ejecutar el contenedor con shell interactivo
docker run -it real-coder-task-1:latest /bin/bash

# 3. Dentro del contenedor, ejecutar las pruebas
bash run.sh
```

Si pierdes el rastro de la imagen, usa `docker images` para listar todas las imágenes disponibles.

---

## ⚠️ PASO 2b: System Prompt para Verificar Sobre-Especificidad en Pruebas

Puedes alimentar el siguiente system prompt al agente para verificar si tus pruebas unitarias son excesivamente específicas:

```
Eres el Auditor Principal de Cumplimiento QA. Tu misión es determinar si 
una suite de pruebas contiene pruebas "Excesivamente Específicas".

1. DOCTRINA DE AUDITORÍA (TOLERANCIA CERO)
   Cualquier prueba que imponga un detalle de implementación no explícitamente 
   encontrado en el prompt es una Violación Crítica.

   A. El "Requisito Fantasma": Si una prueba afirma un detalle no explícito 
      en el prompt, es Excesivamente Específica.
   B. La "Trampa de Implementación": Cualquier prueba usando mock.patch en 
      una ruta de módulo local que fallaría si el dev usó un estilo de import 
      diferente válido es una Violación.

2. PROTOCOLOS DE AUDITORÍA
   Umbral: 0%. Una sola prueba "Excesivamente Específica" resulta en FAIL.

OUTPUT (SOLO JSON):
{
  "audit_result": "PASS" | "FAIL",
  "compliance_metrics": {...},
  "violation_details": [...],
  "coverage_gaps": [...]
}
```

---

## 🚚 Entregables del Paso 2

- Captura de pantalla de la salida de `run.sh` con todas las pruebas mostrando **FAILED** (Ejecución Base).
- Archivo `results.json` con los resultados parseados de `parsing.py` (todos FAILED).
- Copiar y pegar todas las pruebas unitarias de cada archivo de pruebas.

---

## 🛡️ Guía de Stack Tecnológico Precautorio `[⚡ DIFERENTE — SECCIÓN NUEVA]`

> Esta guía no existe en tu proyecto actual. Es crítica para evitar fallos F2P.

| Categoría | Evitar (Alto Riesgo de Fallo F2P) | Recomendado (Estable y Portable) |
|---|---|---|
| **Bases de Datos** | PostgreSQL, MongoDB: requieren servicios externos dentro del contenedor | SQLite, En Memoria, o JSON/Texto Local |
| **Testing** | Jest, Playwright: tienen dependencias de navegador difíciles de gestionar | Pytest (Python) o Vitest (JS/TS) |
| **Lenguajes** | Go, Rust: para tu primera tarea, evitar leng উল্লেখযোগ্য a código máquina | Python, Node.js (TypeScript/JavaScript) |

---

## 📊 PASO 3a: Rúbrica Experta

Una rúbrica es un conjunto de requisitos claros y específicos. Debes crear un documento de rúbrica con **mínimo 5 criterios y máximo 30** sobre los requisitos más importantes de tu prompt reescrito que NO pueden cubrirse por pruebas unitarias agnósticas.

### Criterios de las Rúbricas

- **Atómico:** Cada criterio verifica solo una idea.
- **Verificable:** Puede auditarse directamente desde el código.
- **Positivo:** Usa frases positivas (ej. "El código incluye..." vs "El código no olvida...").

### Pesos de la Rúbrica

| Peso | Significado | Descripción |
|---|---|---|
| **5** | Mandatorio | Requisito central, la respuesta es inaceptable sin él |
| **3** | Importante | Hace la respuesta sustancialmente mejor |
| **1** | Deseable (Opcional) | Bueno tenerlo, pero la respuesta puede ser fuerte sin él |

**NO seleccionar 2 o 4 como pesos. Las únicas opciones permitidas son 1, 3 o 5.**

### Dimensiones de la Rúbrica

1. **Seguimiento de Instrucciones:** Asegurar que la respuesta sigue las directrices explícitas del prompt (formato, restricciones, lenguaje, bibliotecas, elementos requeridos).
2. **Corrección del Código:** Asegurar que el código realiza la tarea correctamente y produce resultados correctos.
3. **Calidad del Código:** Robustez, mantenibilidad, patrones idiomáticos, evitar diseños frágiles.
4. **Claridad del Código:** Código legible y bien estructurado, incluyendo nombres, organización y formato.
5. **Eficiencia del Código:** Concisión, evitar pasos innecesarios, reducción de redundancia.

### Reglas de Puntuación

Para cada elemento de la rúbrica:
- **Criterio Completamente Cumplido (PASS):** Declarar brevemente que el criterio se cumplió.
- **No Cumplido (FAIL):** Nombrar el problema bloqueante específico.

---

## ⚙️ PASO 3b: System Prompt para Verificar Cobertura

Puedes alimentar el siguiente system prompt al agente para verificar si todos los requisitos del prompt están cubiertos por pruebas unitarias y rúbricas:

```
Evalúa la calidad y cobertura de las rúbricas y pruebas en el archivo 
tests.zip adjunto relacionado con los requisitos del prompt.

Para cada prueba, evalúa:
- Si la prueba es excesivamente específica → quality: "FAIL", reason: "overly_specific"
- Si se superpone sustancialmente con otras pruebas → "overlapped"
- Si está mal enmarcada/ambigua → "framing"
- Si es correcta, relevante, no superpuesta → "relevant"

Para cada rúbrica, evalúa:
- Si agrupa múltiples requisitos independientes → "atomic"
- Si no es autocontenida → "self_contained"
- Si es excesivamente específica → "overly_specific"
```

---

## 👑 PASO 4: Construyendo el Golden Patch

- Una vez que tu suite de pruebas unitarias y rúbricas cubren todos los requisitos explícitos del prompt, alimenta el prompt al agente Cursor con Claude para generar una solución inicial.
- Realiza verificaciones para asegurar que satisface todos los requisitos. Si no, corrige la solución del agente hasta que sea perfecta.
- Está bien usar funciones auxiliares, APIs de terceros (no APIs externas) o paquetes auxiliares siempre que no contradigan tu prompt.
- Asegúrate de no usar imágenes o datasets con copyright.

---

## 💼 PASO 5: Ejecutar la Suite de Pruebas Nuevamente

- Ejecutar las suites de pruebas para asegurar que la solución PASA TODAS LAS PRUEBAS.
- Si hay fallos: revisar si es la solución dorada o las pruebas unitarias.
  - Si la solución tiene problemas: corregir la solución y ejecutar de nuevo.
  - Si las pruebas tienen problemas: corregir las pruebas, re-ejecutar contra base de código vacía en Paso 2, re-enviar capturas, luego ejecutar contra la solución perfecta.
- Calificar los criterios de la rúbrica contra el Golden Patch. El Golden Patch debe pasar TODOS los criterios.

### Entregables del Paso 5
- Captura de pantalla del comando `run.sh` mostrando todos los casos de prueba **PASSED**.
- Agregar `results.json` mostrando todos los tests como PASSED.
- Pegar TODAS las pruebas unitarias ejecutadas DESPUÉS de que el Golden Patch esté construido.
- Subir el `tests.zip` más actualizado.

```
tests.zip/
└── tests/
    (todas tus pruebas aquí)
```

---

## 🔐 PASO 6: Script de Validación

Para asegurar que tu Golden Patch y pruebas son reproducibles, debes ejecutar el script `validation.sh`.

### Estructura del Directorio `/app` `[⚡ DIFERENTE — directorio raíz es /app no /workspace]`

```
/app/
│
├── Dockerfile         # Definición de imagen Docker
├── tests.zip          # Tu suite de pruebas
├── codebase.zip       # Tu Golden Patch
├── run.sh             # Script que ejecuta tus casos de prueba
└── parsing.py         # Parsea las salidas de los casos de prueba a JSON
```

### Qué Puedes Cambiar en el Script

- La ruta del archivo raíz principal si es necesario (por defecto `/app`).
- Puedes agregar estas dos líneas si el script no corre:
  - `/bin/bash -c 'parse_results stdout.txt stderr.txt before.json' || true`
  - `/bin/bash -c 'parse_results stdout.txt stderr.txt after.json' || true`
- **NO cambiar nada más del script.**

### Entregables del Paso 6

- Subir `before.json` después de ejecutar el script de verificación.
- Copiar y pegar el contenido completo de `before.json`.
- Subir `after.json` después de ejecutar el script de verificación.
- Copiar y pegar el contenido completo de `after.json`.
- Subir el Golden Patch finalizado como `codebase.zip`.
  - ❌ **NO** comprimir la carpeta. Solo comprimir los archivos dentro de la base de código.
  - ❌ **NO** tener zips anidados.
- Subir el Dockerfile más actualizado/finalizado.
- Subir el `parsing.py` más actualizado/finalizado.
- Subir el script `run.sh` más actualizado/finalizado.
- Subir cualquier archivo de requisitos de paquetes (`requirements.txt` o `package.json`).
- Subir una captura de pantalla del timestamp de última edición de cada archivo.

---

## 🛠️ Lista de Verificación de Validación: Errores Comunes

### 1. Estructura del Directorio `/app`

Exactamente estos 5 archivos/carpetas, ni más ni menos:
- `codebase.zip`
- `tests.zip`
- `Dockerfile`
- `parsing.py`
- `run.sh`

### 2. La Regla de Oro de los Archivos ZIP

| Archivo | Estructura Interna | Cómo Comprimirlo |
|---|---|---|
| `tests.zip` | Debe contener la carpeta `tests/` primero | Comprimir la carpeta completa |
| `codebase.zip` | Debe contener solo los contenidos (sin carpeta padre) | Comprimir los archivos dentro de la carpeta |

> ⚠️ No hacer `codebase.zip` anidado (ej. `codebase.zip → codebase/ → archivos`). Debe ser `codebase.zip → archivos`.

### 3. Integridad de Archivos y Gestión de Cursor

**`run.sh` y `parsing.py`:**
- Monitorear estos archivos de cerca.
- No permitir cambios en las secciones marcadas "DO NOT MODIFY".

**`verification.sh`:**
- Solo puedes editar una sección: tu Path.
- No actualizar nada más. Asegurarse de que el agente Cursor no "alucine" mejoras.

---

## ❓ FAQs

**1. ¿Está bien cambiar la ruta principal de la app en el script de verificación?**
Sí, pero solo esa línea puede cambiarse, no el resto del script.

**2. ¿Qué debemos hacer con la salida del script de verificación?**
Para tareas antiguas de taxonomía: simplemente copiar y pegar `before.json` y `after.json`.

**3. Cobertura: ¿Cuál dimensión es la más actualizada?**
- Algunos requisitos son cubribles por pruebas unitarias, otros por rúbricas. Pueden superponerse pero ninguno debe perderse.
- Backend → principalmente pruebas unitarias.
- Frontend + cosas no testeables por código → rúbricas.
- La Expected Interface también debe testearse.

**4. ¿Las pruebas F2P deben FAIL o pueden ERROR?**
Las pruebas deben FAIL, no crashear el programa.

**5. ¿Las rúbricas deben cubrir todos los requisitos explícitos del prompt reescrito?**
Sí.

**6. ¿Podemos cambiar el Dockerfile?**
Sí, puedes agregar dependencias adicionales si es necesario.

**7. ¿Hay que usar WSL o Docker es suficiente?**
WSL facilita construir imágenes en Windows, pero también puedes usar PowerShell o git bash.

**8. ¿Deben crearse casos de prueba para frontend y backend?**
Backend es el requisito mínimo. Para frontend, usar rúbricas.

**9. ¿Qué modelo usar en Cursor?**
Cualquier modelo. Se recomienda Claude 4.6.

**10. ¿Qué pasa si un criterio de rúbrica ya está cubierto por pruebas unitarias?**
Puedes incluirlo en rúbricas, pero esto debe ser raro.

---

## 📎 Apéndice: Ejemplos de Rúbricas por Tipo

### A. Seguimiento de Instrucciones — Buenos Ejemplos
- "La solución implementada debe ejecutarse con Python 3 (no Python 2)."
- "La respuesta debe ser JSON válido (parseable por máquina), no markdown ni prosa."
- "La UI debe hacer la acción primaria/siguiente paso visualmente obvio."

### B. Corrección del Código — Buenos Ejemplos
- "Dado el input `[]`, la función debe retornar `[]`."
- "La función debe lanzar un `ValueError` con mensaje legible cuando falta el valor X."

### C. Calidad del Código — Buenos Ejemplos
- "La solución evita valores hardcodeados y usa parámetros configurables."
- "El código usa funciones modulares para separar responsabilidades."

### D. Claridad del Código — Buenos Ejemplos
- "El código usa nombres de variables y funciones claros y descriptivos."
- "La implementación está lógicamente organizada en secciones legibles."

### E. Eficiencia del Código — Buenos Ejemplos
- "La solución avoids bucles redundantes y cómputo repetido."
- "El código evita estructuras de datos intermedias innecesarias."

---

> 📌 **Nota Final:** Esta guía corresponde a la versión más reciente (26/03/2026). Los cambios más significativos respecto a versiones anteriores son la Regla de Determinismo (Paso 1a), el nuevo Paso 1c de auditoría de prompts, y las plantillas oficiales de `run.sh` y `parsing.py` que tienen una estructura diferente a la de tu proyecto actual.
