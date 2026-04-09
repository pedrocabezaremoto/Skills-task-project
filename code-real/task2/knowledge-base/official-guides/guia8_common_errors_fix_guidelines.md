# Real Coder — Technical Reference Guide (G8)
## Common Errors & Fix Guidelines | Senior Engineering Standards

> **Project:** Real Coder (mattock_name) — Outlier Platform  
> **Source:** QC Fail Analysis — Last 4 Weeks  
> **Release:** March 18, 2026 | **Scope:** Task Quality Assurance

---

## 1. Golden Patch / Response Quality

### 1.1 Explicit Instruction Miss (FAIL)

The golden patch must implement **every** requirement stated in the rewritten prompt — no exceptions.

**Critical failure patterns:**
- Monorepo installs that skip client package installation (`npm install` at root only)
- UI features only accessible via URL parameters, not through the actual interface
- Wrong exit codes (e.g., argparse exits `2` for missing args; prompt requires `1`)
- Runtime network calls when "no internet access" was mandated
- Using custom implementations instead of the explicitly required library (`deepdiff`, `difflib`)
- Required files never created; logic embedded inline instead
- Inline `onclick` handlers when the prompt explicitly bans inline scripts
- Pipeline stages skipped (e.g., `evaluate_model()` never called after training)

**Fix protocol:**
- Read the prompt line-by-line as a checklist — every requirement must be traceable to code
- Search the codebase for each required feature, file, function, and constraint
- Pay special attention to: startup contracts, error/HTTP code contracts, and forbidden patterns
- For frontend tasks: verify every user-facing feature is reachable through the UI, not just the API

---

### 1.2 Incorrect Code Output / Not Fulfilled (FAIL)

The implementation must handle all flows correctly, including edge cases.

**Critical failure patterns:**
- Unauthenticated routes returning `302` instead of `401`
- Database re-seeded on every startup, wiping user data after restart
- Single-quote characters in identifiers causing runtime errors
- Panels not shown on first login without manual interaction
- Non-string inputs returning `500` instead of the required `400`
- Real-time state not propagating across connected clients (WebSocket/SSE)
- Test coverage at 62% when the prompt requires ≥80%
- `localStorage` vote state without 24-hour expiration mismatch

**Fix protocol:**
- Run end-to-end through all user flows — not just the happy path
- Test edge cases: special characters, first-time logins, unauthenticated requests, server restarts
- Verify every error/status code and validation rule against the prompt spec
- For real-time features: test state propagation across multiple connected clients simultaneously
- Run the full test suite inside Docker — never assume local success equals Docker success
- If a coverage threshold is specified, check the coverage report, not just that tests pass

---

### 1.3 Misleading Code Documentation (FAIL)

Code must be self-documenting at both function and inline levels.

**Critical failure patterns:**
- Source files with zero inline comments or docstrings
- README-only documentation with no code-level coverage
- Complex logic (UTC arithmetic, scoring formulas, state machines) left unexplained
- Only section-separator comments (`# API`) with no function-level explanation

**Fix protocol:**
- Add docstrings to every public function and class (purpose, parameters, return value)
- Add inline comments for non-obvious logic: complex queries, math formulas, state transitions
- A README does **not** substitute for code-level documentation — both are required

---

## 2. Rewritten Prompt Quality

### 2.1 Prompt Conflicting Instructions (FAIL)

All requirements in the rewritten prompt must be simultaneously satisfiable.

**Critical failure patterns:**
- Requiring distinct error messages for `wrong passphrase` vs `tampered data` — impossible with AES-256-GCM (no way to distinguish failure modes)
- `no internet access` + a tech stack that auto-downloads data (NLTK, spaCy)
- `runs until killed` AND a `max_cycles` termination parameter — direct contradiction

**Fix protocol:**
- Before finalizing the prompt, verify all requirements can be satisfied by the same implementation
- Check library compatibility with network constraints (NLTK, spaCy download data on first use)
- If the original task is ambiguous, pick one interpretation and commit — do not inherit contradictions
- Feed the finished prompt to Cursor and validate for structure, ambiguity, and contradictions

---

### 2.2 Misaligned Description (NON-FAIL)

The rewritten prompt must faithfully reconstruct the original task — no additions, no reductions.

**Common issues:**
- Original says "SQLite or JSON" → rewrite hard-requires SQLite only
- Original mentions a messy spreadsheet → rewrite adds CSV import/export and delete (never requested)
- Title contains internal references like "(Task 9)"
- Prompt written in imperative style ("Build a…") instead of freelance-brief style ("I need a…")

**Fix protocol:**
- Every added requirement must be traceable to the original brief
- Preserve original flexibility (e.g., "SQLite or JSON")
- Strip all internal references (task numbers, CB notes) before submission

---

## 3. Expected Interface

The Expected Interface section is the **most critical** part of the rewritten prompt.

### 3.1 Required Fields — Every Interface Entry

| Field | Requirement |
|---|---|
| **Path** | File path or URL route |
| **Name** | Function, class, or endpoint name |
| **Type** | Function / Class / API Endpoint / CLI / File |
| **Input** | Parameter names and types (e.g., `filepath: str`) |
| **Output** | Return type or HTTP response code/shape |
| **Description** | Everything a test will assert |

> If a field does not apply, write **N/A** — never omit it.

---

### 3.2 Missing Interface Section / Fields (FAIL)

**Critical failure patterns:**
- Expected Interface section missing entirely
- Entries present but missing `Type`, `Input`, or `Output` fields
- Inputs described vaguely without parameter types
- Output field absent for multiple interfaces

---

### 3.3 Undocumented Interface (FAIL)

Every component imported or called by the test suite must be documented.

**Critical failure patterns:**
- Test imports `app` from `server/index.js` — file not documented in Expected Interface
- Exported functions (`getDataBase`, `formatRelativeTime`, `startReminderJob`) called by tests but not listed
- Frontend store members (`createQuiz`, `stopTimer`, `allQuestionsAnswered`) checked by tests but only partially documented

**Fix protocol:**
- After writing tests, go through every import statement — every imported name must have an interface entry
- Think from the test suite's perspective: what does the test need to import or call? That is your interface surface
- Helper functions and private/internal utilities do **not** need to be documented

---

### 3.4 Misleading Interface Description (FAIL)

The Description must contain everything a test will assert.

**Critical failure patterns:**
- `uploadAudio` described with artwork-upload behavior from a different endpoint
- `build_photo_groups` output documents 4 fields; test expects 5th (`near_duplicate_pairs`)
- Input documents 3 parameters; tests call it with 7
- Component description says "displays in reverse chronological order" but test requires `<h1>` heading with specific text
- API endpoint documented generically but test asserts specific CSV headers (`Student Name, Score, Total Questions, Completed At`)
- Frontend verifiers require specific DOM selectors (`#title`, `#studentName`) not mentioned in interface

**Fix protocol:**
- After writing the interface, ask: "Would a developer reading only this interface know how to implement X?"
- Cross-check: run tests against a stub implementation built from the interface only — if any test fails, the interface is misleading
- List all input parameters including optional ones (e.g., `eps: float = 0.5`)

---

## 4. F2P Test Suite — Over-Specificity

Tests must cover all explicit backend requirements **without** being overly specific to one implementation.

### 4.1 More Than 5% Overly Specific Tests (FAIL)

**Critical failure patterns:**
- Enforcing keyword-only argument style (breaks positional-arg implementations)
- Hardcoding CLI flag names (`--folder`) when the prompt only requires "accept a folder path"
- Brittle import-path mocks: `mock.patch("src.file_sync.paramiko.SSHClient")` breaks if dev writes `from paramiko import SSHClient`
- Testing idempotency contracts not in the prompt
- Asserting a specific constant name (`MAX_AUDIO_SIZE`) when the prompt only requires enforcing a limit
- Checking `app.config["DB_PATH"]` directly instead of verifying general "stores db_path in config" behavior

**Fix protocol:**
- Test behavior, not implementation — ask: "Would another valid solution that satisfies the prompt fail this test?"
- Avoid hardcoding specific argument/flag names unless the prompt explicitly specifies them
- Use interface-neutral mocks: patch at library level (`mock.patch("paramiko.SSHClient")`) not at module import path
- Do not test "best practices" the prompt didn't require (idempotency, specific constant names, type annotation conventions)
- Run the overly-specific audit prompt (Step 2b in guidelines) before proceeding
- If a requirement can only be tested in an overly specific way — cover it with a **rubric criterion** instead

---

### 4.2 Tests Pass on Empty Codebase (FAIL)

Every test must FAIL on an empty codebase.

**Critical failure patterns:**
- Tests catching broad `Exception` accidentally passing because the empty codebase raises `TypeError`
- `before.json` produced locally (macOS) instead of inside Docker
- Manually modifying `run.sh` or `parsing.py` to force a desired output

**Fix protocol:**
- Always run baseline (`before`) execution inside Docker — never locally
- After writing tests, run against a completely empty codebase and confirm every test shows as **FAILED** (not ERROR, not PASSED)
- For broad exception catches, ensure the empty codebase raises the specific exception being checked — or narrow the exception type
- `before.json` and `after.json` must be produced by the same validation script in the same Docker environment
- Never modify "DO NOT MODIFY" sections

---

## 5. Verifier Coverage

The combination of F2P tests and rubric criteria must cover **all** explicit requirements.

### 5.1 Major Insufficient Verifier Coverage (FAIL)

**Critical failure patterns:**
- Prompt forbids libraries (`httpx`, `aiohttp`, `scrapy`, `click`, `typer`) — neither tests nor rubric check these restrictions
- `train_model()` calls `evaluate_model()` never verified — tests only call it in isolation
- Keyword search tests only verify that a response array is returned, never that both `title` and `body` are actually searched
- Frontend key component rendering mentioned in requirements but zero frontend tests or rubric criteria cover it
- Mobile responsiveness not covered by any verifier
- W3C HTML validation and Lighthouse ≥95 with zero coverage
- Cookie-based 24-hour voting limit only verified to be "set" — not that it actually expires

**Fix protocol:**
- After finalizing tests and rubrics, go through every sentence of the prompt and mark each requirement as covered by test, rubric, or both
- For banned libraries/patterns: add a rubric criterion — "The solution does not import [X, Y, Z]"
- For frontend features that can be tested automatically: write frontend tests
- For features that cannot be automatically tested (layout, visual design): add rubric criteria
- Tests must verify actual content/behavior — not just "a response is returned" or "an array exists"
- Think about observable side effects: did it write to the database? did it call the required sub-function?

---

## 6. Rubric Quality

Rubric criteria must be: **atomic, self-contained, positively framed, correctly weighted, and cover all requirements not in the test suite.**

### 6.1 Missing Criteria for Critical Requirements (FAIL)

**Critical failure patterns:**
- Rubric rechecks tech-stack choices/file presence already covered by tests — while core features (restart persistence, pagination, read-only jobs) have no coverage
- No criterion checks admin panel access control (only accessible on performer's turn)
- No criterion covers tie-breaking behavior, admin access codes, or full-slots sign-up prevention
- Feature importance summary and recall prioritization — both explicit prompt requirements — with no coverage

**Fix protocol:**
- Map every explicit prompt requirement to a test or rubric criterion (or both)
- Rubrics should cover the top 30 most important requirements that cannot be objectively verified by unit tests
- Do not waste rubric slots re-verifying things the test suite already validates

---

### 6.2 Overfitting / Underfitting Criteria (NON-FAIL)

**Overfitting examples:**
- "React Router defines exactly two primary routes" — fails a valid solution with a redirect/fallback route
- "AdminPanel displays a success or error message after each CRUD operation" — prompt never specified this
- Requiring step numbers displayed in UI when prompt only requires ascending step order
- Requiring chunk size stored as named constant when prompt only requires fixed-size chunks
- Requiring Python type annotations when prompt never mandated them

**Underfitting examples:**
- "The app has no network access" — passes even if the solution makes remote API calls alongside local writes

**Fix protocol:**
- Before finalizing a criterion, ask: "Would a valid alternative implementation that satisfies the prompt still pass this?"
- Use example-based wording: "uses a loop or equivalent mechanism" instead of "uses a for loop"
- For "no network access": phrase as observable constraint — "The solution does not make any HTTP requests to external URLs during execution"

---

### 6.3 Other Rubric Issues

| Issue | Severity | Fix |
|---|---|---|
| **Overlapping/redundant criteria** | NON-FAIL | If two criteria would both PASS/FAIL for the same behavior, merge them |
| **Subjective/vague criteria** | NON-FAIL | Replace "clear error message" with "the error message includes the field name and reason for rejection" |
| **Criteria not self-contained** | NON-FAIL | Embed specific details: "requirements.txt includes Flask, SQLAlchemy, and pytest" |
| **Criteria not in prompt** | NON-FAIL | Only write criteria traceable to explicit prompt requirements |
| **Incorrect weights** | NON-FAIL | Weight 5 = cannot imagine acceptable response without it; Weight 3 = substantially better; Weight 1 = nice to have |

---

## 7. Environment & Docker Setup

The Docker environment must be fully self-contained and reproducible.

### 7.1 Incompatible Environment (FAIL)

**Critical failure patterns:**
- Dockerfile fails to install `pytest`, `fastapi`, `httpx`, or other test-suite dependencies
- Base image changed from required `ubuntu:22.04` to `python:3.11-slim`
- Golden patch requires `pillow-heic` but dependency absent from Dockerfile
- Dockerfile does not copy application code into the image (tests run against nothing)

**Fix protocol:**
- Use the provided Dockerfile template — do not change the base image (`ubuntu:22.04`) or "DO NOT MODIFY" sections
- Cross-reference every import in codebase and test files against installed packages
- After building the Docker image, run `bash run.sh` inside the container before submitting
- For system-level dependencies (e.g., `libheif` for HEIC): add to the `apt-get install` section
- Remember: you **cannot** use the `COPY` command — all code is injected at runtime; only dependencies go in the Dockerfile

---

### 7.2 Other Environment Issues

| Issue | Severity | Fix |
|---|---|---|
| **Windows line endings in run.sh** | NON-FAIL | Always use Unix LF line endings; run `dos2unix run.sh` before uploading |
| **Python version mismatch** | NON-FAIL | Align `pyproject.toml`, `setup.py`, prompt tech stack, and Dockerfile Python versions |

---

## 8. Quick Reference — FAQ Decisions

| Question | Answer |
|---|---|
| Golden patch passes locally but fails in Docker | Missing Dockerfile dependency, system-level lib not in Ubuntu 22.04, Windows line endings, or wrong base image |
| How to tell if interface is "misleading" | Write a stub from interface only — if any test fails, it's misleading |
| Difference: "Undocumented Interface" vs "Missing Interface Section" | Missing = section absent or field missing; Undocumented = section exists but a tested component not listed |
| Tests pass on empty codebase | Broad exception catch; fix by narrowing exception type |
| Can I add type hint criteria? | Only as weight-1 if the prompt never required it. When in doubt, omit it |
| Patch at `src.mymodule.X` or `somelib.X`? | Always patch at source library level to support all valid import styles |
| More rubric criteria = better? | No. Overlapping criteria double-penalize — aim for maximum unique coverage |
| Include N/A for non-applicable fields? | Yes, always. Omitting required fields is a failing issue |

---

## 9. Final Submission Checklist

```
✓ Golden patch passes all rubric criteria when self-evaluated
✓ All tests FAIL on empty codebase inside Docker (not locally)
✓ All tests PASS with golden patch inside Docker
✓ Every explicit prompt requirement covered by at least one test OR rubric criterion
✓ Every interface tested by the test suite documented with all 6 required fields
✓ No test enforces a specific implementation detail not required by the prompt
✓ No rubric criterion checks something not in the prompt
✓ run.sh uses Unix line endings and runs inside Docker without errors
✓ Dockerfile uses ubuntu:22.04 as base image and includes all dependencies
```

---

*Generated from Real Coder QC Fail Analysis | Outlier Platform | G8 Reference*
