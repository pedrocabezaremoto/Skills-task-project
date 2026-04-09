# task2 — Outlier Real Coder | New Task Workspace

Test of the new modular structure for Real Coder tasks.
Based on: `code-real-reorganization-proposal.md` + `sop-technical-prompt.md`

---

## Structure

```
task2/
├── knowledge-base/          # Permanent knowledge — guides, SOP, reference
│   ├── official-guides/     # G1-G10 official guides (add as needed)
│   ├── onboarding/          # Training docs
│   ├── sop/                 # Standard Operating Procedures
│   │   └── sop-validation-workflow.md   ← MAIN SOP (read this first)
│   └── reference/           # master-guide, checklists, rubric template
│
├── templates/               # Reusable files for every task
│   ├── docker/              # Dockerfile.template
│   ├── scripts/             # run.sh.template, parsing.py.template
│   ├── prompts/             # prompt-pattern-a.md, prompt-pattern-b.md
│   └── testing/             # pytest templates
│
├── workspace/               # Active task work area
│   └── task-{id}-{nombre}/  # One folder per task
│       ├── TASK.md          # Task metadata and timeline
│       ├── fase-1-prompt/   # Prompt engineering
│       ├── fase-2-tdd/      # Test-Driven Development
│       ├── fase-3-rubrics/  # Expert rubrics
│       ├── fase-4-golden-patch/  # Implementation
│       ├── fase-5-validation/   # Docker F2P validation
│       ├── fase-6-submission/   # Final deliverables
│       └── logs/            # Decisions, errors, time tracking
│
└── archive/                 # Completed tasks
    └── 2026-q1/
```

---

## How to Start a New Task

```bash
# 1. Copy workspace template
cp -r workspace/task-{id}-{nombre} workspace/task-NEWID-taskname

# 2. Fill in TASK.md metadata
# 3. Copy seeded prompt to fase-1-prompt/inputs/
# 4. Work through phases 1-6 in order
# 5. When done, move to archive/
mv workspace/task-NEWID-taskname archive/2026-q1/
```

## Key Rules (from SOP)
- before.json must be 100% FAILED (F2P baseline)
- after.json must be 100% PASSED (golden patch)
- Overfitting < 5% of tests
- Prompt must follow Pattern A or Pattern B
- 5 files exactly in /app, all LF endings
- All timestamps within 5 minutes
