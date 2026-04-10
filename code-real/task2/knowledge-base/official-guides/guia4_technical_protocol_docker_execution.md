# Technical Protocol: Real Coder Docker Environment Setup and Execution

## 1. Strategic Overview and Environment Initialization

This protocol defines the definitive technical requirements for establishing the standardized Docker environment for the Real Coder project. As a Senior DevOps Architect, I am mandating this configuration to ensure an immutable, isolated workspace where automated validation scripts function without environmental interference or "it works on my machine" discrepancies. Precision is the primary objective; the evaluation framework depends on the exact reproduction of this environment to maintain the integrity of the results.

### Document Metadata
* **Creation Date**: February 24, 2026
* **Primary Objective**: Standardize containerized execution for dependency installation, shell-based test automation, and JSON-formatted result parsing.

Adherence to the following specifications is critical. Any deviation from these configurations may result in a failure of the validation pipeline and a subsequent zero-score evaluation.

---

## 2. Component Architecture: The Dockerfile Specification

The Dockerfile is the foundational blueprint for our containerization strategy. It ensures that every agent operates within a bit-identical OS layer. The following structure is required to ensure that the validation scripts can locate assets and execute commands at predictable, hard-coded paths.

### Dockerfile Technical Requirements

| Section | Requirement | Technical Detail |
|---|---|---|
| Base Image | Ubuntu 22.04 | Must include `ENV DEBIAN_FRONTEND=noninteractive` to prevent build-time stalls. |
| System Dependencies | Core Binaries | `apt-get update && apt-get install -y git python3 python3-pip python3-setuptools python-is-python3 unzip && rm -rf /var/lib/apt/lists/*` |
| Virtual Environment | Python Isolation | Create and use a virtual environment via `RUN python3 -m venv /opt/venv`. |
| Python Libraries | Data & Vision | `pip install "numpy>=1.24,<3" "opencv-python"`. |
| Working Directory | `/app` | The primary context for all codebase operations. |
| Asset Storage | `/eval_assets` | Created via `mkdir -p /eval_assets` for runtime evaluation injection. |
| Entry Point | `/bin/bash` | Default command to provide an interactive shell environment. |

### Working Directory + Git Setup

The environment requires a valid Git repository within the `/app` directory to support version-control-dependent logic. The engineer MUST execute the following concatenated command to ensure identical layer construction:

```dockerfile
RUN git init \
    && git config --global user.email "agent@example.com" \
    && git config --global user.name "Agent" \
    && echo "# Workspace" > README.md \
    && git add README.md \
    && git commit -m "Initial commit"
```

The `/eval_assets` directory is reserved for assets populated at runtime by the evaluation script. This directory's existence is a prerequisite for the final validation phase.

---

## 3. Execution and Logic Layer: `run.sh` and `parsing.py` Templates

Successful execution relies on the seamless integration between shell-level execution and Python-based result parsing.

### `run.sh` Configuration

The `run.sh` script utilizes protected zones to maintain shell stability.

* **Mandatory Wrappers**: The sections labeled `### COMMON SETUP; DO NOT MODIFY ###` (which includes `set -e`) and `### COMMON EXECUTION; DO NOT MODIFY ###` must remain untouched.
* **Implementation**: The engineer must implement the `run_all_tests()` function. Based on the system execution logs, the preferred test framework is `pytest`.

### `parsing.py` Implementation

The parsing logic transforms raw stdout and stderr into a structured JSON schema. The following components are strictly non-negotiable:

* **TestStatus Enum**: `PASSED = 1`, `FAILED = 2`, `SKIPPED = 3`, `ERROR = 4`.
* **TestResult Dataclass**: Maps the test name to its status.

**Architectural Directive**: You MUST implement the `parse_test_output` function to extract results from the test logs. You are prohibited from altering the boilerplate code, including the `TestStatus` Enum, `TestResult` dataclass, `export_to_json` function, or the main entry point. The validation script expects this exact mapping for successful scoring.

---

## 4. Operational Workflow: Build and Deployment Procedures

Organization during the build phase is paramount. All commands must be executed from the project root directory where the Dockerfile is located.

### Execution Guide

1. **Image Construction**: Build the Docker image using the `-t` flag. Use the standardized naming convention for the task.
   * Command: `docker build -t real-coder-task-1 .`
2. **Container Instantiation**: Launch the container in an Interactive Terminal (`-it`) to access the bash environment.
   * Command: `docker run -it real-coder-task-1:latest /bin/bash`
   * Significance: The `latest` tag ensures you are testing the most recent build of the task environment.
3. **Test Execution**: Trigger the execution and parsing logic from within the active container shell.
   * Command: `bash run.sh`

> [!IMPORTANT]
> **System Audit**: If you lose track of the specific image version, execute the `docker images` command. This is an essential auditing step to ensure the active container is derived from the correct task image.

---

## 5. Compliance Framework and Prohibited Actions

Configuration drift—the unintended divergence of the environment from the specified protocol—invalidates the environment's hash-sum and will result in a zero-score evaluation.

### Prohibited Actions Checklist

* [ ] Do not modify the fundamental structure of the provided Dockerfile.
* [ ] Do not remove existing instructions or environment variables (e.g., `DEBIAN_FRONTEND`).
* [ ] Do not add unrelated layers or steps that increase image complexity.
* [ ] Do not change the entry points or default commands (keep `/bin/bash`).
* [ ] Do not edit the "DO NOT MODIFY" sections in `run.sh` or `parsing.py`.

### Final Technical Directive

Full operational compliance is only achieved when all "Golden solution files" and the complete "test suite" are present within the environment. Failure to ensure these assets are in place prior to execution will result in an invalid evaluation.
