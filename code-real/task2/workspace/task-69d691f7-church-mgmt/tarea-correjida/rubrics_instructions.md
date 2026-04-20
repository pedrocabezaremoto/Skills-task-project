# Rubric Writing Guide for AI Agents

> **Purpose:** This document is your operating manual for producing perfect evaluation rubrics. Follow every section precisely. A rubric you generate must pass all checks described here before it is considered complete.

---

## 1. What You Are Building

A **rubric** is a structured set of requirements that define what a strong response to a given prompt looks like. Each requirement is an **atomic**, **self-contained**, and **verifiable** criterion. Together, the criteria provide a holistic, auditable evaluation framework — without forcing a single rigid style.

Your rubric must:

- Reflect **all** required elements of the prompt (explicit and implied).
- Avoid injecting details not supported by the prompt.
- Allow more than one valid way to satisfy the instructions.
- Contain zero overlapping criteria (each criterion checks exactly one idea).
- Use **positive phrasing** (e.g., "Code includes…" not "Code doesn't forget…").
- Be specific enough that any reviewer can audit it directly from the response.

---

## 2. Rubric Dimensions

Every criterion you write must belong to exactly one of the following dimensions. Use all dimensions that are relevant to the prompt; omit any that genuinely do not apply.

### 2.1 Instruction Following

Measures **intent alignment** — did the response do exactly what was asked?

- Checks: format, constraints, language/library choices, explicit feature requests.
- Red flag to catch: hallucinated requirements or silently ignored instructions.

### 2.2 Code Correctness

Measures **functional integrity** — does the code work?

- Checks: correct output for provided inputs, edge-case handling, absence of syntax errors.
- Red flag to catch: logic bugs, off-by-one errors, mishandled boundaries.

### 2.3 Code Quality

Measures **robustness and maintainability**.

- Checks: modular design, separation of concerns, avoidance of hard-coded values, configurable parameters, no fragile assumptions about input structure.
- Red flag to catch: brittle code, god functions, magic numbers.

### 2.4 Code Clarity

Measures **readability and organization**.

- Checks: descriptive variable/function names, logical section organization, consistent formatting, meaningful comments and docstrings.
- Red flag to catch: cryptic names, tangled control flow, missing documentation.

### 2.5 Code Efficiency

Measures **performance and conciseness**.

- Checks: algorithmic complexity (time/space), avoidance of redundant loops or intermediate data structures, single-pass processing where appropriate.
- Red flag to catch: unnecessary computation, heavy unused libraries, duplicated logic.

### 2.6 Visual Design / UI/UX *(when applicable)*

Measures **user-facing output quality**.

- Checks: layout, responsiveness, accessibility, aesthetic consistency with modern standards.
- Red flag to catch: broken layouts, inaccessible elements, inconsistent styling.

---

## 3. How to Write Each Criterion

Follow these three rules for every single criterion:

| Rule | Definition | Example ✅ | Anti-Example ❌ |
|------|-----------|-----------|----------------|
| **Atomic** | Checks only one idea. | "The function returns results in the required JSON format." | "The function returns JSON and handles edge cases." (two ideas) |
| **Verifiable** | Can be audited directly from the code/output. | "The solution uses only the libraries explicitly allowed in the prompt." | "The code is high quality." (subjective) |
| **Positive** | States what must be present, not what must be absent. | "The code uses modular functions to separate concerns." | "The code is not messy." (negative) |

### Dimension-Specific Examples

**Instruction Following**
- ✅ "The response uses Python 3 as specified in the prompt."
- ✅ "The response outputs the result in the required JSON format."
- ❌ "The response follows the instructions well." *(vague)*

**Code Correctness**
- ✅ "The function correctly returns the expected output for the provided inputs."
- ✅ "The implementation correctly handles all edge cases described in the prompt."
- ❌ "The code does not fail." *(negative)*

**Code Quality**
- ✅ "The solution avoids hard-coded values and uses configurable parameters."
- ✅ "The implementation avoids fragile assumptions about input structure."
- ❌ "The code is not messy." *(negative)*

**Code Clarity**
- ✅ "The code uses clear and descriptive variable and function names."
- ✅ "The implementation is logically organized into readable sections."
- ❌ "The code looks clean." *(subjective)*

**Code Efficiency**
- ✅ "The solution avoids redundant loops and repeated computation."
- ✅ "The implementation uses a single pass over the data where appropriate."
- ❌ "The code is fast." *(unsupported)*

---

## 4. Assigning Weights

Every criterion must carry exactly one of these weights. **Do not use 2 or 4.**

| Weight | Label | When to Use |
|--------|-------|-------------|
| **5** | Mandatory | Core requirement. The prompt clearly expects it. An acceptable response is hard to imagine without it. |
| **3** | Important | Makes the response substantially better. Reasonably or implicitly expected, but an acceptable response is possible without it if all weight-5 criteria are met. |
| **1** | Nice to Have | Necessary for a *perfect* response, but a strong response can exist without it. |

### Weight Assignment Heuristic

1. Read the prompt and list every **explicit instruction** → these start as weight 5 candidates.
2. Identify **implicit expectations** a skilled developer would naturally satisfy → these start as weight 3 candidates.
3. Identify **polish items** (naming conventions, extra documentation, optional optimizations) → these are weight 1 candidates.
4. Review: if a weight-5 item is actually survivable without, downgrade to 3. If a weight-3 item is truly non-negotiable, upgrade to 5.

---

## 5. Scoring a Response Against the Rubric

For each criterion, assign exactly one of:

| Verdict | Rule |
|---------|------|
| **PASS** | The criterion is fully met. State briefly what was observed. |
| **FAIL** | The criterion is not met. Name the specific blocking issue. |

There is no partial credit. A criterion either passes or it does not.

---

## 6. Quality Checks — The Perfect Rubric Checklist

Before finalizing your rubric, verify every item below. If any check fails, revise until it passes.

### Coverage & Accuracy
- [ ] Every **explicit** requirement from the prompt has at least one criterion.
- [ ] Every **critical implicit** expectation has at least one criterion.
- [ ] No criterion checks for something the prompt does **not** require.
- [ ] No criterion contradicts the prompt.

### Structure & Atomicity
- [ ] Each criterion evaluates exactly **one** distinct aspect.
- [ ] No two criteria independently assess the same element (zero redundancy).
- [ ] Each criterion is labeled under the correct dimension.

### Usefulness
- [ ] Following every criterion would make the response **better**, not worse.
- [ ] No criterion punishes a reasonable, evidence-based approach.
- [ ] No criterion is irrelevant (every one either improves quality or catches a defect).

### Phrasing
- [ ] All criteria use **positive** phrasing.
- [ ] All criteria are **specific** enough to audit from the response alone.
- [ ] All labels and annotations are accurate.

### Prompt Validation *(if you also control the prompt)*
- [ ] The prompt requires genuine reasoning, not just factual lookup.
- [ ] The prompt is feasible for an LLM to answer in a single response.
- [ ] Constraints feel natural (something a real user would ask).
- [ ] The prompt contains no factual errors or contradictions.
- [ ] Expected interfaces are documented: path, name, type, input, output, description.

### Environment & Verification *(if applicable)*
- [ ] Test suite plus rubric criteria collectively verify all prompt requirements.
- [ ] Environment is self-contained (runs in Docker with zero manual configuration).
- [ ] All critical data fields are present: Dockerfile, build script, golden patch, and at least one verification method.

---

## 7. Step-by-Step Workflow

Use this sequence every time you build a rubric:

```
1. READ the prompt carefully. Highlight every explicit instruction and constraint.
2. INFER implicit expectations (standard practices, edge cases, design norms).
3. DRAFT criteria — one per identified requirement, assigned to a dimension.
4. ASSIGN weights (5, 3, or 1) using the heuristic in Section 4.
5. SELF-CHECK against the checklist in Section 6.
   - Deduplicate any overlapping criteria.
   - Fill gaps for any uncovered requirements.
   - Remove anything irrelevant or counterproductive.
6. FORMAT the final rubric as a numbered list, grouped by dimension,
   with weight and criterion text clearly visible.
7. REVIEW once more: read the prompt, then read the rubric top to bottom.
   Ask — "If a response passes every criterion here, would it be a genuinely
   good answer?" If not, iterate.
```

---

## 8. Output Format Template

Present your rubric in this structure:

```
## Rubric for: [Task/Prompt Title]

### Instruction Following
1. [Weight 5] [Criterion text]
2. [Weight 3] [Criterion text]

### Code Correctness
3. [Weight 5] [Criterion text]
4. [Weight 5] [Criterion text]

### Code Quality
5. [Weight 3] [Criterion text]

### Code Clarity
6. [Weight 1] [Criterion text]

### Code Efficiency
7. [Weight 3] [Criterion text]

### Visual Design (if applicable)
8. [Weight 3] [Criterion text]
```

Omit any dimension section that has zero applicable criteria for the given prompt.

---

## 9. Common Mistakes to Avoid

| Mistake | Why It's Bad | Fix |
|---------|-------------|-----|
| Vague criteria ("code works well") | Cannot be audited | Specify the exact behavior being checked |
| Negative phrasing ("code doesn't crash") | Inconsistent evaluation | Rewrite as a positive ("code handles invalid input gracefully") |
| Compound criteria (two ideas in one) | Double-penalizes on failure | Split into two separate criteria |
| Redundant criteria | Skews scoring by weighting the same thing twice | Merge or remove the duplicate |
| Missing coverage | Lets bad responses pass | Cross-check every prompt instruction against your criteria list |
| Over-specification | Rejects valid alternative approaches | Focus on *what* must be achieved, not *how* |
| Wrong weight | Misrepresents priority | Re-apply the heuristic from Section 4 |

---

*Follow this guide exactly. A rubric that satisfies every section here will be robust, fair, and comprehensive.*

**Project rubric:** For the On-Device Face Recognition & Smart Photo Organization task, the rubric that follows this guide (dimensions, weights 5/3/1, atomic criteria, positive phrasing) is maintained in `revised_rubric.md`.
