# Autonomous Technical Quality Assurance & Verification Protocol (ATQAV-P)

## 1. Operational Framework & Executive Logic

The implementation of a standardized verification protocol is a strategic imperative for maintaining high-velocity, high-quality code generation within agentic workflows. As LLMs transition from assistant roles to autonomous contributors, the ATQAV-P bridges the gap between manual oversight and deterministic verification. This framework ensures that every "Golden Patch" is not merely functional but strictly compliant with 100% of prompt requirements, establishing a rigorous defense against regression and task drift.

```javascript
INIT Protocol_v2.1 {
    SET TARGET_MODELS = ["Claude 4.6 (Preferred)", "Any Agent/Model"];
    SET PRIMARY_OBJECTIVE = "100% Prompt Requirement Coverage";
    SET TECH_STACK = GET_FROM_PROMPT() || "Lead_Architect_Favorite_Stack";
    SET VERIFICATION_SUCCESS = (Unit_Tests_Pass && Rubric_Criteria_Met);
    
    VALIDATE System_Readiness();
}
```

The efficacy of this ecosystem relies on the utilization of fully "closed-ended" prompts. Deterministic testing outcomes are only achievable when ambiguity is eliminated from the task description. By enforcing a closed-ended structure, we facilitate objective validation, ensuring that both human auditors and AI agents achieve identical, repeatable results across the verification lifecycle.

With system parameters initialized, we proceed to the specific execution logic of verification scripts and state persistence.

---

## 2. Verification Script & Data Handling Logic

Reliable verification requires a balance between script flexibility and data persistence. JSON structures serve as the definitive state-capture mechanism, ensuring that codebase transformations are documented with high fidelity from the initial state to the final solution.

**Verification Logic & Data Persistence Procedure:**

*   **Path Configuration Logic:**
    *   IF the script requires environment-specific pathing to execute:
    *   THEN modify the main application path. **RESTRICTION:** This modification is strictly limited to the single relevant line of code. Do not alter surrounding script logic.
*   **Legacy Data Handling (Old Taxonomy):**
    *   IF processing an "Old Taxonomy Task":
    *   THEN execute the Data Persistence Procedure: Manually copy-paste the `before.json` and `after.json` data into the designated fields to maintain state history.
*   **Future-State Data Handling (New Taxonomy):**
    *   IF processing a "New Taxonomy Task":
    *   THEN handle `before.json` and `after.json` as dedicated file attachments.
*   **Recovery Logic (Execution Failure):**
    *   IF a pathing error or script failure occurs:
    *   THEN re-validate the single-line path modification. Ensure the pointer accurately reflects the entry point of the built solution.

Pathing errors remain the primary driver of execution failure. Adherence to the single-line modification rule prevents the introduction of secondary bugs during verification. Successful script execution is the prerequisite for the Fail-to-Pass (F2P) testing methodology.

---

## 3. Fail-to-Pass (F2P) Testing Methodology

The Fail-to-Pass (F2P) test serves as the ultimate validator of the "Golden Patch." It eliminates false positives by proving that the test suite is sensitive enough to detect the absence of the solution. A test suite that passes against an empty or unpatched codebase is inherently flawed and must be rejected.

**F2P Algorithmic Process:**

1.  **Phase I: Empty Code Base (Baseline Validation)**
    *   **Execution:** Run the complete test suite against the environment prior to applying the solution.
    *   **Expected Outcome:** FAIL. Every test case must return a failure status.
    *   **Constraint:** The program must not crash. The suite must handle the missing logic gracefully and return explicit failure reports.
2.  **Phase II: Golden Patch (Solution Validation)**
    *   **Execution:** Apply the patch and run the identical test suite.
    *   **Expected Outcome:** PASS. All test cases must return a success status.

**Test Organization & Volume:** The verification environment requires a total of 85 test cases (comprising 80 F2P baseline cases and 5 specific task-driven cases). These must be centralized within the `/tests` folder directory. If the complexity of the built solution demands additional validation beyond the 5-10 cases mentioned in the prompt, architects are authorized to add supplemental cases to ensure complete functional coverage.

These unit tests provide the functional baseline, which must be synthesized with rubric-based qualitative checks.

---

## 4. Dual-Layer Coverage Logic: Unit Tests vs. Rubrics

Our "Total Coverage" philosophy utilizes unit tests and rubrics as overlapping safety nets. While unit tests provide automated validation of functional logic, rubrics ensure that visual, interactive, and explicit prompt requirements are met without exception.

**Coverage Decision Matrix**

| Dimension | Coverage Method | Constraint / Condition |
| :--- | :--- | :--- |
| Backend Logic | Unit Test (Priority) | Mandatory baseline; must cover all functional logic. |
| Frontend UI/UX | Rubric (Priority) | Primary for visual elements; secondary if unit tests are feasible. |
| Expected Interface | Unit Test + Rubric | Interface naming and structure must be validated by both layers. |
| Naming Conventions | Conditional | **Mandatory Constraint:** Solutions must not fail for file/variable naming differences unless the prompt explicitly defines them. |

The "Most Updated Coverage Dimension" dictates that requirements can be overlapped by tests and rubrics, but under no circumstances can a requirement be omitted. Rubrics must be derived directly from the rewritten prompt, capturing every explicit requirement—especially those untestable by automated scripts.

---

## 5. Environment, Tech Stack, and Dependency Management

Environmental parity is non-negotiable for script portability. The verification environment must remain lean to ensure it can be reproduced across different agentic nodes without manual setup overhead.

**Environment & Compliance Rules:**

*   [ ] **Docker Implementation:** Docker is the primary standard. Ensure all processes are self-contained within the container (WSL is not required if Docker is present).
*   [ ] **Dependency Management:** Permission is granted to add extra dependencies to the Dockerfile if required to support the solution logic.
*   [ ] **Tech Stack Hierarchy:** Strictly follow the tech stack specified in the prompt. If no stack is defined, utilize a "Favorite Stack" that provides the most efficient solution.
*   [x] **Forbidden Elements:**
    *   **No API Keys:** Avoid any library or service requiring external authentication or setup-heavy keys.
    *   **No Image Inputs:** Currently restricted due to technical challenge constraints.
    *   **No Copyrighted Icons:** Use open-source or generic placeholders only.
    *   **Meta-Data Exclusion:** Do not include budget or timeline data in rewritten prompts or rubrics; these are meta-data only.
*   [x] **Task Flagging:** If a task requires the cloning of an existing website UI or layout, it must be flagged immediately to PT.

Avoiding "setup-heavy" environments ensures that the protocol remains portable and ready for final Quality Control audit.

---

## 6. QC Dimensional Analysis & Final Validation

The final Quality Control gate focuses on the technical truth of the solution and the human-readability of the rubrics. A technically "correct" solution that provides a poor user experience is a failure of the protocol.

**QC Quality Gates:**

*   **Atomicity:** Each rubric criterion must be single-purpose, checking one specific requirement in isolation.
*   **Self-contained:** Criteria must be intelligible without requiring the auditor to search for external context.
*   **Accuracy:** Every claim in the rubric and test suite must represent a verifiable technical truth.
*   **Overlap/Redundancy:** Minimize repetitive checks to ensure audit efficiency.
*   **UX Alignment:** Rubrics must account for the end-user experience. Even if a solution is technically prompt-compliant, it must be rejected if the UX is poor or objectively hindered.
*   **Tech Stack Organization:**
    *   **General Requirements:** You may group general tech stack requirements (e.g., "Uses Vue 3, Vite, and Pinia") into a single, comma-separated rubric criterion.
    *   **Functional Features:** Non-general features and specific functional requirements must remain isolated as atomic criteria.

This protocol serves as the definitive guide for autonomous technical verification, ensuring that every submission meets the highest standards of architectural integrity and task adherence.
