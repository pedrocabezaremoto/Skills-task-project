# 📄 Final Technical Report: Mattock/Outlier Onboarding Certification

Este informe resume los estándares técnicos fundamentales requeridos para el proyecto Mattock/Real Coder.

### 🏗️ 1. Infrastructure & Docker Standards
*   **Base Image:** Mandated `ubuntu:22.04` for all execution environments.
*   **Isolation Policy:** Strictly prohibited the use of `COPY` or `ADD` inside the `Dockerfile`. Files must be injected via dynamic volumes to ensure environment determinism.
*   **Root Structure:** The `/app` directory must contain exactly five files: `codebase.zip`, `tests.zip`, `Dockerfile`, `run.sh`, and `parsing.py`.
*   **Immutability:** The only permissible modification in the validation scripts is the `APP_DIR` path variable.

### 📦 2. Packaging & Validation Logic
*   **Fail-to-Pass (F2P) Protocol:** All tasks must generate a `before.json` with 100% failure rate (Baseline) and an `after.json` with 100% pass rate.
*   **ZIP Hierarchy:**
    *   `codebase.zip`: Flat structure (files at root).
    *   `tests.zip`: Nested structure (starts with `tests/` folder).
*   **Line Endings:** All shell scripts (`run.sh`) must use **LF (Unix)** format to avoid execution crashes within the container.

### 🔍 3. Quality & Coverage Auditing
*   **System Prompts:** Utilized `prompt.md`, `rubrics.md`, and `prompt_requirements.md` as automated linters.
*   **Total Coverage Audit:** Every requirement in the prompt must be mapped to either a unit test (Functional) or a rubric criterion (Qualitative).
*   **Homeless Requirements:** Identified and eliminated requirements that lacked verification layers to ensure 100% audit scores.
*   **Human Oversight:** Expert review of "Overflags" to distinguish between model hallucinations and genuine architectural gaps.

---

### 🛠️ Explicación Interna (Post-Mortem Técnico)

Peterhead, ya eres un experto en el flujo. Aquí lo que realmente aprendimos:

1.  **Agnosticismo de Tests:** Los tests deben validar el "qué" (el contrato del prompt) y no el "cómo" (tu código específico). El QC rechaza tests acoplados a tu implementación técnica.
2.  **La Trampa del /app:** La plataforma es alérgica a los archivos basura. Mantener ese `/app` limpio con solo los 5 archivos base es lo que separa a un Junior de un Senior en Outlier.
3.  **Lógica de Cobertura:** Si algo no se puede testear con código (ej. diseño o arquitectura), **debe** estar en la rúbrica. No puede haber ni una sola coma del prompt que no sea evaluada. No permitas "Homeless Requirements".
