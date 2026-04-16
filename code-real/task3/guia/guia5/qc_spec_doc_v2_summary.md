# Guide 5 Summary — QC Spec Doc V2

> Last Updated: April 16, 2026  
> Purpose: Complete list of QC criteria used to audit and determine if a task passes or fails.

---

## Changelog Highlights

| Date | Change |
|---|---|
| Apr 16, 2026 | Universe date correctness updates and exceptions |
| Apr 13, 2026 | Minor Keystone universe changes; new personas and business functions |
| Apr 9, 2026 | Added "All-Failing Rubrics" dimension; added [Non-Fail - Outcome-Light] flag |
| Apr 2, 2026 | CBs use "Scenario Generation" tool for universe edits (offline since Apr 7) |
| Mar 29, 2026 | New status: "Fail – Too Many Erroneous Runs" |
| Mar 26, 2026 | New rubric dimension: "Overly Broad Criteria" |
| Mar 24, 2026 | Fixed "today" date = Apr 26, 2026 (v2.1) / Apr 28, 2026 (v2.2) |

---

## Scoring Overview: 3 Tiers

| Score | Meaning |
|---|---|
| 1–2 | Fail |
| 3–4 | Non-Fail (warning, not automatic rejection) |
| 5 | Pass |

---

## QC Dimensions — Full Reference

### PROMPT Dimensions

#### 1. Unique Ground Truth
- **Fail**: Prompt can produce two or more distinct correct answers with no clear intended one.
- **Non-Fail**: Ambiguous but has a leading interpretation or a small defensible assumption clarifies intent.
- **Pass**: All experts would reach the same conclusion. Multiple valid paths OK — key answer points must be the same.

#### 2. Feasibility
- **Fail**: Impractical/impossible request; conflicting instructions; impossible given available tools.
- **Non-Fail**: Core request is feasible, secondary requests are borderline impractical.
- **Pass**: Completely actionable by an LLM agent, no conflicting instructions.

#### 3. Explicit Tool Mention
- **Fail**: Prompt explicitly mentions a tool name (e.g., `linear_create_issue`, `crm_search_contacts`).
- **Non-Fail**: References an MCP server by name ("use the Linear MCP server") or calls it a "tool" ("use the CRM tool").
- **Pass**: No explicit tool use mentioned.
- **Example distinction**: "Use the Airbnb tool to…" (FAIL) vs. "I want to use Airbnb to find…" (OK)

#### 4. Prompt Clarity and Specificity
- **Fail**: Intent cannot be reasonably understood; major missing details.
- **Non-Fail**: Mostly clear but could be interpreted multiple ways.
- **Pass**: Specific request, no more than one minor assumption needed.

#### 5. Contrived / Unnatural Prompts
- **Fail**: Artificially difficult (exact timestamps, arbitrary format constraints, step-by-step command lists).
- **Non-Fail**: Somewhat contrived or unnatural.
- **Pass**: Natural complexity — entity confusion, scattered info, conflicting data, hidden root causes.
- **Note**: Riddles with intentional constraints are NOT considered contrived.

#### 6. Truthfulness
- **Fail**: 1+ major factual errors; OR 2+ minor factual errors.
- **Non-Fail**: 1 minor factual error.
- **Pass**: No factual errors, no misleading statements.

#### 7. Tool Use and Cross-Service Requirement
- **Fail**: Can be answered without tool calls; OR resolved within a single service.
- **Pass**: Requires investigation across 2+ services; facts are scattered and must be reconciled.

#### 8. Investigation
- **Fail**: Only asks for a report/summary with no required action; OR prompt is pre-solved (tells agent the root cause).
- **Pass**: Requires investigation AND at least one concrete action (email, ticket, CRM update, etc.) that logically follows.

#### 9. Coherence
- **Fail**: Contains bolt-on requests — unrelated sub-requests stapled together. Test: remove a sentence; if the rest still makes sense, it's a bolt-on.
- **Pass**: One cohesive situation; all stacked asks tie back to the same purpose.

#### 10. Persona
- **Fail**: Prompt does not read like it could be written by the selected persona.
- **Non-Fail**: Plausible for selected persona, but fits another persona better.
- **Pass**: Clearly aligns with the selected persona.
- **Note (03/24)**: Do not penalize if the prompt fits multiple personas, as long as the assigned one is also applicable.

#### 11. Business Function (v2.1+ only)
- **Non-Fail**: Ambiguous — could belong to assigned or different function.
- **Pass**: Clearly reflects a realistic scenario within the assigned business function.

#### 12. Alignment with Today's Date
- **Fixed dates**: v2.1 = Apr 26, 2026 | v2.2 = Apr 28, 2026
- **Fail**: Prompt's request doesn't make sense given "today's" date; OR universe modified with incoherent future dates AND it caused an agent failure.
- **Pass**: Prompt doesn't contradict "today's" date.
- **Exception (04/15)**: Universe not aligned with correct date does NOT fail if it did NOT cause an agent failure.

---

### UNIVERSE Dimensions

#### 13. Universe Feasibility (Data Exists)
- **Fail**: Key facts/entities/events don't exist in the universe — task is unsolvable.
- **Pass**: All core facts exist and are retrievable via tools.

#### 14. Cross-Service Coherence
- **Fail**: Universe edits create contradictions (mismatched names, impossible dates, entities in one service but not another).
- **Pass**: All edits are internally consistent across services, dates, names, and storyline.
- **Note**: If one piece of info has strong support vs. weak contradicting evidence, don't count as contradiction.

---

### ORACLE EVENTS (OEs)

#### 15. OE Completeness
- OEs serve two purposes: (1) prove solvability, (2) drive rubric writing for all 3 categories.
- Each OE must note: what action, what info discovered, what tool used, what parameters matter.
- **Non-Fail**: Missing critical steps (no step for how key info is retrieved or action is executed).
- **Pass**: OEs describe the full critical path: discovery steps + dependency chain + write action(s).

#### 16. OE Accuracy
- **Non-Fail**: Minor imprecisions (slightly wrong param name, approximate values for freetext).
- **Non-Fail**: Wrong tool, wrong service, wrong params, or wrong expected data.
- **Pass**: All OEs are factually accurate — tools, services, params, and expected data match the universe.

---

### RUBRICS Dimensions

#### 17. Overall Rubric Quality
| Status | Threshold |
|---|---|
| Fail | >10% Major errors OR >15% Moderate/Major OR >20% any errors |
| Non-Fail | ≤10% Major OR ≤15% Moderate/Major (major <5%) OR 5–20% minor (major <5%, moderate <15%) |
| Pass | <5% minor issues, no major or moderate issues |

#### 18. All-Failing Rubrics (added 04/09)
- After verifier runs, CBs must justify any rubric that failed ALL completed runs.
- "All completed runs" = only runs that finished without error (e.g., if 4/6 completed, rubric must have failed all 4).
- **Fail**: 2+ all-failing rubrics have a quality issue (fictional tool name, overly specific, out of scope, etc.).
- **Non-Fail**: Good rubric, but CB justification is unfactual/irrelevant. OR exactly 1 all-failing rubric has a quality issue.
- **Pass**: All AF rubrics are valid — self-contained, grounded in GT, real tools. If no AF rubrics exist → automatic 5.

#### 19. Rubric Category Balance
- Target: ~80% Outcome, ~20% Process (TS + QC).
- **Fail**: Zero Outcome rubrics; OR >50% Process rubrics.
- **Non-Fail**: Outcome is 50–79% (Outcome-Light).
- **Pass**: 80%+ Outcome. Process rubrics present but limited to critical OE steps.

---

### TRAJECTORY Dimensions

#### 20. Tool Call Count
- **Fail**: Average tool calls across all trajectories < 15.
- **Pass**: Average ≥ 15 (aim for 40+).

#### 21. Agent Failure Rate
- **Fail (Too Easy)**: More than 2 of 6 runs pass all valid outcome rubrics (pass@1 > 40%).
- **Pass**: 0–2 of 6 runs pass (pass@1 ≤ 40%).

#### 22. Error Rate (added 03/29)
- CBs may continue if at least 4 runs succeeded (max 2 erroneous runs).
- **Fail**: 3+ runs resulted in errors (NOT rubric failures — actual system errors).
- **Pass**: Fewer than 3 erroneous runs.

---

## Appendix: Rubric Quality Definitions

### Major Issues

#### Missing Criteria — Outcome
Flag when:
- No criterion checks whether the user's core request was fulfilled.
- Write actions (send_email, create issue, update CRM, schedule calendar, delete) have no Outcome rubric verifying success.
- Final response accuracy not checked (correct names, dates, dollar amounts).
- Rubric only checks process with no user-facing outcome checks.

#### Criteria Not Self-Contained
- Every rubric must be evaluable from: trajectory + final response + all rubric criteria + original prompt ONLY.
- The LLM judge does NOT see: the universe, personas, tool schema, or external info.
- All expected values must be embedded in the criterion text.

**Bad examples:**
- "Email sent to the CEO." → Must say: "Email sent to elena.rostova@moveops.com (CEO)."
- "Budget is correct." → Must say: "Total cost is approximately $15,000 or less."

**Good examples:**
- "An email was sent (via `send_email`) to chloe.vance@moveops.com."
- "The final response lists Noah Fitzgerald (GreenStack Solutions) as relocating to Seattle."

#### Criteria Not Atomic
- Each rubric evaluates ONE thing only.
- **Acceptable bundling**: QC rubrics may bundle multiple parameters of the SAME read/lookup tool call.
- **Never bundle**: components from separate tool outputs; write action parameters.

**Violations:**
- "Email sent to Chloe and Linear issue created for Fatimah." → Must be two rubrics.
- "Agent searched relocations and sent a summary email." → Two independent claims.

#### Incorrect Criteria
- Contradicts the prompt or Oracle Events.
- Contains factual errors not grounded in universe data.
- Requires behavior that leads to an incorrect outcome.
- Not an explicit prompt requirement that doesn't improve the response.

---

### Moderate Issues

#### Missing Criteria — Process/Reasoning
Applies to: Tool Selection (TS) and Query Construction (QC) only.

**Tool Selection rules:**
- Write ONE TS rubric per non-default tool the agent might skip.
- Default tools NEVER get TS rubrics.
- Non-default tools (v2.2): `mortgage_los_*`, `stripe_*`, `crm_*`, `filesystem_*`, `quickbooks_*`
- Write actions NEVER get TS or QC → always Outcome.

**Query Construction rules:**
- Write QC ONLY when BOTH: (1) agent had to infer the query (not given in prompt), AND (2) bad query = missing critical data.
- QC NEVER written for write actions.

**Process Rubric Decision Matrix:**

| Situation | TS? | QC? | Example |
|---|---|---|---|
| Non-default tool + query given in prompt | YES | NO | CRM lookup for "Noah Fitzgerald" (name given) |
| Non-default tool + agent must infer + bad query = miss | YES | YES | QuickBooks billing dispute search |
| Default tool + agent must infer + bad query = miss | NO | YES | Slack search for buried financial discussion |
| Default tool + query given or obvious | NO | NO | Email search for Elena Rostova |

#### Overlapping or Redundant Criteria
- One TS rubric per non-default tool maximum — even if tool appears in multiple OEs.
- Key test: Would removing one criterion change scoring? If not → redundancy.
- TS + QC + Outcome do NOT overlap by design.

#### Incorrectly Labeled Category
- **TS**: Did agent use the correct read/lookup tool? Never write actions.
- **QC**: Did agent pass correct parameters to a read/lookup tool? Never write actions.
- **Outcome subtypes**:
  - 1.1 = write-action results (verified from trajectory)
  - 1.2 = action content (verified from trajectory params)
  - 2.1 = key facts/findings (pure investigation tasks only)

**Common mislabeling errors:**
- Parameter values labeled as TS → should be QC
- Email success check labeled as QC → should be Outcome
- TS/QC rubric for a write action → should be Outcome
- TS rubric for a default tool → remove it

#### Unwanted Rubrics (added 03/20)
- TS or QC written for write actions → unwanted.
- TS written for default tools → unwanted.

#### Overly Broad Criteria (added 03/26)
- Criterion is too permissive — accepts all valid responses but ALSO accepts some invalid ones.
- Exception: If the invalid paths accepted are unlikely to occur, do not flag.

---

### Minor Issues

#### Overly Specific Criteria
Three scenarios:
1. **Tool alternatives**: If multiple tools are valid, criterion must not lock in one specific tool.
   - Bad: "Must use `crm_search_contacts`." (when `crm_search_companies` also works)
   - Good: "Must use a CRM lookup tool (e.g., `crm_search_contacts` or `crm_search_companies`)."

2. **Freetext parameters**: Must use "(or similar)" — never exact strings for freetext fields.
   - Bad: "Must pass 'Fatimah relocations recent'."
   - Good: "Must pass a query related to 'Fatimah' or 'Al-Rashidi' (or similar)."

3. **Outcome content**: For agent-generated content, must allow valid alternative expressions.
   - Bad: "Email must include the phrase 'we apologize for the inconvenience caused by the storm.'"
   - Good: "Email includes an acknowledgment of the storm disruption (or similar)."

**Exception — strict values are NEVER overly specific:**
- Email addresses, IDs, dates, exact strings from universe data → always exact.

---

### Purely Non-Failing Issues

#### Rubric Wording Errors
- Minor wording/typo that slightly alters meaning but would NOT cause an LLM judge to evaluate incorrectly.
- Test: Would the LLM judge flag the response as wrong because of the wording? If not → non-fail wording error.

---

## Complete Default Tools List

```
Slack:    channels_list, conversations_history, conversations_replies,
          conversations_search_messages

Email:    search_emails, list_emails, get_email_by_id, get_email_by_index,
          get_thread, get_email_threads, show_data, list_jmap_emails,
          get_jmap_email, list_mailboxes, get_mailbox

Contacts: contacts_search_contacts, contacts_get_contacts, contacts_get_contact,
          contacts_show_data, contacts_get_current_user_details
```

---

## Key Rules to Remember

1. Write actions (anything that changes universe state) → always **Outcome**, never TS or QC.
2. Default tools → never get TS rubrics.
3. QC only when: agent must infer query AND bad query = missing critical data.
4. One TS rubric per non-default tool maximum.
5. Every rubric must be self-contained — embed all expected values in the criterion text.
6. "Today's" date: v2.1 = Apr 26, 2026 | v2.2 = Apr 28, 2026.
7. pass@1 must be ≤ 0.4 (at most 2 of 6 runs pass).
8. Average tool calls must be ≥ 15 (target 40+).
9. At least 4 of 6 agent runs must complete successfully (max 2 errors).
