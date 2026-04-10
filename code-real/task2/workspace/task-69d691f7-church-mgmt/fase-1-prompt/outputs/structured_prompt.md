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

1. An organization registers with a name, mission statement, and an initial admin staff account (email + password).
2. Staff can create, read, update, and delete member profiles. Each profile includes: full name, email, phone number, membership date (ISO date string), and one or more involvement areas selected from a configurable list.
3. A member profile supports linked family connections: a spouse (linked by member ID) and zero or more children (each linked by member ID), all stored as separate member profiles.
4. Staff can manage the involvement area list: add, rename, and delete areas (e.g., "worship team", "youth ministry", "hospitality", "outreach").
5. Authenticated users can create small groups. Each group stores: name, description, meeting frequency (`weekly` | `biweekly` | `monthly`), meeting day (integer 0–6), meeting time (HH:MM string), location, leader ID (must be an existing member), and category (`bible_study` | `support_group` | `service_team` | `social`).
6. Any authenticated member can browse the list of available groups and submit a join request to any group they are not already a member of.
7. A group leader can list pending join requests for their groups and approve or reject each request individually. Approved members are added to the roster; rejected requests are discarded.
8. Each group exposes a roster endpoint returning the list of all currently approved members.
9. A group leader records meeting attendance by submitting a meeting date and an array of member IDs who attended. Each submission creates or replaces the attendance record for that specific date.
10. Each group has a discussion board. Approved group members can post a message with an optional `parentId` for threaded replies and retrieve all messages in the board.
11. Each group has a prayer request list. Only current approved group members can post or view prayer requests. Each request has a title and a description field.
12. Staff can create church-wide events. Each event stores: title, date (ISO date), time (HH:MM), location, and description.
13. Any authenticated member can RSVP to an event with status `attending` or `not_attending`. A member can update their own RSVP. Staff can retrieve the full RSVP list for any event.
14. The check-in system for events allows searching members by name fragment and marking a matched member as checked in for a specific event. A member can only be checked in once per event; a duplicate check-in returns HTTP 409.
15. Staff define volunteer roles (e.g., "Sunday greeter", "sound technician"). Roles are reusable across schedule slots.
16. Staff create weekly volunteer schedule slots, each containing a role ID, a date, and an optional member ID assignment. Members can self-sign-up for unassigned slots.
17. If assigning a member to a slot would result in that member having two slots on the same date, the API returns HTTP 409 with a conflict error body `{ error: string, conflictingSlotId: number }`.
18. Any schedule slot with no assigned member is flagged as `gap: true` in the response. The schedule endpoint accepts a `date` query parameter (YYYY-MM-DD) to filter results by date.
19. Staff record donations per member: amount (decimal, two decimal places), date (ISO date), and fund designation (`general` | `missions` | `building`).
20. Staff can retrieve an annual giving summary per member (total and count per fund for a given year) and organization-wide donation totals grouped by fund for a given year.
21. Staff can send announcements with a title and body to all members or filtered to members with a specific involvement area. Announcements are stored and retrievable by all authenticated users.
22. The reports endpoint for a group returns: the average attendance count across the group's last 12 recorded meetings and an array of per-meeting attendance counts representing the trend.
23. The engagement endpoint returns a score per member calculated as: `(number of events the member checked in to) + (number of group meetings the member attended)`.
24. All data persists in a SQLite database file. The database initializes all required tables automatically on server startup if they do not already exist.
25. The API implements JWT authentication. Every protected route requires a valid `Authorization: Bearer <token>` header. The JWT payload includes `{ id, email, role }`. Missing tokens return HTTP 401; invalid or expired tokens return HTTP 403.
26. Three roles exist: `staff`, `group_leader`, `member`. Role-based access control is enforced on all protected routes: staff access all endpoints; group leaders manage only their own groups (attendance, roster, join requests); members access browsing, events, RSVP, volunteer sign-up, and group participation features.

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
- **Input:** `dbPath?: string` — optional SQLite file path; defaults to `./church.db`
- **Output:** `Database` — connected better-sqlite3 `Database` instance with all tables created
- **Description:** Creates all tables if they do not exist (users, organizations, members, family_links, involvement_areas, groups, group_members, group_join_requests, meeting_attendance, discussion_posts, prayer_requests, events, rsvps, checkins, volunteer_roles, volunteer_slots, donations, announcements) and returns the database instance.

### Auth Router
- **Path:** `server/src/routes/auth.ts`
- **Name:** `authRouter`
- **Type:** Express Router
- **Input:** `POST /auth/register` body `{ name: string, email: string, password: string, role: 'staff'|'group_leader'|'member' }` · `POST /auth/login` body `{ email: string, password: string }`
- **Output:** `{ token: string, user: { id: number, name: string, email: string, role: string } }` · HTTP 401 on invalid credentials · HTTP 409 on duplicate email
- **Description:** Registers a new user with hashed password and authenticates existing users. Returns a signed JWT on success.

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
- **Description:** Church-wide event management (staff create only), RSVP tracking, and check-in recording. The search endpoint returns members matching the name fragment for the check-in interface.

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
- **Input:** `POST /communications/announcements` body `{ title: string, body: string, involvementArea?: string }` (staff only) · `GET /communications/announcements`
- **Output:** Announcement object `{ id, title, body, targetArea: string|null, sentAt: string, sentBy: number }` or array
- **Description:** Staff create announcements targeted to all members or filtered by involvement area. All authenticated users can read the announcement feed.

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
- **Output:** `void` — attaches `req.user: { id: number, email: string, role: string }` on success · HTTP 401 if token missing · HTTP 403 if token invalid or expired
- **Description:** Verifies the JWT signature, decodes the payload, and attaches the user object to the request. Calls `next()` on success.

### Role Guard Middleware
- **Path:** `server/src/middleware/auth.ts`
- **Name:** `requireRole`
- **Type:** function (middleware factory)
- **Input:** `...roles: ('staff' | 'group_leader' | 'member')[]`
- **Output:** Express `RequestHandler` — calls `next()` if `req.user.role` is in the allowed list; returns HTTP 403 otherwise
- **Description:** Returns an Express middleware that enforces role-based access. Used after `authenticateToken` on routes requiring specific roles.

## Current State
This is a greenfield project. No existing codebase, files, or database exist. Build the entire full-stack application from scratch following the tech stack and requirements listed above. The final deliverable must include both the backend (`server/`) and frontend (`client/`) in a single repository with a `README.md` containing instructions to install dependencies and start both services.
