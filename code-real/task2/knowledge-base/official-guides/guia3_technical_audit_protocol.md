# Technical Audit Protocol: AI-Generated Software Solution Evaluation (Project 697b72cae052640b8db3e22d)

## 1. Executive Context and System Overview

In high-value software engineering, standardized auditing is the primary mechanism for mitigating the risks of non-deterministic AI generation. To ensure the delivery of production-grade codebases, auditors must rigorously apply the dual-check strategy: Atomic Rubrics for qualitative outcome assessment and Fail-to-Pass (F2P) Integrity for deterministic functional verification. This protocol mandates a systematic evaluation of four core artifacts: the Agent Prompt (System Specification), the Golden Patch (Ground Truth), the Dual-Layer Verification Suite (Automated Tests), and the Multi-dimensional Expert Rubric. Our objective is to validate that each solution adheres to elite engineering standards, executes perfectly within a restricted Ubuntu 22.04 Docker environment, and demonstrates the domain-specific reasoning required for professional freelance-level execution.

## 2. Phase I: Input Architecture and Prompt Validation

The Agent Prompt serves as the immutable System Specification. Any ambiguity or feasibility failure here compromises the entire audit chain. Auditors must treat the prompt as a technical requirement document that must provide sufficient context for an LLM to generate a zero-defect solution.

### Expected Interfaces Evaluation (Active Audit Commands)

Verify the "Expected Interfaces" section. This must document every newly introduced file, class, or function intended for external application or test suite interaction.

*   **Verify Path:** Confirm the absolute or relative file pathing resolves exactly within the intended repository structure.
*   **Confirm Name:** Ensure class, method, and function names are explicitly stated without ambiguity.
*   **Validate Type:** Check the classification (e.g., class, interface, method) for technical accuracy.
*   **Audit Input/Output:** Confirm all parameters, types (e.g., `chunk: GlibcChunk`), and return types (e.g., `Promise<void>`, `None`) are explicitly defined.
*   **Evaluate Description:** Assess if side effects and behaviors are documented with enough detail for a verifier to validate them without referencing the implementation.
*   **Language-Specific Field Validation:** For the following languages, ensure these mandatory fields are present where applicable:
    *   **TypeScript/Java:** Inheritance (`extends`), Implementations (`implements`).
    *   **Go:** Embedding (`embeds`), Interface compliance.
    *   **Python:** Bases (`bases`), Overrides (`overrides`), Decorators (`@dataclass`, `@cached_property`).

### Feasibility, Constraints, and Rendering Logic

*   **Natural vs. Contrived Check:** Determine if constraints reflect real-world requirements. Fail the prompt if constraints are "unrealistically stacked" (e.g., $\ge 3$ arbitrary formatting constraints or sorting logic like "sort by the second letter of the title").
*   **Feasibility Check:** Identify "Impossible Requests" or conflicting instructions that cannot be fulfilled simultaneously.
*   **Internet Connectivity:** Prompts may design internet-dependent solutions (per 03/17 update), but they must not require external APIs, as these render the solution unverifiable.
*   **Markdown Rendering Alert (03/21):** Auditors must account for platform-specific rendering issues. If a field like `"duplicates": "\[testlogin\]"` appears incorrectly as `"duplicates": "testlogin"`, check the "Original JSON" via the Lookup Tool before flagging as a failure.

### The "So What?" Layer (Reasoning Requirement)

Evaluate the reasoning depth. A passing prompt must necessitate domain-specific expertise and synthesis that aligns with the assigned expertise level. If the prompt only requires simple factual lookup or basic definitions without professional-grade reasoning, it results in a Reasoning Requirement Fail.

---

## 3. Phase II: Golden Patch Logic and Performance Optimization

The Golden Patch is the "Ground Truth" implementation. It must be functionally perfect and optimized for the target environment.

**Execution Quality Dimensions**

| Dimension | Audit Command | Fail Condition (1-2) | Not-Fail (3-4) |
| :--- | :--- | :--- | :--- |
| Instruction Following | Cross-check every prompt constraint against the code. | Any explicit instruction missed. | Subjective/minor misses. |
| Compilation | Execute in Ubuntu 22.04 Docker. | Code fails to compile or run. | Warnings or side-effects only. |
| Execution Output | Validate logic and output accuracy (03/16 update). | Functional crashes or material errors. | Insignificant edge cases (those not requiring an emergency fix). |
| Performance | Analyze Big-O efficiency. | Highly inefficient (e.g., O(n^3) when O(n log n) is viable). | Moderately efficient (e.g., O(n^2) instead of O(n log n)). |

**Readability and Design Schema**

*   **Reject Misleading Naming:** Variable names must reflect function. A variable `even_array = [1, 3, 5, 7]` is an automatic readability failure.
*   **Verify Modularity:** Ensure code follows separation of concerns and appropriate abstraction levels.
*   **Documentation:** Reject redundant comments (e.g., `# Main function`). Require docstrings and comments that explain "why," not just "what."

**Terminal Failure Condition:** If the Golden Response fails any single unit test or any single rubric criterion, the audit results in an automatic Score 1-2.

---

## 4. Phase III: Automated Verification Protocol (F2P Suite)

The Fail-to-Pass (F2P) methodology ensures tests are deterministic and coupled to the prompt requirements, not the contributor's specific implementation.

### Script Execution Instructions (real_coder_e2e.sh)

Auditors must follow these steps precisely (refer to comments at the top of the script for environment-specific metadata):

1.  **Build Environment:** Execute the command to build the Docker image specified in the task's Dockerfile.
2.  **Initial Run (Fail):** Run the script against the empty or buggy codebase. Confirm the "Before" JSON result shows failing tests.
3.  **Patch Application:** Apply the Golden Patch.
4.  **Final Run (Pass):** Execute the script again. Confirm the "After" JSON result shows 100% passing tests.
5.  **Determinism Check:** Ensure results are reproducible and do not rely on external state or non-deterministic APIs.

### Test Suite Coverage & Thresholds

*   **Coverage Requirement:** The verifiers (rubric + tests) must address all explicit and implicit requirements.
*   **Failure Threshold (03/17 Update):** A missing coverage gap of > 5% for major backend requirements results in a Major Insufficient Verifier Coverage failure.
*   **Bottleneck Rule (02/27):** A section is "covered" if a representative test exists that, upon failure, indicates a breakdown of all related logic.

### Specificity vs. Breadth Logic (03/25 Update)

| Error Type | Fail Threshold | Definition |
| :--- | :--- | :--- |
| Overly Specific | > 5% | Tests requiring details not found in the prompt (e.g., specific file names/paths not explicitly asked for). |
| Overly Specific/Broad | > 10% | Combined total of overly specific tests AND tests that allow invalid implementations to pass (e.g., static text analysis of an import instead of logic). |

---

## 5. Phase IV: Expert Rubric Schema and Atomicity Analysis

The Expert Rubric provides qualitative assessment. Rubrics must be Self-Contained and Atomic.

### Rubric Quality Definition Matrix

*   **Major Errors:**
    *   **Missing Critical Requirements:** Missing coverage for explicit prompt requests (see "Top 30" rule).
    *   **Non-Self-Contained:** Criteria requiring the auditor to look back at the prompt (e.g., "Fixes the bug" vs "Fixes the bug where the submit button fails").
    *   **Non-Atomic (Bundling):** Grouping unrelated constraints into one item. Note: Closely related features (02/26) or "tech stack" requirements (x, y, z) may be grouped.
    *   **Incorrect Weights:** A 2-level gap in weight (e.g., Weight 1 assigned when Weight 5 is appropriate).
*   **Moderate Errors:**
    *   **Overlap/Redundancy:** Multiple criteria checking the same logic.
    *   **Overfitting/Underfitting:** Criteria that are too rigid or too permissive.
*   **Minor Errors:** Misaligned descriptions or formatting issues.

### Audit Exercise: Atomic Rewrite Guide

Auditors must ensure all criteria are positively framed (evaluating to "Yes/True" for a good response).

*   **Vague/Subjective (Reject):** "The code has good variable names."
*   **Atomic/Measurable (Accept):** "Variable names follow the snake_case convention and reflect the underlying data type, such as user_id_list for an array of integers."

### The "Top 30" Rule (02/22)

*   **If < 30 requirements exist:** All must be covered. Fail if > 3 important explicit criteria are missing.
*   **If >= 30 requirements exist:** At least 30 must be covered. Fail only if > 3 top-impact criteria are missing and replaced by non-critical/minor ones.

---

## 6. Phase V: Final Grading Algorithm and Scoring Logic

We adhere to the "Grade to the Lowest Dimension and Lowest Turn" philosophy. The chain's strength is defined by its weakest link.

### Score Selector Guide

| Score | Classification | Triggering Conditions |
| :--- | :--- | :--- |
| 1-2 | Fail | Missing critical fields; any Major Factual Error; Golden Response fails any verifier; > 5% Major Rubric Errors; > 15% Moderate Rubric Errors. |
| 3-4 | Not-Fail | Minor issues (insignificant edge cases); minor readability concerns; <= 5% Major Rubric Errors; 5-25% Minor Rubric Errors. |
| 5 | Perfect | All instructions followed; 0 compilation errors/warnings; optimized algorithms; < 5% minor rubric issues; 100% coverage. |

### Critical Field Completeness Check

The audit is incomplete and must be failed if any of the following are missing:

*   Dockerfile (Ubuntu 22.04 compatible).
*   Golden Patch.
*   Verification Method (Rubric and/or Test Suite).
*   Execution Results (If testing: `run.sh`, `parsing.py`, and Before/After JSON results).

**Audit Summary:** Synthesize all Major and Moderate errors. Actionable feedback must distinguish between Functional Failures (runtime/logic issues) and Architectural Failures (poor design/non-atomic rubrics). Failure to adhere to language-specific interface requirements or the 03/25 test thresholds mandates an immediate Score 1-2.
