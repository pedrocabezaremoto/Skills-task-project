# Technical Deployment Protocol: Environment Validation and File Integrity

## 1. System Root Archetype and Directory Initialization

In containerized infrastructure, the establishment of a standardized root directory is a strategic imperative for ensuring predictable deployment cycles and agent reliability. Maintaining a rigid directory archetype is not merely a matter of organization; it is a critical defense against non-deterministic build artifacts. Any extraneous file present during image construction can lead to bloated layer sizes, unintended "globbing" into the container image, and potential security vulnerabilities.

The `app` folder is defined as the mandatory root for this environment. To ensure strict environment hygiene and prevent contamination, the directory must contain exactly the following items:

```text
app/
├── codebase.zip
├── tests.zip
├── Dockerfile
├── parsing.py
└── run.sh
```

**Technical Requirement**: Adhere to a "No more, no less" file constraint. The presence of any file or directory outside this list constitutes an immediate Validation Failure during the CI/CD initialization phase. This strict hygiene ensures that the agent operates within a lean, immutable environment where pathing conflicts are mathematically eliminated. Once the physical presence of these five assets is confirmed, the protocol shifts to the technical validation of internal data packaging.

## 2. ZIP Compression Protocols and Internal Data Mapping

The methodology utilized for ZIP compression directly impacts automated extraction layers and system compatibility. Because deployment scripts rely on specific directory offsets, specific compression techniques are non-negotiable. Failure to follow these mapping protocols will result in pathing errors during the evaluation phase.

The following matrix defines the immutable standards for archive preparation:

### Compression Methodology Matrix

| Target File | Required Internal Structure / Action |
|---|---|
| `tests.zip` | **Zip the folder itself**: The root level of the archive must contain the `tests/` directory. |
| `codebase.zip` | **Zip the contents only**: Execute the compression command from within the codebase directory to ensure the root level of the ZIP contains the source files directly, with no parent folder wrapping. |

> [!WARNING]
> Critical failure occurs if `codebase.zip` is recursively nested (e.g., `codebase.zip` → `codebase/` → `files`). To maintain system compatibility, the structure must be `codebase.zip` → `files`.

Correct data packaging ensures that the extraction logic places assets in their expected offsets, enabling accurate environment variable mapping.

## 3. Host Environment Configuration and Variable Mapping

Environment variables serve as the "source of truth," bridging host-to-container paths. For evaluation scripts to function, these **Immutable Host-to-Container Mappings** must be explicitly defined and verified.

**Prerequisite**: All input files listed below must physically exist at the specified `APP_DIR` path prior to script execution. Absence of any asset will trigger an immediate termination of the deployment protocol.

* `APP_DIR`: `/home/abhisek007/mattock_code/task1_nabid_review_copy/app` (The primary host location).
* `DOCKERFILE`: `${APP_DIR}/Dockerfile`
* `TESTS_ZIP`: `${APP_DIR}/tests.zip`
* `CODEBASE_ZIP`: `${APP_DIR}/codebase.zip`
* `RUN_SCRIPT`: `${APP_DIR}/run.sh`
* `PARSE_SCRIPT`: `${APP_DIR}/parsing.py`
* `IMAGE_TAG`: `agent-evaluator:latest`
* `MAX_ZIP_DEPTH`: `3`

The `MAX_ZIP_DEPTH=3` constraint functions as a specialized "nesting guard." The system is configured to error out if ALL files within a ZIP archive are buried deeper than three levels (e.g., `dir1/dir2/dir3/file.py` is the limit). This fail-safe prevents redundant top-level directory wrapping and deep-path errors, ensuring extraction remains within the manageable scope of the deployment logic.

## 4. Agent Modification Constraints and Integrity Guardrails

While LLM-based agents (such as Cursor) provide "Auto-edit" capabilities, these features introduce significant risks to script integrity. To protect the evaluation environment, strict human-in-the-loop oversight is mandatory. Any attempt by an agent to refactor existing logic—even if the refactor is functionally sound—is a protocol violation and must be rejected to prevent architectural drift.

The following **Hard Constraints** are non-negotiable:

1. `run.sh` and `parsing.py`:
  * **Monitoring**: Continuous oversight is required when these files are open.
  * **Integrity Guard**: Absolutely no modifications are permitted in any section labeled "DO NOT MODIFY."
2. `verification.sh`:
  * **Permitted Entry Point**: You are permitted to edit one section only: your local Path.
  * **Lockdown**: No other lines in this file may be updated, moved, or deleted.
3. **Hallucination Prevention**: Agents are strictly prohibited from implementing "improvements" or unsolicited architectural changes to the evaluation logic. The protocol demands adherence to the provided source code to ensure consistent results across all deployment nodes.

This protocol ensures the idempotency and cryptographic integrity of the evaluation environment, maintaining the total stability of the deployment package from initialization to execution.
