# Church & Community Organization Management Platform

## Context
A church or community organization needs a centralized web platform to coordinate its small groups, member involvement, events, volunteering, giving, and internal communications. Administrative staff manage the organization and its data; group leaders manage their specific groups; and members interact with groups, events, and volunteer opportunities. The platform replaces fragmented spreadsheets and manual tracking with a unified system backed by SQLite and JWT-based role authentication.

## Tech Stack
- **Language:** TypeScript 5.4
- **Frontend:** React 18.3, React Router v6.23, Axios 1.6
- **Backend:** Node.js 20 LTS, Express.js 4.18
- **Database:** SQLite via better-sqlite3 9.4
- **Authentication:** jsonwebtoken 9.0, bcryptjs 2.4
- **Build (frontend):** Vite 5.2
- **Build (backend):** ts-node 10.9 (dev), tsc (production)
- **Package manager:** npm

## Requirements

1. An organization is bootstrapped via a single registration endpoint that accepts the organization name, mission statement, and an array of one or more initial admin staff accounts (each with full name, email, and password). This creates the organization record and the initial `staff` accounts in one atomic operation. `POST /auth/bootstrap` is the one-time-only public exception to account creation and MUST return HTTP 409 on any subsequent call after a successful bootstrap. All subsequent user accounts MUST be created exclusively by existing staff via `POST /auth/users`; no other public account-creation path exists after bootstrap. The implementation MUST use staff-only provisioning as the account creation model: (a) staff MUST first create a member profile via `POST /members`, then (b) staff MUST create a linked user account via `POST /auth/users` referencing that member profile's ID. No self-registration endpoint exists in the system. A group leader user account requires a pre-existing member profile, and a member can only be assigned as a group `leaderId` after their member profile exists.
2. The system MUST allow staff to create, read, update, and delete member profiles, and MUST restrict these actions to the staff role. Each profile includes: full name, email, phone number, membership date (ISO date string), and one or more involvement areas selected from a configurable list.
3. A member profile supports linked family connections via a dedicated `family_links` table. Invariants: maximum one `spouse` link per member; spouse links are symmetric (if A is spouse of B, B is spouse of A); parent-child links are directional (posting `child` from member A to member B creates a directional parent→child link); self-linking is prohibited. All connections link to separate member profiles. Member retrieval MUST materialize inverse parent relationships in the response so that a child's profile exposes the parent link explicitly.
4. The system MUST implement endpoints for staff to add, rename, and delete involvement areas. The involvement area list is dynamic and user-managed; no areas are pre-seeded by the system.
5. The system MUST restrict small group creation exclusively to users with the staff role. Each group stores: name, description, meeting frequency (`weekly` | `biweekly` | `monthly`), meeting day (integer 0–6), meeting time (HH:MM string), location, leader ID (must reference an existing member record), and category (`bible_study` | `support_group` | `service_team` | `social`).
6. The system MUST provide endpoints for authenticated members to browse the list of available groups and submit join requests to groups they are not already a member of.
7. The system MUST provide endpoints for group leaders to list pending join requests for their groups and to approve or reject each request individually. Approved members are added to the roster; rejected requests are discarded. The `group_members` table MUST enforce `UNIQUE(group_id, member_id)`. The `group_join_requests` table MUST enforce at most one pending request per member per group; a duplicate join request from a member who already has a pending request or is already on the roster MUST return HTTP 409.
8. Each group exposes a roster endpoint returning the list of all currently approved members.
9. A group leader records meeting attendance by submitting a meeting date and an array of member IDs who attended. Each submission creates or replaces the attendance record for that specific date. The `meeting_attendance` table MUST enforce `UNIQUE(group_id, meeting_date)` so that each group has exactly one attendance record per date; a new submission for an existing date MUST replace (not duplicate) that record.
10. Each group has a discussion board. The `discussion_posts` table MUST include a `parentId` column that is nullable to support threaded replies. The system MUST allow approved group members to post messages with or without a `parentId`, and to retrieve all messages in the board.
11. Each group has a prayer request list. Only current approved group members can post or view prayer requests. Each request has a title and a description field. The group leader is considered an approved member for all group access purposes (discussion, prayer requests, attendance); the system MUST treat `req.user.memberId === group.leaderId` as sufficient authorization for any feature restricted to approved group members.
12. Staff can create organization-wide events. Each event stores: title, date (ISO date), time (HH:MM), location, and description.
13. The system MUST support exactly two RSVP statuses: `attending` and `not_attending`. The system MUST allow any authenticated member to RSVP to an event with one of these statuses and to update their own RSVP. Staff MUST be able to retrieve the full RSVP list for any event.
14. The check-in system for events is restricted to staff. Staff search members by name fragment and mark a matched member as checked in for a specific event. Before inserting a check-in record, the endpoint MUST first verify the event exists and return HTTP 404 if not found. A member can only be checked in once per event; a duplicate check-in MUST return HTTP 409. The `checkins` table MUST enforce `UNIQUE(event_id, member_id)`; SQLite UNIQUE constraint violations on insert MUST be mapped to HTTP 409 (distinct from the pre-insert 404 path).
15. The system MUST implement endpoints for staff to dynamically create and manage volunteer roles. Roles are reusable across schedule slots. No roles are pre-seeded; all roles are created by staff at runtime.
16. Staff create weekly volunteer schedule slots, each containing a role ID, a date, and a member ID assignment (null when unassigned). The system MUST provide an endpoint for authenticated members to self-sign-up for unassigned slots; this endpoint MUST assign the caller's linked member profile (derived from `req.user.memberId`) and MUST return HTTP 403 if `req.user.memberId` is null.
17. If assigning a member to a slot would result in that member having two slots on the same date, the API MUST return HTTP 409 with a conflict error body `{ error: string, conflictingSlotId: number }`. The `conflictingSlotId` MUST be obtained by selecting the existing assigned slot for that member on the same date within the same `BEGIN IMMEDIATE` transaction before the insert. This conflict check MUST be performed inside that transaction within the single server process; the re-query and insert MUST occur within the same transaction. This guarantee is scoped to the POST and PUT assignment endpoints running in a single Node.js server process.
18. Any schedule slot with no assigned member is flagged as `gap: true` in the response. The schedule endpoint accepts a `date` query parameter (YYYY-MM-DD) to filter results by date.
19. Staff record donations per member: amount (decimal, two decimal places), date (ISO date), and fund designation (`general` | `missions` | `building`).
20. Staff can retrieve an annual giving summary per member (total and count per fund for a given year) and organization-wide donation totals grouped by fund for a given year.
21. The API MUST implement an endpoint for staff to send announcements with a title and body targeted to member-linked users. Announcements with no `involvementAreaId` target are visible to all users whose accounts are linked to a member profile. Announcements with a specific `involvementAreaId` are visible only to member-linked users whose member profile includes that involvement area. Staff accounts MUST be able to read all announcements regardless of member linkage (i.e., even if `req.user.memberId` is null).
22. The reports endpoint for a group returns: the average attendance count across the group's last 12 recorded meetings and an array of per-meeting attendance counts representing the trend. "Last 12 recorded meetings" MUST be determined by ordering `meeting_attendance` records `ORDER BY meeting_date DESC LIMIT 12`.
23. The engagement endpoint returns a score per member. The score is calculated using the following declared formula: `score = (number of organization-wide events the member was checked in to) + (number of group meeting attendance records the member appears in)`. This formula is the explicit implementation definition for engagement scoring.
24. All data persists in a SQLite database file. The database initializes all required tables automatically on server startup if they do not already exist.
25. The API implements JWT authentication. Every protected route requires a valid `Authorization: Bearer <token>` header. The JWT payload includes `{ id, email, role, memberId }` where `memberId` is the linked member profile ID (null for accounts not yet linked to a member profile). Missing tokens return HTTP 401; invalid or expired tokens return HTTP 403.
26. Three roles exist: `staff`, `group_leader`, `member`. Role-based access control is enforced on all protected routes: staff access all endpoints; group leaders manage their own groups, including attendance, roster, join requests, and all approved-member group features (discussion board, prayer requests) for groups they lead, identified by matching `req.user.memberId` to the group's `leaderId`; members access browsing, events, RSVP, volunteer sign-up, and group participation features. All member and group_leader feature access requires both an allowed role AND a non-null `req.user.memberId`; any request with a null `memberId` attempting a member-identity-required feature MUST return HTTP 403, regardless of role.
27. The `users` table stores a `memberId` foreign key referencing the `members` table. Staff and group_leader/member accounts that are created after bootstrap must supply a valid `memberId` (HTTP 400 if absent or invalid for group_leader/member roles). The database schema MUST allow `memberId` to be null for staff accounts. Referential integrity is enforced: a member profile cannot be deleted if it is linked to a user account or referenced as a group `leaderId`. Any protected route requiring member identity returns HTTP 403 if `req.user.memberId` is null.

## Expected Interface

### Express App Export
- **Path:** `server/src/app.ts`
- **Name:** `app`
- **Type:** exported constant (Express Application)
- **Input:** none — module export
- **Output:** `Application` — configured Express app with all routes and middleware mounted
- **Description:** Exports the Express app without calling `app.listen()`, enabling test suites to import and wrap it with supertest without starting a live HTTP server.

### Database Initializer
- **Path:** `server/src/db/database.ts`
- **Name:** `initializeDatabase`
- **Type:** function
- **Input:** `dbPath: string` — SQLite file path. If no value is provided, the function MUST default to `./church.db`
- **Output:** `Database` — connected better-sqlite3 `Database` instance with all tables created
- **Description:** Creates all tables if they do not exist (users, organizations, members, family_links, involvement_areas, groups, group_members, group_join_requests, meeting_attendance, discussion_posts, prayer_requests, events, rsvps, checkins, volunteer_roles, volunteer_slots, donations, announcements) and returns the database instance.

### Auth Router
- **Path:** `server/src/routes/auth.ts`
- **Name:** `authRouter`
- **Type:** Express Router
- **Input:** `POST /auth/bootstrap` body `{ organizationName: string, missionStatement: string, staffAccounts: { name: string, email: string, password: string }[] }` (public; returns HTTP 409 if an organization record already exists — enforces singleton) · `POST /auth/users` body `{ name: string, email: string, password: string, role: 'staff'|'group_leader'|'member', memberId?: number }` (staff-only; `memberId` required for group_leader/member, optional for staff) · `POST /auth/login` body `{ email: string, password: string }` · `GET /auth/me`
- **Output:** Bootstrap: `{ success: boolean, organizationId: number }` · Login: `{ token: string, user: { id: number, name: string, email: string, role: string, memberId: number|null } }` · GET /auth/me: `{ id: number, name: string, email: string, role: string, memberId: number|null, member: MemberObject|null }` · HTTP 401 on invalid credentials · HTTP 409 on duplicate email
- **Description:** Bootstraps the organization and initial staff accounts in one operation. Staff create all subsequent user accounts; every non-staff account must be linked to an existing member profile. All users authenticate via login and receive a JWT containing memberId. The /auth/me endpoint returns the authenticated user with their linked member profile.

### Members Router
- **Path:** `server/src/routes/members.ts`
- **Name:** `membersRouter`
- **Type:** Express Router
- **Input:** `GET /members` · `GET /members/:id` · `POST /members` body `{ name: string, email: string, phone: string, membershipDate: string, involvementAreas: number[] }` · `PUT /members/:id` same body · `DELETE /members/:id` · `POST /members/:id/family` body `{ relatedMemberId: number, relationshipType: 'spouse'|'child' }`
- **Output:** Member object `{ id, name, email, phone, membershipDate, involvementAreas: Area[], familyLinks: FamilyLink[] }` or array · HTTP 404 if not found · HTTP 403 if non-staff attempts create/update/delete
- **Description:** Full CRUD for member profiles and family link management. Create, update, and delete restricted to staff role.

### Involvement Areas Router
- **Path:** `server/src/routes/areas.ts`
- **Name:** `areasRouter`
- **Type:** Express Router
- **Input:** `GET /areas` · `POST /areas` body `{ name: string }` · `PUT /areas/:id` body `{ name: string }` · `DELETE /areas/:id`
- **Output:** Area object `{ id: number, name: string }` or array · HTTP 404 if not found · HTTP 403 if non-staff attempts write operations
- **Description:** Manages the configurable involvement area list. Write operations restricted to staff.

### Groups Router
- **Path:** `server/src/routes/groups.ts`
- **Name:** `groupsRouter`
- **Type:** Express Router
- **Input:** `GET /groups` · `POST /groups` body `{ name, description, frequency, meetingDay, meetingTime, location, leaderId, category }` · `GET /groups/:id` · `POST /groups/:id/join-request` · `GET /groups/:id/join-requests` · `PUT /groups/:id/join-requests/:requestId` body `{ action: 'approve'|'reject' }` · `GET /groups/:id/roster` · `POST /groups/:id/attendance` body `{ meetingDate: string, attendeeIds: number[] }` · `GET /groups/:id/attendance`
- **Output:** Group object, roster array, or attendance record · HTTP 403 if unauthorized · HTTP 409 if member already in group or duplicate request
- **Description:** Group lifecycle management: creation, join request submission, leader approval or rejection, roster retrieval, and meeting attendance recording per date.

### Discussion & Prayer Router
- **Path:** `server/src/routes/groups.ts`
- **Name:** `discussionAndPrayerRoutes`
- **Type:** Express Router (sub-routes mounted on groupsRouter)
- **Input:** `GET /groups/:id/discussion` · `POST /groups/:id/discussion` body `{ message: string, parentId?: number }` · `GET /groups/:id/prayer-requests` · `POST /groups/:id/prayer-requests` body `{ title: string, description: string }`
- **Output:** Post array `{ id, authorId, message, parentId, createdAt }[]` or prayer request array `{ id, memberId, title, description, createdAt }[]` · HTTP 403 if requester is not an approved group member
- **Description:** Group-scoped discussion board with optional threaded replies and a prayer request list. Both endpoints verify the requesting user is an approved group member before granting access.

### Events Router
- **Path:** `server/src/routes/events.ts`
- **Name:** `eventsRouter`
- **Type:** Express Router
- **Input:** `GET /events` · `POST /events` body `{ title, date, time, location, description }` · `GET /events/:id` · `POST /events/:id/rsvp` body `{ status: 'attending'|'not_attending' }` · `GET /events/:id/rsvp` · `POST /events/:id/checkin` body `{ memberId: number }` · `GET /events/:id/checkin` · `GET /events/:id/checkin/search?name=<string>`
- **Output:** Event object, RSVP list `{ memberId, name, status }[]`, check-in list `{ memberId, name, checkedInAt }[]` · HTTP 409 on duplicate check-in · HTTP 404 if event not found
- **Description:** Organization-wide event management (staff create only), RSVP tracking, and check-in recording. The search endpoint returns members matching the name fragment for the check-in interface.

### Volunteers Router
- **Path:** `server/src/routes/volunteers.ts`
- **Name:** `volunteersRouter`
- **Type:** Express Router
- **Input:** `GET /volunteers/roles` · `POST /volunteers/roles` body `{ name: string }` · `GET /volunteers/schedule?date=YYYY-MM-DD` · `POST /volunteers/schedule` body `{ roleId: number, date: string, memberId?: number }` · `PUT /volunteers/schedule/:slotId` body `{ memberId: number }` · `DELETE /volunteers/schedule/:slotId`
- **Output:** Role list `{ id, name }[]` · Schedule slots `{ id, roleId, roleName, date, memberId, memberName, gap: boolean }[]` · HTTP 409 on double-booking `{ error: string, conflictingSlotId: number }`
- **Description:** Volunteer role management and weekly scheduling. Every slot response includes `gap: true` when unassigned. Conflict detection triggers on POST and PUT if the same member already has a slot on the same date.

### Giving Router
- **Path:** `server/src/routes/giving.ts`
- **Name:** `givingRouter`
- **Type:** Express Router
- **Input:** `POST /giving` body `{ memberId: number, amount: number, date: string, fund: 'general'|'missions'|'building' }` · `GET /giving/member/:memberId?year=YYYY` · `GET /giving/summary?year=YYYY`
- **Output:** Donation record `{ id, memberId, amount, date, fund }` · Member annual summary `{ fund, total: number, count: number }[]` · Org-wide summary `{ fund, total: number, count: number }[]` · All routes staff-only
- **Description:** Records individual donations and returns fund-grouped annual summaries at both the member level and organization level. All giving routes require staff role.

### Communications Router
- **Path:** `server/src/routes/communications.ts`
- **Name:** `communicationsRouter`
- **Type:** Express Router
- **Input:** `POST /communications/announcements` body `{ title: string, body: string, involvementAreaId?: number }` (staff only) · `GET /communications/announcements`
- **Output:** Announcement object `{ id, title, body, involvementAreaId: number|null, targetAreaName: string|null, sentAt: string, sentBy: number }` or array. GET returns only announcements where `involvementAreaId` is null or matches the requesting user's linked member involvement areas.
- **Description:** Staff create announcements targeted by numeric area ID or to all member-linked users. GET filters results: area-targeted announcements are visible only to member-linked users of that area; non-targeted announcements are visible to all member-linked users. Staff accounts MUST always receive all announcements regardless of member linkage.

### Reports Router
- **Path:** `server/src/routes/reports.ts`
- **Name:** `reportsRouter`
- **Type:** Express Router
- **Input:** `GET /reports/group-health/:groupId` · `GET /reports/engagement`
- **Output:** Group health `{ groupId: number, averageAttendance: number, trend: number[] }` where `trend` is the per-meeting attendance count array for the last 12 meetings · Engagement list `{ memberId: number, name: string, score: number }[]`
- **Description:** Returns attendance trend data for the last 12 recorded meetings of a group and member engagement scores (sum of event check-ins and group meeting attendances per member).

### JWT Auth Middleware
- **Path:** `server/src/middleware/auth.ts`
- **Name:** `authenticateToken`
- **Type:** function (Express RequestHandler)
- **Input:** `req: Request, res: Response, next: NextFunction` — reads `Authorization: Bearer <token>` header
- **Output:** `void` — attaches `req.user: { id: number, email: string, role: string, memberId: number|null }` on success · HTTP 401 if token missing · HTTP 403 if token invalid or expired
- **Description:** Verifies the JWT signature, decodes the payload, and attaches the user object to the request. Calls `next()` on success. Error handling MUST discriminate by error type: missing `Authorization` header returns HTTP 401; `TokenExpiredError` from `jwt.verify` returns HTTP 403; all other verification failures return HTTP 403.

### Role Guard Middleware
- **Path:** `server/src/middleware/auth.ts`
- **Name:** `requireRole`
- **Type:** function (middleware factory)
- **Input:** `...roles: ('staff' | 'group_leader' | 'member')[]`
- **Output:** Express `RequestHandler` — calls `next()` if `req.user.role` is in the allowed list; returns HTTP 403 otherwise
- **Description:** Returns an Express middleware that enforces role-based access. Used after `authenticateToken` on routes requiring specific roles.

### Frontend App Entrypoint
- **Path:** `client/src/main.tsx`
- **Name:** `main`
- **Type:** React application entrypoint
- **Input:** none — renders `<App />` into `#root` DOM element
- **Output:** void — mounts the React application
- **Description:** Bootstraps the React 18 application using `ReactDOM.createRoot`. Wraps `<App />` with `BrowserRouter` from React Router v6.

### Frontend App Router
- **Path:** `client/src/App.tsx`
- **Name:** `App`
- **Type:** React functional component
- **Input:** none
- **Output:** JSX — top-level router with protected and public routes
- **Description:** Defines the client-side route tree. Public routes: `/login`, `/`. Protected routes (requires valid JWT in localStorage): `/dashboard`, `/members`, `/groups`, `/groups/:id`, `/events`, `/volunteers`, `/giving`, `/communications`, `/reports`. Unauthenticated access to protected routes redirects to `/login`.

### Frontend API Client
- **Path:** `client/src/api/client.ts`
- **Name:** `apiClient`
- **Type:** exported constant (Axios instance)
- **Input:** none — module export
- **Output:** `AxiosInstance` — configured with `baseURL` of `http://127.0.0.1:3000` (the local backend), and a request interceptor that attaches `Authorization: Bearer <token>` from localStorage on every request
- **Description:** Centralized Axios instance used by all frontend service modules. The baseURL MUST be exactly `http://127.0.0.1:3000`. No requests to external or third-party URLs are permitted. Handles auth header injection automatically.

## Current State
This is a greenfield project. No existing codebase, files, or database exist. Build the entire full-stack application from scratch following the tech stack and requirements listed above. The final deliverable must include both the backend (`server/`) and frontend (`client/`) in a single repository with a `README.md` containing instructions to install dependencies and start both services. The application must operate entirely on the local machine. The backend server MUST call `app.listen` exclusively on `127.0.0.1` and MUST NOT bind to `0.0.0.0`. Application code MUST NOT initiate any outbound socket, TCP connection, or HTTP connection to any external host. Express `app.listen('127.0.0.1', 3000)` is the only permitted inbound listening socket; Node's internal HTTP server stack invoked by `app.listen` is allowed. Backend application code MUST NOT explicitly import or use the following modules to make outbound connections: `https`, `net`, `tls`, `dns`, `dgram`, `child_process`, or any third-party HTTP client (`fetch`, `axios`). No code in the frontend may perform outbound network requests to external origins. The frontend MUST use Axios exclusively to communicate with the local backend; all Axios requests in the frontend MUST target `http://127.0.0.1:3000` only. All fonts, icons, and static assets MUST be sourced exclusively from the npm packages listed in the Tech Stack. The backend MUST only use the packages listed in the Tech Stack section; no additional backend packages may be introduced.
