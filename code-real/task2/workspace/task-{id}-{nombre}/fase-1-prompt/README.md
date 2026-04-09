# Phase 1: Prompt Engineering

## Objective
Transform the seeded prompt into a structured rewritten prompt following Pattern A or B.

## Inputs
- `inputs/seeded-prompt.md` — Original task description from Outlier
- `inputs/task-description.txt` — Client brief

## Outputs
- `outputs/prompt-rewritten.md` — Final validated prompt
- `outputs/expected-interface.md` — Public interface documentation

## Iterations
- v1: First AI-generated version
- v2+: Corrections after linter/checker feedback

## Lessons Learned
- [ ] Always include explicit mathematical formulas
- [ ] Avoid "at least one" or "or" (breaks determinism)
- [ ] Verify tech stack has exact versions

## Status
🔄 IN PROGRESS
