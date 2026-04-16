# Opposite Classic: Common Errors & How to Fix Them

**Released:** Mar 24  
A practical guide covering the most frequent errors in task and rubric creation, organized in 4 parts.

---

## Part 1: Prompt Writing Errors

### Error 1: Being Too Specific in the Prompt
**Problem:** Giving away IDs, values, or exact data the agent is supposed to discover defeats the investigation challenge.

| Bad | Good |
|-----|------|
| "Check the Heartland invoice HM-2026-Q1-0042 for overbilling." | "The quarterly bill from our Midwest mover looks inflated." |
| "Find the email from January 15th at exactly 3:47 PM mentioning $14,237.89." | "I think there was a billing discrepancy in last quarter's invoices. Can you look into it?" |

> **Rule:** If the information is something the agent should look up, don't include it in the prompt.

---

### Error 2: Writing Sequential Instructions Instead of a Natural Request
**Problem:** Step-by-step command lists tell the agent exactly what to do and in what order — eliminating the investigation challenge and producing scripted, short runs.

| Bad | Good |
|-----|------|
| "Search emails > Check CRM > Send apology email to NovaCorp." | "NovaCorp seems upset about something. Figure out what's going on and handle it." |
| "First… Second… Third." | (same as above) |

> **Rule:** Real employees don't receive instruction scripts. They receive **situations**. Write situations.

---

### Error 3: Mentioning Tool Names or Parameter Names
**Problem:** Prompts should read like messages from a colleague, not API documentation.

| Bad | Good |
|-----|------|
| "Use crm_search_contacts to find Noah Fitzgerald and then use send_email with his address." | "Can you pull up Noah Fitzgerald's account and send him a follow-up?" |

---

### Error 4: Pre-Solving the Problem
**Problem:** Telling the agent the root cause eliminates the core investigation challenge.

| Bad | Good |
|-----|------|
| "Julian's demo is calling the weather API every 3 seconds, causing rate limiting. Fix the bug." | "The API keeps failing and I'm getting paged. Something changed in the last few days. Figure out what's going on." |

> The good version requires the agent to connect Julian's demo to the rate limit problem across multiple services. The bad version is just a command.

---

### Error 5: Bolting Unrelated Requests Together
**Problem:** Multiple tasks with no common context don't test cross-service reasoning — they just inflate apparent complexity with isolated sub-tasks.

| Bad (bolted) | Good (stacked) |
|--------------|----------------|
| "Check weather in Miami, update my calendar for next week, email Marcus about Q3, and look up Seattle flights." | "I'm meeting Patricia at Canopy Health tomorrow and I need to walk in prepared. Make sure our internal tracking is up to date, get me caught up on any open items ops is working on for them, and block time with Catalina this afternoon so we can align before the call." |

> In the good example, every sub-task flows from the same situation. In the bad example, the four tasks have nothing to do with each other.

---

### Error 6: Every Task Ending with "Send an Email"
**Problem:** Creates a monotonous pattern and misses more interesting write actions.

**Alternative write actions to use instead or in combination:**
- Linear ticket updates
- Airtable record updates
- CRM deal stage changes
- Calendar events
- Slack messages

---

### Error 7: Tasks That Are Too Short or Too Simple
**Problem:** Terse prompts give the agent nothing to work with. Real work requests include context, constraints, and multiple asks.

| Bad | Good |
|-----|------|
| "Rebook the retreat." | "The Apex AI retreat venue fell through due to the storm. Find an alternative city that still works for the team, stays within roughly the same budget, and get the new details to everyone who needs to know. Make sure we're tracking this properly internally too." |

---

## Part 2: Oracle Event Errors

### Error 1: Skipping Discovery Steps
**Problem:** OEs should reflect *how* the agent finds information, not just what it finds. Jumping to a send/update step without a prior lookup step skips required discovery.

| Bad OE | Good OE Sequence |
|--------|-----------------|
| "Send email to Jordan about the delay." | OE 1: Search contacts for "Jordan" to identify the correct person and retrieve their email. OE 2: Send email to jordan.chen@client.com about the delay. |

---

### Error 2: Describing Findings Instead of Tool Use Steps
**Problem:** OEs describe *actions the agent takes with tools*, not conclusions the agent reaches. Judgment about what data means belongs in rubrics — the OE is the mechanical step.

| Bad | Good |
|-----|------|
| "The agent discovers that the Terraform deal stage is closedwon." | "Search CRM deals for the Terraform account using crm_search_deals. The result will show the deal stage as 'closedwon'." |

---

## Part 3: Rubric Errors

### Error 1: Writing TS or QC Rubrics for Things Already Covered by Outcome Rubrics
**Problem:** If an Outcome rubric already confirms a tool was called with the right parameters, adding a TS or QC rubric for the same tool creates redundant overlap.

**Fix — Outcome-first workflow:**
1. Write all Outcome rubrics (1.1, 1.2, 2.1) first
2. Look at remaining non-write-action tool calls from OEs
3. Apply the Decision Matrix to decide if TS and/or QC is warranted
4. **Never write TS/QC for a tool that Outcome already covers**

---

### Error 2: QC Rubric That Doesn't Name the Tool
**Problem:** A query construction rubric without a tool name is unverifiable — the judge doesn't know which tool call to inspect.

| Bad | Good |
|-----|------|
| "The query must include 'Mosaic'." | "The model must pass a query related to 'Mosaic' (or similar) when calling crm_search_companies." |

---

### Error 3: Forcing a Single Channel When the Prompt Allows Multiple
**Problem:** If the prompt says "send" or "share" without specifying a channel, both email and Slack may be valid. A rubric requiring only email would fail correct Slack-based runs.

| Bad | Good |
|-----|------|
| "An email was sent (via send_email) to chloe.vance@moveops.com." | "A message was sent (via send_email or conversations_add_message) to Chloe Vance (chloe.vance@moveops.com or Slack equivalent)." |

> When both channels are genuinely valid, list them with **"or."**

---

### Error 4: Bundling Independent Tool Calls into One Rubric
**Problem:** A single rubric checking 3 recipients across 3 different tool calls cannot be graded atomically — if one fails and two succeed, you lose signal on what went wrong.

**The only acceptable bundling:** parameters of the *same* tool call, or tightly coupled facts from the same data record.

| Bad (bundled across calls) | Good (split into 3 rubrics) |
|----------------------------|-----------------------------|
| "Emails were sent to Marcus (Q3), Elena (board meeting), and Chloe (coordinator issue)." | Rubric 1: email to marcus.thorne@moveops.com about Q3. Rubric 2: email to elena.rostova@moveops.com about board meeting. Rubric 3: email to chloe.vance@moveops.com about coordinator issue. |

**Acceptable bundling:** "An email was sent to chloe.vance@moveops.com, CC elena.rostova@moveops.com." — both are parameters of the same tool call.

---

### Error 5: Criterion That Requires External Knowledge to Evaluate
**Problem:** The judge only sees the trajectory. If the rubric says "email sent to the CEO" without naming the CEO, it cannot be evaluated.

> **Rule: Every rubric must be fully self-contained.**

| Bad | Good |
|-----|------|
| "Email was sent to the CEO." | "An email was sent (via send_email) to elena.rostova@moveops.com (CEO)." |
| "The agent contacted the right coordinator." | "An email was sent (via send_email) to fatimah.al-rashidi@moveops.com (relocation coordinator)." |

---

### Error 6: Values in Rubrics That Don't Match Universe Data
**Problem:** If your rubric says deal stage is "qualification" but the CRM shows "closedwon," every correct agent run will fail — false negatives caused by your rubric, not the agent.

**Fix:** Always verify rubric values against the explorer and trajectory runs before finalizing.

---

### Error 7: Rubric Requiring Actions the Prompt Never Asked For
**Problem:** Rubrics that require actions not asked in the prompt will fail every run — not because the agent failed, but because you invented a requirement.

**Valid rubric sources:**
- A direct ask from the prompt
- An implicit ask (something a reasonable person would obviously do)
- A write action that logically follows from the task

> If you can't point to why the prompt requires this action, the rubric shouldn't exist.

---

### Error 8: Mixing Reasoning into the Criterion Field
**Problem:** The criterion field must be a clean, standalone yes/no claim. Reasoning belongs in the justification field.

| Field | Bad | Good |
|-------|-----|------|
| Criterion | "The model must pass 'marcus.thorne@moveops.com' in CC, as Elena's email instructs David to loop in Marcus." | "The model must pass 'marcus.thorne@moveops.com' in the CC field when calling send_email." |
| Justification | (included above — wrong place) | "Elena's email thread explicitly instructs David to loop in Marcus. Failing to CC him would mean Marcus is unaware of the client issue." |

---

### Error 9: Using "Approximately" for Fixed Static Values
**Problem:** "Approximately" signals a calculated/rounded value. Using it for exact counts, IDs, or dates implies uncertainty that doesn't exist.

| Bad | Good |
|-----|------|
| "The agent created approximately 3 Linear issues." | "The agent created 3 Linear issues." |
| "The email body references the exact budget of $15,432.10" | "The email body references a budget of approximately $15,000." |

> **Rule:** Only use "approximately" when the agent has to calculate or round a value and slight variation is expected.

---

### Error 10: Unfair Rubric Criteria
**Problem:** If a rubric criterion fails all 6 trajectories, investigate before keeping it. It may be unfairly penalizing correct runs.

**Fix:**
- Always review the **Rubrics Verifier Matrix** for criteria that fail all 6 runs
- If all outcome rubrics are met but a TS rubric keeps failing → identify and potentially remove it
- Keep the criterion only if you can **vehemently defend** its existence
- Otherwise, remove it

---

## Part 4: Writing TS Rubrics for Default Tools

**Problem:** Writing Tool Selection rubrics for default tools wastes rubric slots and produces no training signal — the agent always uses these tools regardless.

> TS rubrics only have discriminating power for **non-default tools** the agent might plausibly skip entirely.

| Default — Skip TS | Non-Default — Write TS |
|-------------------|------------------------|
| search_emails | airtable_* |
| conversations_search_messages | quickbooks_* |
| conversations_history | crm_* |
| contacts_get_contacts | calendar_* |
| contacts_search_contacts | linear_* |

| Bad TS rubric | Good TS rubric |
|---------------|----------------|
| "The model must use the search_emails tool." | "The model must use the crm_search_deals tool (or equivalent CRM deal lookup)." |

---

## Quick Reference Summary

| Part | Key Rule |
|------|----------|
| Prompt writing | Write situations, not scripts. Don't reveal what the agent should discover. |
| Oracle Events | Describe tool use steps, not conclusions. Always include discovery steps before write steps. |
| Rubric structure | Outcome-first. One claim per rubric. Criterion = yes/no claim only. |
| Rubric values | Verify against universe data. Self-contained. No invented requirements. |
| TS rubrics | Only for non-default tools. Never for search_emails, contacts, or conversations tools. |
