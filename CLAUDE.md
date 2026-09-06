# CLAUDE.md — School Platform Engineering Contract

## Project

Comprehensive School Management Platform.

## Current Phase

Phase 1 — Foundation.

## Product Architecture

This is a multi-school, multi-academic-year school management platform.

The platform will eventually support:

- Manager
- Educational Deputy
- Cultural/Educational Deputy
- Executive Deputy
- Teacher
- Subject Teacher
- Counselor
- Health Coach
- Sports Coach

A user may belong to multiple schools and may have different roles in different schools.

School data must never leak between schools.

Academic-year data must be preserved historically.

## Technology Stack

### Frontend

- Next.js
- TypeScript
- React
- RTL-first Persian interface
- Mobile-first responsive design

### Backend

- Python
- FastAPI
- REST API
- API versioning

### Database

- PostgreSQL
- SQLAlchemy
- Alembic migrations

### Infrastructure

- Docker
- Docker Compose

### AI

AI must be accessed through a backend AI service layer.

The frontend must never call an AI provider directly.

AI receives only permission-filtered and minimized context.

## Architecture Principles

1. Backend authorization is the final security boundary.
2. Frontend visibility is never considered security.
3. Every school-scoped resource must be isolated by school.
4. Academic-year data must be preserved.
5. Important academic records should not be hard-deleted.
6. Shared school information must be entered once and reused.
7. Business logic must not exist only in the frontend.
8. Database schema changes require Alembic migrations.
9. Features require automated tests.
10. Keep modules independent and maintainable.
11. Avoid unnecessary dependencies.
12. Do not change the approved technology stack without explicit approval.
13. Do not introduce microservices during the MVP unless explicitly approved.
14. The MVP uses a modular monolith architecture.
15. Sensitive student information must have restricted access.
16. AI must not receive unnecessary sensitive student information.
17. Never invent official school events or regulations.
18. User-facing text is Persian by default.
19. Internal code, database fields and API identifiers use English.
20. RTL must be treated as a first-class requirement.

## Current Foundation Scope

The current phase is intentionally small.

### Allowed

- Repository structure
- FastAPI application
- FastAPI health endpoint
- Next.js application
- TypeScript configuration
- Docker Compose
- PostgreSQL container
- Basic automated tests
- Foundation documentation

### Not Allowed Yet

Do NOT implement:

- Authentication
- Registration
- Users database models
- Schools database models
- Academic years
- Roles
- Permissions
- Students
- Classes
- Teachers
- Calendar
- Reports
- AI
- Dashboards
- Cultural modules
- Counseling
- Health
- Sports
- Any other business module

These belong to later phases.

## Foundation API

The only API endpoint required in this phase is:

GET /api/v1/health

Expected response:

```json
{
  "status": "ok",
  "service": "school-platform-api"
}
