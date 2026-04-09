# SKILL: Real Coder — Docker Environment Setup & Execution Reference

> **Version:** 1.0 | **Source:** Real Coder — Guide 4 (Docker Instructions, created Feb 24, 2026)  
> **Scope:** Authoritative technical reference for configuring, running, and validating the Docker environment used in all Real Coder task submissions. Deviating from this spec breaks the evaluation pipeline.

---

## 1. Core Principle

> ⚠️ **The validation script depends on a strict directory and file structure. Any unintended deviation will break the evaluation process and may fail your task.**

All code must execute inside an **Ubuntu 22.04 Docker container** using three standardized files:

| File | Role | Editable? |
|---|---|---|
| `Dockerfile` | Defines the container image and installs dependencies | ✅ Dependencies section only |
| `run.sh` | Executes the full test suite inside the container | ✅ Configure section only |
| `parsing.py` | Parses test output into a structured JSON result | ✅ Parsing logic section only |

---

## 2. Dockerfile — Canonical Template

```dockerfile
###############################################
# BASE IMAGE
###############################################
FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive

###############################################
# SYSTEM DEPENDENCIES
###############################################
RUN apt-get update && apt-get install -y \
    git \
    python3 \
    python3-pip \
    python3-setuptools \
    python-is-python3 \
    unzip \
    && rm -rf /var/lib/apt/lists/*

###############################################
# WORKING DIRECTORY + GIT SETUP
###############################################
WORKDIR /app
RUN git init \
    && git config --global user.email "agent@example.com" \
    && git config --global user.name "Agent" \
    && echo "# Workspace" > README.md \
    && git add README.md \
    && git commit -m "Initial commit"

###############################################
# EVALUATION ASSETS DIRECTORY
###############################################
# Populated at RUNTIME by the evaluation script.
RUN mkdir -p /eval_assets
CMD ["/bin/bash"]
```

### 2.1 What You MAY Change

- Add `apt-get install` packages inside the `SYSTEM DEPENDENCIES` block.
- Add `pip install` or language-specific package manager commands (e.g., `npm install`, `cargo install`) as a new labeled block after `SYSTEM DEPENDENCIES`.

### 2.2 What You MUST NOT Change

| Prohibited Action | Reason |
|---|---|
| Modify the file structure or section order | Breaks the evaluation pipeline. |
| Remove any existing instruction | Breaks Git setup or eval assets directory. |
| Add unrelated layers or steps | Introduces unpredictable behavior. |
| Change `WORKDIR`, `CMD`, or entry points | Breaks the validation script's assumptions. |
| Use `COPY` to inject solution files | Solution files are injected at runtime, not build time. |

---

## 3. run.sh — Canonical Template

```bash
#!/bin/bash
### COMMON SETUP; DO NOT MODIFY ###
set -e

# --- CONFIGURE THIS SECTION ---
# Replace this with your command to run all tests
run_all_tests() {
    echo "Running all tests..."
    # TODO: Replace with your actual test runner command
    # Examples:
    #   pytest tests/ -v --tb=short --no-header
    #   cargo test --workspace --lib --no-fail-fast
    #   npm test
    #   go test ./...
}
# --- END CONFIGURATION SECTION ---

### COMMON EXECUTION; DO NOT MODIFY ###
run_all_tests
```

### 3.1 Rules

- Only edit code **between** `# --- CONFIGURE THIS SECTION ---` and `# --- END CONFIGURATION SECTION ---`.
- The `run_all_tests()` function must invoke your full test suite and produce output that `parsing.py` can parse.
- Do **not** modify `set -e` or the final `run_all_tests` call.
- If `bash run.sh` produces no output or errors inside the container, fix `run.sh` before proceeding.

---

## 4. parsing.py — Canonical Template

### 4.1 Fixed Header (DO NOT MODIFY)

```python
import dataclasses
import json
import sys
from enum import Enum
from pathlib import Path
from typing import List

class TestStatus(Enum):
    """The test status enum."""
    PASSED = 1
    FAILED = 2
    SKIPPED = 3
    ERROR = 4

@dataclasses.dataclass
class TestResult:
    """The test result dataclass."""
    name: str
    status: TestStatus

### DO NOT MODIFY THE CODE ABOVE ###
```

### 4.2 Your Implementation Zone

```python
### Implement the parsing logic below ###

def parse_test_output(stdout_content: str, stderr_content: str) -> List[TestResult]:
    """
    Parse the test runner output and return a list of TestResult objects.

    Args:
        stdout_content: Full stdout string from run.sh execution.
        stderr_content: Full stderr string from run.sh execution.

    Returns:
        List of TestResult with name (str) and status (TestStatus).

    Implementation notes:
    - Parse the test runner output format specific to your framework
      (pytest, cargo test, jest, go test, etc.)
    - Map runner-specific outcomes to TestStatus.PASSED / FAILED / SKIPPED / ERROR
    - Each test must have a unique, stable name (typically: file::class::method)
    - Do not raise NotImplementedError — replace it with your parsing logic
    """
    raise NotImplementedError('Implement the test output parsing logic')

### Implement the parsing logic above ###
```

### 4.3 Fixed Footer (DO NOT MODIFY)

```python
### DO NOT MODIFY THE CODE BELOW ###

def export_to_json(results: List[TestResult], output_path: Path) -> None:
    json_results = {
        'tests': [
            {'name': result.name, 'status': result.status.name}
            for result in results
        ]
    }
    with open(output_path, 'w') as f:
        json.dump(json_results, f, indent=2)

def main(stdout_path: Path, stderr_path: Path, output_path: Path) -> None:
    with open(stdout_path) as f:
        stdout_content = f.read()
    with open(stderr_path) as f:
        stderr_content = f.read()
    results = parse_test_output(stdout_content, stderr_content)
    export_to_json(results, output_path)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: python parsing.py <stdout_file> <stderr_file> <output_json>')
        sys.exit(1)
    main(Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]))
```

### 4.4 Expected JSON Output Format

```json
{
  "tests": [
    { "name": "tests/test_module.py::TestClass::test_method", "status": "FAILED" },
    { "name": "tests/test_module.py::TestClass::test_other",  "status": "PASSED" }
  ]
}
```

- **Before Golden Patch:** every `status` must be `"FAILED"`.
- **After Golden Patch:** every `status` must be `"PASSED"`.
- `"ERROR"` on baseline is **not acceptable** — fix your test setup until all tests genuinely FAIL.

---

## 5. Execution Workflow

### 5.1 Commands (run from the project root where Dockerfile is located)

```bash
# Step 1 — Build the Docker image
docker build -t real-coder-task-1 .

# Step 2 — Launch an interactive shell inside the container
docker run -it real-coder-task-1:latest /bin/bash

# Step 3 — Inside the container: run the test suite
bash run.sh

# Step 4 — List available images if you lose track of image names
docker images
```

### 5.2 Execution Sequence Per Phase

| Phase | What to Run | Expected Result |
|---|---|---|
| **Baseline (Before)** | `run.sh` + `parsing.py` on empty codebase | All tests → `FAILED` |
| **Verification (After)** | `run.sh` + `parsing.py` with Golden Patch applied | All tests → `PASSED` |

### 5.3 Running parsing.py Manually

```bash
# Inside the container, after run.sh has been executed:
python parsing.py stdout.txt stderr.txt result.json
```

---

## 6. Required File Structure in `/app`

```
/app/
├── Dockerfile          # Image definition (template-based)
├── codebase.zip        # Golden Patch (injected at runtime by eval script)
├── tests.zip           # Test suite (injected at runtime by eval script)
├── run.sh              # Test runner script (template-based)
└── parsing.py          # Output parser (template-based)
```

> The `/eval_assets` directory is populated **at runtime** by the evaluation script. Do not pre-populate it.

---

## 7. Common Errors & Fixes

| Symptom | Root Cause | Fix |
|---|---|---|
| `bash run.sh` produces no output | Test runner command not configured | Implement `run_all_tests()` in `run.sh` with your framework's command. |
| `bash run.sh` throws an error | Dependency not installed | Add missing package to Dockerfile dependencies block; rebuild image. |
| Tests show `ERROR` instead of `FAILED` on baseline | Import errors or missing modules due to empty codebase | Add stub files or adjust test imports so they fail gracefully (assertion failure, not crash). |
| `parsing.py` produces empty `tests` array | Parser doesn't match test runner output format | Debug by printing `stdout_content` inside `parse_test_output` and adjusting regex/parsing logic. |
| Validation script fails | File structure not as expected | Ensure `/app` contains exactly: `Dockerfile`, `codebase.zip`, `tests.zip`, `run.sh`, `parsing.py`. |
| Image name conflict | Reused image name across tasks | Use unique image names per task: `real-coder-task-N`. |

---

## 8. Framework-Specific run.sh Examples

### Python / pytest

```bash
run_all_tests() {
    echo "Running all tests..."
    cd /app
    python -m pytest tests/ -v --tb=short --no-header 2>&1
}
```

### Node.js / Jest

```bash
run_all_tests() {
    echo "Running all tests..."
    cd /app
    npm test -- --verbose 2>&1
}
```

### Rust / Cargo

```bash
run_all_tests() {
    echo "Running all tests..."
    cd /app
    cargo test --workspace --lib --no-fail-fast 2>&1
}
```

### Go

```bash
run_all_tests() {
    echo "Running all tests..."
    cd /app
    go test ./... -v 2>&1
}
```

---

## 9. Framework-Specific parsing.py Examples

### pytest output parser

```python
import re

def parse_test_output(stdout_content: str, stderr_content: str) -> List[TestResult]:
    results = []
    seen = set()
    combined = stdout_content + "\n" + stderr_content

    pattern = re.compile(
        r'^(tests/[\w/\.]+::[\w:]+)\s+(PASSED|FAILED|ERROR|SKIPPED)',
        re.MULTILINE
    )
    for match in pattern.finditer(combined):
        name, raw_status = match.group(1), match.group(2)
        if name in seen:
            continue
        seen.add(name)
        status_map = {
            'PASSED':  TestStatus.PASSED,
            'FAILED':  TestStatus.FAILED,
            'ERROR':   TestStatus.ERROR,
            'SKIPPED': TestStatus.SKIPPED,
        }
        results.append(TestResult(name=name, status=status_map[raw_status]))
    return results
```

---

## 10. Key Non-Negotiables

1. Use the **canonical Dockerfile template** — no structural modifications.
2. Never use `COPY` to inject solution or test files into the image.
3. `run.sh` must exit cleanly; modify only the `CONFIGURE` section.
4. `parsing.py` must only implement `parse_test_output()` — all other code is immutable.
5. Baseline run must produce all `FAILED` statuses — `ERROR` is not acceptable.
6. After Golden Patch, all statuses must be `PASSED`.
7. Run all Docker commands from the **project root** where `Dockerfile` is located.
8. Use unique, task-specific image names to avoid cross-task conflicts.
