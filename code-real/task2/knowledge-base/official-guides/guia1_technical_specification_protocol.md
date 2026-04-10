# Technical Specification & Execution Protocol: Real Coder Agent Framework

## 1. Core Directives and System Philosophy

This protocol serves as the definitive technical guide for transforming high-level seed tasks into production-ready, verified software solutions. In the domain of AI-assisted engineering, the transition from raw requirement to a "Golden Patch"—a fully functional, legally compliant codebase—requires a strategic move away from conversational interaction toward rigorous architectural engineering. By applying this protocol, engineers ensure that AI agents operate within strict execution boundaries, yielding predictable, reproducible, and verifiable results.

### The Mandatory Determinism Rule

Architecture compliance is predicated on the Determinism Rule. The rewritten prompt must function as a strict state machine, enforcing a single, predictable execution path. Engineers must eliminate all forms of linguistic non-determinism that allow an AI agent to "choose" implementation details.

**Mandatory Phrasing:** Use direct, imperative commands. You MUST use verbs such as "Implement," "Create," or "Generate." Phrases such as "You should" or "If you want" are architectural failures.

### Requirement Philosophy: Preventing Task Overfitting

The hierarchy of requirements distinguishes between functional necessity and technical overreach:

*   **Implementation-Agnostic Verification:** Focus on observable behaviors.
*   **Overly Specific (Critical Fail):** Prompts that dictate internal modularization, private helper functions, or specific library internals cause Task Overfitting. This is a primary cause of system failure as it prevents the agent from adopting standard professional patterns.
*   **Nice to Have (Rubric Only):** Qualitative nuances (UI polish, animations) that are difficult to capture in unit tests are reserved for the Expert Rubric.

### Forbidden Non-Deterministic Terms

The following terms are strictly forbidden in any specification block:

*   "or"
*   "alternatively"
*   "either X or Y"
*   "recommended"
*   "should"
*   "etc."
*   "you can"
*   "something like"
*   "relevant technologies"

Adherence to these linguistic constraints provides the foundation for the structured task workflow.

---

## 2. Phase I: Requirement Synthesis and Interface Design (Steps 0 - 1)

Step 0 and Step 1 constitute the architectural blueprints of the entire process. Precision here dictates the success of automated testing and the integrity of the final "handshake" between the codebase and the test suite.

### Step 0: Discovery

Analyze the seed task to determine scope and constraints:

*   **Task Type:** Identify the domain (e.g., CLI Tool, React Dashboard, Data Pipeline).
*   **Coding Language:** If the source specifies "Any," the engineer MUST select a specific tech stack (e.g., Python/FastAPI, TypeScript/Next.js) to maintain determinism.
*   **Global Constraints:** Enforce the "Short Description" rules: No live data fetching, no external dataset downloads, and local-only execution.

### Step 1a & 1b: Prompt Construction

Construct a structured brief consisting of Title, Description/Context, Tech Stack, and Key Requirements. This document acts as a professional freelance brief for the agent.

#### The "Expected Interface" Protocol

This section is the most critical component of the prompt, defining the public entry points for testing. Mandatory Fields:

*   **Path:** Exact file path in the repository.
*   **Name:** Class, method, function, or API endpoint name.
*   **Type:** Explicitly define the nature (e.g., API Endpoint, React Component, Prisma Model, interface, method).
*   **Input/Output:** Define parameters and return types (e.g., `Promise<void>`, HTTP 200 JSON).
*   **Description:** The observable behavior asserted by the test suite.

#### Linguistic Determinism Audit

Perform a mandatory audit using `promptchecker.md` logic. If any optionality or non-deterministic language remains, the prompt is non-compliant and must be refactored before proceeding to the test generation phase.

---

## 3. Phase II: Test-Driven Development & Environment Setup (Step 2)

The "Fail-to-Pass" (F2P) methodology is the framework's primary validation engine. By proving that tests fail on an empty codebase, we eliminate false positives and ensure the test suite is a reliable judge of implementation.

### Step 2a: Unit Test Generation

Generate tests covering all functional requirements. Tests MUST target the public interfaces defined in Step 1b. Avoid testing private logic to prevent overfitting.

### Step 2b: Dockerization

All code must execute in a strictly isolated Docker environment.

*   **The COPY Prohibition:** You are strictly forbidden from using the `COPY` command in the Dockerfile. Dependencies must be installed via the environment configuration only.
*   **Mandatory Assets:** You must provide `run.sh` (test runner config) and `parsing.py` (implementing `parse_test_output`).

#### Baseline Execution Logic (The before.json Requirement)

The "Baseline" execution validates the environment. Use the following logic to generate the `before.json` manifest:

```bash
# Baseline Execution Protocol
1. Initialize EMPTY codebase.
2. Build Docker Image: docker build -t <image_name> .
3. Run Environment via run.sh + parsing.py.
4. Evaluate Results:
   IF results_json contains "passed":
      CRITICAL FAIL: Fix tests (Tests must fail on empty code).
   ELSE IF results_json contains "error":
      CRITICAL FAIL: Fix environment (Tests must fail, not crash/error).
   ELSE IF all tests are "failed":
      SUCCESS: Generate before.json.
```

---

## 4. Phase III: Implementation and Human-Centric Evaluation (Steps 3 - 4)

While automation handles functionality, qualitative rubrics ensure the solution meets professional freelance standards. This phase balances functional correctness with expert assessment.

### Step 3: Expert Rubric Design

Design rubrics to evaluate the top 30 requirements not covered by unit tests (e.g., UI flow, professional polish).

*   **Scoring Mechanics:** Use mandatory weights of 1, 3, or 5.
*   **Criteria:** Must be atomic, verifiable, and positively phrased (e.g., "The dashboard displays a responsive sidebar" vs "The sidebar isn't broken").

### Step 4: Golden Patch Development

Refine the "Golden Patch" using a coding agent (OpenCode is recommended for cost-effectiveness; Cursor is permitted).

*   **Iterative Refinement:** Debug the solution until it passes 100% of the unit tests (Verification Execution) and satisfies all rubric criteria. The Golden Patch must be a complete, "from-scratch" solution.

---

## 5. Phase IV: Verification, Compliance, and Delivery (Steps 5 - 6)

The final phase prevents structural errors and ensures the package is legally and technically deployable.

### Step 5: Verification Execution

Apply the Golden Patch to the environment. Re-running `run.sh` and `parsing.py` must result in a passed status for all tests, producing the `after.json` file.

### Step 6: Final Validation Script

Execute the validation script to confirm the Fail-to-Pass transition.

#### 🛠 Validation Checklist (Common Errors):

1.  **The (app) Folder Structure:** Ensure the codebase follows the exact naming convention specified in the task workflow.
2.  **The Golden Rule of ZIP Files:** All files must be at the root level of the ZIP. Nested folders (e.g., a folder inside the ZIP containing the code) will result in immediate rejection.
3.  **File Integrity:** Remove all `<<<< HEAD` or `>>>>` branch markers. Use Cursor/OpenCode linter to ensure no leftover Git merge artifacts remain.

#### Visual Asset Compliance

*   **AI/ML Approval:** Visuals (icons, fonts, images) must be 100% commercially free AND approved for use in AI and ML development.
*   **Forbidden Sources:** Do NOT use content from Unsplash.
*   **Safe Sources:** Use Google Fonts, Lucide, Heroicons, or Pexels.
*   **Fallback:** If license status is uncertain, use an image placeholder.

#### Final Delivery Manifest

*   [ ] `codebase.zip`: Full Golden Patch solution (Root level).
*   [ ] `Dockerfile`: Environment setup (No COPY).
*   [ ] `run.sh`: Test runner configuration.
*   [ ] `parsing.py`: Test output parser.
*   [ ] `tests.zip`: Complete unit test suite.

**The Golden Rule:** Submission is successful only if the validation script confirms a 100% transition from `before.json` (FAIL) to `after.json` (PASS) with perfect structural integrity.

---

## Appendix: Implementation Reference

### Interface Mapping Guide

| Language | Specific Interface Fields / Annotations |
| :--- | :--- |
| Python | Bases, Overrides (e.g., `bases: <BaseA>`, `overrides: <Base.method>`), `@dataclass` |
| TypeScript | Inheritance, Implementations (e.g., `extends <Base>`, `implements <Iface>`) |
| Go | Embedding, Implements (e.g., `embeds <TypeA>`, `implements <IfaceA>`) |
| Java | Annotations (e.g., `@Override`, `@Inject`), Inheritance, Interfaces |
| Flutter/Dart | `@override`, Mixins, Interface Implementations |

### Rubric Dimensions

| Dimension | Focus Area |
| :--- | :--- |
| Instruction Following | Strict adherence to the Determinism Rule and all specified constraints. |
| Correctness | Logical accuracy, functional requirements, and functional user flows. |
| Quality | Professional freelance standards, clean code practices, and UI/UX aesthetics. |
| Clarity | Code readability, public interface documentation, and structural logic. |
| Efficiency | Performance optimization, resource management, and execution speed. |
