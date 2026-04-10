# TECHNICAL PROTOCOL: REAL CODER TASK REVIEW & VALIDATION (VERSION 1.0)

## 1. SYSTEM_INITIALIZATION: Environment Configuration

As a Senior Technical Systems Architect, your role as a reviewer is the "first line of defense" in our quality control pipeline. Establishing a standardized local environment is not merely a procedural step; it is a strategic mandate to ensure reproducibility and prevent "errored" states—failures caused by environmental drift rather than code defects. By maintaining a deterministic sandbox, you ensure that every quality standard is measurable, verifiable, and strictly aligned with the project's data specifications.

The setup requires a precise hierarchical directory structure to support our Fail-to-Pass (F2P) validation logic. Configure your environment as follows:

*   **Root Directory**: (e.g., `/review_task_ID`)
    *   `/app`: Primary workspace for automated execution scripts.
        *   **Scripts**: `run.sh`, `parsing.py` *(Note: Ensure template alignment; some tasks may utilize `parsing.sh`)*.
        *   **Configs**: `Dockerfile` (Targeting Ubuntu 22.04).
        *   **Archives**: `codebase.zip` (Original source), `tests.zip` (Unit test suite).
        *   **Dependencies**: `requirements.txt` or `package.json` (Environment-specific).
    *   `/without_solution`: Baseline validation directory.
        *   Contains the extracted test suite and base repository files, excluding the Golden Patch.
    *   `/with_solution`: Verification validation directory.
        *   Contains the extracted test suite, base repository, and the final Golden Patch implementation.

> [!IMPORTANT]
> The architectural distinction between the `without_solution` and `with_solution` directories is the core of F2P logic. This separation allows us to verify that the base repository fails the requirements as intended (the "Fail" state) and that the Golden Patch provides the necessary and sufficient resolution (the "Pass" state). Once the structure is validated, proceed to automated evaluation.

---

## 2. EXECUTION_LAYER: Tara Eval & Baseline Analysis

The Tara Eval tool serves as a diagnostic guide to accelerate the identification of guideline violations. However, it is a diagnostic aid, not a source of truth. 

> [!WARNING]
> Architects must understand a critical limitation: Tara Eval only flags requirements extracted from the "Expected Interface" section of the prompt. It frequently ignores the "Description," "Key Requirements," and "Deliverables" sections. You are commanded to manually extract requirements from these ignored sections to ensure 100% verification coverage.

Use the following parameters to analyze the Task Info:

| Parameter | Type | Logic Definition |
| :--- | :--- | :--- |
| **Metadata** | Identifiers | Tracks unique Task ID and Attempt ID for session auditing. |
| **Prompt/Rubrics** | Logic Definitions | Contains the re-written prompt and weighted criteria for manual scoring. |
| **Unit Test** | Automation Results | Summarizes the names and PASSED/FAILED status of automated checks. |

The "Eval" section acts as a logic gate for task integrity. The system performs a comparison between `before.json` and `after.json`:

1.  **Baseline Verification (`before.json`)**: You must verify that the base repository results in a FAILED state. If the output is ERRORED, it indicates a broken environment or script configuration, not a valid baseline failure.
2.  **Patch Verification (`after.json`)**: You must verify that the application of the Golden Patch results in a 100% pass rate.

These automated results define the scope of the manual "Fix Task" phase, highlighting where the attempter failed to meet the functional or architectural specifications.

---

## 3. LOGIC_REFINEMENT: Prompt & Unit Test Optimization

Instruction Completeness and Clarity are the foundations of a solvable task. A prompt must be implementation-agnostic yet technically exhaustive, ensuring the model is not forced into "contrived" patterns or left guessing at edge-case handling.

### Prompt Review Technical Checklist:

*   **Impossible Asks**: Ensure all requirements are enforceable within the Ubuntu 22.04 container.
*   **Unnatural Requirements**: Remove instructions that force non-standard coding patterns.
*   **Constraint Integrity**: Confirm explicit definitions for filtering, status handling, and ordering.
*   **Prompt Linter**: Utilize the `promptchecker.md` system prompt in your IDE to identify missing requirements or contradictions.

### Unit Test Validation Protocol:

1.  **Baseline Failure**: Confirm the `without_solution` setup results in failure for every test associated with the intended fix.
2.  **Verification Success**: Confirm the `with_solution` setup achieves a 100% pass rate.
3.  **Assertion Correctness**: Audit test expectations to ensure they validate behavior, not just side effects.
4.  **Audit Tooling**: Execute the `overly_specific_check.md` linter to identify and remove fragile tests that rely on hardcoded values or implementation-specific helper functions.

> [!TIP]
> The synergy between the prompt and the test suite ensures that the model is verified against functional outcomes without penalizing valid, alternative implementation paths.

---

## 4. QUALITY_CONTROL: Rubric Atomic-Mapping & Golden Patch Integrity

Rubrics capture the qualitative traits—such as UI/UX standards—that unit tests cannot verify. Rubrics must remain implementation-agnostic, focusing on the result rather than the specific method used to achieve it.

### Rubric Standards:

*   **Atomicity**: One requirement per criterion. Do not "bundle" unrelated constraints.
*   **Self-Containment**: Reviewers must be able to evaluate the item using only the response and the rubric—no external facts required.
*   **Weighting**: Strict adherence to the 1, 3, or 5 scale (Nice to have, Important, Mandatory).
*   **Framing**: All criteria must be positively phrased. Evaluate for "True" or "Yes." For example, "Does not use X" must be reframed as "Successfully avoids X" to ensure scoring consistency.

### Golden Patch Technical Audit: 

The Golden Patch is our "ground truth." It must demonstrate modularity and proper abstraction. 

> [!CAUTION]
> Architects must enforce strict asset compliance: the use of Unsplash assets is strictly prohibited. All visual assets must be 100% commercially free. This audit ensures 100% requirement coverage and functional excellence.

---

## 5. COVERAGE_AUDIT: Requirement Satisfaction Matrix

The Dual-Layer Coverage Approach (Tests + Rubrics) is strategically designed to eliminate "orphan" requirements—instructions in the prompt that are never actually verified. Every functional, technical, and constraint-based requirement must map to at least one validation layer.

### Step-by-Step Audit Guide:

1.  **Initialize Audit**: Create a `coverage_audit.md` file using the specialized system prompt.
2.  **Execution**: Load the re-written prompt, tests, Golden Patch, and rubrics into your IDE and run the audit.
3.  **Matrix Interpretation**: Analyze the "Requirements Coverage Matrix."
    *   **PASS**: The requirement is verified by at least one layer.
    *   **FAIL**: The requirement is "MISSING" and requires an additional test or rubric.
4.  **Verification Split**: Backend logic should be covered by unit tests; frontend and qualitative traits (UI/UX) must be covered by rubrics.

Identifying these gaps prevents manual oversight and ensures that the model response is fully verified before the task is finalized.

---

## 6. DEPLOYMENT_VAL: Final Validation & Scoring Logic

The final validation ensures results are deterministic within the clean Ubuntu 22.04 Docker environment. This is the final gate for submission.

### Final Environment Checklist:

*   [ ] **ZIP Structure**: `codebase.zip` contains files at the root (no parent folder); `tests.zip` contains the `tests/` folder at the root.
*   [ ] **Timestamp Accuracy**: Artifact "last edited" timestamps must match the final session timestamps to ensure the absolute latest versions are submitted.
*   [ ] **Script Alignment**: `run.sh` and `parsing.py` are correctly configured and aligned with implementation logic.
*   [ ] **F2P Integrity**: `before.json` is 100% FAILED (not errored); `after.json` is 100% PASSED.

### The Lowest Dimension Rule: 
To maintain systemic integrity, we employ a "Weakest Link" scoring model. A single low score in any individual dimension (e.g., Instruction Following) dictates the entire task’s final grade. A failure in instruction following constitutes a total failure of model reliability, regardless of code correctness.

> [!NOTE]
> **Operational Loop Summary**: Follow this linear loop for every task: 
> `INIT (Environment Setup)` -> `ANALYZE (Tara Eval & Manual Gap Extraction)` -> `FIX (Prompt, Test, & Rubric Refinement)` -> `AUDIT (Coverage Matrix Verification)` -> `SUBMIT (Final Docker Validation)`.
