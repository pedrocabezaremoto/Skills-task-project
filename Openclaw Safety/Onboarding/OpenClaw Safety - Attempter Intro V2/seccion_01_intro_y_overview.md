# OpenClaw Safety — Attempter Intro V2
## Sección 1: Welcome + Brief Overview + Getting Running + Workflow + Constraints

---

## Slide 1 — Welcome
**Proyecto:** OpenClaw Safety  
**Rol:** Attempter  
**Curso:** Attempter Intro V2 (7 sections, 38 min)

---

## Slide 2 — Brief Overview

**What you'll do:**
- Design realistic tasks for an agent with a verifiable final artifact
- Run the same task across **6 models** to compare
- Evaluate each model against a rubric
- Rank the models and annotate safety issues

---

## Slide 3 — Getting OpenClaw Running

Each task must require **coordination across systems in at least 3 stages:**

### 1. Data acquisition (retrieve/read something real)
- Read a Google Sheet or CSV
- Pull data from web sources
- Download and parse a policy doc
- Collect evidence to justify decision

### 2. Processing / reasoning (normalize, compare, decide)
- Clean messy fields and normalize units or currency
- Merge or dedupe records across sources
- Apply explicit ranking rules
- Ask clarifying questions

### 3. Output generation (produce a structured artifact)
- Export a ranked table with reasons and evidence links
- Generate a review-ready report or memo with citations
- Produce a checklist or action plan

---

## Slide 4 — Workflow Overview (6 steps)

| Step | Action | Description |
|------|--------|-------------|
| 1 | **Design the agent objective** | Define scope, constraints and complexity |
| 2 | **Validate the idea** | Ensure it meets the minimum architectural bar |
| 3 | **Run the preference test (6 models)** | Generate comparable trajectories |
| 4 | **Extract trajectories** | Submit evaluation artifacts |
| 5 | **Evaluate performance** | Apply a task-specific rubric consistently |
| 6 | **Rate and rank** | Produce the final ordering (and verify it makes sense) |

---

## Slide 5 — Constraints

### Live environments only
- Use **real, live tools/services** (no mocked apps, nor simulated UIs)
- No fake personas or simulated actions — the model must NOT "pretend" it logged in, contacted someone, or executed an external action
- Use your own **test/fake accounts** for any required logins

### Session persistence
- Do **not** force-end sessions if you want the trajectory to remain extractable
- When a run is finished, **close the tab normally**
- If you need to continue later, **reopen and resume the conversation**
