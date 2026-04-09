# Phase 5: F2P Docker Validation

## Objective
Run automated F2P validation in Docker to produce before.json (all FAILED) and after.json (all PASSED).

## /app Directory (exactly 5 files required)
- [ ] `app/Dockerfile` — ubuntu:22.04, no COPY for project code
- [ ] `app/run.sh` — LF line endings
- [ ] `app/parsing.py` — LF line endings
- [ ] `app/tests.zip` — tests/ as first-level dir
- [ ] `app/codebase.zip` — flat structure, no nested folder

## Outputs
- `outputs/before.json` — 100% FAILED (empty codebase)
- `outputs/after.json` — 100% PASSED (golden patch)
- `outputs/before_stdout.txt` — raw output log
- `outputs/after_stdout.txt` — raw output log
- `outputs/validation-report.md` — summary

## Execution
```bash
cd /path/to/{task-id}
bash validation.sh
```

## Timestamp Check
All 5 app/ files must have timestamps within 5 minutes of each other.

## Status
🔄 IN PROGRESS
