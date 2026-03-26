# Informe General de Onboarding: Hawkins Experiments Intro Course (Proyecto P2P)

> **Proyecto:** P2P (Code Refactoring & Performance Optimization)
> **Curso:** Hawkins Experiments Intro Course (10 secciones)

---

## Página 1/10: Introducción y Objetivo del Proyecto

**¿De qué trata Hawkins Experiments?**
El objetivo principal del proyecto es enseñar a crear tareas basadas en código (Code-Based o CB tasks) que puedan ser construidas y evaluadas de forma determinística por un sistema automatizado.

**El "Task Package" (Paquete de Tarea)**
El rol del ingeniero (SWE) es proveer un paquete completo y funcional que consta estrictamente de 4 elementos:
1. **Prompt** (Instrucciones)
2. **Docker** (Entorno determinístico)
3. **Scripts** (Para validación/tests)
4. **Golden Patch** (La solución ideal o parche perfecto)

**Reglas Generales del Curso:**
- Todas las respuestas de texto libre deben estar escritas obligatoriamente en **Inglés**.
- Se debe leer cada pregunta con atención, asumiendo que se trata de una entrega real del proyecto.

*Fin de la Página 1.*

---

## Página 2/10: Project Resources (Recursos del Proyecto)

Esta página presenta los recursos oficiales y plantillas que utilizaremos durante el proyecto. Los enlaces apuntan a la documentación de las directrices y scripts estándar de la plataforma.

**Plantillas y Scripts Clave Identificados:**
1. **Dockerfile Template:** La plantilla oficial base para construir los entornos de evaluación.
2. **Parsing Template:** Un script en Python. La plataforma indica explícitamente una regla estricta: **"Be sure to rename the file to parsing.py!!"** (Asegúrate de renombrar el archivo a `parsing.py`). 
3. **End To End Script:** Un script bash (`e2e_new.sh`) que probablemente orquesta la construcción de Docker y la ejecución de pruebas.

> *Nota: Descargaremos y analizaremos el código de estos scripts a detalle más adelante. Por lo pronto, queda registrada la regla de renombrar el archivo parsing.*

---
*Fin de la Página 2.*

---

## Página 3/10: Project Overview and Required Deliverables

**Objetivo de Hawkins Experiments:**
Crear una estructura para evaluar la capacidad de un modelo de IA para realizar cambios en un repositorio de código que solucionen un problema específico **sin introducir regresiones**. Tu trabajo es construir el entorno (Prompt + Entorno de Evaluación) para calificar la respuesta del modelo que se generará en el futuro.

**Dos Tipos de Tareas en P2P:**
1. **Refactoring/Maintainability (R/M)** → (Refactorización y Mantenibilidad)
2. **Performance Optimization (PO)** → (Optimización de Rendimiento)

**Entregables Requeridos (Deliverables):**
Para *TODAS* las tareas, independientemente de su tipo, debes entregar The **"Core 6"**:
- [ ] User-facing problem description (Descripción del problema)
- [ ] Dockerfile
- [ ] Prompt
- [ ] Run Script
- [ ] Parsing file
- [ ] Golden Patch

**Entregables Adicionales según el Tipo de Tarea:**
*   Para tareas de **Refactoring (R/M)** debes entregar adicionalmente:
    - [ ] **Grading Rubric** (Rúbrica de evaluación)
*   Para tareas de **Performance Optimization (PO)** debes entregar adicionalmente:
    - [ ] **Target Functions** (Funciones objetivo a optimizar)
    - [ ] **Reproduction Script** (Script para reproducir y medir el rendimiento)

---
*Fin de la Página 3.*

---

## Página 4/10: Common Steps 1–4 (Source → Prompt → Docker → Task Type)

Esta página define el flujo de trabajo inicial estructurado en 4 pasos críticos:

**Paso 1: Entender la fuente (source_url)**
Se proporciona un enlace a un PR de GitHub. Debemos analizar el PR para entender qué problema resuelve, ya que con esto crearemos la descripción del problema y el prompt.

**Paso 2: Configurar Dockerfile y proporcionar metadatos**
*   **User-Facing Problem Description:** Un resumen breve del problema que resuelve el PR, escrito *como si el problema aún no estuviese resuelto*.
*   **Reglas Estrictas del Dockerfile:**
    *   Hacer checkout del **commit padre** del PR (usando el *hash* específico, NO el nombre de la rama).
    *   Instalar todas las librerías necesarias.
    *   Debe ser **agnóstico a la arquitectura** (no usar `x86_64`, `AArch64`, etc.).
    *   **Prohibido usar comandos `COPY`** para: `run_script.sh`, `reproduction_script.sh`, `golden.patch`, o `parsing.py`. (Esta es una regla de fallo automático si se rompe).

**Paso 3: Escribir el Prompt (Lo que ve el modelo)**
El prompt no debe hacer referencia al PR, scripts o rubricas. Solo debe describir el error y pedir que lo arreglen. Tampoco usar la "segunda persona" (you).
*Requisitos:* Autocontenido, restricciones claras, definición de "hecho", conservar la funcionalidad (no pedir features), sin pistas o soluciones.
*   **Plantilla Obligatoria del Prompt:**
    *   `## Context`
    *   `## Problem Statement`
    *   `## Requirements` (restricciones específicas)
    *   `## Success Criteria` (criterios medibles, pruebas pasando)
    *   `## Files to Modify`
    *   `## Notes` (sin pistas hacia la solución)

**Paso 4: Elegir el tipo de Tarea (Task_Type)**
La plataforma sugiere un tipo, pero es nuestra responsabilidad verificarlo y elegir la categoría correcta.
*   **Refactoring** → Evalúa con `Grading Rubric + Unit Tests`.
*   **Performance Optimization** → Evalúa con `Quantitative Metrics + Unit Tests`.

---
*Fin de la Página 4.*

---

## Página 5/10: Run Script, Parsing Script, Golden Patch

Esta página detalla los 3 entregables técnicos más importantes y sus restricciones:

**1. Run Script (`run_script.sh`)**
*   **Propósito:** Asegurar que el Golden Patch no introduzca regresiones. 
*   **Regla de Oro:** SOLO debe ejecutar pruebas (unit tests) que **ya pasaban** ANTES de aplicar el Golden Patch.
*   **Flujo esperado:** Se ejecuta sin el parche (pasan todas las pruebas) -> Se aplica el parche -> Se vuelve a ejecutar (siguen pasando todas las pruebas).
*   **Requisitos:** Debe ejecutar compilaciones/builds (si aplica), linters (si aplica) y las pruebas unitarias que pasan originalmente.

**2. Parsing File (`parsing.py`)**
*   **Propósito:** Toma los resultados del `run_script.sh` (`stdout.txt` y `stderr.txt`) y los convierte a un JSON. Este paso es automático al correr `e2e.sh`.
*   **Regla Estricta:** Se DEBE usar la plantilla proporcionada. ¡**CUIDADO**: Solamente tienes permitido modificar la función `parse_test_output`! El resto de la lógica no debe tocarse.

**3. Golden Patch**
*   **Propósito:** La solución "Perfecta" y oficial al problema descrito en el Prompt.
*   **Reglas:**
    *   **NADA de código extra:** Solo debe contener los cambios estrictamente necesarios para resolver lo que pide el prompt.
    *   No siempre se puede usar el parche del PR original (solo si es la solución perfecta). De lo contrario, toca crearlo desde cero.
    *   Debe ser formato "unified diff" con extensión `.patch`.
    *   Debe aplicarse "limpiamente" (cleanly) sobre el commit base en el Dockerfile.
    *   Debe pasar todas las validaciones del script `e2e.sh`.
    *   *(Para tareas R/M)* Debe cumplir con absolutamente todos los criterios de la Rúbrica.

---
*Fin de la Página 5.*

---

## Página 6/10: Refactoring/Maintainability Tasks (Rúbricas)

Las tareas de Refactorización (R/M) exigen la creación de una Rúbrica (Grading Rubric). Esta página marca reglas estrictísimas sobre cómo construirla. 

**Reglas de Oro Básicas:**
*   **Peligro con la IA:** Te darán un generador LLM de rúbricas, pero **PROHIBIDO** dejar el resultado tal cual. Si no lo editas y afinas, te deshabilitan del proyecto.
*   **Cantidad:** Debe tener entre **15 (mínimo) y 20 (máximo)** criterios.
*   **Evaluación Agnóstica:** Debe evaluar *cualquier* solución correcta posible, no solo tu "Golden Patch".

**Reglas de Construcción de Criterios (Rubric Requirements):**
1.  **Rubric-Specific:** NO evalúes cosas que ya validen los scripts (ej. prohibido poner un criterio evaluando si "pasan los test unitarios", porque eso ya lo hace el `run_script`).
2.  **Atomic (Atómico):** 1 criterio = 1 sola idea. No mezcles cosas.
3.  **Self-Contained (Autocontenido):**  El evaluador debe poder calificar el criterio solo leyendo el criterio y el código. Prohibido requerir que el evaluador lea el prompt original u otros scripts para entender qué debe revisar.
4.  **Not Overfitting/Underfitting:** Ni tan específico que rechace soluciones válidas (sobreajustado), ni tan general que acepte basura (subajustado).
5.  **Otras:** Objetivo (Pasa/Falla), Positivo, Preciso, Único y enmarcado para que la respuesta correcta sea "Verdadero".

**Pesos Permitidos (Rubric Weights):**
*   **`5` — Obligatorio (Mandatory):** Requisito central del prompt.
*   **`3` — Importante (Important):** Mejora la respuesta, el prompt lo insinúa fuertemente.
*   **`1` — Deseable (Nice to have):** Opcional, pero necesario para la perfección.
*   ⚠️ **PROHIBIDO ABSOLUTAMENTE:** Usar pesos `2` o `4`.

**Formateo y Puntaje:**
*   **Prohibido:** Usar tiempo pasado, preguntas, o frases que empiecen con "The model...".
*   El **Golden Patch DEBE pasar todos** los criterios con "PASS".

**Categorías de Criterios:**
1. Instruction Following (Seguimiento de instrucciones)
2. Code Correctness (Corrección del código)
3. Code Clarity (Claridad del código)
4. Efficiency (Eficiencia)
5. Risk Security (Seguridad y riesgo)

---
*Fin de la Página 6.*

---

## Página 7/10: Performance Optimization Tasks (PO Tasks)

Si se elige el camino de "**Performance Optimization**", no se entrega Rúbrica, sino estos dos elementos que tienen reglas estrictas:

**1. Reproduction Script**
*   **Propósito:** Medir el rendimiento del código que tiene el "cuello de botella" (bottleneck) real y comprobar cuantitativamente (velocidad, memoria, latencia, etc.) que el Golden Patch lo mejora de forma tangible.
*   **Regla de Oro (Caída de Tarea):** Está **ESTRICTAMENTE PROHIBIDO** crear benchmarks simulados o dummies. Debe correr el código y cuello de botella *real* del repositorio. Debe ser determinista.
*   **Script Requirements:** 
    *   Ejecutar build/compile.
    *   Crear el benchmark y ejecutarlo.
    *   **Importante:** Debe escupir una única métrica parseable con este formato exacto: `"METRIC_VALUE: [valor]"`.

**2. Target Functions (Funciones Objetivo)**
*   **Propósito:** Listar las funciones específicas y reales del código donde está el cuello de botella que el modelo debe optimizar.
*   **Regla Formato:** Deben listarse incluyendo: Ruta completa del archivo + Nombre de la Clase (si aplica) + Nombre de la función.
*   **Ejemplos Requeridos:** 
    *   `src/data/processor.py::DataProcessor::process_batch`
    *   `src/utils/parser.py::parse_large_file`

---
*Fin de la Página 7.*

---

## Página 8/10: Final Steps: Self-Check (End to End Script)

Esta página describe el "Jefe Final" de cada tarea: el script **`e2e.sh`** (End-to-End). Este script junta y evalúa todo lo que hemos construido.

**Regla IMPERDONABLE:** 
Está **PROHIBIDO modificar el script `e2e.sh`**. Si el script falla o tira un error, significa que *nuestros* archivos están mal. Debemos corregir *nuestros* archivos (Dockerfile, scripts, parche) hasta que el `e2e.sh` corra perfecto de principio a fin sin errores y sin ninguna intervención manual.

**Estructura de Carpetas OBLIGATORIA para el E2E:**
Para que el script funcione, debemos organizar los archivos exactamente así:
1.  **Raíz:** Aquí va el script `e2e.sh`.
2.  **Carpeta `app/`:** Debe existir una carpeta llamada **exactamente** `app` en la raíz.
    *   Dentro de `app/` van estos 5 archivos **obligatorios** con esos nombres exactos:
        *   `Dockerfile`
        *   `golden.patch`
        *   `parsing.py`
        *   `reproduction_script.sh` (o script equivalente de repro)
        *   `run_script.sh`

**El Flujo Automático del `e2e.sh` (Lo que hace por detrás):**
1. Construye la imagen Docker.
2. Corre el contenedor.
3. Corre el *reproduction_script* (Rendimiento Pre-parche).
4. Corre el *run_script* (Las pruebas deben pasar).
5. Corre *parsing.py* (Extrae el output y genera **`before.json`**).
6. Aplica automáticamente nuestro *golden patch*.
7. Vuelve a correr el *reproduction_script* (Rendimiento Post-parche).
8. Vuelve a correr el *run_script* (Comprueba que las mismas pruebas sigan pasando, 0 regresiones).
9. Corre *parsing.py* nuevamente (Genera **`after.json`**).

**Archivos Finales de Salida (Entregables Finales):**
*   Para *todas* las tareas el script escupirá localmente: `before.json` y `after.json`.
*   Para tareas de Optimización de Rendimiento (PO), también sacará: `reproduction_before_stdout.txt` y `reproduction_after_stdout.txt`.

El script debe terminar mostrando un mensaje de **"OK"** confirmando que copió los archivos del contenedor a tu máquina local.

---
*Fin de la Página 8.*

---

## Página 9/10: Quick Exam (Resultados)

Examen rápido de 5 preguntas para validar la comprensión del curso.

| # | Pregunta | Respuesta Correcta | Justificación |
|---|----------|---------------------|---------------|
| 1 | ¿Qué artefactos son obligatorios en cada tarea? | `prompt, dockerfile, task type, run_script, golden patch, parsing.py` | Son los "Core 6" definidos en la Página 3. |
| 2 | ¿Un prompt que dice "Use chunked reads with iter(lambda...)" es válido? | **Not compliant** | Página 4: Prohibido dar pistas o la solución directa dentro del prompt. |
| 3 | ¿A qué se fija el Dockerfile para reproducibilidad? | **Specific commit hash (SHA)** | Página 4: Nunca usar branch name, siempre el SHA del commit padre. |
| 4 | ¿Qué campos adicionales requieren las tareas PO? | **reproduction script + target functions** | Páginas 3 y 7: R/M lleva rúbrica, PO lleva script de reproducción + funciones objetivo. |
| 5 | Lista 3 cosas a verificar antes de enviar (abierta) | ✅ Script e2e.sh corre sin errores ni intervención manual generando before/after.json ✅ Dockerfile usa SHA y no tiene COPY de scripts ✅ Prompt sigue la plantilla sin dar soluciones | Score: **1/1** — AI Feedback confirmó respuesta correcta. |

---
*Fin de la Página 9.*

---

## Página 10/10: Hawkins Experiments Screening

*(Pendiente — Examen práctico con preguntas de opción múltiple, verdadero/falso y preguntas basadas en código. Se documentará tras completarlo.)*

---
---

# ANEXOS: Guías de Referencia Completas

---

## ANEXO G1: Especificaciones Completas para la Evaluación de Modelos de Código

### Resumen
Guía maestra que consolida todas las reglas del proyecto Hawkins Experiments.

### 1. Clasificación de Tareas
| Tipo | Descripción | Método de Calificación |
|------|-------------|------------------------|
| **R/M** (Refactoring/Maintainability) | Mejora de estructura, migraciones, estándares | Rúbrica + Unit Tests |
| **PO** (Performance Optimization) | Velocidad, memoria, latencia, eficiencia I/O | Métricas cuantitativas + Unit Tests |

### 2. Entregables Comunes (Core 6)
1. **Prompt** — Descripción del problema orientada al usuario
2. **Dockerfile** — Entorno reproducible
3. **Run Script** (`run_script.sh`) — Ejecuta pruebas unitarias existentes
4. **Parsing File** (`parsing.py`) — Convierte output a JSON
5. **Golden Patch** (`golden.patch`) — Solución perfecta
6. **User-Facing Problem Description** — Resumen del problema

### 3. Entregables Específicos
*   **R/M:** Rúbrica (15-20 criterios, pesos 1/3/5)
*   **PO:** Target Functions + Reproduction Script (`METRIC_VALUE: <número>`)

### 4. Reglas Críticas del Dockerfile
*   ✅ Usar SHA del commit padre (prohibido branch name)
*   ✅ Agnóstico a arquitectura
*   ❌ Prohibido `COPY` para scripts de evaluación
*   ✅ Instalar TODAS las dependencias

### 5. Reglas Críticas del Prompt
*   Autocontenido, sin referencias a PR/scripts/rúbricas
*   Plantilla obligatoria: Context → Problem Statement → Requirements → Success Criteria → Files to Modify → Notes
*   Prohibido dar pistas o soluciones

### 6. Reglas del Golden Patch
*   Formato unified diff (`.patch`)
*   Se aplica limpiamente sobre el commit base
*   Pasa todas las validaciones de `e2e.sh`
*   Para R/M: PASS en todos los criterios de la rúbrica

### 7. Flujo de Validación (e2e.sh)
1. Build Docker → 2. Run container → 3. Repro pre-parche → 4. Run tests → 5. Parse → `before.json` → 6. Apply patch → 7. Repro post-parche → 8. Run tests → 9. Parse → `after.json`

### 8. Mejores Prácticas y Errores Comunes
*   ❌ Métricas no deterministas → Usar seeds fijas, warm-up, mediana
*   ❌ Pistas en el prompt
*   ❌ Branch names en Dockerfile
*   ❌ Benchmarks simulados/dummies en PO

### 9. Checklist Final de Envío
- [ ] URL fuente pública y accesible
- [ ] Dockerfile construye sin errores vía `e2e.sh`
- [ ] Golden Patch se aplica limpiamente y resuelve el 100%
- [ ] `before.json` y `after.json` idénticos (todas PASSED)
- [ ] Script de reproducción (PO) genera `METRIC_VALUE: <número>`
- [ ] Rúbrica (R/M) es objetiva, presente, sin "The model..."

---

## ANEXO G2: Guía del Analizador de Resultados (parsing.py)

### Arquitectura
*   **Entradas:** `stdout.txt` + `stderr.txt`
*   **Salida:** `results.json`
*   **Estructura JSON obligatoria:**
```json
{
  "tests": [
    { "name": "nombre_prueba", "status": "PASSED|FAILED|SKIPPED|ERROR" }
  ]
}
```

### Implementación Requerida
*   Función: `parse_test_output(stdout_content: str, stderr_content: str) -> List[TestResult]`
*   Estado por defecto: Lanza `NotImplementedError` — **hay que implementarla**.
*   Adaptar la lógica según el framework (pytest, junit, go test, cargo test, etc.)

### Ejecución
*   **Directa:** `python3 parsing.py stdout.txt stderr.txt results.json`
*   **Via `run.sh`:** Editar la función `run_all_tests()` con el comando real de tests.
*   **Via Docker:** `docker run --rm -it -v "$PWD:/app" test-parser bash -lc "./run.sh > stdout.txt 2> stderr.txt && python3 parsing.py stdout.txt stderr.txt results.json"`

### Checklist de Despliegue
- [ ] `run.sh` ejecuta pruebas reales (no placeholder)
- [ ] `stdout.txt` y `stderr.txt` generados correctamente
- [ ] `parse_test_output()` implementada
- [ ] `python3 parsing.py` se ejecuta sin errores
- [ ] `results.json` contiene la clave `"tests"` con su lista

---

## ANEXO G3: Guía de Referencia Rápida de Docker

### Estructura del Dockerfile (Secciones No Modificables)
*   `RUN mkdir /app` + `WORKDIR /app` → Directorio de trabajo fijo
*   `ENTRYPOINT ["/bin/bash"]` → Punto de entrada fijo

### Imágenes Base Recomendadas
| Imagen | Tag | Caso de Uso |
|--------|-----|-------------|
| Python | `python:3.10-slim` | Proyectos Python |
| Node.js | `node:20-slim` | Proyectos JS/TS |
| Ubuntu | `ubuntu:22.04` | Configuraciones complejas/multi-lenguaje |

### Comandos Operativos Clave
| Acción | Comando |
|--------|---------|
| Build estándar | `docker build -t hawkins-task:v1 .` |
| Build sin caché | `docker build --no-cache -t hawkins-task:v1 .` |
| Run interactivo | `docker run -it --rm hawkins-task:v1` |
| Montar volumen | `docker run -it --rm -v $(pwd)/patch:/patch hawkins-task:v1` |
| Ejecutar script | `docker run --rm hawkins-task:v1 -c "./validation_script.sh"` |
| Shell en container | `docker exec -it <container_id> /bin/bash` |
| Ver logs | `docker logs <container_id>` |
| Limpiar todo | `docker system prune -a` |

### Dependencias del Sistema (Debian-based)
```bash
apt-get update && apt-get install -y git python3 python3-pip python3-setuptools python-is-python3 && apt-get clean && rm -rf /var/lib/apt/lists/*
```

---

## ANEXO G4: Guía Completa de Rúbricas (Rubric Guidelines)

### Requisitos de la Rúbrica
*   **15 mínimo — 20 máximo** criterios
*   Debe cubrir TODO lo que pide el prompt y que NO ya verifican los scripts
*   Debe evaluar CUALQUIER solución correcta (no solo el Golden Patch)

### Requisitos de cada Criterio
| Propiedad | Regla |
|-----------|-------|
| **Rubric-Specific** | No verificar lo que ya verifican `run_script` o `reproduction_script` |
| **Atomic** | 1 criterio = 1 sola idea |
| **Objective** | PASS o FAIL sin ambigüedad |
| **Correctly Framed** | Respuesta buena = "Yes" / "True" = PASS |
| **Positive** | "Code includes..." no "Code doesn't forget..." |
| **Accurate** | Coincidir exactamente con lo que pide el prompt |
| **Scoped** | Solo evaluar lo pedido en el prompt |
| **Self-Contained** | Evaluable solo con el criterio + el diff del response |
| **Unique** | Sin redundancia entre criterios |
| **Not Over/Underfitting** | Ni demasiado específico ni demasiado genérico |

### Pesos Permitidos
| Peso | Significado |
|------|-------------|
| **5** | Mandatory — Requisito central, imposible aceptar respuesta sin esto |
| **3** | Important — Mejora sustancial, implícitamente esperado |
| **1** | Nice to have — Para respuesta perfecta, no crítico |
| ❌ **2, 4** | **PROHIBIDO** |

### Formateo
*   ❌ Tiempo pasado
*   ❌ Preguntas
*   ❌ Empezar con "The model..."
*   ✅ Presente, positivo, afirmativo

### Scoring
*   **PASS** = Criterio completamente cumplido
*   **FAIL** = No cumplido
*   **Golden Patch DEBE tener todos en PASS**

### Categorías de Criterios
1. **Instruction Following** — Adherencia a instrucciones explícitas
2. **Code Correctness** — Funcionalidad correcta
3. **Code Clarity** — Legibilidad, nombres, estructura
4. **Efficiency** — Concisión, sin redundancia
5. **Risk Security** — Seguridad y contenido apropiado

---
---

# RESUMEN EJECUTIVO DEL ONBOARDING

> **Hawkins Experiments** es un proyecto para construir entornos de evaluación de modelos de IA que modifican código. El ingeniero entrega un paquete de 6 artefactos base (+ extras según tipo R/M o PO) que permiten medir si el modelo resuelve problemas sin romper nada. Todo se valida automáticamente con el script `e2e.sh` que es INTOCABLE. Las reglas más críticas: SHA commits (no branches), sin COPY en Dockerfile, sin pistas en prompts, rúbricas de 15-20 criterios con pesos 1/3/5, y benchmarks reales (no dummies) para PO.

*Informe completado el 20 de marzo de 2026.*
