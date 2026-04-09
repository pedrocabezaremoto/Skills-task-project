# Real Coder – Docker & Validation Technical Reference
> **Project:** Real Coder | **Platform:** Outlier  
> **Scope:** Docker environment setup, validation workflow, and submission pipeline  
> **Audience:** Senior developers working on Real Coder tasks

---

## Table of Contents

1. [Architecture Overview](#1-architecture-overview)
2. [Environment Prerequisites](#2-environment-prerequisites)
3. [Dockerfile Contract](#3-dockerfile-contract)
4. [Project Directory Structure](#4-project-directory-structure)
5. [Validation Pipeline](#5-validation-pipeline)
6. [run.sh & parsing.py Contract](#6-runsh--parsingpy-contract)
7. [Docker Workflow — Mac](#7-docker-workflow--mac)
8. [Docker Workflow — Windows](#8-docker-workflow--windows)
9. [Expected Output & Success Criteria](#9-expected-output--success-criteria)
10. [Troubleshooting Reference](#10-troubleshooting-reference)
11. [Quick Command Reference](#11-quick-command-reference)

---

## 1. Architecture Overview

The Real Coder evaluation system follows a **build-once, mount-at-runtime** Docker pattern. The container image is responsible exclusively for the execution environment (OS, system packages, Python runtime, dependencies). Project code is never baked into the image — it is injected via volume mounts at runtime.

```
┌─────────────────────────────────────────┐
│           Docker Image (build-time)     │
│  ubuntu:22.04 base                      │
│  + system packages (apt)                │
│  + Python 3.14 venv + pip deps          │
│  + git, curl, unzip, tooling            │
└───────────────────┬─────────────────────┘
                    │ docker run -v $(pwd):/app
          ┌─────────▼──────────────┐
          │  /app  (runtime mount) │
          │  ├── codebase/         │  ← agent's submitted code
          │  ├── tests/            │  ← hidden test suite
          │  ├── run.sh            │  ← test runner
          │  └── parsing.py        │  ← output parser
          └────────────────────────┘
```

The **validation script** (`validation.sh`) orchestrates two sequential test runs:

- **Before run** → empty `/app` → all tests must **FAIL** (baseline)
- **After run** → agent's `codebase.zip` injected → all tests must **PASS** (golden patch)

---

## 2. Environment Prerequisites

### Mac
| Requirement | Notes |
|---|---|
| Docker Desktop | Apple Silicon (M1/M2/M3/M4) or Intel. Download from docker.com |
| Terminal | Built-in Terminal app (Applications → Utilities → Terminal) |

```bash
# Verify Docker is running
docker --version
docker info --format '{{.ServerVersion}}'
```

### Windows
| Requirement | Notes |
|---|---|
| Docker Desktop | WSL2 backend **must** be enabled during install |
| Terminal | PowerShell (recommended), Git Bash, or WSL Ubuntu shell |

```powershell
# Verify Docker
docker --version
```

> **WSL2 setup (Windows):** `wsl --install -d Ubuntu` → reboot → enable Docker WSL Integration in Docker Desktop Settings → Resources → WSL Integration.

---

## 3. Dockerfile Contract

### 3.1 Base Template (Do NOT alter)

```dockerfile
########################################
# BASE IMAGE
########################################
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

########################################
# SYSTEM DEPENDENCIES
########################################
RUN apt-get update && apt-get install -y \
    git \
    curl \
    unzip \
    openssh-client \
    software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get update && apt-get install -y \
    python3.14 \
    python3.14-venv \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

########################################
# CREATE VENV AT /opt/venv
########################################
RUN python3.14 -m venv /opt/venv \
    && /opt/venv/bin/pip install --upgrade pip "setuptools>=61.0" \
    && /opt/venv/bin/pip install --no-cache-dir \
        "click>=8.0" \
        "paramiko>=3.0" \
        "pyyaml>=6.0" \
        "rich>=13.0" \
        "pytest>=9.0.2"

ENV PATH="/opt/venv/bin:${PATH}"

RUN ln -sf /opt/venv/bin/python3.14 /usr/local/bin/python3 \
    && ln -sf /opt/venv/bin/python3.14 /usr/local/bin/python

########################################
# WORKING DIRECTORY + GIT SETUP
########################################
WORKDIR /app
ENV PYTHONPATH=/app

RUN git init \
    && git config --global user.email "agent@example.com" \
    && git config --global user.name "Agent" \
    && echo "# Workspace" > README.md \
    && git add README.md \
    && git commit -m "Initial commit"

########################################
# EVALUATION ASSETS DIRECTORY
########################################
RUN mkdir -p /eval_assets

CMD ["/bin/bash"]
```

### 3.2 Allowed Modifications

Only add dependencies. Do not alter structure, order, comments, or existing instructions.

```dockerfile
# ✅ Allowed — after existing apt block
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# ✅ Allowed — after venv creation
RUN /opt/venv/bin/pip install --no-cache-dir \
    requests \
    numpy \
    pandas \
    pytest-asyncio
```

### 3.3 Forbidden Modifications

| Forbidden | Reason |
|---|---|
| `COPY` or `ADD` for project code | Code is always volume-mounted |
| Changing `FROM ubuntu:22.04` | Breaks base OS contract |
| Changing `WORKDIR /app` | Breaks path resolution |
| Modifying `ENV DEBIAN_FRONTEND=noninteractive` | Breaks non-interactive installs |
| Altering `CMD` or `ENTRYPOINT` | Breaks evaluation harness |
| Removing any existing lines | Breaks the established environment |
| Installing runtime deps in `run.sh` | Must be build-time only |

---

## 4. Project Directory Structure

### Validation Flow (evaluation-style)

```
Task_{task_number}/
├── app/                          # ← place all 5 required files here
│   ├── Dockerfile                # modified (deps only)
│   ├── tests.zip                 # hidden test suite (provided by task)
│   ├── codebase.zip              # agent's golden patch as zip
│   ├── run.sh                    # test runner (do not modify protected sections)
│   └── parsing.py                # output parser (do not modify protected sections)
└── validation.sh                 # evaluation orchestrator (outside app/)
```

### Codebase Flow (interactive development)

```
Task_{task_number}/
└── codebase/
    ├── Dockerfile
    ├── tests/                    # test suite
    ├── run.sh
    ├── parsing.py
    └── ... (project source files)
```

> **Critical:** `validation.sh` must remain **outside** the `app/` folder, at the project root.

---

## 5. Validation Pipeline

`validation.sh` performs a 6-step automated process:

```
Step 1 → Build Docker image from app/Dockerfile
Step 2 → Start container
Step 3 → Inject tests.zip + scripts into container
Step 4 → Run tests on empty /app (BEFORE)  →  before_stdout.txt, before_stderr.txt, before.json
Step 5 → Inject codebase.zip into /app
Step 6 → Run tests again (AFTER)           →  after_stdout.txt, after_stderr.txt, after.json
         Container auto-cleanup on exit
```

### Output files (all appear inside `app/`)

```
app/
├── before_stdout.txt
├── before_stderr.txt
├── before.json          ← baseline: expect FAILED
├── after_stdout.txt
├── after_stderr.txt
└── after.json           ← golden patch: expect PASSED
```

### Configuring validation.sh

Update `APP_DIR` to match your local path:

```bash
# Option A — absolute path
APP_DIR="/Users/youruser/path/to/project/app"

# Option B — relative (run from project root)
APP_DIR="$(pwd)/app"
```

### Running validation

```bash
# Make executable (once)
chmod +x validation.sh

# Execute from project root
bash validation.sh
```

---

## 6. run.sh & parsing.py Contract

### Rules

- **Do NOT** modify protected sections (marked `### DO NOT MODIFY ###`).
- Only update the *configure* and *parsing logic* sections if the task requires it.
- `run.sh` is a **Linux shell script** — must remain LF line endings (not CRLF on Windows).
- Dependencies must **never** be installed inside `run.sh` — all installs belong in `Dockerfile`.

### Expected JSON output from parsing.py

```json
{
  "tests": [
    { "name": "tests/test_auth.py::test_login",        "status": "PASSED" },
    { "name": "tests/test_auth.py::test_invalid_email","status": "FAILED" },
    { "name": "tests/test_auth.py::test_rate_limit",   "status": "FAILED" }
  ]
}
```

### Baseline vs. Golden Patch behavior

| Phase | Codebase state | Expected result |
|---|---|---|
| Before (baseline) | Empty `/app` | All tests **FAIL** (not ERROR) |
| After (golden patch) | Agent's code injected | All relevant tests **PASS** |

> Tests must **FAIL**, not **ERROR**. An error indicates a broken test setup; a failure indicates correct detection of missing implementation.

---

## 7. Docker Workflow — Mac

### Build image

```bash
# Navigate to codebase directory
cd ~/path/to/project/codebase

# Build Docker image
docker build -t real-coder-env .
```

### Run interactively (codebase-mounted)

```bash
docker run -it --rm \
  -v $(pwd):/app \
  real-coder-env bash
```

Inside the container:

```bash
chmod +x run.sh
./run.sh
python3 parsing.py
```

### Run full validation

```bash
# From project root (where validation.sh lives)
bash validation.sh
```

---

## 8. Docker Workflow — Windows

### PowerShell — Build image

```powershell
# From project root
docker build -t real-coder-env .\codebase
```

### PowerShell — Run interactively

```powershell
docker rm -f rc-test-run 2>$null | Out-Null

docker run --name rc-test-run `
  -v "${PWD}\codebase:/app" `
  -w /app `
  -it real-coder-env bash -lc "chmod +x run.sh && ./run.sh"

docker rm -f rc-test-run
```

### PowerShell — Run validation

```powershell
docker build -t real-coder-env .
docker run --rm -it -v "${PWD}:/app" -w /app real-coder-env bash -lc "./validation.sh"
```

### Git Bash — Run interactively

```bash
docker run --rm -it \
  -v "$PWD/codebase:/app" \
  -w /app \
  real-coder-env bash
```

### WSL Ubuntu — Run validation

```bash
# From directory containing validation.sh
bash ./validation.sh
```

### Windows CRLF Warning

`run.sh` and `parsing.py` must use **LF** line endings only. CRLF will cause:
```
python3\r: No such file or directory
```

Fix: Convert to LF in VS Code (bottom-right status bar) or with `dos2unix run.sh`. Add `.gitattributes` to enforce LF:
```
*.sh  text eol=lf
*.py  text eol=lf
```

---

## 9. Expected Output & Success Criteria

### before.json — Correct baseline (all FAILED)

```json
{
  "tests": [
    { "name": "tests/test_feature.py::test_case_one", "status": "FAILED" },
    { "name": "tests/test_feature.py::test_case_two", "status": "FAILED" }
  ]
}
```

### after.json — Correct golden patch (all PASSED)

```json
{
  "tests": [
    { "name": "tests/test_feature.py::test_case_one", "status": "PASSED" },
    { "name": "tests/test_feature.py::test_case_two", "status": "PASSED" }
  ]
}
```

### Evaluation checklist

- [ ] Docker image builds without errors
- [ ] `before.json` shows all tests as `FAILED` (not `ERROR`)
- [ ] `after.json` shows all tests as `PASSED`
- [ ] `Dockerfile` uses no `COPY` or `ADD` for project code
- [ ] `run.sh` has LF line endings
- [ ] `codebase.zip` is not nested deeper than `MAX_ZIP_DEPTH=3`
- [ ] No extra files in `app/` beyond the 5 required

---

## 10. Troubleshooting Reference

| Symptom | Cause | Fix |
|---|---|---|
| `docker: command not found` | Docker Desktop not running | Open Docker Desktop first; restart Terminal |
| Build permission error (Mac) | Docker permissions not accepted | Accept permissions in Docker Desktop prompts |
| Slow first build on M1/M2/M3 | ARM emulation overhead | Normal — caching speeds up subsequent builds |
| `python3\r: No such file or directory` (Windows) | CRLF line endings in shell scripts | Convert `run.sh` and `parsing.py` to LF |
| Mount path error in PowerShell | Unix-style path in PowerShell context | Use `"${PWD}\codebase:/app"` not `$PWD/codebase` |
| Tests not found at runtime | Path resolution in `run.sh` | Ensure `run.sh` checks both `/eval_assets/tests` and `/app/tests`; use `SCRIPT_DIR` pattern |
| Runtime import errors (all tests ERROR) | Missing pip package in Dockerfile | Scan test imports → add to Dockerfile → rebuild |
| Validation build error (vague) | `COPY` command in Dockerfile | Remove `COPY`; use volume mount `-v` instead |
| `before.json` shows ERROR not FAILED | Test setup issue / missing module | Ensure all dependencies are installed at build time |
| Zip nesting too deep | `codebase.zip` has extra wrapper folder | Rezip so files appear at depth ≤ 3 from root |

---

## 11. Quick Command Reference

```bash
# ── DOCKER FUNDAMENTALS ────────────────────────────────────────

# Build image (from directory containing Dockerfile)
docker build -t real-coder-env .

# Run interactively with codebase mounted
docker run -it --rm -v $(pwd):/app real-coder-env bash

# Run and auto-remove after exit
docker run --rm real-coder-env bash -c "./run.sh"

# Stop all running containers (emergency)
docker stop $(docker ps -q)


# ── VALIDATION WORKFLOW ────────────────────────────────────────

# Mac / Linux / WSL
chmod +x validation.sh
bash validation.sh

# PowerShell (Windows)
docker run --rm -it -v "${PWD}:/app" -w /app real-coder-env bash -lc "./validation.sh"


# ── INSIDE THE CONTAINER ───────────────────────────────────────

chmod +x run.sh
./run.sh
python3 parsing.py


# ── VERIFY DOCKER ──────────────────────────────────────────────

docker --version
docker info --format '{{.ServerVersion}}'


# ── WSL SETUP (Windows only) ───────────────────────────────────

wsl --install -d Ubuntu
wsl --list --verbose
wsl --update
wsl --set-default-version 2
```

---

> **Summary:** The Real Coder evaluation pipeline is a strict contract. The Docker image defines the environment; code is always mounted at runtime. `validation.sh` runs tests twice — before and after your golden patch — producing JSON results that are compared for FAIL → PASS transitions. Any deviation from the Dockerfile structure, the directory layout, or the `run.sh`/`parsing.py` contracts will break evaluation silently or with cryptic errors. Adhere precisely to the rules in this document.
