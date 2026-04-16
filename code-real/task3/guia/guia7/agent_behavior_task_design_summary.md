# Agent Behavior & Task Design Summary

## Overview

This guide shares observations from analyzing 10+ task trajectories using Claude Opus 4.6. It covers how agents search, common failure patterns, and principles for designing tasks with the right level of difficulty. Use for intuition — not as a checklist.

---

## Part 1: How Agents Search (Observed Behaviors)

### 1. Agents Do Broad Keyword Searches and Stop Early
- Agents search broadly, take the first plausible answer, and move on
- They rarely follow up unless results explicitly point to another source
- **Implication:** If the correct answer requires a second search, most agents will miss it

### 2. Agents Skip Structured Databases
- Agents discover info through Slack and email, but rarely query Airtable, QuickBooks, or CRM directly
- Real example: Agent read hundreds of Slack messages mentioning QuickBooks data and Airtable records by name — but never called a single Airtable or QuickBooks tool
- It used secondhand information from conversations instead of querying the source
- **Design implication:** If your task requires data from Airtable/QuickBooks/CRM, add a rubric that verifies the agent used the actual data source, not a conversation that mentions it

### 3. Agents Don't Search for Responses to Things They Find
- If an agent finds a dispute, it reports the dispute — it doesn't search for the vendor's reply
- Real example: Heartland Movers had emailed back saying one of three disputed charges was actually valid (cancellation missed 48-hour SLA). 4 of 5 runs never found the reply. The 1 run that did had searched for the vendor by name
- **Design implication:** If you add a dispute or open question to the universe, also add a response from the other party. The response changes the correct answer

### 4. Agents Latch onto the First Framing They Encounter
- When a client complaint named 2 incidents and an internal audit documented 5 (including those same 2), the agent reported 2 — it adopted the simpler, first-found framing
- **Design implication:** If the same issue appears in multiple sources with different levels of detail, agents default to whichever version they find first. Placing the most complete version in a less obvious location (e.g., a Linear ticket description instead of a Slack thread) makes the task harder

### 5. Data Past Search Result Limits Is Invisible
- Search results cap at a fixed number of top results
- If your edit uses the same keywords as many existing messages, it may get pushed out of results by more recent traffic
- Slack thread replies are especially hard to find — agents often see the question in a thread but not the answer in the replies
- **Fix:** Date your edits recently, or make them replies to existing threads so they appear near the top

---

## Part 2: Designing Edits That Create Difficulty

### Linked Edit Chains
Single edits are binary (found or not found). Chains are where real difficulty comes from.

**The pattern:**
- Edit A creates a problem (easy to find)
- Edit B resolves or changes it (harder to find)
- Agent needs **both** to get the correct answer

**Real example:**
- A: Marcus disputes Heartland's $4,800 charge → easy to find
- B: Jake at Heartland replies — one charge is valid because cancellation missed 48-hour SLA → harder to find
- Result: Only 1 of 5 runs found Jake's reply. That was the only run with the correct financial total

**Three-link chains are harder:**
- A: describes a problem
- B: hints where the resolution might be ("I filed that on a different ticket")
- C: actual evidence on another service
- Agent must follow two hops

### Making Edits Findable
Difficulty should come from **connecting evidence**, not from **hiding it**.

| Principle | Details |
|-----------|---------|
| Use words the agent will search for | If agent searches "invoice", your edit needs "invoice" in it. "Re: Follow-up on account" won't surface for "invoice" or "dispute" searches |
| Stay inside result limits | Date edits recently, or make them replies to existing threads |
| First link must be discoverable | If Edit A can't be found through normal broad searches, the entire chain is invisible. Difficulty = connecting A to B, not finding A |

### Edit Ideas (Starting Points)
- A reply that changes a conclusion (vendor pushes back, someone corrects a number, insurer threatens denial)
- A Linear issue filed with no corresponding Slack discussion
- Conflicting data across services (CRM says one thing, a Linear investigation says another)
- A near-miss entity (similar names in related contexts)
- An unanswered message (agents notice what's there, not what's missing)
- A dependency chain (answering X requires first looking up Y on a different service)

---

## Part 3: Writing Prompts That Push the Agent

| Technique | How to Apply |
|-----------|-------------|
| **Go broad, not specific** | "Compile the quarterly financial summary" forces investigation. "Check if the cancellation met the SLA deadline" is a one-answer lookup |
| **Hint without giving it away** | Use phrases like "I've been using estimates but the real numbers might be different" or "double-check my assumptions" — tells the agent to dig without saying where |
| **Name services or leave them unnamed** | "Cross-check QuickBooks, Airtable, Slack, and email" = multi-service but guided. "Figure out what's really going on" = harder because the agent decides where to look |
| **Diversify write actions** | Most tasks end with "send an email." Try: update Linear tickets, change Airtable records, update CRM deal stages, schedule calendar events |
| **Use multiple write actions** | Push tool call count above 40. Every write action needs reads first (contact lookups, ticket IDs, channel names) — this naturally increases tool call count |
| **Ask for both investigation AND action** | Research-then-act tasks are harder than pure investigation. In 5 of 6 runs on one task, the agent wrote a great report but never actually sent it — it confused producing content with executing the action |

> **Key insight:** If your prompt says "send David a summary," your rubrics must check that `send_email` was actually called — not just that the agent drafted good content.

---

## Part 4: Calibrating Difficulty

### Too Easy
- Edit shows up in the first search, agent grabs it, done
- Example: A Slack message saying "the budget is $75K not $50K" — no reasoning needed

### Sweet Spot
- Findable with normal searches, but the agent has to notice it matters and follow up
- Example: Agent finds a vendor dispute → vendor's reply says "two of these charges are valid per our SLA" → agent must re-examine which charges are actually disputed, look up the SLA, and revise its numbers
- Requires: finding A, finding B, connecting them, and updating the conclusion

---

## Summary: Key Design Rules

| Rule | Why It Matters |
|------|---------------|
| Add a response to every dispute/complaint | Agents find disputes but not replies — the reply changes the correct answer |
| Put critical data in structured databases, not just Slack | Forces rubric: "did the agent actually query Airtable/CRM?" |
| Use linked edit chains (A→B or A→B→C) | Real difficulty comes from connecting evidence, not hiding it |
| First link must be findable via normal search | If A is invisible, the whole chain fails |
| Use keywords the agent will actually search for | Vague subject lines = invisible edits |
| Require multiple write actions | Naturally drives tool call count up; tests whether the agent executes, not just drafts |
| Go broad in the prompt | Open-ended prompts force the agent to decide what to investigate |
