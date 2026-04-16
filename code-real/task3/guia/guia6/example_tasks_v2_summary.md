# Example Tasks – V2 Summary

## Overview

This guide provides two fully worked example tasks with Oracle Events and Rubrics. It shows how an agent should plan tool calls, gather data, fix records, and communicate results. Each task includes:
- A realistic business persona and prompt
- Step-by-step Oracle Events (what the agent should discover/do)
- A rubric table with numbered criteria, categories, justifications, and evidence instructions

---

## TASK 1: 69bbb4c5721d4acd27296c8f

**Business Function:** Operations  
**Persona:** Fatimah Al-Rashidi – Relocation Coordinator

### Prompt Summary
Two employees named Noah Fitzgerald (GreenStack) and Noah Fitzpatrick (Axiom) are both relocating to Seattle in April 2026. The coordinator suspects she mixed up their arrangements. She asks the agent to:
1. Verify that the right apartment, flight, and moving arrangements are matched to the right person
2. Fix any mix-ups in Airtable and Linear records
3. Create a tracking ticket
4. Email Emeka Diallo (account manager)
5. Post in #operations to alert Chloe and the team

### Oracle Events Summary

| Step | Action | Key Finding |
|------|--------|-------------|
| 1 | `airtable_search_records` for "Noah Fitzgerald" | Found recReloc00000006 – GreenStack, Seattle, Apr 28-29 |
| 2 | `airtable_search_records` for "Noah Fitzpatrick" / "Axiom" | No record exists – Fitzpatrick was never entered |
| 3 | `search_emails` for Fitzgerald | Apartment: 412 Boylston Ave E, Apt 3B, Capitol Hill ($2,100/mo). Flight booked April 14 **instead of requested April 27** |
| 4 | `search_emails` for Fitzpatrick | Same apartment (412 Boylston) and same flight (ACT-77492, Apr 14) sent to Fitzpatrick too – double-assigned |
| 5 | `search_emails` for flight ACT-77492 | Only one booking exists: Passenger = Noah Fitzgerald, Apr 14 – used for both Noahs |
| 6 | `conversations_search_messages` (Slack) | Emeka confirmed: Fitzpatrick = Axiom, Fitzgerald = GreenStack |
| 7 | `crm_search_deals` for GreenStack | deal_greenstack_q2: $13,500 with Fitzgerald |
| 8 | `crm_search_companies` / deals for Axiom | company_axiom found but **no Axiom deal** in CRM |
| 9 | `linear_list_issues` for Fitzgerald | Tickets #316 (Apartment), #317 (Flight – booked Apr 14 wrong), #318 (Moving – Swift Relocations Apr 28-29) |
| 10 | `linear_list_issues` for Fitzpatrick | **No tickets** despite Slack mentions of an intake ticket |
| 11 | `contacts_search_contacts` for Emeka | emeka.diallo@moveops.com |
| 12 | `contacts_search_contacts` for Chloe | chloe.vance@moveops.com |
| 13 | `airtable_create_record` for Fitzpatrick | Create: Name, Company (Axiom Precision Manufacturing), Status: In Progress, Origin: PHL, Dest: Seattle, Coordinator: Fatimah |
| 14 | `airtable_update_records` for Fitzgerald (recReloc00000006) | Flag: wrong flight date (Apr 14 not Apr 27), double-assigned apartment |
| 15 | `linear_create_issue` | URGENT ticket: Fitzgerald/Fitzpatrick mix-up, flight date wrong, double apartment, Fitzpatrick missing from systems |
| 16 | `linear_create_comment` on #316/#317 | Flag apartment and flight mix-ups |
| 17 | `send_email` to emeka.diallo@moveops.com | Explain: wrong flight date, double apartment, missing Fitzpatrick records, vendor course-correction needed |
| 18 | `conversations_add_message` to C006 (#operations) | Alert Chloe: two relocations crossed, contact Atlas (flight) and UrbanNest (apartment) for correction |

### Mix-Ups Identified
1. **Wrong flight date:** Fitzgerald's flight booked Apr 14 (Fitzpatrick's date) instead of his requested Apr 27
2. **Double-assigned apartment:** Both Noahs sent to 412 Boylston Ave E, Apt 3B, Capitol Hill
3. **Missing tracking records:** Fitzpatrick has no Airtable record, no Linear tickets, no CRM deal

### Rubric – Task 1 (19 criteria)

| # | Title | Category |
|---|-------|----------|
| 1 | Airtable record created for Fitzpatrick (Axiom, Seattle) | outcome |
| 2 | Fitzgerald's Airtable record updated with mix-up flags | outcome |
| 3 | Linear urgent tracking ticket created for mix-up resolution | outcome |
| 4 | Email sent to Emeka Diallo explaining mix-ups | outcome |
| 5 | Message posted to #operations (channel C006) | outcome |
| 6 | Linear ticket references both "Fitzgerald" and "Fitzpatrick" + ≥2 of 3 mix-ups | outcome |
| 7 | Email to Emeka mentions wrong flight date (Apr 14 vs Apr 27) | outcome |
| 8 | Email to Emeka mentions double-assigned apartment (412 Boylston, Apt 3B) | outcome |
| 9 | Email to Emeka mentions Fitzpatrick's missing tracking records | outcome |
| 10 | #operations Slack message mentions vendor course-correction (Atlas / UrbanNest) | outcome |
| 11 | Final response identifies flight date error (ACT-77492, Apr 14 vs Apr 27) | outcome |
| 12 | Final response identifies apartment double-booking (412 Boylston, Apt 3B) | outcome |
| 13 | Final response identifies ≥1 tracking gap for Fitzpatrick | outcome |
| 14 | Agent uses `airtable_search_records` for both Noah Fitzgerald AND Noah Fitzpatrick | tool selection |
| 15 | Agent uses CRM tool (`crm_search_deals` / `crm_search_companies`) for GreenStack and/or Axiom | tool selection |
| 16 | Agent uses `linear_list_issues` for tracking tickets for both Noahs | tool selection |
| 17 | Fitzpatrick Airtable record includes Coordinator = "Fatimah Al-Rashidi" | outcome |
| 18 | Final response reports Fitzpatrick's flight status (same ACT-77492 as Fitzgerald / no separate booking) | outcome |
| 19 | Final response reports moving vendor status for ≥1 Noah (Swift Relocations or similar) | outcome |

---

## TASK 2: 69b85a78e999475175628a49

**Business Function:** Engineering  
**Persona:** Dmitri Volkov – Software Engineer

### Prompt Summary
Samira needs a status update on all ExpenseBot remediation work before Elena's Friday rollout readiness check. Dmitri asks the agent to:
1. Review all open tickets (config fixes, audit, pipeline hardening, dashboard validation, duplicate detection)
2. Determine which are done vs. in progress vs. blocked
3. Update ticket statuses and add comments where needed
4. Send Samira a summary email with readiness status
5. Post in #engineering to loop in the whole team

### Oracle Events Summary

| Step | Action | Key Finding |
|------|--------|-------------|
| 1 | `linear_list_issues` (query: "ExpenseBot" / "expense" / "auto-categorizer") | 9 tickets found: ENG-211 through ENG-220 |
| 2 | `linear_list_comments` / `linear_get_issue` for each ticket | Discover detailed statuses, Samira's pause plan, Lena's deployment verification, edge case (Kevin Tran), Dmitri's schema tests |
| 3 | `conversations_search_messages` (Slack) | Samira's pilot pause announcement, root cause: silent parse error (Vectral) + malformed JSON types (Mosaic) |
| 4 | `search_emails` (query: "ExpenseBot" / "audit" / "false rejection") | Samira's remediation plan to Elena: audit by 3/19, pipeline fix by 3/20-3/21; audit summary: 83% accuracy, 5 false rejections (Vectral), 3 false approvals (Mosaic) |
| 5 | `linear_update_issue` → state: "done" for ENG-214/215 | Lena's comment confirms config corrections deployed 3/18 but ticket still "in progress" |
| 6 | `linear_create_comment` on updated tickets | Document reason for status change |
| 7 | `contacts_search_contacts` for Samira | samira.tariq@moveops.com |
| 8 | `send_email` to samira.tariq@moveops.com | Summary: all ticket statuses with due dates, overall readiness for Elena's Friday check, 83% accuracy metric |
| 9 | `channels_list` / `conversations_search_messages` | Find #engineering = channel C003 |
| 10 | `conversations_add_message` to C003 | Post full remediation status: done vs. in progress, due dates, blockers, what's left before Friday |

### Tickets Reference

| Ticket | Description | Assignee | Status | Due |
|--------|-------------|----------|--------|-----|
| ENG-211 | Pilot monitoring | Samira | Paused | — |
| ENG-212 | Edge case coverage | Dmitri | In Progress | 3/20 |
| ENG-214 | Vectral config fix | Lena | **Done** (deployed 3/18) | 3/18 |
| ENG-215 | Mosaic config fix | Lena | **Done** (deployed 3/18) | 3/18 |
| ENG-216 | Full audit (47 expenses) | Dmitri | In Progress, **P0** | 3/19 |
| ENG-217 | Pipeline hardening | Lena | In Progress | 3/20 |
| ENG-218 | Dashboard type validation | Anh | In Progress | 3/21 |
| ENG-219 | Launch readiness checklist | Samira | To Do | 3/21 |
| ENG-220 | Duplicate detection | Dmitri | To Do | 3/25 |

**Root cause:** Both client incidents trace back to the policy ingestion pipeline (ENG-209)  
**Remaining edge case:** Kevin Tran's internet setup fee (flagged in Lena's comment on ENG-215)

### Rubric – Task 2 (21 criteria)

| # | Title | Category |
|---|-------|----------|
| 1 | Agent uses `linear_list_issues` to search for ExpenseBot tickets | tool selection |
| 2 | Agent uses `linear_list_comments` or `linear_get_issue` for detailed status | tool selection |
| 3 | `linear_list_issues` query uses "ExpenseBot" / "expense" / "auto-categorizer" / "pilot" | query construction |
| 4 | `conversations_search_messages` query uses "ExpenseBot" / "audit" / "remediation" / "pilot pause" | query construction |
| 5 | `search_emails` query uses "ExpenseBot" / "audit" / "remediation" / "pilot" / "false rejection" | query construction |
| 6 | Email sent to samira.tariq@moveops.com with success | outcome |
| 7 | Email body mentions ENG-216 as P0 urgent audit ticket (47 expenses) | outcome |
| 8 | Email body mentions ≥1 due date from remediation plan (3/19, 3/20, or 3/21) | outcome |
| 9 | Email body mentions Lena Bjorkstrom + pipeline hardening (ENG-217) | outcome |
| 10 | Email body reports ENG-220 status "to do" with due date 3/25 | outcome |
| 11 | Email body mentions Kevin Tran's internet setup fee as remaining edge case | outcome |
| 12 | Email body mentions Elena's Friday rollout readiness check | outcome |
| 13 | Email body identifies root cause: policy ingestion pipeline (ENG-209) | outcome |
| 14 | `conversations_add_message` sent to #engineering (channel C003) with success | outcome |
| 15 | Slack message references ≥3 different ENG ticket numbers from remediation set | outcome |
| 16 | Slack message mentions what's still outstanding before Friday (≥1 incomplete ticket) | outcome |
| 17 | Agent uses `linear_update_issue` to close ≥1 ticket where work is done (ENG-214/215) | outcome |
| 18 | Agent uses `linear_create_comment` on a ticket that was also updated | outcome |
| 19 | Tool responses show ≥6 different ENG remediation tickets (from ENG-211 to ENG-220 set) | outcome |
| 20 | Tool responses from `linear_list_comments` / `linear_get_issue` contain ≥1 due date from Samira's pause confirmation | outcome |
| 21 | Final response mentions ENG-216 as high-priority / P0 / urgent audit ticket | outcome |

---

## Key Patterns Across Both Tasks

### Tool Selection Principles
- **Airtable**: Use when the prompt says "check records" – search both matching AND non-matching names to discover gaps
- **CRM**: Use when the prompt mentions "CRM" or company-level relationships
- **Linear**: Use for ticket tracking; always read comments (`linear_list_comments` / `linear_get_issue`) not just issue list
- **Slack**: Use `conversations_search_messages` for team communications and status announcements
- **Email**: Use `search_emails` for formal communications, booking confirmations, and plans

### Query Construction
- Search by person name AND company name AND project name to cover all angles
- When looking for completion status, search Slack/email for team announcements even if tickets still show "in progress"

### Record Hygiene Actions
- If a system is missing a record → create it (`airtable_create_record`, `linear_create_issue`)
- If a ticket status doesn't match evidence → update it (`linear_update_issue`) AND add a comment explaining why
- Always fill in coordinator/assignee fields when creating records

### Communication Pattern
1. Fix the data first
2. Notify the direct manager/coordinator via email (detailed, specific errors)
3. Notify the broader team via Slack (channel-specific, with ticket numbers and outstanding work)
4. Final response must surface the key findings explicitly (errors, gaps, statuses)
