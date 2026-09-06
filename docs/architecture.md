# Architecture

## Architecture Style

نسخه MVP سامانه به صورت Modular Monolith طراحی می‌شود.

در MVP از Microservices استفاده نمی‌شود مگر اینکه بعداً به صورت صریح تصویب شود.

## Layers

```text
Frontend
    ↓
REST API
    ↓
Backend
    ↓
Database
