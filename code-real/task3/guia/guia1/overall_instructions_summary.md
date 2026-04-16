# Overall Instructions — Technical Summary
**Source:** Overall Instructions (Last Updated: Apr 10, 2026)

---

## Key Changes (Change Log)

| Date | Type | What Changed |
|---|---|---|
| Apr 10, 2026 | New Universe | Keystone Mortgage Partners — rolls out with v2.2 tasks |
| Apr 07, 2026 | Resource | Scenario Generation **disabled** temporarily |
| Mar 12, 2026 | Rubrics | Outcome-first workflow; simplified outcome categories (5→3) |
| Mar 12, 2026 | Tool Call Count | Average 40+ tool calls required (not just one run) |
| Mar 12, 2026 | Failure Rate | 0% pass rate is acceptable if rubrics are high-quality |
| Mar 7, 2026 | Rubrics | Removed 'goal' text after tool name in Tool Selection rubrics |

---

## Goal

Create **complex tasks for an AI agent** operating inside fictional business companies. The agent has access to: email, Slack, Linear, calendar, CRM, and other work servers.

**Core objective:** Find situations where the agent **fails** — misses data, gets confused, makes wrong assumptions, or doesn't explore deeply enough.

**Hard requirements:**
- Average **40+ tool calls** across multiple services per task
- Task involves **investigation + action** (read data → reason → write actions)
- Agent must **fail on at least some rubric criteria**

---

## The Two Universes

### v2.1 and prior — MoveOps Universe
- B2B travel/relocation company, Wanderlust acquisition
- 20–40 employees
- **Fixed date: April 26, 2026**

### v2.2 and above — Keystone Mortgage Partners Universe
- Residential mortgage brokerage, Charlotte NC
- 30 employees, 8 departments
- **Fixed date: April 28, 2026**

---

## Step-by-Step Workflow

### Step 1: Understand the Universe
- Read the Universe Guide carefully (personas, scenarios, artifacts, business functions)
- Each CB has their own universe copy — edits are isolated
- The **persona shapes the task perspective**, not what data the agent can access (agent sees everything)

### Step 2: Explore and Edit the Universe
**Explore:**
- Search emails, Slack, Linear, CRM, contacts, Quickbooks
- Look for: mistakes, incomplete work, conflicting information, business pressure, hidden root causes

**Edit (add complexity):**
- Email threads creating new problems
- Linear issues to discover
- CRM deal status changes
- Slack messages with conflicting info
- Contacts with similar names (near-miss confusion)

> **Warning:** The edit agent is unconstrained — it won't detect conflicts or cascade changes. Review manually for universe consistency, storyline consistency, and cross-service coherence.

### Step 3: Write the Prompt

**Core rules:**
- Do NOT name tools or parameters in the prompt
- Do NOT pre-solve — agent must investigate and discover
- Do NOT use internal IDs
- Write naturally — like a real person talking to their assistant
- One coherent situation — all sub-requests flow from the same problem
- Agent must fail — if it solves everything, iterate

**Prompt patterns that create difficulty:**

| Pattern | Description |
|---|---|
| **Branching** | Agent decides based on findings, takes different paths |
| **Step-by-step dependency** | Must resolve A before B, B before C |
| **Stacking** | Multiple related asks with shared context (NOT bolting) |
| **Investigation + Action** | Figure it out, then do something about it |
| **Information Friction** | Answer is scattered across 3+ services |
| **Implicit Requirements** | Things the agent should obviously do but aren't stated |
| **Constraints** | Budget limits, policy requirements, approval needs |

**Good prompt example:**
> *"I'm reviewing our relocation coordinators and want to check how Fatimah Al-Rashidi is doing. Can you look at her recent work and tell me if everything looks good or if there are any concerns?"*

**Bad prompts:**
- Simple lookups (too few tool calls)
- Single-service tasks (no cross-service reasoning)
- Command lists (agent should figure out the steps)
- Tasks solvable from general knowledge (no tools needed)
- Contrived/artificial scenarios

### Step 3.5: Plan Oracle Events (OEs)
Before running the agent, write the key steps a correct agent would take.

For each OE note:
- What action needs to happen
- What information needs to be discovered
- What tool would be used and what parameters matter
- **Write action vs. read/lookup** — determines which rubric type applies

**OEs drive rubric writing via a two-filter workflow:**
1. **Filter 1 — OEs:** Write actions → Outcome rubrics (1.1 + 1.2). Key facts to report → Outcome (2.1). Remaining read/lookup actions → candidates for process rubrics.
2. **Filter 2 — Matrix:** Apply the Process Rubric Decision Matrix to each candidate.

### Step 4: Run the Agent and Iterate
- Submit prompt → agent runs (~30+ min)
- While agent runs → start writing rubrics from OEs
- Review trajectory → what did agent do? What did it miss?
- If agent solves everything perfectly → **task is too easy, iterate**
- If agent fails → write rubrics capturing what it got right AND wrong
- Use **Haiku** for quick iteration, switch to **Opus 4.6** for final 6 runs

**Difficulty target:**
- Average 40+ tool calls
- At most 2 out of 6 runs pass (pass@1 ≤ 40%)
- All 6 failing is acceptable

**Where AI agents typically fail:**
- Confusing two entities with similar names
- The obvious answer is wrong; real answer requires deeper digging
- Information scattered across many services — agent misses some
- Correct observations but wrong conclusion
- Takes some actions correctly but misses others

### Step 5: Write the Rubrics

**Three categories:**
- **Tool Selection (TS)** — did the agent use the right tool?
- **Query Construction (QC)** — did it pass the right parameters?
- **Outcome** — was the result correct?

**Core rule: Outcome First**
- Write all Outcome rubrics before TS/QC
- Outcome rubrics are the most reliable training signal
- Aim for **50/50 to 80/20 outcome-to-process split**
- If Outcome already confirms a tool was called correctly → do NOT add TS/QC for that tool

**Outcome sub-categories (3, not 5):**
- **1.1** Write-action results — did the right action happen with right details? (verified from trajectory)
- **1.2** Action content — does content match what was needed? (verified from trajectory parameters)
- **2.1** Key facts/findings — only for pure investigation tasks where the response is the deliverable

**Process Rubric Decision Matrix:**

| Situation | TS? | QC? |
|---|---|---|
| Non-default tool + query is obvious | Yes | No |
| Non-default tool + bad query could miss data | Yes | Yes |
| Default tool + query is non-trivial | No | Yes |
| Default tool + any keyword finds data | No | No |

**Default vs Non-default tools:**

*MoveOps Universe:*
- Default (skip TS): `search_emails`, `conversations_search_messages`, `conversations_history`, `contacts_get_contacts`, `contacts_search_contacts`
- Non-default (write TS): `airtable_*`, `quickbooks_*`, `crm_*`, `calendar_*`, `linear_*`

*Keystone Mortgage Universe:*
- Default (skip TS): `email*`, `conversations_*` (slack), `contacts_*`
- Non-default (write TS): `mortgage_los_*`, `stripe_*`, `crm_*`, `filesystem_*`, `quickbooks_*`

> **Warning:** `filesystem_*` is NOT ready yet as of Apr 10, 2026 — do not use it in rubrics.

**Other rubric rules:**
- Each rubric has 3 fields: **criterion + justification + evidence**
- QC rubrics: Exact Match (EM) for structured fields, Fuzzy for free-text (include "or similar")
- A run passes only if **ALL rubrics pass** — any single failure = run failure
- Every rubric must be: specific, self-contained, objective, verifiable from trajectory
- **Banned language in criteria:** "enough," "professional," "thorough," "helpful," "good"

### Step 6: Verify Before Submitting

Checklist:
- [ ] Data exists in the universe (verified in explorer)
- [ ] Broad exploration: 3+ services required
- [ ] Tool-dependent: cannot be answered from general knowledge
- [ ] No tool names in prompt
- [ ] No pre-solving
- [ ] No internal IDs
- [ ] Natural language — reads like a real person
- [ ] Not bolted — every request connects to the same situation
- [ ] Not contrived — difficulty from real data complexity
- [ ] Agent fails on at least one run
- [ ] Universe edits are consistent
- [ ] Rubrics written: Outcome first, then process via decision matrix

---

## Common Mistakes

| # | Mistake | Fix |
|---|---|---|
| 1 | Agent solves everything perfectly | Add complexity, make prompt more open-ended, add more stacking |
| 2 | Command lists instead of tasks | State the goal, not the steps |
| 3 | Data doesn't exist | Always verify in the universe explorer |
| 4 | Contrived difficulty | Use natural business complexity, not artificial constraints |
| 5 | Bolted-together requests | Every sub-request must flow from the same situation |
| 6 | Pre-solved prompts | Give the symptom, not the diagnosis |
| 7 | Too short / too simple | Add context, constraints, and multiple stacked asks |

---

## Natural Difficulty Examples (GOOD)
- Two clients with similar names causing entity mix-up
- Unauthorized action buried in a CRM note, not in any incident ticket
- Cost spike whose root cause requires connecting a Slack message to a CRM contract signed weeks apart

## Contrived Difficulty Examples (BAD)
- "Respond in exactly 3 sentences using passive voice"
- "Find the email from January 15th at exactly 3:47 PM"
- "Intentionally send an incorrect email to test error handling"
