# Job Application Tracker

A modern job application tracking system built with FastAPI, PostgreSQL, and SQLAlchemy.

Track applications, monitor interview progress, organize opportunities, and gain insights into your job search through a clean dashboard.

## Features

* Create and manage job applications
* Track application status
* Dashboard statistics
* PostgreSQL persistence
* Async SQLAlchemy ORM
* Repository-Service architecture
* RESTful API
* Input validation with Pydantic
* FastAPI automatic OpenAPI documentation

## Application Status Flow

```text
Wishlist
    ↓
Applied
    ↓
Assessment
    ↓
Interview
    ↓
Offer

Rejected
```

## Tech Stack

### Backend

* FastAPI
* PostgreSQL
* SQLAlchemy 2.0
* AsyncPG
* Pydantic v2
* Uvicorn

### Architecture

```text
Routes
  ↓
Services
  ↓
Repositories
  ↓
PostgreSQL
```

## Project Structure

```text
.
├── api
│   └── application_route.py
├── core
│   ├── config.py
│   └── database.py
├── models
│   └── application.py
├── repositories
│   └── application_repository.py
├── schemas
│   └── application.py
├── services
│   └── application_service.py
├── seed.py
├── main.py
└── README.md
```

## Database Model

### Application

| Field       | Type     |
| ----------- | -------- |
| id          | Integer  |
| company     | String   |
| position    | String   |
| location    | String   |
| job_url     | String   |
| status      | Enum     |
| notes       | Text     |
| resume_path | String   |
| applied_at  | DateTime |
| created_at  | DateTime |
| updated_at  | DateTime |

## API Endpoints

### Applications

| Method | Endpoint          | Description           |
| ------ | ----------------- | --------------------- |
| POST   | /application/new  | Create application    |
| GET    | /application      | Get all applications  |
| GET    | /application/{id} | Get application by ID |
| DELETE | /application/{id} | Delete application    |

### Dashboard

| Method | Endpoint               | Description          |
| ------ | ---------------------- | -------------------- |
| GET    | /application/dashboard | Dashboard statistics |

Example dashboard response:

```json
{
  "total": 20,
  "wishlist": 3,
  "applied": 8,
  "assessment": 2,
  "interview": 4,
  "offer": 1,
  "rejected": 2
}
```

## Local Development

### Clone Repository

```bash
git clone <repository-url>
cd Job-Application-Tracker
```

### Create Virtual Environment

```bash
uv sync
```

### Environment Variables

Create a `.env` file:

```env
DB_URL=postgresql+asyncpg://postgres:password@localhost:5432/job_tracker
```

### Run Database

```bash
createdb job_tracker
```

### Seed Sample Data

```bash
uv run seed.py
```

### Start Development Server

```bash
uv run uvicorn main:app --reload
```

### Open API Docs

```text
http://127.0.0.1:8000/docs
```

## Future Enhancements

* Jinja2 templates
* HTMX integration
* Tailwind CSS UI
* Search applications
* Filter by status
* Update application status
* Resume uploads
* Interview scheduling
* Authentication and authorization

## Learning Objectives

This project demonstrates:

* FastAPI development
* PostgreSQL integration
* Async SQLAlchemy
* Repository Pattern
* Service Layer Architecture
* REST API Design
* Data Validation
* Dashboard Aggregation Queries

## License

MIT License
