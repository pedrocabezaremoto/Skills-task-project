# SKILL: Real Coder Task Execution Framework

> **Version:** 1.0 | **Source:** Real Coder (mattock_name) Guidelines — Guide 1  
> **Scope:** End-to-end workflow for generating high-quality, verifiable freelance-style software solutions from a blank slate.

---

## 1. Mission

Transform a raw freelance task description into:
1. A structured, implementation-ready **agent prompt** (Golden Prompt).
2. A functional, from-scratch **Golden Patch** (solution codebase).
3. A dual-layer **verification suite**: automated F2P unit tests + expert rubric.

All solutions must be locally runnable, externally verifiable, and free of live data fetching or copyrighted assets.

---

## 2. Visual Asset Compliance (Hard Rules)

| Rule | Detail |
|---|---|
| **Commercially free only** | Icons, images, illustrations, fonts must be 100% free for commercial + AI/ML use. |
| **No paid/attributed licenses** | No assets requiring payment or attribution (unless explicitly specified). |
| **Approved sources** | Google Fonts, Lucide/Heroicons, Pexels. |
| **Unsplash** | ❌ Strictly prohibited. |
| **Uncertain assets** | Use image placeholders in code instead. |

---

## 3. Task Workflow (Ordered Steps)

### STEP 0 — Understand Task Requirements

Review all four seed sections before writing anything:

| Section | Purpose |
|---|---|
| **Task Type** | Defines the application domain (web platform, CLI tool, data pipeline, etc.). |
| **Task Coding Language** | Constrains the tech stack. If `Any`, you must explicitly choose one in the prompt. |
| **Short Description** | Global constraints: professional UI standards, no live data fetching, local datasets only, rubric limits. |
| **Task Description** | The client-style brief — the primary source of requirements. |

**Transformation goal:** Convert the vague client brief into specific, unambiguous, implementation-ready requirements with no contradictions, no guessing, and full logical consistency.

---

### STEP 1a — Prompt Generation (Golden Prompt)

**Mandatory sections** (Pattern A — most common):

```
# Title
## Description / Context
## Tech Stack
## Key Requirements (with ### subsections)
## Expected Interface (with ### per function/class/endpoint)
## Current State
## Required Implementation
## Deliverables
```

**Rules:**
- If `Task Coding Language` is `Any`, **never** write `ANY` in the prompt. Choose a specific stack.
- Do **not** include unit test or rubric instructions inside the prompt.
- Always include `## Current State` = `"Empty repository with test files only."` for greenfield builds.
- Every dataset must be bundled locally. No external downloads.

#### Expected Interface — Required Format (per entry)

```
- Path: <exact file path>
- Name: <Class.method | function | API Endpoint | React Component>
- Type: <class | function | method | API Endpoint | interface | ...>
- Input: <parameters and types>
- Output: <return type or HTTP response>
- Description: <observable behavior asserted by tests>
```

**Language-specific additions (as applicable):**
- Python: `Bases`, `Overrides`, `Annotations / Decorators`
- TypeScript/Java: `Inheritance`, `Implements`
- Go: `Embedding`, `Implements`

**Rules for Expected Interface:**
- Cover every file, function, or class that an **external test suite** will interact with.
- Do **not** expose internal helpers, private methods, or third-party library fields.
- There must be **one Expected Interface entry per test case**.
- The interface must be **implementation-agnostic** — it must not dictate internal architecture.
- Simple tasks: 4–6 entries. Complex tasks: 20–40+ entries.
- Expected Interface makes up **30–70% of total prompt content**.

---

### STEP 1b — Prompt Requirements Classification

Split all prompt requirements into two categories:

| Category | Coverage Method |
|---|---|
| **Unit-testable** | F2P automated tests (non-overly-specific) |
| **Non-unit-testable** | Expert rubrics (top 30 most important, not covered by tests) |

**Frontend/Fullstack tasks:**
- Use **Instruction Following (IF) rubrics** to cover all UI design requirements.
- If you don't want to write many UI rubrics, do **not** include UI design asks in the prompt.
- Regardless of prompt scope, the website must meet **professional freelance UI standards**.

---

### STEP 2a — F2P Test Case Verification (Fail-to-Pass)

**TDD approach — tests are written before the Golden Patch.**

Process:
1. Use a coding agent (OpenCode / Cursor + Claude 4.6) to generate unit tests covering all backend-testable requirements.
2. Audit tests for over-specificity (see STEP 2b system prompt).
3. **Baseline Execution (Before):** Run `run.sh` + `parsing.py` on an empty codebase.  
   → Goal: `before.json` must show **every test as FAILED** (not ERRORED).
4. Build the Golden Patch.
5. **Verification Execution (After):** Re-run both scripts.  
   → Goal: `after.json` must show **every test as PASSED**.

**Over-specificity rule:** A test is overly specific if it would fail on a valid alternative implementation of the same prompt. Overly specific tests must be rewritten or removed.

---

### STEP 2b — Over-Specificity Audit (System Prompt)

Feed the following to a coding agent to audit unit tests:

```
You are the Lead QA Compliance Auditor. Flag any test that:
- Asserts implementation details not stated in the prompt ("Ghost Requirements").
- Uses mock.patch on internal module paths that would break with a different valid import style ("Implementation Trap").
- Adds best practices (e.g., idempotency) not required by the prompt.
- Uses interface elements not defined in the Expected Interface section.

Return a JSON audit result with:
- audit_result: PASS | FAIL
- compliance_metrics: { total_tests, overly_specific_count, requirements_covered_pct }
- violation_details: [ { test_name, issue, requirement_source, severity } ]
- coverage_gaps: [ { requirement, issue } ]
```

---

### STEP 3a — Expert Rubric

**Scope:** Top 30 most important requirements from the prompt **not coverable by unit tests**.  
**Minimum:** 5 criteria. **Maximum:** 30 criteria.

#### Rubric Weights

| Weight | Label | Meaning |
|---|---|---|
| **5** | Mandatory | Core requirement; unacceptable without it. |
| **3** | Important | Makes solution substantially better; acceptable without it if all else passes. |
| **1** | Nice to have | Needed for a perfect response, but not a blocker. |

> ⚠️ Only weights **1, 3, or 5** are allowed. Never use 2 or 4.

#### Rubric Dimensions

| Dimension | Focus |
|---|---|
| Instruction Following | Adherence to explicit prompt directives (format, constraints, required elements). |
| Code Correctness | Correct results and behavior for all inputs, including edge cases. |
| Code Quality | Robustness, maintainability, idiomatic patterns, no fragile design. |
| Code Clarity | Readable, well-named, organized, properly formatted. |
| Code Efficiency | Concise, no redundant steps, avoids unnecessary intermediate structures. |

#### Rubric Criteria Guidelines

- **Atomic:** Each criterion checks exactly one idea.
- **Verifiable:** Auditable directly from code.
- **Positive phrasing:** "Code includes X" — never "Code doesn't forget X".
- **Self-contained:** Must be evaluable without external context.
- **Non-overlapping:** Must not duplicate existing unit tests or other rubric items.

**Scoring per criterion:**
- `PASS` → Briefly state how the criterion is met.
- `FAIL` → Name the specific blocking issue.

---

### STEP 3b — Coverage Audit (System Prompt)

Feed the following to a coding agent to verify full requirement coverage:

```
Evaluate the quality and coverage of rubrics and tests against the prompt requirements.
For each test: assess relevance, over-specificity, overlap, and framing quality.
For each rubric: assess atomicity, self-containment, relevance, over-specificity, overlap, framing.
Report overall coverage and list any missing tests or rubrics.
```

> ⚠️ These system prompts are guides only — not a source of truth. You are responsible for correctness.

---

### STEP 4 — Build the Golden Patch

1. Feed your finalized prompt to the coding agent (Claude 4.6 recommended).
2. Verify the agent's output satisfies all prompt requirements.
3. Fix and refine until the solution is complete — this is your **Golden Patch**.
4. Ensure no copyrighted images or datasets are used (see Visual Asset Compliance).
5. Third-party libraries and helper functions are allowed if they don't contradict the prompt.

---

### STEP 5 — Run the Test Suite Again

1. Apply the Golden Patch to the codebase.
2. Re-run `run.sh` + `parsing.py`.
3. `after.json` must show **all tests PASSED**.
4. Rate every rubric criterion against your Golden Patch — all must PASS.
5. If any test fails: fix the Golden Patch and re-run.
6. If any test has issues: fix the test → re-run baseline → re-run with Golden Patch → resubmit screenshots.

---

### STEP 6 — Validation Script

**Purpose:** Confirm the task is deterministic and reproducible across any environment.

**Required `/app` directory structure:**

```
/app/
├── Dockerfile
├── tests.zip
├── codebase.zip
├── run.sh
└── parsing.py
```

**Execution:**
- Run `validation.sh` in `/app`.
- `before.json` → all tests **FAILED**.
- `after.json` → all tests **PASSED**.

**You may only modify:**
- The main root file path in `validation.sh` (default: `/app`).

---

## 4. Docker Environment

### Dockerfile Template (Base)

```dockerfile
FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    git python3 python3-pip python3-setuptools python-is-python3 unzip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
RUN git init \
    && git config --global user.email "agent@example.com" \
    && git config --global user.name "Agent" \
    && echo "# Workspace" > README.md \
    && git add README.md \
    && git commit -m "Initial commit"

RUN mkdir -p /eval_assets
CMD ["/bin/bash"]
```

- Only modify the **System Dependencies** section.
- Never use `COPY` to inject solution files.
- Add additional pip/apt packages as needed.

### run.sh Template

```bash
#!/bin/bash
### COMMON SETUP; DO NOT MODIFY ###
set -e
# --- CONFIGURE THIS SECTION ---
run_all_tests() {
  echo "Running all tests..."
  # TODO: Replace with your test runner command
}
# --- END CONFIGURATION SECTION ---
### COMMON EXECUTION; DO NOT MODIFY ###
run_all_tests
```

### parsing.py Template (Key Function)

```python
def parse_test_output(stdout_content: str, stderr_content: str) -> List[TestResult]:
    """
    Parse the test runner output and return a list of TestResult objects.
    Each TestResult has: name (str), status (TestStatus: PASSED | FAILED | SKIPPED | ERROR)
    """
    raise NotImplementedError('Implement the test output parsing logic')
```

> ⚠️ Only modify the section between `### Implement the parsing logic below ###` and `### Implement the parsing logic above ###`.

---

## 5. ZIP File Rules

| File | Internal Structure | How to Zip |
|---|---|---|
| `tests.zip` | Contains the `tests/` folder. | Zip the folder itself. |
| `codebase.zip` | Contains files directly (no parent folder). | Zip the files *inside* the folder. |

> ❌ Never create nested zips. `codebase.zip` must be: `codebase.zip → files` (not `codebase.zip → codebase/ → files`).

---

## 6. Deliverables Checklist

### After STEP 2 (Baseline)
- [ ] Screenshot of `run.sh` with all tests **FAILED**.
- [ ] `results.json` from `parsing.py` showing all tests **FAILED**.
- [ ] All unit test code pasted into the platform.

### After STEP 5 (Verification)
- [ ] Screenshot of `run.sh` with all tests **PASSED**.
- [ ] `results.json` from `parsing.py` showing all tests **PASSED**.
- [ ] All unit test code pasted (post-Golden Patch version).
- [ ] Most updated `tests.zip`.

### After STEP 6 (Validation)
- [ ] `before.json` uploaded + content pasted.
- [ ] `after.json` uploaded + content pasted.
- [ ] `codebase.zip` (finalized Golden Patch).
- [ ] Finalized `Dockerfile`.
- [ ] Finalized `parsing.py`.
- [ ] Finalized `run.sh`.
- [ ] Package requirements file (`requirements.txt` / `package.json`), or `does_not_apply.txt`.
- [ ] Screenshot of file timestamps for all uploaded files.

---

## 7. Recommended Tooling

| Tool | Purpose | Notes |
|---|---|---|
| **OpenCode** (`opencode.ai`) | Primary coding agent | Free; link to your LLM account. Recommended over Cursor. |
| **Cursor** | Alternative coding agent | $20/mo reimbursed after first qualified task. |
| **Claude 4.6** | Recommended model | Use with Cursor agent or OpenCode. |

---

## 8. Key Anti-Patterns to Avoid

| Anti-Pattern | Consequence |
|---|---|
| Writing `ANY` as tech stack in the prompt | Invalid prompt — choose a specific stack. |
| Including test/rubric instructions in the prompt | Corrupts the agent prompt structure. |
| Tests that ERRORED instead of FAILED on baseline | Fails validation — fix test setup. |
| Overly specific tests (mock internal paths, exact error strings) | Penalizes valid alternative solutions. |
| Nested zip files | Breaks the validation script. |
| Using Unsplash assets | Copyright violation. |
| External dataset downloads | Not allowed — bundle data locally. |
| Modifying `DO NOT MODIFY` sections in `run.sh` / `parsing.py` | Breaks evaluation pipeline. |
| `codebase.zip` with a parent folder inside | Validation script failure. |

---

## 9. Coverage Requirements Summary

| Requirement Type | Coverage Method |
|---|---|
| Backend functional logic | Unit tests (F2P) |
| Frontend UI/UX behavior | Rubrics |
| Architecture and design patterns | Rubrics |
| Expected Interface entries | Unit tests (mandatory) |
| Qualitative code properties | Rubrics |

> Tests + Rubrics combined must achieve **100% coverage** of all explicit prompt requirements.
