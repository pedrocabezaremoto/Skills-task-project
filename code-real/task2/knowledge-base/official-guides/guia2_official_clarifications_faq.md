# SKILL: Real Coder — Official Clarifications & Decision Rules (FAQ)

> **Version:** 1.0 | **Source:** Real Coder — Guide 2 (War Room Q&A / Official Clarifications)  
> **Scope:** Authoritative answers to recurring ambiguities in the Real Coder workflow. Use this as the decision reference when Guide 1 leaves a question open.

---

## 1. Validation Script Clarifications

| Question | Authoritative Answer |
|---|---|
| Can I modify the `verification.sh` / `validation.sh` script? | **Yes — one line only:** the main `APP_DIR` path. No other changes allowed. |
| What do I submit for the verification script output? | Upload and paste `before.json` + `after.json`. For legacy taxonomy tasks, copy-paste their content until the taxonomy is updated. |
| Is WSL required for Windows users? | No. WSL makes Docker easier on Windows but is not mandatory. PowerShell or Git Bash are valid alternatives. |
| Can extra dependencies be added to the Dockerfile? | **Yes.** You may add `apt` or `pip` packages as needed. Structure must remain unchanged. |

---

## 2. Coverage — Definitive Rules

### 2.1 What Must Be Covered

All explicit requirements from the **re-written prompt** must be covered by the combined set of unit tests + rubrics. Nothing may be missed.

### 2.2 Coverage Assignment Matrix

| Requirement Type | Primary Coverage Method | Notes |
|---|---|---|
| Backend functional logic | **Unit tests (F2P)** | Mandatory baseline. |
| Frontend UI/UX behavior | **Rubrics** | Unit tests for frontend are optional but allowed. |
| Anything unit tests cannot verify | **Rubrics** | Required fallback — no gaps allowed. |
| Expected Interface entries | **Unit tests** | Every interface entry must have at least one corresponding test. |
| UX quality (subjective) | **Rubrics** | If prompt is technically satisfied but UX is poor, rubrics must account for this. |

### 2.3 Overlap Policy

- Requirements **may be covered by both** unit tests and rubrics — overlap is acceptable.
- Requirements that are **missed by both** is a critical error.

---

## 3. F2P Test Suite — Clarifications

| Question | Authoritative Answer |
|---|---|
| How is the test suite executed? | Complete suite runs against **empty codebase** first (all FAIL), then against the **Golden Patch** (all PASS). Same test files, same suite, two runs. |
| What is acceptable baseline behavior? | Tests must **FAIL** — not crash, not error out. A test that errors on an empty codebase indicates a setup problem, not a valid failure state. |
| Can I add test cases beyond what the prompt mentions? | Yes. Tests and rubrics are **external evaluation mechanisms**, not part of the prompt itself. Adding more tests post-build is valid. |
| Where do all test cases go? | All tests go into the single `/tests` folder. No separate paths needed for task-described tests vs. F2P tests. |
| Do I need frontend unit tests? | **No.** Backend unit tests are the baseline. Frontend is covered by rubrics. You *may* write frontend tests, but rubrics must cover what they cannot. |

---

## 4. Tech Stack & Framework Decisions

| Question | Authoritative Answer |
|---|---|
| Am I limited to the tech stack in the task description? | If the prompt specifies a stack, **follow it**. If no stack is specified, choose any stack that correctly solves the problem. |
| Which frameworks are allowed? (Next.js, Nuxt, React, Flask, Django, etc.) | Any framework specified in the prompt. If unspecified, you choose — prioritize solving the problem correctly. |
| Which model/mode should I use in Cursor? | Any model, any agent mode. **Claude 4.6 is the recommended model.** |
| Can I write a random budget or timeline if not in the task description? | **No.** Budget and timeline are metadata sourced from real freelance platforms. Never invent them. They are not part of the re-written prompt. |

---

## 5. Rubric Authoring — Clarifications

### 5.1 Scope

- Rubrics must be based on the **re-written prompt**, covering every single explicit requirement.
- Requirements already covered by unit tests **may also appear in rubrics** — but this should be rare. Avoid systematic duplication.
- The re-written prompt **must be fully closed-ended** — no ambiguity, no open-ended requirements.

### 5.2 Grouping Rules

| Scenario | Rule |
|---|---|
| **General requirements** (e.g., full tech stack) | Grouping into one rubric criterion is acceptable. Example: *"The solution uses Vue 3, Vite, Pinia, Express, SQLite, Sequelize, Vitest, and Supertest."* |
| **Specific / non-general features** | **Must be separated** into individual atomic rubric criteria. |

### 5.3 Rubric Quality Dimensions (QC Doc Reference)

Every rubric criterion is evaluated against these eight dimensions. Violations on any dimension result in a rubric `FAIL`:

| Dimension | Failure Trigger |
|---|---|
| **Atomicity** | Criterion bundles more than one independent requirement. |
| **Self-contained** | Criterion depends on external context not present in the prompt or code. |
| **Accuracy** | Criterion is factually incorrect or objectively wrong given the prompt. |
| **Overlap / Redundancy** | Criterion duplicates another rubric item or a unit test (unless rare and justified). |
| **Labels / Annotations** | Criterion is miscategorized by dimension or weight. |
| **Criteria Objectively Wrong** | Criterion would penalize a correct implementation. |
| **Counterproductive Criteria** | Criterion incentivizes a worse implementation. |
| **Irrelevant Criteria** | Criterion has no basis in the re-written prompt. |

---

## 6. Prohibited Content & Asset Rules

### 6.1 What to Avoid in Solutions

| Category | Rule |
|---|---|
| **API keys / external setup** | Must be avoided. Solutions must run without any external configuration. |
| **Copyrighted icons or UI assets** | Prohibited. Use Lucide/Heroicons, Google Fonts, or Pexels only. |
| **Disallowed libraries** | Any library explicitly prohibited in the prompt is disallowed. |
| **Image inputs** | Challenging to test reliably — best avoided unless explicitly required. |
| **Cloned website UI/layout** | Tasks requiring UI cloning of a specific website should be **flagged to QMs** — not implemented. |
| **Unsplash** | ❌ Prohibited entirely. |

### 6.2 UX Failures

If the prompt requirements are technically satisfied but the user experience is poor, this does **not** cause an automatic failure. UX quality must be evaluated and enforced through **rubric criteria**, not through unit tests.

---

## 7. Quick Decision Tree

```
Is the requirement backend logic?
├── YES → Cover with unit test (F2P).
└── NO → Is it frontend behavior or qualitative?
    ├── YES → Cover with rubric.
    │         Optionally also write a frontend unit test.
    └── MAYBE BOTH → Cover with rubric (mandatory) + unit test (optional).

Is the requirement in the Expected Interface?
└── YES → Must have at least one unit test covering it.

Does the rubric criterion group multiple things?
├── General requirement (tech stack, runtime version) → Grouping OK.
└── Specific feature or behavior → Separate into individual criteria.

Is a requirement missed by both unit tests AND rubrics?
└── YES → Critical gap — fix before submission.
```

---

## 8. Summary of Non-Negotiables

1. `validation.sh` — only the `APP_DIR` path may be changed. Nothing else.
2. Tests on an empty codebase must **FAIL** (not crash, not error).
3. Every Expected Interface entry must be covered by at least one unit test.
4. Every explicit prompt requirement must be covered by tests + rubrics combined.
5. Budget and timeline are never invented — only included when sourced from a real freelance platform.
6. The re-written prompt must be fully closed-ended with no open-ended requirements.
7. No external API keys or setup steps — all solutions must run offline and locally.
8. Cloned UI/layout tasks must be flagged to QMs — never implemented.
