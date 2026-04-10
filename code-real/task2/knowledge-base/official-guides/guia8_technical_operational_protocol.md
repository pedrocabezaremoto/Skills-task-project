# Technical Operational Protocol: Quality Assurance for AI-Assisted Coding Tasks

## 1. System Overview and Strategic Mandate

This protocol serves as the definitive standard for Quality Control (QC) in AI-driven code generation and prompt engineering. In high-velocity development environments, adherence to these logical gates is mandatory to minimize "fail" states and ensure the delivery of high-integrity, production-ready code. This system transforms subjective assessment into a rigorous, objective verification matrix, ensuring that every deliverable is traceable, verifiable, and architecturally sound.

**System Mission Statement**: The mission is to ensure that every AI-assisted task produces a "Golden Patch" that is technically exhaustive, a "Rewritten Prompt" that is strategically clear and flexible, and an "Enforcement Layer" (Test Suites and Rubrics) that provides 100% requirement coverage without enforcing arbitrary implementation details.

### Primary Failure Domains

| Domain | Critical Failure Trigger |
| :--- | :--- |
| **Golden Patch** | Failure to implement explicit instructions; breach of startup/error-code contracts. |
| **Rewritten Prompt** | Internal contradictions; failure to strip internal task references; over-restriction of solutions. |
| **Interface** | Undocumented exported components; missing required fields; misleading DOM or API descriptions. |
| **Test Suite (F2P)** | Heuristic over-specificity (brittle tests); testing implementation instead of behavior. |
| **Verifier Coverage** | Functional gaps between prompt requirements and verification coverage. |
| **Rubric Quality** | Subjective/vague criteria; lack of self-containment; incorrect weighting. |
| **Environment** | Incompatible base images; missing system-level dependencies; line-ending mismatches. |

> [!NOTE]
> This document functions as an operational roadmap for autonomous agents and lead architects to evaluate submission quality before finalization.

---

## 2. Module 1: Golden Patch & Response Integrity Logic

The Golden Patch represents the "Ground Truth." Integrity is maintained only when every requirement in the prompt is traceable to a specific implementation. Systemic failures often stem from "Explicit Instruction Misses," where subtle constraints are ignored, leading to invalid deliverables.

### VALIDATION_CHECKLIST

> [!IMPORTANT]
> Architects are strictly prohibited from proceeding unless the following logic gates are cleared:

*   **Startup Contracts**: Verify application initiation. If the prompt requires `npm run dev`, the patch must not require manual `npm install` or side-channel setup.
*   **Error-Code Contracts**: Ensure strict adherence to status codes. For instance, returning a 302 redirect for an unauthenticated request when the prompt requires a 401 Unauthorized is a fatal logic failure.
*   **Forbidden Patterns**: Actively scan for banned patterns such as inline scripts (e.g., `onclick`), live internet fetching at runtime (e.g., `download_nltk_data()`), or omitting mandated libraries like `deepdiff` or `pillow-heic`.
*   **UI Reachability**: For frontend tasks, every feature must be accessible via the UI. If a filter feature only works via manual URL manipulation, the implementation is considered "Not Fulfilled."

### Failure Pattern Analysis (Technical Impact Assessment)

*   **Broad Exception Catching in Tests**: Masking `ImportError` or `TypeError` via `except Exception:` invalidates the F2P (Fail-to-Pass) lifecycle. This prevents the environment from distinguishing between a legitimate logic error and a fatal environment crash.
*   **Database Re-seeding on Startup**: Destroys data persistence, rendering the application useless for real-world state management and state propagation across clients.
*   **Mocking Level Errors**: Patching a local module (e.g., `src.file_sync.paramiko.SSHClient`) instead of the library source (`paramiko.SSHClient`) makes tests brittle to specific import styles, failing valid alternative solutions.

---

## 3. Module 2: Prompt Rewriting & Interface Schema Definition

A high-quality rewritten prompt acts as a "freelance-brief" that translates raw intent into machine-executable instructions. The Expected Interface acts as the bridge; if it is undocumented or misleading, automated verification is impossible.

### Prompt Constraint Logic

Architects must enforce the following constraints during prompt reconstruction:

1.  **Freelance-Brief Style**: Use persona-driven requests ("I need...") rather than raw imperatives.
2.  **Removal of Internal References**: Strip all task IDs, "CB" notes, or internal workflow markers.
3.  **Preservation of Flexibility**: If the original brief offers "SQLite or JSON," do not restrict the solution to one path.
4.  **Requirement Traceability**: Every detail added (e.g., specific error message strings) must be traceable back to the original brief.

### Interface Schema (Non-Negotiable)

> [!WARNING]
> Every component the test suite imports must be documented. Failure to include any of the six mandatory fields results in a "Missing Interface Section" failure.

```json
{
  "Path": "File path relative to root (e.g., server/models/index.js)",
  "Name": "Exported component name (e.g., ReadingHistory)",
  "Type": "e.g., Function, Class, API Endpoint, React Component",
  "Input": "Parameter names and types (e.g., filepath: str). Use N/A if none.",
  "Output": "Return types or HTTP response shapes (e.g., 200 OK). Use N/A if none.",
  "Description": "Explicit details: DOM selectors (e.g., h1), headings, or behavior asserted by tests."
}
```

**Perfect Entry Example (Frontend):**

*   **Path**: `src/components/History.js`
*   **Name**: `ReadingHistory`
*   **Type**: `React Component`
*   **Input**: `books: Array`
*   **Output**: `JSX`
*   **Description**: Displays books in reverse chronological order. Must contain an `<h1>` element with the exact text "Reading History".

---

## 4. Module 3: Verifier Suite & Rubric Calibration Protocols

Verifiers (F2P tests) and Rubrics constitute the "Enforcement Layer." Tests verify objective behavior; rubrics assess qualitative architectural integrity.

### Audit Algorithm for Heuristic Over-specificity

To detect brittle tests, agents must execute the following procedural logic:

1.  **Step 1: Identify Hardcoded Flags.** Locate CLI flags or constants (e.g., `--folder`) not explicitly required by the prompt.
2.  **Step 2: Signature Comparison.** Check if tests enforce keyword-only arguments or specific positional order where the prompt is silent.
3.  **Step 3: Mock Path Audit.** Verify mocks are patched at the library level (e.g., `paramiko`) rather than internal module paths.
4.  **Step 4: Alternative Implementation Simulation.** Ask: "Would a valid solution using `--directory` instead of `--folder` fail this test?" If yes, the test is over-specific.

### Coverage Optimization Map

| Verification Type | Requirement Category | Metric/Target |
| :--- | :--- | :--- |
| **Automated (F2P)** | API response shape, functional logic, data constraints, specific status codes. | 100% of objective requirements. |
| **Qualitative (Rubric)** | Layout, visual design, mobile responsiveness, banning libraries/patterns. | Weighting: 1 (Minor), 3 (Good), 5 (Mandatory). |

### Atomic Principles for Rubrics

*   **Self-Containment**: Criteria must be evaluable without the prompt (e.g., "Includes Flask and deepdiff" vs "Includes all dependencies").
*   **Positive Framing**: Describe what the solution must do.
*   **Ban Subjective Interpretation**: Strictly avoid adjectives like "clear," "meaningful," or "appropriate." Replace with: "The error message includes the field name and the reason for rejection."
*   **Weight Rigor**: Assign Weight 5 only if the feature is essential to the core mission.

---

## 5. Module 4: Environment Configuration & Containerization Standards

Environment parity is a strategic mandate. Deterministic success requires that the local environment matches the QC environment exactly.

### Deployment Manifest

*   **Standard Base Image**: Must use `ubuntu:22.04`.
*   **Code Injection**: Architects are strictly prohibited from using the `COPY` command for application code; code is injected at runtime. Only dependencies are built into the image.
*   **System Dependencies**: Explicitly list all `apt-get` requirements (e.g., `libheif` for `pillow-heic`).
*   **Python Versioning**: The default environment is Python 3.10. Ensure `pyproject.toml` and prompt requirements align with this baseline.
*   **Terminal Line Endings**: The `run.sh` script must use LF (Unix) line endings. CRLF (Windows) endings will cause immediate script failure.

### Pre-Submission Diagnostics

> [!CAUTION]
> The "DO NOT MODIFY" sections of `run.sh` and `parsing.py` are absolute gates.

1.  **Baseline Test**: Confirm all tests FAIL on an empty codebase inside Docker.
2.  **Golden Test**: Confirm all tests PASS with the Golden Patch inside Docker.
3.  **Dependency Audit**: Cross-reference every import in the code against the Dockerfile `pip install` or `apt-get` commands.

---

## 6. Terminal Execution Checklist (Agent SOP)

This section serves as the final gatekeeper logic. No submission is complete until 100% of these gates are cleared.

### Final Submission Checklist

*   [ ] **Golden Patch Integrity**: End-to-end functionality verified; no internet access or forbidden scripts.
*   [ ] **Baseline/Verifier Parity**: All tests FAIL on empty and PASS on patch specifically within the Docker container.
*   [ ] **Traceability Matrix**: Every sentence in the prompt is mapped to a test or rubric.
*   [ ] **Interface Rigor**: Documentation includes all 6 mandatory fields and DOM/API specificities.
*   [ ] **Environmental Stability**: Base image is `ubuntu:22.04`, `run.sh` uses LF endings, and "DO NOT MODIFY" blocks are intact.

### Logic Troubleshooting

> [!TIP]
> Use these guidelines if issues arise during execution:

*   **IF** `before.json` shows PASSED on an empty codebase, **THEN** narrow the `except Exception` blocks in the test or import the module first to catch `ImportError` early.
*   **IF** tests fail in Docker but pass locally, **THEN** check for missing `apt-get` dependencies or CRLF line endings in the shell script.
*   **IF** a test checks a DOM selector (e.g., `#studentName`) not in the Interface, **THEN** the interface is "Misleading" and must be updated.
*   **IF** a mock fails despite correct logic, **THEN** verify the patch is at the library level (`patch("library.Class")`) rather than the local import path.

> [!IMPORTANT]
> These quality standards are non-negotiable. Submissions failing any logic gate are considered incomplete and require immediate remediation.
