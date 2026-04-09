# Real Coder — Technical Reference Guide (G3)
## Grading Instructions & Rubric Quality Definitions | Senior Engineering Standards

> **Project:** Real Coder (mattock_name) — Outlier Platform  
> **Project ID:** 697b72cae052640b8db3e22d  
> **Source:** Official Grading Guidelines | Last Major Update: March 12, 2026  
> **Scope:** Auditor Evaluation Framework for CB-submitted Tasks

---

## 1. Project Context & Objective

The Real Coder project produces verified software solutions for freelance-style coding tasks built from a blank slate. Each submission consists of four artifacts evaluated independently:

| Artifact | Description |
|---|---|
| **Agent Prompt** | Structured rewritten prompt guiding an AI agent to solve the task |
| **Golden Patch** | Fully functional "ground truth" implementation |
| **F2P Test Suite** | Automated Fail-to-Pass test cases (optional but evaluated if present) |
| **Expert Rubric** | Multi-dimensional evaluation rubric tailored to the prompt requirements |

**Two valid verification methods exist** — at least one must be used:
- **Atomic Rubrics:** Minimum 5 criteria across 5 dimensions: Instruction Following, Code Correctness, Code Efficiency, Code Clarity, and Code Quality.
- **Fail-to-Pass (F2P) Integrity:** Tests must FAIL on empty/buggy codebase and PASS after golden patch is applied. Tests must not assume an implementation strategy not explicitly required by the prompt.

**Environment:** All code must execute inside the provided Docker container (Ubuntu 22.04) using the standardized `run.sh` and `parsing.py` scripts.

---

## 2. Audit Workflow

| Step | Action | Key Rule |
|---|---|---|
| 1 | Review task instructions | Read the full task guidelines link before auditing |
| 2 | Evaluate the Prompt | Must be a rigorous translation of the original; must include Expected Interfaces section |
| 3 | Evaluate the Golden Patch | Verify logic and Docker file accuracy; multiple valid solutions exist — check that it makes sense |
| 4 | Evaluate F2P tests (if present) | Review Before (FAIL) and After (PASS) JSON; both must be present and deterministic |
| 5 | Evaluate the Rubric (if present) | Audit 5+ criteria — must be atomic and verifiable |
| 6 | Tally final score | Apply grading instructions; do NOT edit tasks or touch the "Task Action" field |

---

## 3. General Grading Rules (1–5 Scale)

### 3.1 Score Determination Logic

```
IF any dimension = 1-2 (FAIL)         → Task score = FAIL (1 or 2)
IF no fail AND any dimension = 3-4    → Task score = 3 or 4 (NON-FAIL)
IF ALL dimensions = 5                 → Task score = 5

Grade to the LOWEST dimension.
Grade to the LOWEST turn (multi-turn tasks).
```

### 3.2 Choosing Between Adjacent Scores

| Decision | Rule |
|---|---|
| 1 vs 2 | Select 1 if the contributor put little to no effort |
| 3 vs 4 | Use judgment on how seriously the minor issue affects quality |

### 3.3 Priority Rule

> Prompt instructions or task instructions always take precedence over other grading dimensions. Example: if the task asks for intentional spelling mistakes, do not flag spelling errors.

---

## 4. Grading Dimensions — Prompt

### 4.1 Reasoning Requirement

| Score | Condition |
|---|---|
| **FAIL** | Prompt only requires factual lookup or definition — no reasoning required at all |
| **NON-FAIL** | Prompt loosely or trivially includes domain reasoning |
| **5** | Prompt requires reasoning aligned with the assigned domain/expertise level, beyond simple recall |

### 4.2 Prompt Constraints

| Score | Condition |
|---|---|
| **FAIL** | Constraints feel clearly unrealistic, contrived, or absurdly stacked (3+ formatting constraints) |
| **FAIL** | Constraints are basic or overused (e.g., "keep it brief," "explain to a child") |
| **NON-FAIL** | Subjective constraints — believable that someone in this context would add them |
| **5** | Constraints feel natural and reflect what a real user would request from a chatbot |

### 4.3 Contrived / Unnatural Prompts

| Score | Condition |
|---|---|
| **FAIL** | Prompt is clearly contrived or unnatural |
| **NON-FAIL** | Prompt is somewhat contrived or unnatural |
| **5** | Prompt is neither contrived nor unnatural |

> Note: Riddles and intentionally constraint-laden prompts should NOT be considered contrived.

### 4.4 Truthfulness

| Score | Condition |
|---|---|
| **FAIL** | 1+ major factual errors OR 2+ minor factual errors |
| **NON-FAIL** | 1 minor factual error |
| **5** | No factual errors, no misleading statements |

### 4.5 Feasibility

| Score | Condition |
|---|---|
| **FAIL** | Request cannot be answered by an LLM in a single response |
| **FAIL** | Request cannot be fulfilled at all |
| **FAIL** | Instructions conflict/contradict and cannot be satisfied simultaneously |
| **NON-FAIL** | Multiple requests where only secondary ones are impractical |
| **5** | Fully actionable, no conflicting instructions |

---

## 5. Grading Dimensions — Expected Interface

> **Rule:** CBs must include an Expected Interfaces section within the rewritten prompt defining every newly introduced file, function, or class that an external application or test suite will interact with.
> Do NOT flag for helper functions or fields from third-party libraries (updated 03/12).

### 5.1 Required Interface Fields

| Field | Description |
|---|---|
| **Path** | Exact file path as it appears in the intended structure |
| **Name** | Class.method or function name |
| **Type** | e.g., class, method, function, or interface |
| **Input** | Parameters and types, e.g., `chunk: GlibcChunk` |
| **Output** | Return type, e.g., `None` or `Promise<void>` |
| **Description** | Observable side effects or behavior asserted by tests |

**Language-Specific Fields (as applicable):**
- TypeScript/Java: `Inheritance: extends <Base>; implements <IfaceA, IfaceB>`
- Go: `Embedding / Implements: embeds <TypeA>; implements <IfaceA, IfaceB>`
- Python: `Bases / Overrides: bases: <BaseA, BaseB>; overrides: <Base.method>`
- Annotations: `@Override, @Inject, @dataclass, @cached_property, @sealed`

### 5.2 Interface Fail Conditions

| Error Type | Condition |
|---|---|
| **FAIL — Missing Interface Section** | Section is missing entirely OR any required/language-specific field is absent for any documented interface |
| **FAIL — Undocumented Interface** | A publicly accessible component or one tested by the verifier is not listed (helper functions and trivial imports are exempt) |
| **FAIL — Misleading Interface Description** | Documentation is incomplete such that a correct implementation would still fail a verifier |
| **FAIL — Invalid Interface** (03/12) | A documented interface is a helper function or third-party library field not needed by external applications |
| **5** | All required fields present; no public interface is undocumented or misleadingly documented |

> **Critical reminder:** Do NOT reference back to the golden patch when auditing interfaces. The golden patch is only one of many valid solutions.

---

## 6. Grading Dimensions — Response (Golden Patch)

### 6.1 Instruction Following / Response Fulfillment

| Score | Condition |
|---|---|
| **FAIL** | 1+ explicit instructions not followed |
| **FAIL** | Response does not fully answer the question |
| **NON-FAIL** | Subjectively misses some aspects |
| **5** | All explicit instructions clearly followed; question fully answered |

### 6.2 Compilation

| Score | Condition |
|---|---|
| **FAIL** | Code does not compile or throws runtime errors |
| **NON-FAIL** | Code runs but produces warnings |
| **5** | Code runs perfectly without any errors or warnings |

### 6.3 Execution Output

| Score | Condition |
|---|---|
| **FAIL** | Output is irrelevant, incorrect, or incomplete; fails edge cases |
| **5** | Output perfectly aligns with all prompt requirements including edge cases |

### 6.4 Performance

| Score | Condition |
|---|---|
| **FAIL** | Clearly inefficient — e.g., O(n³) when O(n log n) is achievable |
| **NON-FAIL** | Moderately efficient — e.g., O(n²) when O(n log n) is possible |
| **5** | Well-optimized with efficient algorithms and data structures |

### 6.5 Readability

| Score | Condition |
|---|---|
| **FAIL** | Difficult to read in >2 areas: missing indentation, excessive whitespace, minified code |
| **FAIL** | Misleading variable/class/method names (e.g., `even_array = [1, 3, 5, 7]`) |
| **NON-FAIL** | Formatting issues in ≤2 areas; still readable |
| **NON-FAIL** | Names don't follow language conventions but are not misleading |
| **5** | Well organized, consistent formatting; meaningful and reflective names |

### 6.6 Code Documentation

> Note: Having a properly documented README.md is acceptable if the codebase doesn't have excessive comments in every single function (section removed 02/22 as standalone dimension but still applies).

| Score | Condition |
|---|---|
| **FAIL** | Very poorly commented, almost no comments, or incorrect/redundant comments |
| **NON-FAIL** | Reasonable documentation but could be more detailed |
| **5** | Well documented with detailed comments and docstrings |

### 6.7 Code Design

| Score | Condition |
|---|---|
| **FAIL** | Poor design — lacks fundamental principles like modularity and abstraction |
| **NON-FAIL** | Partially adheres to design principles — bare minimum |
| **5** | Follows most design principles: modularity, separation of concerns, abstraction |

### 6.8 Missing / Excessive Detail

| Score | Condition |
|---|---|
| **FAIL** | Overly simplistic — superficial treatment of a topic requiring deeper exploration |
| **FAIL** | Overly lengthy — key points obscured by excessive detail |
| **NON-FAIL** | Generally helpful but needs additional nuance |
| **5** | Clear, focused, appropriate depth without overwhelming |

---

## 7. Grading Dimensions — Test Suite

### 7.1 Overly Specific Tests

> Tests must ONLY cover explicit or implicit backend requirements from the CB's rewritten prompt. They must not be so specific that only a subset of valid solutions pass.

| Score | Condition |
|---|---|
| **FAIL** | More than 5% of tests are overly specific — test for requirements not in the prompt |
| **NON-FAIL** | At most 5% of tests are overly specific |
| **5** | No overly specific unit tests |

**Examples of overly specific tests to avoid:**
- Hardcoding specific CLI flag names when the prompt only says "accept a folder path"
- Enforcing keyword-only argument style when the prompt doesn't specify
- Asserting a specific constant name when only the behavior matters
- Patching at a specific import path (`src.module.X`) instead of at the library level (`somelib.X`)

---

## 8. Grading Dimensions — All CB Content

### 8.1 Repetitiveness / Relevance

| Score | Condition |
|---|---|
| **FAIL** | 3+ sentences expressing the exact same idea OR 4+ irrelevant sentences |
| **NON-FAIL** | 2 sentences with similar ideas OR 3 irrelevant sentences |
| **5** | ≤2 repeated ideas; ≤2 irrelevant sentences |

### 8.2 Clarity

| Score | Condition |
|---|---|
| **FAIL** | Content is extremely difficult to follow or unclear |
| **NON-FAIL** | Makes sense but has minor clarity issues |
| **5** | Clear, easy to follow, well-structured |

### 8.3 Original Work

| Score | Condition |
|---|---|
| **FAIL** | Clear evidence of unsanctioned LLM usage (excessive pleasantries, generic responses, lack of human nuance) |
| **FAIL** | Direct plagiarism without citation |
| **NON-FAIL** | Suspected LLM usage but not obvious |
| **5** | No clear evidence of LLM usage; no plagiarism |

> Note: Copy-paste prompts asking for summaries of pasted material are acceptable.

### 8.4 Harmful Content

| Score | Condition |
|---|---|
| **FAIL** | Content contains any harmful material not called for by the project |
| **5** | No harmful content |

---

## 9. Data Specification Completeness

### 9.1 Critical Fields (FAIL if any are missing)

**Always required:**
- Dockerfile
- Golden Patch

**If a test suite is included, additionally required:**
- `run.sh` — test execution script
- `parsing.py` — test output parsing script
- Test execution results: `before.json` (FAIL state) and `after.json` (PASS state)
- F2P test list

---

## 10. Verifier Coverage

> Tests and rubric criteria together must verify all requests in the rewritten prompt.

### 10.1 Coverage Rules

| Score | Condition |
|---|---|
| **FAIL** | Test suite does not cover a major backend requirement, AND rubric also does not cover it |
| **FAIL** | Rubric missing at least one criterion for an explicit/critical implicit requirement not verified by any test |
| **FAIL** | Test suite missing at least one test for an explicit/critical implicit requirement not verified by any rubric |
| **NON-FAIL** | Missing coverage for a non-critical implicit requirement not verified by either test or rubric |
| **5** | Verifiers address all explicit and implicit requirements of the rewritten prompt |

### 10.2 Coverage Exceptions — Do NOT flag for

- Subjective UI design requirements (e.g., "elegant", "pretty", "good design style")
- Trivial/minor UI design requirements — this queue is **code-focused**, not UI-design-focused
- Example: "add navigation to the left menu" — do not flag missing coverage for the menu being on the left; DO check that the menu's functionality is verified
- A section of the Expected Interface is "covered" if it has at least one representative unit test whose failure would indicate a breakdown of all related logic in that section — you do not need a test for every minor detail

### 10.3 Optional Instructions

- Instructions explicitly stated as optional may be omitted from verifiers
- **Important distinction:** A mandatory feature that is optional from a user's perspective must still be verified

```
SHOULD NOT FAIL:
Prompt: "...You can also include a light mode/dark mode toggle"
→ No rubric/test needed for this toggle

SHOULD FAIL:
Prompt: "...the customer can optionally include a note with each order"
→ Must verify the ability to add this note is present
```

### 10.4 Bottleneck Tests

If a "bottleneck" test is present — a test whose failure indicates a breakdown of a whole section — you do not need to flag for missing coverage on minor details within that section.

### 10.5 Scope of Tests

- Tests follow the rewritten **prompt**, not the golden patch
- Tests can be generic to accommodate multiple valid solutions
- Only penalize if tests miss explicit **backend** requirements from the prompt
- Frontend requirements should be covered by rubric criteria, not unit tests

---

## 11. Overall Rubric Quality

### 11.1 Error Classification and Thresholds

All rubric errors across criteria are tallied holistically to arrive at a rubric quality rating.

```
Denominator = Number of criteria the CB wrote
Numerator   = Number of criteria with issues of that type
Do NOT double-count: a criterion with 1 major + 1 moderate issue = counted as 1 major issue only
```

| Severity | Threshold | Score |
|---|---|---|
| **FAIL** | >5% criteria have Major issues | 1-2 |
| **FAIL** | >15% criteria have Moderate or Major issues | 1-2 |
| **FAIL** | >25% criteria have Minor, Moderate, or Major issues | 1-2 |
| **NON-FAIL** | ≤5% Major; ≤15% Moderate/Major; 5–25% Minor/Moderate/Major | 3-4 |
| **5** | <5% Minor issues; no Major or Moderate issues | 5 |

---

## 12. Rubric Quality Definitions

### 12.1 MAJOR Issues

#### Missing Criteria — Critical Requirements
- Count each missing rubric that should check for an **explicit** prompt requirement or **critical implicit** expectation
- Critical = you cannot imagine a good response without it
- Only penalize for **backend requirements** not already covered by F2P tests; frontend requirements should be in rubric
- Maximum coverage target: top 30 most important things that cannot be covered by unit tests

**When to flag for missing critical criteria:**
```
IF <30 explicit request criteria:
  → Flag ONLY if more than 3 important explicit criteria are missing

IF >=30 explicit request criteria:
  → Flag ONLY if more than 3 important criteria that should be top-30 are missing
     AND the rubric covers non-critical criteria instead of the explicit requests
```

#### Criteria Not Self-Contained
- Criterion cannot be evaluated using only the model response — requires consulting the prompt, other criteria, or external facts

```
BAD:  "Response identifies the first president of the USA"
GOOD: "Response identifies the first president of the USA as George Washington"

BAD:  "The response addresses the bug mentioned in the prompt"
GOOD: "The response addresses the bug where the submit button doesn't work"
```

#### Criteria Not Atomic — Major
- Criterion groups two or more **completely unrelated** constraints with no coherent focus
- **Acceptable:** Higher-level rubric combining closely related constraints as one coherent instruction
  - Example: "implements a tech stack that includes X, Y, Z" (where X, Y, Z were specified in the prompt)
- **Not acceptable:** A dump of requirements with no thematic connection
- Features that are closely related can be grouped — do NOT flag this as an atomicity issue

#### Incorrect Criteria
- Criterion checks for something not aligned with prompt requirements
- Contains a factual error or misleading point (e.g., "O(n log n) such as selection sort")
- Is not an explicit requirement of the prompt AND does not make the response better
- Is not related to the prompt at all

> Before classifying as Incorrect Criteria, check if a more specific error category applies (e.g., Overfitting).

#### Framing
- Criteria must be **positively framed** — a good response should evaluate to "Yes" / "True" / "Pass"
- Negatively framed criteria are as bad as incorrect criteria

---

### 12.2 MODERATE Issues

#### Missing Criteria — Non-critical Requirements
- Missing rubric for a non-critical explicit requirement or non-critical implicit expectation
- Examples of non-critical: "Use bold text", "Use bullet points"
- Same top-30 cap applies — do not penalize for more than 30 rubric items being needed

#### Overlapping or Redundant Criteria
- Count completely redundant criteria as one moderate issue
- Count a group of overlapping criteria as one moderate issue

```
REDUNDANT:
Criteria 1: "Response does a, b, c"
Criteria 2: "Response does a, b"    ← fully covered by Criteria 1

OVERLAP:
Criteria 1: "Response does a, b, c"
Criteria 2: "Response does b, c, d" ← b and c assessed twice
```

> Exception: A single criterion that introduces and specifies related requirements is NOT overlap (e.g., "follows best practices by ensuring lines are under 79 characters").

#### Overfitting and Underfitting

| Type | Definition |
|---|---|
| **Overfitting** | Criteria too rigid — correctly accept some valid implementations but incorrectly reject others |
| **Underfitting** | Criteria too broad — accept valid implementations but also accept invalid ones |

Criteria must be flexible enough to accept **all** valid implementations and **only** valid implementations.

> Criteria can mention specific answers as examples when framed as such — "e.g.", within parentheses, or "such as" wording does NOT make it overfitted.

**Overfitting examples:**
- Criterion requires a specific file name or path not mandated by the prompt (only in the golden patch)
- Prompt says "Example headers: Film, Year" → criterion checks that headers are named exactly "Film" and "Year" (those were examples, not requirements)

**Overfitted vs Nice-to-Have:**
- If a criterion could be necessary for a perfect response but wasn't explicitly required → it's a **Nice-to-Have** (weight 1), NOT an overfitted criterion
- If a prompt says a feature is "optional but recommended" → criteria checking for it must exist but be assigned weight 1

#### Subjective Criteria
- Criteria are vague, subjective, or immeasurable
- Qualifiers that make criteria fail: "appropriate", "properly", "best practices", "reasonable", "good formatting", "optimal" — unless explicitly defined

> Exception: Intentionally open-ended prompts may allow subjective criteria. Example: "The website has a refined modern look so it could be launched by a reputable company" is acceptable for a prompt asking for an artistic design.

#### Incorrect Weights — Major
- Criteria objectively incorrectly weighted by **two levels** (e.g., weight 1 when weight 5 is appropriate, or vice versa)

---

### 12.3 MINOR Issues

#### Incorrect Weights — Minor
- Criteria incorrectly weighted by **one level** (1 vs 3, or 3 vs 5 scenarios)

#### Miscategorized Criteria
- Criteria tagged with the wrong dimension when a better one is clearly available

**Available dimensions:**
| Dimension | Covers |
|---|---|
| **Instruction Following** | Adherence to explicit directions: format, constraints, language, libraries, required elements |
| **Code Correctness** | Code performs the intended task and produces correct results |
| **Code Quality** | Robustness, maintainability, idiomatic patterns, avoiding fragile design |
| **Code Clarity** | Readability, naming, organization, formatting |
| **Code Efficiency** | Conciseness, avoidance of unnecessary steps, reduction of redundancy |

> CBs are allowed to select the closest available category if none perfectly applies.

---

## 13. Quick Reference — Scoring Thresholds

### Rubric Error Rate Summary

| Error Type | Issue Level | FAIL threshold | NON-FAIL threshold | Perfect |
|---|---|---|---|---|
| Major rubric errors | Major | >5% | ≤5% | 0% |
| Moderate rubric errors | Moderate | >15% (incl. major) | ≤15% | 0% |
| Minor rubric errors | Minor | >25% (incl. all) | 5–25% | <5% |
| Overly specific tests | Test | >5% | ≤5% | 0% |

### Criteria Weight Buckets

| Weight | Meaning |
|---|---|
| **1** | Nice-to-have — optional but would improve the response |
| **3** | Important — substantially better with it |
| **5** | Critical — cannot imagine an acceptable response without it |

---

## 14. Key Decision Rules — At a Glance

```
EXPECTED INTERFACE:
✓ Document every publicly accessible / verifier-tested component
✓ Do NOT document helper functions or 3rd-party library fields
✓ All 6 fields required; language-specific fields required when applicable
✓ Do NOT reference the golden patch when auditing interfaces

VERIFIER COVERAGE:
✓ Tests follow the prompt, not the golden patch
✓ Backend requirements → covered by F2P tests
✓ Frontend requirements → covered by rubric criteria
✓ Do not flag subjective UI design requirements
✓ Optional instructions may be omitted from verifiers (but check the distinction)

RUBRIC CRITERIA:
✓ Must be positively framed (evaluates to YES/PASS for good responses)
✓ Must be self-contained (evaluable without consulting the prompt)
✓ Must cover top 30 most important non-test-coverable requirements
✓ Do not double-count criteria with multiple issue types
✓ Closely related constraints can be grouped — do not flag as atomicity issue
✓ Examples in criteria (framed as "e.g." or "such as") are NOT overfitting
✓ Nice-to-have requirements = weight 1, not overfitting

SCORING:
✓ Grade to the lowest dimension
✓ Grade to the lowest turn (multi-turn)
✓ Any FAIL → task is FAIL
✓ All 5s required for a task score of 5
✓ Task instructions override grading dimensions when they conflict
```

---

*Generated from Real Coder G3 Grading Guidelines | Outlier Platform | Last updated March 12, 2026*
