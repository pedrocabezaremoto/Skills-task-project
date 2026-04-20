# Task Metadata (69d691f7c8ff546a0ea76de6)
- **Platform:** app.outlier.ai → Real Coder
- **Rate:** $27/hr
- **Language:** TypeScript (React + Node.js)
- **Database:** SQLite
- **Status:** 🔄 RESTRUCTURING (Phase 2 - TDD)

---

# Title: Church & Community Organization Management Platform

## Description / Context
A church or community organization needs a centralized web platform to coordinate small groups, member involvement, events, volunteering, giving, and internal communications. Administrative staff manage the organization; group leaders manage their groups; and members interact with events and volunteering. The system uses SQLite and JWT-based role authentication.

## Tech Stack
- **Language:** TypeScript 5.4
- **Frontend:** React 18.3, React Router v6.23, Axios 1.6, Vite 5.2
- **Backend:** Node.js 20 LTS, Express.js 4.18
- **Database:** SQLite (better-sqlite3 9.4)
- **Authentication:** jsonwebtoken 9.0, bcryptjs 2.4

## Key Requirements

### 1. Bootstrap & Identity
- One-time `POST /auth/bootstrap` for org and initial staff creation. Returns 409 after first use.
- No self-registration. Staff create all users via `POST /auth/users`.
- Every user (except bootstrap staff) must be linked to a member profile created via `POST /members`.

### 2. Member & Family Management
- Staff CRUD for member profiles (name, email, phone, involvement areas).
- `family_links` table: max one spouse (symmetric), parent-child links (directional), no self-linking.

### 3. Small Groups & Attendance
- Staff create groups (name, leaderId, category: bible_study, support_group, etc.).
- Members browse and submit join requests.
- Group leaders approve/reject requests. `UNIQUE(group_id, member_id)`.
- Attendance: Leader records attendance per date. `UNIQUE(group_id, meeting_date)` (replaces existing date).

### 4. Communication & Engagement
- Discussion Board: Threaded replies (`parentId`nullable).
- Prayer Requests: Restricted to approved group members.
- Announcements: Targeted by `involvementAreaId` or broad broadcast. Filtered at GET for members.

### 5. Events & Volunteering
- Events: Staff create, members RSVP (attending/not_attending).
- Check-ins: Staff mark check-ins. `UNIQUE(event_id, member_id)`.
- Volunteering: Staff create slots, members sign up (self-sign-up).
- Conflict Check: Returns 409 if member has 2 slots on same date. Must be atomic (transactional).

### 6. Financials & Reporting
- Giving: Staff record donations fund (`general`, `missions`, `building`). Annual summaries.
- Reports: Attendance trend (last 12 meetings).
- Engagement Score: `Score = (Event Check-ins) + (Group Attendances)`.

## Expected Interface

### Express App Export
- **Path:** `server/src/app.ts`
- **Name:** `app`
- **Type:** Express Application (Export)
- **Input:** none
- **Output:** `Application` (Express Instance)
- **Description:** Configured Express app without `app.listen()`.

### Database Initializer
- **Path:** `server/src/db/database.ts`
- **Name:** `initializeDatabase`
- **Type:** Function
- **Input:** `dbPath: string` (default: `./church.db`)
- **Output:** `Database` (better-sqlite3 instance)
- **Description:** Creates all 18+ tables if non-existent.

### Auth Router
- **Path:** `server/src/routes/auth.ts`
- **Name:** `authRouter`
- **Type:** Express Router
- **Input:** `POST /auth/bootstrap`, `POST /auth/users`, `POST /auth/login`, `GET /auth/me`
- **Output:** JSON with tokens and user/org metadata.

### Members Router
- **Path:** `server/src/routes/members.ts`
- **Name:** `membersRouter`
- **Type:** Express Router
- **Input:** CRUD endpoints for members and `/family` connections.
- **Description:** Restricted to `staff` role for writes.

### Groups Router
- **Path:** `server/src/routes/groups.ts`
- **Name:** `groupsRouter`
- **Type:** Express Router
- **Input:** CRUD for groups, join-requests, roster, and attendance.
- **Description:** Leader-based authorization for specific group actions.

### Volunteers Router
- **Path:** `server/src/routes/volunteers.ts`
- **Name:** `volunteersRouter`
- **Type:** Express Router
- **Input:** CRUD for roles and schedule slots. Self-sign-up for members.
- **Output:** Includes `gap: true` for unassigned slots and conflict errors for double-booking.

### Giving Router
- **Path:** `server/src/routes/giving.ts`
- **Name:** `givingRouter`
- **Type:** Express Router
- **Input:** `POST /giving`, `GET /giving/member/:id`, `GET /giving/summary`.
- **Description:** Restricted to `staff`.

## Current State
Empty repository. No inbound/outbound external connections allowed (strict 127.0.0.1:3000). All assets local.
