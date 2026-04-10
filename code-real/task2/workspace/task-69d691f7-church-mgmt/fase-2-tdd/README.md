# Phase 2: Test-Driven Development (F2P)

## Objective
Create unit test suite that FAILS on empty codebase (before.json) and PASSES with Golden Patch (after.json).

## Inputs
- `inputs/prompt-rewritten.md` — Technical specification
- Requirements decomposition list

## Outputs
- `outputs/test_main.py` — pytest test suite
- `outputs/before.json` — Evidence of 100% FAILED on empty codebase
- `outputs/requirements-decomposition.md` — Mapped requirements

## Anti-Overfitting Strategy
- Tests only interact with Expected Interface
- No import path mocks
- No hardcoded names not specified in prompt

## Quality Gates
- [ ] 100% FAILED on empty codebase (before.json)
- [ ] Overfitting rate < 5%
- [ ] Every requirement has at least 1 test

## Status
🔄 IN PROGRESS
