# SKILL: Real Coder — QC Grading Spec & Evaluation Framework

> **Version:** 1.0 | **Source:** Real Coder — Guide 3 (QC Spec / Grading Rubrics — Project ID: 697b72cae052640b8db3e22d)  
> **Scope:** Official Quality Control evaluation framework. Use this as the authoritative reference for understanding how your submissions are scored, what causes failures, and how to write rubrics that pass auditor review.

---

## 1. What Auditors Evaluate (The Four Artifacts)

Every submission is audited across four distinct artifacts:

| Artifact | Description |
|---|---|
| **Agent Prompt** | Structured, rewritten prompt that guides an AI agent to solve the task from scratch. |
| **Golden Patch** | Fully functional, high-quality reference implementation. |
| **F2P Test Suite** | Automated Fail-to-Pass unit tests (fail on empty codebase, pass on Golden Patch). |
| **Expert Rubric** | Multi-dimensional criteria set (minimum 5) rating the Golden Patch against the prompt. |

**Two valid verification paths** (at least one required, both may be used):
- **Atomic Rubrics** — 5+ criteria across five dimensions.
- **F2P Integrity** — Tests fail on empty/buggy codebase, pass after Golden Patch is applied.

> All code must execute within the provided Docker container (Ubuntu 22.04) using standardized `run.sh` and `parsing.py` scripts.

---

## 2. Audit Workflow (6 Steps)

| Step | Action | Key Check |
|---|---|---|
| **1** | Review task instructions | Understand the original task scope. |
| **2** | Evaluate the Prompt | Rigorous translation of task description; includes Expected Interface section. |
| **3** | Evaluate the Golden Patch | Logic correctness; Dockerfile technical accuracy. |
| **4** | Evaluate F2P Tests | `before.json` all FAILED; `after.json` all PASSED; both deterministic. |
| **5** | Evaluate the Rubric | 5+ criteria; atomic; verifiable. |
| **6** | Tally final score | Apply 1–5 scale per grading rules; select error categories if applicable. |

> ⚠️ **Do NOT edit tasks or make any selection on the "Task Action" field.**

---

## 3. General Grading Rules (1–5 Scale)

### 3.1 Scale Logic

| Rule | Detail |
|---|---|
| **Grade to the lowest dimension** | If any single dimension scores a 2, the entire task is a 2. |
| **Grade to the lowest turn** | If any turn scores a 2, the task is a 2. |
| **1–2 = Fail** | Any criterion meeting a Fail condition makes the task a fail. |
| **3–4 = Not-Fail** | Task does not fail but has issues; any 3–4 dimension keeps the task at 3–4 max. |
| **5 = Perfect** | ALL dimensions must score a 5 for the task to receive a 5. |

### 3.2 Choosing Between Adjacent Scores

| Choice | Rule |
|---|---|
| **1 vs 2** | Select 1 if the contributor put little to no effort. |
| **3 vs 4** | Use judgment on how seriously the minor issue affects overall task quality. |

### 3.3 Priority Rule

Prompt instructions and task instructions **always take precedence** over other dimensions. Example: if the task explicitly instructs the contributor to include spelling mistakes, those mistakes are not marked as failures.

---

## 4. Grading Dimensions — Prompt

### 4.1 Reasoning Requirement

| Score | Condition |
|---|---|
| **Fail (1–2)** | Prompt only requires factual lookup or definition — no reasoning involved. |
| **Not-Fail (3–4)** | Prompt loosely or trivially includes domain reasoning. |
| **Pass (5)** | Prompt requires reasoning aligned with the assigned domain/expertise level, beyond simple recall. |

### 4.2 Prompt Constraints

| Score | Condition |
|---|---|
| **Fail (1–2)** | Constraints are contrived, unrealistic, clearly stacked (3+ formatting constraints), or overly basic (e.g., "explain it to a child"). |
| **Not-Fail (3–4)** | Constraints are somewhat subjective but believable for a real user. |
| **Pass (5)** | All constraints feel natural for a user asking this to a chatbot. |

### 4.3 Contrived / Unnatural Prompts

| Score | Condition |
|---|---|
| **Fail (1–2)** | Prompt is contrived or unnatural (riddles intentionally detail-laden are excluded). |
| **Not-Fail (3–4)** | Prompt is somewhat contrived or unnatural. |
| **Pass (5)** | Prompt is neither contrived nor unnatural. |

### 4.4 Truthfulness

| Score | Condition |
|---|---|
| **Fail (1–2)** | 1+ major factual errors, or 2+ minor factual errors. |
| **Not-Fail (3–4)** | 1 minor factual error. |
| **Pass (5)** | No factual errors, no misleading statements. |

### 4.5 Feasibility

| Score | Condition |
|---|---|
| **Fail (1–2)** | Request is impractical (cannot be answered in one LLM response), impossible, or contains conflicting instructions. |
| **Not-Fail (3–4)** | Multiple requests, verging on impractical, but core request is fulfillable with minor concessions. |
| **Pass (5)** | Fully actionable by an LLM; no conflicting instructions. |

### 4.6 Expected Interface — Full Specification

**This section is mandatory in every rewritten prompt.**

**Required fields per interface entry:**

```
- Path:        [Exact file path as it appears in the intended structure]
- Name:        [Class.method or function name]
- Type:        [class | method | function | interface | API Endpoint | React Component | ...]
- Input:       [Parameters and types]
- Output:      [Return type or HTTP response]
- Description: [Observable side effects or behavior asserted by tests]
```

**Language-specific additions (as applicable):**

| Language | Field |
|---|---|
| TypeScript / Java | `Inheritance: extends <Base>; implements <IfaceA, IfaceB>` |
| Go | `Embedding / Implements: embeds <TypeA>; implements <IfaceA>` |
| Python | `Bases / Overrides: bases: <BaseA>; overrides: <Base.method>` |
| Any | `Annotations / Decorators: @Override, @dataclass, @cached_property` |

**Fail conditions for Expected Interface:**

| Error | Description |
|---|---|
| **[Fail - Missing Interface Section]** | Section is entirely absent, or any required field is missing for a documented interface. |
| **[Fail - Undocumented Interface]** | A publicly accessible file, function, or class that an external test suite or app interacts with is not documented. Do NOT reference the Golden Patch — it is only one valid solution. |
| **[Fail - Misleading Interface Description]** | Description is incomplete or insufficient such that a fully correct implementation would still fail a verifier. |
| **[Fail - Invalid Interface]** | Documents a helper function or third-party library field that external applications do not need to interact with directly. *(Added 03/12)* |

> ✅ **Pass:** Interface section is present, all required fields are complete, all applicable language-specific fields are included, and every publicly accessible / verifier-tested component is documented without ambiguity.

---

## 5. Grading Dimensions — Response (Golden Patch)

### 5.1 Instruction Following / Fulfillment

| Score | Condition |
|---|---|
| **Fail (1–2)** | 1+ explicit instructions not followed; response does not fully answer the question. |
| **Not-Fail (3–4)** | Subjectively misses some aspects of fully answering. |
| **Pass (5)** | All explicit instructions clearly followed; response fully answers the question. |

### 5.2 Compilation

| Score | Condition |
|---|---|
| **Fail (1–2)** | Code does not compile or throws runtime errors. |
| **Not-Fail (3–4)** | Code runs but has warnings or side effects. |
| **Pass (5)** | Code runs perfectly without errors or warnings. |

### 5.3 Execution Output

| Score | Condition |
|---|---|
| **Fail (1–2)** | Output is irrelevant, incorrect, incomplete, or fails on edge cases. |
| **Pass (5)** | Output perfectly aligns with all prompt requirements, including edge cases. |

### 5.4 Performance

| Score | Condition |
|---|---|
| **Fail (1–2)** | Highly inefficient implementation with clear room for significant improvement (e.g., O(n³) when O(n log n) is feasible). |
| **Not-Fail (3–4)** | Moderately efficient; room for further optimization (e.g., O(n²) when O(n log n) is possible). |
| **Pass (5)** | Well-optimized; uses efficient algorithms and data structures throughout. |

### 5.5 Readability

| Score | Condition |
|---|---|
| **Fail (1–2)** | Difficult to read in >2 areas due to poor formatting; or variable/class/method names are misleading (e.g., `even_array = [1, 3, 5, 7]`). |
| **Not-Fail (3–4)** | Formattable in ≤2 areas; names don't follow language naming conventions but aren't misleading. |
| **Pass (5)** | Well-organized, consistent formatting; all names are meaningful and reflective of purpose. |

### 5.6 Code Design

| Score | Condition |
|---|---|
| **Fail (1–2)** | Poor design choices; lacks fundamental principles (modularity, abstraction); hard to maintain or extend. |
| **Not-Fail (3–4)** | Partially adheres to design principles but has room for improvement. |
| **Pass (5)** | Follows most design principles; code is easy to maintain and extend. |

### 5.7 Missing / Excessive Detail

| Score | Condition |
|---|---|
| **Fail (1–2)** | Response is overly simplistic for the topic depth required, or is excessively verbose to the point of obscuring key points. |
| **Not-Fail (3–4)** | Generally helpful but needs more detail or nuance, or contains some extraneous information. |
| **Pass (5)** | Clear, focused, sufficient detail and nuance without overwhelming. |

---

## 6. Grading Dimensions — Test Suite

### 6.1 Overly Specific Tests *(Added 02/24)*

Tests must cover only **explicit or implicit backend requirements** from the rewritten prompt. They must not be so specific that only one implementation path passes them while other valid implementations fail.

| Score | Condition |
|---|---|
| **Fail (1–2)** | More than 5% of tests are overly specific (test requirements not in the prompt). |
| **Not-Fail (3–4)** | At most 5% of tests are overly specific. |
| **Pass (5)** | Zero overly specific unit tests. |

**Rule:** If the prompt did not specify error code handling, do not assert specific error codes in tests.

---

## 7. Grading Dimensions — Verifier Coverage

Tests + rubrics combined must verify **all requests in the rewritten prompt**.

### 7.1 Scope Exclusions *(03/04)*

Do **not** flag for missing coverage on:
- Subjective UI design requirements (e.g., "elegant", "pretty", "good design style").
- Trivial or minor UI design requirements (e.g., "navigation on the left"). Check functionality, not position.

### 7.2 Bottleneck Test Rule *(02/27)*

An Expected Interface section is considered "covered" if it has **at least one representative unit test** that, upon failure, would indicate a breakdown of all related logic in that section. You do not need to flag missing coverage on minor details when a bottleneck test is present.

### 7.3 Optional Instructions Rule *(02/02)*

Optional prompt instructions **may be omitted** from verifiers — but only if the instruction itself is optional (not a mandatory feature that is optional in some other context).

- ✅ `"...You can also include a light mode/dark mode toggle"` → No rubric/test required.
- ❌ `"...the customer can optionally include a note with each order"` → Must be verified (the capability must exist).

### 7.4 Fail / Pass Thresholds

| Score | Condition |
|---|---|
| **Fail (1–2) — Major** | Test suite misses a major backend requirement of the prompt AND the rubric also misses it entirely. |
| **Not-Fail (3–4) — Minor** | Test suite misses a non-critical implicit requirement AND no rubric covers it either. |
| **Pass (5)** | Rubrics + tests together address all explicit and implicit prompt requirements. |

---

## 8. Data Specification Completeness

### 8.1 Critical Fields (All Required)

| Field | Required? |
|---|---|
| `Dockerfile` | ✅ Yes |
| `Golden Patch` (codebase.zip) | ✅ Yes |
| At least one verification method (rubric and/or test suite) | ✅ Yes |
| `run.sh` (if test suite present) | ✅ Yes |
| `parsing.py` (if test suite present) | ✅ Yes |
| Test execution results (`before.json` + `after.json`) | ✅ Yes |
| F2P test list | ✅ Yes |

> **[Fail - Missing Critical Fields]:** Any of the above is absent → automatic fail.

---

## 9. Overall Rubric Quality — Error Thresholds *(Added 02/19)*

Rubric errors are classified as Major, Moderate, or Minor. All errors across the rubric are tallied holistically.

**Denominator** = total number of criteria written by the contributor.  
**Do NOT double-count** a criterion with multiple issues — count it once at its highest severity.

### 9.1 Fail Thresholds

| Threshold | Condition |
|---|---|
| **Fail — 5%+ Major Errors** | More than 5% of criteria have major issues. |
| **Fail — 15%+ Moderate Errors** | More than 15% of criteria have moderate or major issues combined. |
| **Fail — 25%+ Minor Errors** | More than 25% of criteria have minor, moderate, or major issues combined. |

### 9.2 Not-Fail Thresholds

| Threshold | Condition |
|---|---|
| **Not-Fail — ≤5% Major** | Up to 5% major issues. |
| **Not-Fail — ≤15% Moderate** | Up to 15% moderate+major (with major <5%). |
| **Not-Fail — 5–25% Minor** | Between 5–25% minor+moderate+major (with major <5%, moderate <15%). |

### 9.3 Pass

- Less than 5% of rubrics have minor issues.
- Zero major or moderate issues.

---

## 10. Rubric Error Definitions (Appendix)

### MAJOR Issues

#### 10.1 Missing Criteria — Critical Requirements

- Count each missing rubric that should check for an **explicit requirement** in the prompt or a **critical implicit expectation** (i.e., you cannot imagine a good response without it).
- Only applies to requirements **not already covered by F2P tests**.
- Cap: cover the **top 30 most important** criteria not coverable by unit tests.

**When to flag:**

| Prompt size | Flag condition |
|---|---|
| **< 30 explicit requirements** | Flag only if **more than 3** important explicit criteria are missing from rubrics. |
| **≥ 30 explicit requirements** | Flag only if **more than 3** top-30-worthy criteria are missing AND rubric covers non-critical criteria instead. |

> This error only applies to requirements unit tests did NOT touch.

#### 10.2 Criteria Not Self-Contained

Every rubric must be evaluable using **only** the model response — no access to the prompt, other criteria, or external facts.

| Bad Example | Fixed |
|---|---|
| "Response identifies the first president of the USA" | "Response identifies the first president of the USA as George Washington" |
| "The response addresses the bug mentioned in the prompt" | "The response addresses the bug where the submit button doesn't work" |

#### 10.3 Criteria Not Atomic — Major *(Updated 02/26)*

Criterion groups **two or more completely unrelated constraints** with no single coherent focus.

- ✅ **Acceptable grouping:** Related constraints under one coherent instruction (e.g., "implements a tech stack including Vue 3, Vite, Pinia, Express, SQLite"). This prevents rubric sprawl.
- ❌ **Major failure:** Bundling totally unrelated constraints (e.g., "the UI is responsive AND the database uses transactions AND error messages are logged").

#### 10.4 Incorrect Criteria

- Criterion checks something not aligned with prompt requirements.
- Contains a factual error (e.g., "runs in O(n log n), such as selection sort" — selection sort is O(n²)).
- Is not an explicit requirement and implementing it doesn't make the response better.
- Is completely unrelated to the prompt.

> Before classifying as "Incorrect Criteria", check if a more specific error type applies (e.g., Overfitting).

#### 10.5 Framing

Criteria must be **positively framed** — a good response must evaluate to `True` / `Yes` / `Pass`.

Incorrectly framed criteria are treated as severely as incorrect criteria.

---

### MODERATE Issues

#### 10.6 Missing Criteria — Non-critical Requirements

Same logic as Critical, but for non-critical explicit requirements or implicit expectations (e.g., "use bold text", "use bullet points").

- Cap: top 30 most important rubric-only criteria.
- Do not penalize for minor requirements or for having more than 30 rubrics (this batch allows extra coverage).

#### 10.7 Overlapping or Redundant Criteria

- **Redundant:** Criterion A is completely encompassed by Criterion B.
- **Overlapping:** Criteria A and B independently assess some of the same elements.

Count each group of redundant/overlapping criteria as **one moderate issue**.

```
Redundant: C1 checks {a, b, c} and C2 checks {a, b} → C2 is redundant.
Overlap:   C1 checks {a, b, c} and C2 checks {b, c, d} → both overlap on {b, c}.
```

#### 10.8 Overfitting and Underfitting *(Updated 03/12)*

- **Overfitting:** Criterion is too rigid — correctly accepts some valid implementations but incorrectly rejects others.
- **Underfitting:** Criterion is too loose — accepts valid implementations but also incorrectly accepts invalid ones.

Criteria must be flexible enough to **accept all valid implementations and only valid ones**.

> A criterion may mention specific answers as **examples** (in parentheses, with "for example", etc.) without being considered overfitted.

**Overfit examples:**
- Criterion checks a specific file path/name not specified in the prompt (that only the Golden Patch uses).
- Prompt says "Example headers: Film, Year" → Criterion requires headers named exactly "Film" and "Year" → overfitted (alternative names like "Movie" and "Release Year" would be unfairly rejected).

**Distinction — Overfitting vs Nice-to-Have:**
- If a criterion is necessary for a **perfect** response but was not explicitly required → it is **Nice-to-Have** (weight = 1), not overfitted.
- If a prompt says a feature is "optional but recommended" → a criterion checking for it must be written with weight = 1.

#### 10.9 Subjective Criteria

Criteria that are vague, immeasurable, or rely on undefined qualifiers:

- ❌ "The response should have good formatting"
- ❌ "Code must be optimal"
- ❌ Using "appropriate", "properly", "best practices", "reasonable" without explicit definitions.

> Exception: Intentionally ambiguous, open-ended prompts allow for some subjectivity. Example: "The website has a refined modern look so it could be launched as a product by a reputable company" is acceptable for a creative/artistic prompt.

#### 10.10 Incorrect Weights — Major

Criterion is weighted incorrectly by **two levels** (e.g., assigned 1 when 5 is appropriate, or vice versa).

---

### MINOR Issues

#### 10.11 Incorrect Weights — Minor

Criterion is weighted incorrectly by **one level** (1 vs 3, or 3 vs 5).

#### 10.12 Miscategorized Criteria

Criterion is tagged with the wrong dimension when a clearly better one is available.

| Dimension | Scope |
|---|---|
| **Instruction Following** | Adherence to explicit prompt directives (format, constraints, language, required elements). |
| **Code Correctness** | Code performs the intended task and produces correct results. |
| **Code Quality** | Robustness, maintainability, idiomatic patterns, no fragile design. |
| **Code Clarity** | Readable, well-structured code; good naming, organization, formatting. |
| **Code Efficiency** | Conciseness, no unnecessary steps, reduction of redundancy. |

> Contributors may select the closest category if none perfectly applies — minor miscategorization is acceptable.

---

## 11. General Content Dimensions (All CB-Generated Content)

| Dimension | Fail Condition | Pass Condition |
|---|---|---|
| **Repetitiveness / Relevance** | 3+ sentences expressing the same idea; 4+ irrelevant sentences. | ≤2 redundant expressions; ≤2 irrelevant sentences. |
| **Clarity** | Content is extremely difficult to follow or unclear. | Clear, well-structured, effectively communicates intended message. |
| **Unlisted Minor Errors** | N/A (Non-Fail only) | No unlisted errors degrading task quality. |
| **Original Work** | Clear LLM cheating evidence; direct plagiarism without citation. | No obvious LLM usage; no uncited plagiarism. |
| **Harmful Content** | Material contains harmful content not called for by the project. | No harmful content present. |

> LLM cheating signals: excessive pleasantries, generic responses lacking human nuance, no analytical depth. Copy-paste prompts asking for summaries of pasted material are acceptable.

---

## 12. Quick Self-Audit Checklist (Before Submission)

### Prompt
- [ ] Expected Interface section is present with all required fields for every public interface.
- [ ] No helper functions or third-party library fields documented in the interface.
- [ ] All constraints are realistic and non-contrived.
- [ ] No conflicting instructions exist.
- [ ] No factual errors.

### Golden Patch
- [ ] Code compiles and runs without errors or warnings.
- [ ] All prompt requirements are satisfied.
- [ ] Algorithm complexity is appropriate (no obvious inefficiencies).
- [ ] Naming is clear and meaningful throughout.
- [ ] Code is modular and adheres to design principles.

### F2P Tests
- [ ] `before.json` shows all tests as FAILED (not errored).
- [ ] `after.json` shows all tests as PASSED.
- [ ] No test is overly specific (≤5% tolerance maximum).
- [ ] Tests follow the rewritten prompt, not the Golden Patch's specific implementation.

### Rubric
- [ ] Minimum 5 criteria; maximum 30 (for non-unit-testable requirements).
- [ ] Every criterion is self-contained (evaluable from model response alone).
- [ ] Every criterion is positively framed (good response → True/Yes/Pass).
- [ ] No criterion groups unrelated constraints (atomicity).
- [ ] No overfitted criteria (specific file names, header names not required by prompt).
- [ ] No underfitted criteria (too broad to distinguish valid from invalid implementations).
- [ ] No subjective or vague qualifiers without explicit definitions.
- [ ] Weights are correctly assigned (1 = nice-to-have, 3 = important, 5 = mandatory).
- [ ] Dimensions are correctly assigned per criterion.
- [ ] Major backend requirements not covered by unit tests have rubric criteria.
- [ ] Top 30 most important non-unit-testable requirements are covered.
