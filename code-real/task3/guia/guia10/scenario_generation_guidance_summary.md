# Opposite Classic – Scenario Generation Guidance Summary

> **WARNING:** Scenario Generation pipeline is offline since Apr/07.  
> This guide is reference-only until the pipeline is restored.

---

## Overview

The scenario generation process sets up a situation that an agent will subsequently resolve. Two key inputs required:

1. **Scenario Description** — establishes initial conditions and setup for the overall task
2. **Task Prompt** — the actual instruction written from the persona's point of view; guides the agent to investigate, discover, and take action

---

## Workflow (4 Steps)

1. Draft Scenario Description
2. Generate Artifacts (via pipeline)
3. Evaluate Artifacts
4. Develop Task Prompt

---

## Step 1: Understand Your Inputs

1. **Review the Persona** — read their role, recent actions, and identity carefully
2. **Develop a Plausible Scenario** — must be realistic for the persona's role
3. **Incorporate Universe References** — use real names, companies, and vendors from the universe reference sheet

---

## Step 2: Write the Scenario Description

### Story Elements

| Element | Definition | Example |
|---------|-----------|---------|
| **TRIGGER** | The inbound signal the persona sees first, prompting their reaction | "Tessa Moreno emails Chloe about the accelerated start date." |
| **BREADCRUMB** | Evidence hidden in a different system that the agent must proactively discover; not obvious from the trigger | "Suki posted in #operations about UrbanNest capacity constraints." |

> A strong description = **1 trigger + multiple breadcrumbs in different systems**

---

### Description Template

```
[1-2 sentences: Context — what happened and why it matters.
Ground this in real universe data (client names, vendor relationships, ongoing projects).]

[1-2 sentences: The trigger — who sends it, to whom, and what it claims or requests.
If the trigger contains errors, say what's actually true so the LLM can generate
breadcrumbs that expose the discrepancy.]

[1-2 sentences per breadcrumb: Where it lives and what ONE thing it reveals.
State how it relates to the trigger — does it contradict, confirm, or add context?]
```

---

### Example Description (Heartland Invoice)

> Heartland Movers has sent a new Q1 reconciliation invoice to Marcus Thorne that contains several incorrect line items. The invoice includes charges for Priya Venkatesh's GreenStack Energy relocation, which was actually completed by Swift Relocations (not Heartland). It also re-includes the previously disputed charges for Lily Marchetti and Danielle Osei (both cancelled moves).
>
> Jake Loomis at Heartland Movers emails Marcus Thorne with the Q1 reconciliation invoice attached, totaling approximately $18,500, with a polite but firm request for payment within 15 days. The invoice lists 6 line items covering moves from January through March.
>
> The day before the invoice arrived, Chloe Vance posted in #operations confirming that Swift Relocations completed the Priya Venkatesh move after Heartland couldn't handle the specialized equipment requirements — a detail that directly contradicts the Heartland invoice.

**Mapping to template:**

| Template section | In this example |
|-----------------|-----------------|
| Context | First paragraph: incorrect line items, names specific people/companies, references prior dispute — gives LLM enough detail to generate a realistic invoice |
| Trigger | Second paragraph: Jake emails Marcus with the invoice. Specifies tone, dollar amount ($18,500), and structure (6 line items, Jan–Mar), but does NOT reveal which items are wrong |
| Breadcrumb | Third paragraph: Chloe's #operations post. Reveals only one fact (wrong vendor) and includes editorial hint ("directly contradicts the Heartland invoice") |

> Note: The description is **setup only** — it does NOT say what Marcus should do about the invoice.

---

### Tips for Effective Descriptions

- Give the LLM specific context: dollar amounts, policy limits, prior incidents
- Use editorial hints like "this understates the actual severity" or "this directly contradicts the invoice" to guide the LLM without prescribing exact content
- Reference existing universe records by name when breadcrumbs connect to them (e.g., "the existing Linear issue for the Mosaic policy config fix")

---

### Key Rules for the Description

| # | Rule |
|---|------|
| 1 | **Setup only, not resolution.** Only describe what has already happened before the task starts |
| 2 | **Diversify breadcrumb locations.** If trigger is an email, breadcrumbs must be in Slack, Linear, Airtable, etc. |
| 3 | **Don't put the entire situation in one breadcrumb.** Each breadcrumb reveals ONE partial fact. Agent must combine multiple sources |
| 4 | **Timing must be specific.** Use "the day before," "earlier that morning," "a few hours before the email." All artifacts must land between scenario start date and April 26 (universe current date) |
| 5 | **Check names against the reference sheet.** Use exact names for existing people. If a person doesn't exist, reference by role. Never use a name that belongs to a different person in the sheet |
| 6 | **Keep it focused.** Describe 2-3 story elements (trigger + breadcrumbs). More = confusing and unfocused task |

---

## Step 3: Run the Scenario Pipeline

- Click "Enhance" button in Universe Explorer
- Provide scenario description + scenario start datetime
- **DO NOT CHECK "fill gaps with noise after all scenarios"**

### Timing Rules

- Universe fixed "current date" = **April 26, 2026**
- All background artifacts must have timestamps **before April 26**
- Scenario start date sets the **earliest allowed timestamp**
  - Example: `2026-04-24` → 2-day window (April 24–26) for artifacts
- Keep breadcrumbs **within 1-2 days** of the trigger to avoid clamping
- Verify generated artifact timestamps are logical and correct

---

## Step 4: Review Output and Write Task Prompt

### Server Data Integrity Check (MUST DO BEFORE MOVING ON)

In the "Database" tab → select "post-scenario" universe → verify all servers load data:

| Server | Expected |
|--------|----------|
| airtable | data visible |
| contacts | data visible |
| crm | data visible |
| email | data visible |
| linear | data visible |
| quickbooks | data visible |
| slack | data visible |
| Calendar – events | "No records found" |
| Jmap_emails, mailboxes, threads (under Email) | "No records found" |

> If this check fails → return to "pre-scenario" universe and re-generate. Select the correct new "post-scenario" universe after re-generating.

---

### Checklist: Scenario Description

- [ ] Includes at least 1 trigger and 2-3 breadcrumbs
- [ ] Breadcrumbs are in different systems than the trigger
- [ ] No single breadcrumb reveals all information
- [ ] Setup only — no resolution actions described

---

### Checklist: Generated Artifacts

- [ ] Names match the reference sheet; new people don't collide with existing names
- [ ] Timestamps consistent with scenario description and April 26 universe date
- [ ] No background artifacts land after April 26
- [ ] No shortcutting artifacts (see below)
- [ ] Total artifact count reasonable: **6–20** (including supporting records like contacts and threads)

### Common Shortcutting Artifacts to Remove

- CRM notes or engagements that summarize the trigger email
- Internal Slack messages where someone has already connected trigger to breadcrumb
- Calendar events for follow-up meetings the persona hasn't scheduled yet
- Tickets or issues that describe the task itself (e.g., "Resolve vendor billing dispute")

---

### Checklist: Task Prompt

- [ ] 3-6 sentences, first person, persona's voice
- [ ] References the trigger naturally ("I just got an email from...")
- [ ] Does NOT reveal where breadcrumbs are — no "check Slack" or "there's a note in Airtable"
- [ ] States goals, not steps — let the agent decide how to investigate
- [ ] Implies 3-5 concrete actions without being prescriptive

### Good vs Bad Prompt Example

**Good:**
> "Jake Loomis at Heartland just sent over their Q1 reconciliation invoice and it looks wrong again. I need you to go through it line by line, cross-reference against our relocation records to see which charges are legitimate, and figure out the total discrepancy. Then draft a dispute letter to Jake with the specifics, update our books, and flag the findings to Chloe and the finance channel so everyone's on the same page."

**Bad (too prescriptive, reveals breadcrumbs):**
> "Jake Loomis at Heartland just sent over their Q1 invoice. Check the #operations Slack channel — Chloe posted that Swift actually handled Priya Venkatesh's move, not Heartland. Then look at the Linear issue for the Heartland dispute to see that Lily Marchetti and Danielle Osei were already flagged as cancelled. Dispute those three line items, email Jake with the corrections, and update QuickBooks."

---

## Quick Reference

| Phase | Key Rule |
|-------|----------|
| Description | 1 trigger + 2-3 breadcrumbs, different systems, setup only |
| Timing | All artifacts before April 26; keep breadcrumbs within 1-2 days of trigger |
| Artifacts | 6-20 total; no shortcutting; timestamps consistent |
| Prompt | 3-6 sentences; goals not steps; no breadcrumb reveals; first person |
