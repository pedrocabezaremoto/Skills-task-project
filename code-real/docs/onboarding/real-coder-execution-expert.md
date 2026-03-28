# 🛠️ Skill: Real Coder Execution Expert (Outlier)

**Description:** This skill provides the architectural framework, technical constraints, and quality control (QC) protocols required to execute "Greenfield" software tasks for the Real Coder project on Outlier. It ensures 100% adherence to Fail-to-Pass (F2P) methodology and Docker isolation standards.

---

## 🎯 Core Mission
Transform ambiguous freelance-style task descriptions into high-quality, verified software solutions using a dual-verification layer:
1. **Functional (F2P):** Automated tests that prove the fix.
2. **Qualitative (Rubrics):** Expert evaluation of logic, efficiency, and clarity.

---

## 🔄 The 7-Step Workflow

### 1. Prompt Engineering (The Contract)
- **Constraint:** Rewrite the seeded prompt into a professional Markdown specification.
- **Expected Interface:** Every public component MUST have: `Path`, `Name`, `Type`, `Input`, `Output`, and `Description`.
- **Complexity Rule:** If the model (Cursor) solves it instantly, I must increase the logical complexity of the prompt.

### 2. Test Infrastructure
- **`run.sh`:** Must execute the full test suite.
- **`parsing.py`:** Must convert test logs into a standard JSON with `PASSED`, `FAILED`, `SKIPPED`, or `ERROR`.

### 3. Negative Verification (Evidence A)
- **Requirement:** I must run tests against an empty `/app` directory. 
- **Valid Result:** 100% of tests must FAIL. This generates `before.json`.

### 4. The Build
- **Dockerfile:** 
  - Base: `ubuntu:22.04`.
  - **HARD RULE:** No `COPY` or `ADD` commands for project files.
  - Mandatory: Install `python3`, `pip`, and `setuptools` regardless of the project language.
- **Golden Patch:** Implement the complete solution from scratch satisfying every requirement in the prompt.

### 5. Positive Verification (Evidence B)
- **Requirement:** Run tests against the Golden Patch.
- **Valid Result:** 100% of tests must PASS. This generates `after.json`.

### 6. Validation Script
- **Command:** `bash validation.sh`.
- **Constraint:** I only modify the `APP_DIR` variable. Any other change to the script logic is a hard fail.

### 7. Rubric & Grading
- **Dimensions:** Instruction Following, Correctness, Quality, Clarity, Efficiency.
- **Weighting System:** Only use weights **1, 3, or 5**. (2 and 4 are strictly prohibited).
- **Atomicity:** Each criterion must evaluate only one specific requirement.

---

## ⚠️ Anti-Bane & QC Protocols (Internal Knowledge)

- **Implementation Agnostic:** I never write tests that enforce internal function names or specific algorithms unless the prompt explicitly demands them.
- **Flexible Mocking:** Avoid rigid paths like `mock.patch("src.file_sync.paramiko.SSHClient")`. Use broader mocks to allow different import styles.
- **No Internet at Runtime:** If the prompt requires "No Internet," I must pre-download all dependencies (like NLTK data) in the Dockerfile.
- **Agnostic Rubrics:** I ensure rubrics accept any valid solution, not just my Golden Patch (avoiding Overfitting).
- **Self-Contained Criteria:** Every rubric item must be understandable without reading the prompt (e.g., instead of "Fix the bug," use "Fix the bug where the submit button was disabled").

---

## 🛠️ Essential Commands
- **Build Image:** `docker build -t real-coder-task .`
- **Run Container:** `docker run -it real-coder-task:latest /bin/bash`
- **Execute Suite:** `bash run.sh`
- **Validation:** `bash validation.sh`

---

## 📑 Report: Real Coder Intro Course Mastery
**Author:** Pedro "Peterhead" Cabeza  
**Role:** Senior Technical Consultant / Systems Engineer  
**Stack:** Python, Docker, TDD, Prompt Engineering  
**Project Context:** Greenfield Software Development (Outlier AI)

### 🛠️ Section 1: The 7-Step Execution Framework
Para que una tarea de Real Coder sea aprobada, debe seguir este ciclo de vida sin desviaciones:
1. **Prompt Engineering:** Transformar el "Seeded Prompt" en una especificación técnica (Markdown). Debe incluir el Expected Interface.
2. **Test Infrastructure:** Crear `run.sh` (ejecutor) y `parsing.py` (traductor a JSON).
3. **Negative Verification (Evidence A):** Correr los tests en una carpeta vacía. Resultado esperado: 100% FAILED.
4. **The Build:** Escribir el Dockerfile (sin COPY) y desarrollar el Golden Patch (la solución).
5. **Positive Verification (Evidence B):** Correr los tests contra el código. Resultado esperado: 100% PASSED.
6. **Validation Script:** Ejecutar `validation.sh` para empaquetar los resultados. No se toca la lógica, solo `APP_DIR`.
7. **Rubric & Grading:** Crear 15-20 criterios de evaluación (pesos 1, 3, 5) y calificar el Golden Patch.

### 📄 Section 2: Technical Q&A (The "Anti-Bane" Guide)
| Tema | Pregunta Clave | Respuesta Senior (Peterhead) |
| :--- | :--- | :--- |
| **Interface** | ¿Es siempre necesaria? | Yes. It's the contract between the prompt and tests. It covers every public file, function, and class. |
| **TDD** | ¿Qué es y por qué importa? | I use TDD as the foundation of F2P. Writing tests first proves they can catch errors (Evidence A) and verify the fix (Evidence B). |
| **Docker** | ¿Se debe usar COPY? | No. I must install dependencies one by one in the Dockerfile. Using COPY breaks the clean environment check. |
| **Validation** | ¿Cómo se ejecuta? | I run `bash validation.sh` from the host machine. I only modify the `APP_DIR` variable to ensure a clean Docker lifecycle. |
| **Rubrics** | ¿Pueden ser específicas? | No. That's overfitting. I write rubrics to be implementation-agnostic so any valid code can pass, not just mine. |

### 📹 Section 3: Video Intelligence Summary
Basado en los documentos de entrenamiento (vid1, vid2, vid3):
- **Video 1 & 2: Arquitectura del Prompt**
  - **Contrato Técnico:** El prompt no es una charla, es un README. Si el modelo lo resuelve muy fácil en Cursor, subo la complejidad.
  - **Campos Obligatorios:** Cada interfaz debe tener: Path, Name, Type, Input, Output, Description.
- **Video 3: Infraestructura y Docker**
  - **Python es Mandatorio:** Aunque el proyecto sea en otro lenguaje, el contenedor debe tener `python3-pip` y `setuptools` para que los scripts de Outlier funcionen.
  - **The "Blank Slate":** QC verifica que tus tests no tengan "falsos positivos". Si un test pasa sin código, la tarea es rechazada.

### ⚠️ Section 4: QC Audit Patterns (How to avoid failing)
Analizando los errores de las páginas 14 a 19, estas son las reglas de oro:
- **Mocks Flexibles:** Nunca uses rutas de importación exactas en los mocks (ej. `src.file_sync.paramiko`). Usa mocks que acepten diferentes estilos de importación.
- **Alineación Estricta:** Si el Prompt dice "No internet", el código no puede tener `nltk.download()`. La data debe estar en el Dockerfile.
- **Lógica Realista:** No pidas cosas imposibles (como distinguir errores de clave vs. corrupción en AES-GCM sin un HMAC previo).
- **Pesos de Rúbrica:**
  - **5 (Mandatorio):** La app no sirve sin esto.
  - **3 (Importante):** Mejora mucho la calidad.
  - **1 (Deseable):** Estética o detalles menores.
  - **Prohibido:** Usar pesos 2 o 4.
