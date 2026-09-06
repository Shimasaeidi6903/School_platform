# سامانه جامع مدرسه

سامانه جامع مدیریت مدرسه با معماری مدرن، ماژولار و چندمدرسه‌ای.

## وضعیت پروژه

در حال توسعه — Phase 1: Foundation

## هدف

ایجاد یک پلتفرم یکپارچه برای مدیریت فرآیندهای آموزشی، فرهنگی، اجرایی، مشاوره، سلامت و ورزش مدرسه.

## فناوری‌ها

### Frontend

- Next.js
- TypeScript
- React
- RTL
- Persian-first UI
- Responsive Design

### Backend

- Python
- FastAPI
- REST API

### Database

- PostgreSQL
- SQLAlchemy
- Alembic

### Infrastructure

- Docker
- Docker Compose

### AI

AI از طریق Backend و یک لایه مستقل AI Service استفاده خواهد شد.

## معماری

پروژه در نسخه MVP به صورت Modular Monolith توسعه داده می‌شود.

ساختار کلی:

```text
school-platform
│
├── frontend
├── backend
├── docs
├── tests
├── CLAUDE.md
├── README.md
└── docker-compose.yml
