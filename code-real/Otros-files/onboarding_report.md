# 📋 Informe Completo: Real Coder Intro Course — Onboarding
**Fecha:** 26 de Marzo 2026
**Plataforma:** Outlier AI
**Colaborador:** Pedro Cabeza
**Estado:** ✅ COMPLETADO (20/20 páginas)

---

## 📌 Resumen Ejecutivo
Curso introductorio del proyecto Real Coder de Outlier. Cubre el ciclo completo de desarrollo Greenfield: prompt engineering, pruebas F2P, Golden Patch, Docker, y rúbricas de evaluación. Finaliza con 4 casos de auditoría QC reales.

---

## 📄 Respuestas por Página

### Página 5/20 — Step 1: Prompt Engineering
**Pregunta:** Is Expected Interface Section Always Required? Summarize what the Expected Interface is in your own words. Can it also include miscellaneous functions and optional/non-essential libraries? Why or why not?

**Respuesta usada:**
> The Expected Interface is the contract between the prompt and the test suite. It lists only the public functions, classes, or endpoints that tests will actually call — with exact names, input types, and output formats. No, it should not include helper functions or optional libraries. If you add internal helpers, you over-constrain the model and leak the solution. The interface only covers what the verifier needs to run, nothing more.

---

### Página 7/20 — Step 2: Test Infrastructure (TDD)
**Pregunta:** What is Test Driven Development (TDD)? Why is this important in this project?

**Respuesta usada:**
> TDD means writing the tests before writing the actual code. You first confirm all tests fail on an empty repo, then build the solution until every test passes. In this project it matters because it gives us a clear proof — before.json shows the failure, after.json shows the fix. No guessing if the code works.

---

### Página 8/20 — Step 3: Negative Verification / Overly Specific Tests
**Pregunta A (opción múltiple):** If your re-written prompt did NOT mention error code handling in the backend, can you add a unit test that is testing for error code handling in your app?

**Respuesta:** ✅ **Opción B seleccionada:**
> "No, the backend test cannot be overly specific. The purpose of the backend code is that if we give the prompt to another agent, the agent will be able to PASS the backend code if it implements another solution that also fulfill all requirements in your prompt. The test suite HAS TO tolerate multiple possible solutions."

**Pregunta B (texto abierto):** Imagine you write a prompt, build a golden patch, and write 20 unit tests — all 20 pass only with YOUR exact solution. A different developer writes a completely valid solution but fails 5 of your tests because they used a different algorithm internally. Is this a problem?

**Respuesta usada:**
> Yes, this is a problem. If valid solutions fail your tests just because they took a different approach internally, your tests are overly specific. The project requires tests that check behavior and output, not how the code works inside. To fix this, I should only test inputs and outputs through the expected interface, and avoid asserting anything about internal logic or implementation details.

---

### Página 9/20 — Step 4: Docker & Golden Patch
**Pregunta (opción múltiple):** Should you use the COPY command in Dockerfile?

**Respuesta:** ✅ **Opción B seleccionada:**
> "No, you should add the new dependency needed one by one in the file instead."

---

### Página 11/20 — Validation Script
**Pregunta 1:** After you finish building your golden patch and all your tests pass, you need to run a validation script before submitting. What does this script actually do — what does it run, what files does it produce, and what must those files contain for your submission to be valid?

**Respuesta usada:**
> The validation script runs your tests twice inside Docker — first against an empty codebase to get before.json, then after applying your golden patch to get after.json. A valid result means before.json shows all tests as FAILED and after.json shows all tests as PASSED. If any test passes in the before run or fails in the after run, the submission is invalid.

**Pregunta 2:** Walk through the exact steps to execute it — where does it run, what commands do you use, what can and cannot be changed in the script, and what files do you submit at the end? If a colleague ran validation.sh directly on their laptop without Docker, would that be correct?

**Respuesta usada:**
> You run bash validation.sh from the project root where the app/ folder is. The script builds the Docker image, runs the tests before and after the patch, and outputs 6 files inside app/. You cannot change the script itself, only the APP_DIR variable. No, running it without Docker is wrong — the script depends on Docker to build the image and run the tests in an isolated environment.

---

### Página 12/20 — Step 7: Rubric Creation & Grading
**Pregunta 1:** Can rubrics be super specific towards the golden response? Why or why not?

**Respuesta usada:**
> No. Rubrics cannot be overly specific to the golden patch because they would reject other valid implementations. A rubric must accept any correct solution that meets the prompt requirements, not just the one specific way the golden patch solved it.

**Pregunta 2:** Can rubrics be super broad saying "the website uses the tech stack mentioned in the prompt"? Why or why not?

**Respuesta usada:**
> No. Rubrics that broad are not verifiable or measurable. A good rubric needs to be specific enough that you can clearly say pass or fail when reading the code. Vague criteria like "uses the tech stack" could mean anything and leads to inconsistent grading.

**Pregunta 3 (opción múltiple):** Should rubrics be based on the Task Description (seeded prompt) or your own re-written prompt?

**Respuesta:** ✅ **Opción B seleccionada:**
> "Rubrics should be based on the re-written prompt! The seeded prompt is just a very general description of the problem."

**Pregunta 4 (opción múltiple):** If your golden patch didn't pass any of the rubrics, what should you do?

**Respuesta:** ✅ **Opción B seleccionada:**
> "Go back to fix the Golden Patch (codebase) and re-upload any modified files until the Golden Patch can pass all of the rubric criterion."

---

### Página 17/20 — QC FAIL: Overly Specific Mocks
**Pregunta:** Why is the test cases in this task specifically categorized as overly specific? What would you do to fix it?

**Respuesta usada:**
> The tests are overly specific because they use mock.patch with exact import paths like "src.file_sync.paramiko.SSHClient". If a model imports paramiko a different way, 8 tests fail even though the code works fine. Also, two tests check for things the prompt never asked for — ensuring the remote parent directory exists AND idempotency when closing the connection. To fix it, I would remove the rigid mock.patch paths and test the actual behavior instead, and delete the two tests that go beyond what the prompt requires.

---

### Página 18/20 — QC FAIL: Conflicting Instructions
**Pregunta:** What will you do to improve this task?

**Respuesta usada:**
> First I would fix the conflicting instructions — the prompt says no internet but the readme says NLTK downloads automatically on first run. I would pick one and stick with it: either pre-download the NLTK data in the Dockerfile so no internet is needed at runtime, or remove the no-internet restriction from the prompt. I would also loosen C1 in the rubric since it was flagged as overfitting.

---

### Página 19/20 — QC FAIL: Logical Flaws in Prompt
**Pregunta:** What would you do to fix this task?

**Respuesta usada:**
> The biggest problem is that the prompt asks for two different error messages that AES-256-GCM literally cannot produce separately. I would fix this by adding an HMAC-based key verification step before decryption, so the code can actually tell the difference between a bad password and corrupted data. For C#1, I would rewrite it to explicitly ban all remote API calls and network requests, not just say "no network access" in a vague way. For C#3, I would remove the named constant requirement since the prompt only asks for fixed-size chunks, not how the chunk size is stored in the code.

---

## 🔑 Reglas Clave del Curso

### Metodología F2P
| Concepto | Detalle |
|---|---|
| Evidence A | Tests FALLAN antes del Golden Patch |
| Evidence B | Tests PASAN después del Golden Patch |
| before.json | Todos los tests = FAILED |
| after.json | Todos los tests = PASSED |

### Dockerfile — Reglas Críticas
| Regla | Detalle |
|---|---|
| Base Image | FROM ubuntu:22.04 |
| COPY | ❌ PROHIBIDO |
| Python | ✅ OBLIGATORIO siempre |
| WORKDIR | /app o /workspace |

### Rúbricas — Reglas
| Regla | Detalle |
|---|---|
| Pesos permitidos | Solo 1, 3 o 5 (NUNCA 2 o 4) |
| Mínimo criterios | 5 (recomendado 15-20) |
| Dimensiones | Instruction Following, Code Correctness, Code Quality, Code Clarity, Efficiency |
| Base | Re-written prompt (NO seeded prompt) |

### Anti-Patrones QC Identificados
| Anti-Patrón | Ejemplo | Página |
|---|---|---|
| Tests Overly Specific | Exigir --folder cuando el prompt no lo especifica | P15 |
| Shallow Frontend Testing | Solo buscar strings en vez de interactuar con DOM | P16 |
| Mocks Rígidos | mock.patch con rutas de importación exactas | P17 |
| Instrucciones Conflictivas | "No internet" + "NLTK se descarga automáticamente" | P18 |
| Lógica Imposible | Distinguir errores AES-GCM sin verificador de clave | P19 |

---

## ✅ Conclusión
Onboarding completado satisfactoriamente el 26/03/2026.
Conceptos dominados: F2P, Golden Patch, Dockerfile sin COPY, Rúbricas Agnósticas, Anti-patrones QC.
