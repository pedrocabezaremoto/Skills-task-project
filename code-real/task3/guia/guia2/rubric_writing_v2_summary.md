# Rubric Writing V2 — Technical Summary
**Source:** Rubric Writing V2 (Last Updated: Apr 10, 2026)

---

## Key Changes (Change Log)

| Date | Type | What Changed |
|---|---|---|
| Apr 10, 2026 | Default Tools | Added table of default vs non-default tools per universe |
| Mar 25, 2026 | Rubrics | Atomic rubrics per item for multiple write actions — never bundle into "at least N" thresholds |
| Mar 12, 2026 | Rubrics | Outcome-first workflow; 3 outcome categories (down from 5); Process Rubric Decision Matrix added |
| Mar 12, 2026 | Rubrics | TS one-per-tool rule; write actions never appear in TS/QC; "approximately" rule updated |
| Mar 12, 2026 | Failure Rate | 0% pass rate is acceptable if rubrics are high-quality |

---

## What Are Rubrics?

Rubrics are **specific, checkable yes/no statements** about what the AI agent should accomplish.

**The judge sees:**
- The original task prompt
- The agent's full trajectory (every tool call, parameters, responses, reasoning)
- The agent's final response

**The judge does NOT see:**
- The MCP environment directly
- The universe data (only what appeared in the trajectory)
- Other agents' results

> **Critical implication:** Every expected value must be embedded in the rubric itself. Do not write "email sent to the CEO" — write "email sent to `elena.rostova@moveops.com` (CEO)."

---

## Three Rubric Categories

**Core rule: Write Outcome rubrics first. Add TS and QC only for what Outcome doesn't already cover.**

---

### Category 1: Tool Selection (TS)

**Read/lookup tool calls only — never write actions.**

Checks: Did the agent use the right tool?

- **Skip TS for default tools** — agent will always use these (no signal)
- **Write TS for non-default tools** — agent might skip these entirely (real signal)
- **One TS rubric per non-default tool** regardless of how many times the agent calls it

**Format examples:**
```
The model must use the crm_search_contacts tool.
The model must use a CRM search tool (e.g., crm_search_contacts or crm_search_companies).
```
Use "or" when multiple non-default tools could achieve the same goal.

---

### Default vs. Non-Default Tool Tables

**MoveOps Universe (v2.1 and below):**

| Default (skip TS) | Non-Default (write TS) |
|---|---|
| `search_emails` | `airtable_*` |
| `conversations_search_messages` (Slack) | `quickbooks_*` |
| `conversations_history` (Slack) | `crm_*` |
| `contacts_get_contacts` | `calendar_*` |
| `contacts_search_contacts` | `linear_*` |

**Keystone Mortgage Universe (v2.2 and above):**

| Default (skip TS) | Non-Default (write TS) |
|---|---|
| `*_email` | `mortgage_los_*` |
| `conversations_*` (Slack) | `stripe_*` |
| `contacts_*` | `crm_*` |
| | `filesystem_*` |
| | `quickbooks_*` |

---

### Category 2: Query Construction (QC)

**Read/lookup tool calls only — never write actions.**

Checks: Did the agent pass the correct parameters to critical tool calls?

Write QC only when **both** conditions are true:
1. The agent had to **figure out what to query** (value not given in the prompt)
2. A **bad query or missing filter could cause the agent to miss critical data**

If either condition doesn't hold → skip QC.

**QC uses EM/Fuzzy pattern:**
- Exact Match (EM) — structured parameter with one correct value:
  ```
  The model must pass "completed" as the state filter when calling linear_list_issues.
  ```
- Fuzzy — freetext parameter with multiple valid expressions:
  ```
  The model must pass a full_name related to "Noah Fitzgerald" or "Fitzgerald" (or similar) when calling crm_search_contacts.
  ```

> QC rubrics may check multiple parameters of the same tool call in a single rubric (tightly coupled = one action).

**Key distinction — QC vs Outcome:**
- QC checks **parameters**: "The model must pass a query related to 'past 6 months' when calling `linear_list_issues`."
- Outcome checks **results**: "A calendar event was created (via `calendar_add_calendar_event`) on Feb 24, 2026 with Chloe and Elena as attendees."

---

### Category 3: Outcome

Checks: What was accomplished? What does the user see?

**Target split:** 50/50 to 80/20 outcome-to-process (TS + QC = process).

#### The Outcome-First Workflow
1. Write all Outcome rubrics first (for every write action in OEs → 1.1 + 1.2; for key facts to report → 2.1)
2. Identify every non-write-action tool call from your OEs → candidates for process rubrics
3. Apply the Process Rubric Decision Matrix to each candidate

> If Outcome already confirms a tool was called with the right parameters → do NOT write TS or QC for that tool.

---

#### Process Rubric Decision Matrix

| Situation | Write TS? | Write QC? | Example |
|---|---|---|---|
| Non-default tool + query value given in prompt | Yes | No | CRM lookup for "Noah Fitzgerald" — name is given |
| Non-default tool + agent must infer/construct query | Yes | Yes | QuickBooks billing dispute — agent might skip AND use wrong search term |
| Default tool + agent must infer/construct query | No | Yes | Slack search for a buried stipend — always searches Slack, but narrow query misses it |
| Default tool + query value given or obvious | No | No | Email search for Robert Calloway — any keyword returns it |

---

#### Outcome Sub-Categories (3, not 5)

**What NOT to write (deprecated):**
- Grounding checks (trajectory verification of retrieved data) — skip
- Confirmation of actions in the final response — skip (if 1.1 passes, the action happened)

---

**1.1 — Write-Action Results**
Did the right action happen with the right details? Verified from the trajectory (tool call).

```
An email was sent (via send_email) from fatimah.al-rashidi@moveops.com to chloe.vance@moveops.com.
```
Use for: every write action (`linear_create_issue`, `crm_update_deal_stage`, `airtable_create_record`, `send_email`). Always required when a write action exists.

---

**1.2 — Action Content**
Does the content match what was needed? Verified from trajectory (tool call parameters).

```
The email body includes the recommended alternative city name and a cost comparison referencing the approximately $15,000 original budget.
```
Use only when write action has specific content requirements. Only write 1.2 if it adds a distinct check beyond 1.1.

---

**2.1 — Key Facts / Findings (Final Response)**
Did the agent correctly report the right information to the user? Verified from the final response text.

```
The final response lists Noah Fitzgerald (GreenStack Solutions) as relocating to Seattle.
```
Use when: the user asked to be told a specific fact — with or without write actions.

---

#### Which Sub-Categories Apply

| Task Type | 1.1 | 1.2 | 2.1 |
|---|---|---|---|
| Pure write action (send email, create issue) | Always | If content requirements exist | No |
| Pure investigation / summary to user | No | No | Yes |
| Mixed: research then write | Yes | Yes | Only if user also asked to be told findings directly |

---

## Using Tool Names in Rubrics

| Context | Rule |
|---|---|
| Task prompts | Never mention tool names |
| TS rubrics | Always mention tool names — that's the point |
| QC rubrics | Mention tool name to specify which call the parameters apply to |
| Outcome rubrics | Reference tool names with "(via tool_name)" when it adds precision |

Good: `An email was sent (via send_email) to chloe.vance@moveops.com.`
Bad: `The agent sent an email to Chloe.`

---

## Handling Flexibility: Strict vs. Flexible

Before writing each rubric, ask: does this value have **exactly one correct form**, or could the agent get it right a different way?

| Type | When to use | Example |
|---|---|---|
| **Strict (Exact Match)** | One correct answer: email addresses, dates, IDs, specific numbers | `"chloe.vance@moveops.com"` |
| **Flexible (Fuzzy)** | Multiple valid expressions: freetext queries, email subjects, issue titles, agent-generated content | `"related to relocation proposal (or similar)"` |
| **Required Elements** | Content with specific checklist requirements | `"must include: (a) reason, (b) city name, (c) cost comparison"` |
| **Selection Logic** | Similar entities, only one correct | `"priya.venkatesh@... — the Priya with a post-move thread"` |

**Common mistake:** Being too rigid on freetext. If agent passes "Fitzgerald" when you wrote "Noah Fitzgerald" — same intent → use "(or similar)."

---

## Quick Reference — Flexibility Patterns

| Situation | Pattern | Example |
|---|---|---|
| One correct tool / value / fact | Strict (EM) | `"crm_search_contacts"`, `"chloe.vance@moveops.com"` |
| Multiple valid non-default tools | Flexible | `"crm_search_contacts or crm_search_companies"` |
| Freetext parameter / agent-generated label | Flexible (Fuzzy) | `"related to relocation proposal (or similar)"` |
| Agent content with specific requirements | Required Elements | `"must: (a) reason, (b) city name, (c) cost comparison"` |
| Similar entities, one correct | Selection Logic | `"priya.venkatesh@... — the Priya with a post-move thread"` |

---

## Three Fields Per Rubric

Every rubric needs exactly three fields:

1. **Criterion** — The specific yes/no claim the judge evaluates. Must be self-contained, objective, atomic, and verifiable.
2. **Justification** — 1–2 sentences explaining why this rubric exists. Connects to the prompt or a known failure mode.
3. **Evidence** — What to look for in the trajectory. Points to the specific tool call, parameter, or response text that proves pass or fail.

---

## Service Metadata Requirements

Rubrics missing metadata are **incomplete**.

| Service | Required fields |
|---|---|
| **Email** | Recipient (full email address), CC (if specified), Content (specific items — list individually) |
| **Slack** | Recipient (channel name or DM recipient), Content (specific items — list individually) |
| **Linear** | Title (what issue title should contain), Assignee (if specified), Priority (if specified), Subtasks (count/coverage if applicable) |

| Incomplete | Complete |
|---|---|
| "Agent messaged David on Slack" | "Slack message to David Chen mentioning: (a) Apex AI retreat, (b) the new city, (c) the storm reason" |
| "Email sent about rebooking" | "Email (via send_email) to chloe.vance@moveops.com, CC elena.rostova@moveops.com, containing alternative city name and budget comparison to approximately $15,000" |

---

## How to Write Good Rubrics — 5 Rules

### Rule 1: Be Self-Contained
The judge can't look anything up. Include all expected values.

| Bad | Good |
|---|---|
| "Email sent to the CEO" | "Email sent to elena.rostova@moveops.com (CEO)" |
| "Budget is correct" | "Total cost is approximately $15,000 or less" |
| "Slack message has enough context" | "Slack message mentions: (a) Apex AI, (b) new city, (c) storm" |

### Rule 2: One Thing Per Rubric — No Overlaps, No Gaps
Each rubric must check exactly one independent claim. Split if two claims could plausibly fail independently.

**Bundling exception (allowed):**
- Same tool call: parameters visible together in the same call
- Same data point: facts from a single record that are meaningfully inseparable

### Rule 3: Must Be Verifiable from the Trajectory or Final Response

| Bad (unverifiable) | Good (verifiable) |
|---|---|
| "Email exists in SENT folder" | "An email was sent (via send_email) to chloe.vance@moveops.com" |
| "Calendar event was created in Google Calendar" | "A calendar event was created (via calendar_add_calendar_event) on Feb 24, 2026 with Chloe and Elena as attendees" |
| "The agent understood the problem" | "The final response correctly identifies the root cause as the duplicate flight confirmation" |

### Rule 4: Use "Approximately" for Calculated or Rounded Numbers
- ✅ `Cost is approximately $12,500`
- ✅ `Cost is between $12,000 and $13,000`
- ❌ `Cost is $12,487.50` — too precise

**Do NOT use "approximately" for fixed, static values:**
- Counts: "3 overdue tasks" — not approximately 3
- IDs: "issue OPS-312" — not approximately OPS-312
- Dates: "February 24, 2026" — not approximately Feb 24
- Discrete quantities from data: "5 relocations" — if data has exactly 5, say 5

### Rule 5: Handle Multiple Valid Answers Explicitly

| Phrasing | Meaning |
|---|---|
| "must be one of: Austin, Denver, or LA" | Closed — only these are correct |
| "including but not limited to: Austin, Denver" | Open — others also acceptable |
| "at least one of: Austin, Denver, or LA" | Any single one is sufficient |

Never use "such as," "like," or "for example" when defining what counts as correct (these are ambiguous). Fine in Fuzzy rubrics where you're illustrating intent, not defining the answer set.

---

## Writing Rubrics: Step-by-Step

**Step 1: Identify What the Prompt Asks For**
- Explicit asks: actions, information to report, constraints
- Implicit asks: units/context for numbers, disambiguation of similar entities, flagging discovered problems

**Step 2: Write Oracle Events (OEs)**
Map every key step a perfect agent would take. Label each as write action or read/lookup.

**Step 3: Write All Outcome Rubrics**
- Write action OEs → 1.1 (action details) + 1.2 (content if specific requirements exist)
- Key facts to report → 2.1
- Mixed tasks (research then write) → 1.1 + 1.2; add 2.1 only if prompt explicitly asks agent to report findings

**Step 4: Write Process Rubrics for Remaining Read/Lookup OEs**
Apply the Decision Matrix to each non-write-action tool call → TS only / QC only / both / neither.

**Step 5: Check Flexibility**
For each rubric, determine: EM / Fuzzy / Selection Logic / Required Elements. Apply correct pattern.

**Step 6: Verify Checklist**
- [ ] Every rubric has 3 fields: criterion + justification + evidence
- [ ] Every rubric belongs to TS, QC, or Outcome
- [ ] Outcome-to-process split is 50/50 to 80/20
- [ ] Outcome written first; process only for gaps
- [ ] No TS or QC for tools already covered by Outcome
- [ ] TS only for non-default tools agent might skip
- [ ] QC only when agent must infer query AND bad query = missing data
- [ ] Every write action has 1.1; 1.2 if content requirements exist
- [ ] 2.1 only when user asked to be told a specific fact
- [ ] Every criterion is self-contained (all expected values embedded)
- [ ] Every criterion is objective (no banned words: "enough," "professional," "thorough," "helpful," "good")
- [ ] Every criterion is atomic (one claim per rubric)
- [ ] No two rubrics penalize the same error (no overlaps)
- [ ] Every explicit prompt ask covered by at least one rubric (no gaps)
- [ ] Every criterion verifiable from trajectory or final response
- [ ] Email rubrics: recipient, CC, content specifics
- [ ] Slack rubrics: specific content items listed
- [ ] Linear rubrics: title and relevant fields
- [ ] Calculated/rounded numbers → "approximately" or range; counts/IDs/dates → exact
- [ ] Fuzzy values include examples + "(or similar)"
- [ ] Multiple valid answers → "must be one of" / "including but not limited to"

---

## Edge Cases

**When prompt specifies explicit count or names specific items:**
Write one atomic Outcome rubric per item, each naming the specific ticket/record/entity. Never bundle into "at least N."

✅ Correct:
- "A comment was added (via `linear_create_comment`) to ENG-211 reflecting the current status of the weather API fix."
- "A comment was added (via `linear_create_comment`) to ENG-212 reflecting the current status of the duplicate receipt issue."

❌ Wrong:
- "At least 5 of the 9 Linear tickets were updated with current status." → Reward-hackable.

**When prompt is open-ended ("create tickets for anything needing follow-up"):**
Go to the universe, identify the actual GT items, write one rubric per item explicitly. "At least one" is only acceptable when GT is genuinely indeterminate (rare).

> **Key principle:** Rubrics must be grounded in Ground Truth (GT), not arbitrary thresholds. An agent that updates 8 of 9 tickets should fail — the prompt asked for all 9.

---

## Common Mistakes

| # | Mistake | Fix |
|---|---|---|
| 1 | **Subjective language** — "enough context," "professional tone," "thorough" | Replace with specific, countable items — the #1 mistake |
| 2 | **Missing service metadata** — email without recipient, calendar without attendees | Include all required fields per service |
| 3 | **Can't verify from trajectory** — "email exists in SENT folder" | Write only what's visible in the trajectory tool calls |
| 4 | **All rubrics check the same thing** — all are "final response mentions X" | Add 1.1/1.2 for write actions; cover multiple dimensions |
| 5 | **No justification** | Every rubric needs a WHY |
| 6 | **Stacked rubrics** — bundling 4 independent claims in 1 | Split independent claims; bundle only tightly coupled facts |
| 7 | **TS/QC for write actions** | Outcome covers write actions — no TS or QC for them |
| 8 | **TS for default tools** | TS only for non-default tools; default tools provide no signal |
| 9 | **Ordering rubrics in disguise** — "agent must use crm before email" | TS checks tool selection. QC checks parameters. Neither checks order |
| 10 | **Ambiguous tool references** — "the agent sent an email" | Write "An email was sent (via send_email)" |
| 11 | **Overlapping rubrics** — one error fails multiple rubrics | Each error should be caught by exactly one rubric |

---

## Difficulty Target

Run agent 6 times with Opus 4.6:
- All 6 fail → acceptable (pass@1 = 0%)
- At most 2 pass → pass@1 ≤ 40%
- All 6 pass → too easy, iterate

> Tip: Use Haiku for quick iteration. Switch to Opus 4.6 for the final 6 runs.

---

## Examples

### Example 1 — Simple Task (Pure Write Action)
**Prompt:** "Send an email to Chloe from Fatimah about a relocation proposal"

| # | Category | Criterion |
|---|---|---|
| 1 | Outcome 1.1 | An email was sent (via `send_email`) from `fatimah.al-rashidi@moveops.com` to `chloe.vance@moveops.com`. |
| 2 | Outcome 1.2 | The email subject (visible in `send_email` parameters) relates to a relocation proposal (e.g., "Relocation Proposal for GreenStack" or similar). |

Distribution: TS: 0, QC: 0, Outcome: 2 — **process 0%, outcome 100%**

*No TS: both contacts tools are default. No QC: names given in prompt. No 2.1: deliverable is the email, not a summary.*

---

### Example 2 — Pure Investigation Task
**Prompt:** "Search for all of Fatimah's relocations from the past 6 months and compile a summary"
*(GT: 5 relocations — Fitzgerald/Seattle, Fitzpatrick/Austin, Venkatesh/Portland, Webb/Denver, Voss/Chicago)*

| # | Category | Criterion |
|---|---|---|
| 1 | TS | The model must use the `crm_search_contacts` tool (or equivalent CRM lookup). |
| 2 | Outcome 2.1 | The final response lists Noah Fitzgerald (GreenStack Solutions) relocating to Seattle. |
| 3 | Outcome 2.1 | The final response lists Noah Fitzpatrick (Axiom Labs) relocating to Austin. |
| 4 | Outcome 2.1 | The final response lists Priya Venkatesh (GreenStack Energy) relocating to Portland. |
| 5 | Outcome 2.1 | The final response lists Marcus Webb (Helix Corp) relocating to Denver. |
| 6 | Outcome 2.1 | The final response lists Elena Voss (Pinnacle) relocating to Chicago. |
| 7 | Outcome 2.1 | The final response identifies the approximate time range covered (roughly September 2025 through present). |
| 8 | Outcome 2.1 | The final response includes the status of each relocation (completed, in progress, or pending — matching universe data). |
| 9 | Outcome 2.1 | The final response does not include relocations from more than 6 months ago. *(negative rubric for date constraint)* |

Distribution: TS: 1, QC: 0, Outcome: 8 — **process 11%, outcome 89%**

*No QC: "Fatimah" given in prompt. No 1.1/1.2: pure investigation, no write actions. 2.1 carries everything.*

---

## When to Write Rubrics

Write rubrics **during and after** the agent run, not before.

1. Write prompt → submit
2. Agent runs
3. While agent runs → draft rubrics based on what you expect
4. After agent finishes → review trajectory
5. Finalize rubrics — adjust based on what you actually see
6. LLM judge grades rubrics against trajectory

Iterate: tweak prompt → re-run → adjust rubrics. If agent passes everything → task not hard enough → iterate.
