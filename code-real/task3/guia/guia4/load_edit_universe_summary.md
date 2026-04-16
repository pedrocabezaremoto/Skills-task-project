# Guide 4 Summary — Load & Edit Universe

## Change Log

| Date | Type | Description |
|---|---|---|
| April 10, 2026 | New Universe! | Keystone Mortgage Universe launched |
| April 7, 2026 | Environment ID | New ID: `moveops-multienv-4-3-v2` |
| Mar 23, 2026 | Universe ID | New ID: `mcp-advanced-3-20-moveops-metadata` |
| Mar 6, 2026 | Environment ID | New ID: `2t1vdo-multi` |

---

## Universe IDs — Current Active Values

### MoveOps Universe
- **Environment ID:** `moveops-multienv-4-3-v2`
- **Base Universe ID:** `mcp-advanced-3-20-moveops-metadata`

### Keystone Mortgage Universe
- **Environment ID:** `mortgage-broker-v1`
- **Base Universe ID:** `mortgage-broker-01-keystone`

> When you claim a task, it will be pre-filled automatically with Environment ID and Base Universe ID. Use a previous modified Universe ID if you want continuity with your prior edits.

---

## Loading the Universe

1. Claim the task — IDs are pre-filled automatically.
2. Click **"Create & Load"** to deploy the environment.
3. To reuse a previously modified universe, enter that snapshot ID instead of the base ID.

---

## Editing the Universe

Two methods available:

### 1. ChatBot Agent (recommended)
- Use the chatbot for **exploration and edits**.
- Changes are reflected in **both** the ChangeLog (sandbox) and the Explorer page.
- The chatbot can also **summarize the changelog** and **revert changes**.

### 2. SQL Viewer
- Make direct SQL queries in the sandbox's SQL viewer.
- More technical, but functional.
- ChatBot is easier and preferred.

> After running agent trajectories, the universe is snapshotted into a new ID (e.g., `snapshot-multi-caf64d-74942ace`). Use this snapshot ID to load the same edited universe in another task.

---

## Running the Agent

1. After exploring/editing the universe and finalizing your prompt, click **"Run Agent"**.
2. Use **Haiku** for fast iteration during prompt development.
3. Use **Opus 4.6** for final complexity validation and task submission.
4. **At least 4 out of 6 agent runs must complete successfully.**
5. Changes during agent runs are reflected in the ChangeLog under "universe end state".
   - No Universe Explorer for end state yet.
   - No ChatBot for end state yet.

---

## Running the Rubric Verifiers

1. If you see a "re-save" warning — re-save the agent step before continuing.
2. **Must have used Claude Opus** when running the agent before verifying rubrics.
3. **Pass@k must be: 0 < score ≤ 0.4** (aim for 40+ tool calls per run).
4. **At least 4 out of 6 verifiers must run successfully.**
5. Final submission must use **Opus 4.6** (Haiku is only for fast iteration).

---

## Workflow Summary

```
Claim task
    → Load universe (pre-filled IDs or snapshot ID)
    → Explore & edit (ChatBot or SQL)
    → Run Agent with Haiku (iterate prompt)
    → Run Agent with Opus 4.6 (finalize)
    → Run Rubric Verifiers (4/6 must pass, pass@k ≤ 0.4)
    → Submit
```

---

## Key Rules to Remember

- Always use **Opus 4.6** for final agent runs and rubric verification.
- Haiku is only for **fast iteration** — do not submit with Haiku results.
- Minimum **4/6 runs** must succeed (agent runs AND rubric verifiers).
- Target **40+ tool calls** per task to meet difficulty requirements.
- If reusing a modified universe, enter the **snapshot ID**, not the base ID.
