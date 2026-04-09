# Real Coder – Validation Checklist & Common Errors
> **Project:** Real Coder | **Platform:** Outlier  
> **Scope:** Pre-submission validation checklist — folder structure, ZIP packaging, and file integrity  
> **Audience:** Senior developers submitting Real Coder tasks

---

## Table of Contents

1. [Required Folder Structure](#1-required-folder-structure)
2. [ZIP File Packaging Rules](#2-zip-file-packaging-rules)
3. [File Integrity & Protected Sections](#3-file-integrity--protected-sections)
4. [verification.sh — Only Allowed Edit](#4-verificationsh--only-allowed-edit)
5. [Cursor Agent Safety Rules](#5-cursor-agent-safety-rules)
6. [Pre-Submission Checklist](#6-pre-submission-checklist)
7. [Common Errors Quick Reference](#7-common-errors-quick-reference)

---

## 1. Required Folder Structure

The `app/` directory must contain **exactly** these five files — no more, no less:

```
app/
├── codebase.zip    ← agent's submitted code (flat, no parent folder inside)
├── tests.zip       ← hidden test suite (contains the tests/ folder)
├── Dockerfile      ← environment definition (deps only, no COPY)
├── parsing.py      ← output parser (DO NOT MODIFY protected sections)
└── run.sh          ← test runner (DO NOT MODIFY protected sections)
```

> Any extra files in `app/` will break the evaluation harness. Keep it strictly to these five.

---

## 2. ZIP File Packaging Rules

The internal structure of each ZIP is critical. Incorrect packaging is one of the most common causes of silent validation failure.

### 2.1 Structure Contract

| File | Internal structure when opened | How to create it |
|---|---|---|
| `tests.zip` | Contains the `tests/` folder as root entry | Zip **the folder itself** |
| `codebase.zip` | Contains source files directly (no parent folder) | Zip **the contents** inside the folder |

### 2.2 tests.zip — Correct Structure

```
tests.zip
└── tests/              ← folder is the first level
    ├── test_auth.py
    ├── test_api.py
    └── conftest.py
```

```bash
# ✅ Correct — zip the folder itself
cd /path/to/project
zip -r tests.zip tests/

# ❌ Wrong — zip from inside (no top-level folder)
cd /path/to/project/tests
zip -r ../tests.zip .
```

### 2.3 codebase.zip — Correct Structure

```
# ✅ Correct — files at root level, no wrapper folder
codebase.zip
├── main.py
├── utils.py
├── models.py
└── requirements.txt

# ❌ Wrong — nested parent folder (breaks evaluation)
codebase.zip
└── codebase/           ← extra wrapper folder — INVALID
    ├── main.py
    └── utils.py
```

```bash
# ✅ Correct — zip contents from inside the folder
cd /path/to/codebase
zip -r ../codebase.zip .

# ❌ Wrong — zip the folder from outside (creates nesting)
cd /path/to/project
zip -r codebase.zip codebase/
```

### 2.4 Maximum ZIP Depth

The validation script enforces `MAX_ZIP_DEPTH=3`. Files buried deeper than 3 levels will cause evaluation to fail.

```
# Allowed depths (≤ 3)
file.py                      # depth 1 ✅
dir/file.py                  # depth 2 ✅
dir/sub/file.py              # depth 3 ✅

# Rejected (> 3)
dir/sub/deep/file.py         # depth 4 ❌
```

### 2.5 Verification Commands

```bash
# Inspect tests.zip structure
unzip -l tests.zip

# Inspect codebase.zip structure
unzip -l codebase.zip

# Expected output for tests.zip
#   tests/
#   tests/test_auth.py
#   tests/test_api.py

# Expected output for codebase.zip
#   main.py
#   utils.py
#   models.py
```

---

## 3. File Integrity & Protected Sections

### 3.1 run.sh and parsing.py

These files contain sections explicitly marked **`### DO NOT MODIFY ###`**. These blocks must remain byte-for-byte identical to the originals provided by the task.

**Allowed edits:**
- Updating the *configure* section (e.g., test discovery path, output file name) — only when the task explicitly requires it.
- Updating the *parsing logic* section — only when the task explicitly requires it.

**Forbidden edits:**
- Any line inside a `### DO NOT MODIFY ###` block.
- Structural changes (adding imports, changing function signatures, reordering sections).
- Any change introduced automatically by an AI agent without explicit review.

```bash
# Before submission — diff against original to catch unintended changes
diff run.sh run.sh.original
diff parsing.py parsing.py.original
```

### 3.2 Dockerfile

Refer to the Dockerfile contract (Guide 5). In the context of this checklist:

- No `COPY` or `ADD` commands for project code.
- No changes to `FROM`, `WORKDIR`, `ENV`, `CMD`, or `ENTRYPOINT`.
- Only dependency additions (`apt-get install`, `pip install`) are permitted.

---

## 4. verification.sh — Only Allowed Edit

`verification.sh` (also called `validation.sh` depending on the task) must not be modified except for **one line**: the `APP_DIR` path variable.

### 4.1 The Only Permitted Change

```bash
# -- Where everything lives on the host --
APP_DIR="/home/youruser/path/to/your-project/app"   # ← ONLY this line
```

Everything else in the file is locked. The script auto-derives all other paths from `APP_DIR`:

```bash
DOCKERFILE="${APP_DIR}/Dockerfile"
TESTS_ZIP="${APP_DIR}/tests.zip"
CODEBASE_ZIP="${APP_DIR}/codebase.zip"
RUN_SCRIPT="${APP_DIR}/run.sh"
PARSE_SCRIPT="${APP_DIR}/parsing.py"
IMAGE_TAG="agent-evaluator:latest"
MAX_ZIP_DEPTH=3
```

### 4.2 Correct vs. Incorrect Edit

```bash
# ✅ Correct — only APP_DIR updated
APP_DIR="/home/john/projects/task_13/app"

# ❌ Wrong — changed IMAGE_TAG (not permitted)
IMAGE_TAG="my-custom-image:v2"

# ❌ Wrong — changed MAX_ZIP_DEPTH (not permitted)
MAX_ZIP_DEPTH=5

# ❌ Wrong — added extra logic (not permitted)
APP_DIR="/home/john/projects/task_13/app"
export EXTRA_VAR="something"   # hallucinated by AI agent
```

---

## 5. Cursor Agent Safety Rules

When using Cursor's AI agent or auto-edit features, specific risks must be managed actively.

### 5.1 Risk: Agent Modifies Protected Files

Cursor's agent may automatically edit `run.sh`, `parsing.py`, or `verification.sh` when it infers "improvements."

**Mitigation:**

```
1. Never include run.sh, parsing.py, or verification.sh in the agent's context window
   when working on the solution code.

2. After every agent session, run:
     git diff run.sh parsing.py verification.sh
   to detect any unintended changes.

3. Keep original copies:
     cp run.sh run.sh.original
     cp parsing.py parsing.py.original
     cp verification.sh verification.sh.original
   before starting any agent-assisted work.

4. If changes are detected, restore from original:
     git checkout run.sh parsing.py verification.sh
   or copy from backup.
```

### 5.2 Risk: Agent "Hallucinates" ZIP Structure

The agent may suggest zipping the codebase incorrectly (with a parent folder).

**Mitigation:** Always verify ZIP structure manually with `unzip -l` before submission. Never delegate ZIP creation entirely to the agent without verification.

### 5.3 Risk: Agent Modifies Dockerfile Structure

The agent may add `COPY` commands or alter `CMD`/`ENTRYPOINT`.

**Mitigation:** After any agent-assisted Dockerfile change, audit the diff:

```bash
git diff Dockerfile
```

Reject any changes that touch `FROM`, `WORKDIR`, `ENV`, `CMD`, `ENTRYPOINT`, or add `COPY`/`ADD`.

---

## 6. Pre-Submission Checklist

Run through every item before submitting a Real Coder task.

### Folder Structure

- [ ] `app/` contains exactly 5 files: `codebase.zip`, `tests.zip`, `Dockerfile`, `parsing.py`, `run.sh`
- [ ] No extra files or folders inside `app/`
- [ ] `verification.sh` is at project root (outside `app/`)

### ZIP Integrity

- [ ] `unzip -l tests.zip` shows `tests/` as the first-level entry
- [ ] `unzip -l codebase.zip` shows source files at root (no parent folder)
- [ ] No files buried deeper than 3 levels in either ZIP

### File Integrity

- [ ] `run.sh` — `### DO NOT MODIFY ###` sections are unchanged
- [ ] `parsing.py` — `### DO NOT MODIFY ###` sections are unchanged
- [ ] `verification.sh` — only `APP_DIR` line was edited
- [ ] `Dockerfile` — no `COPY`/`ADD` for code; no structural changes

### Validation Run

- [ ] `bash verification.sh` completes without build errors
- [ ] `before.json` shows all tests as `FAILED` (not `ERROR`)
- [ ] `after.json` shows all relevant tests as `PASSED`
- [ ] All 6 output files generated: `before_stdout.txt`, `before_stderr.txt`, `before.json`, `after_stdout.txt`, `after_stderr.txt`, `after.json`

---

## 7. Common Errors Quick Reference

| Error | Root Cause | Fix |
|---|---|---|
| Validation fails silently on ZIP | `codebase.zip` has extra parent folder | Re-zip from inside the folder: `cd codebase && zip -r ../codebase.zip .` |
| Tests not found inside container | `tests.zip` zipped from inside (no `tests/` root) | Re-zip the folder: `zip -r tests.zip tests/` |
| `before.json` shows `ERROR` not `FAILED` | Missing pip dependency; broken import | Add missing package to Dockerfile; rebuild image |
| `after.json` shows tests still `FAILED` | `codebase.zip` nested incorrectly | Verify `unzip -l codebase.zip` — fix nesting |
| Docker build error after agent session | Agent added `COPY` to Dockerfile | `git diff Dockerfile`; revert forbidden changes |
| Verification script fails unexpectedly | `verification.sh` was modified beyond `APP_DIR` | Restore original; re-apply only the `APP_DIR` change |
| CRLF errors in container (Windows) | `run.sh` has Windows line endings | Convert to LF: `dos2unix run.sh` |
| Extra output files in `app/` | Leftover files from previous run or agent | Remove all non-required files from `app/` |
| `MAX_ZIP_DEPTH` exceeded | Files nested too deep inside ZIP | Flatten directory structure before zipping |

---

> **Summary:** The most frequent Real Coder submission failures are ZIP packaging errors (wrong nesting in `codebase.zip`) and unintended file modifications caused by AI agent auto-edits. The validation pipeline is strict and fails silently on structural issues. Always verify ZIP contents with `unzip -l`, always diff protected files after any agent session, and run `bash verification.sh` end-to-end before every submission.
