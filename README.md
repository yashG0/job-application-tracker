# Job Application Tracker

A modern job application tracking system built with FastAPI, PostgreSQL, SQLAlchemy, Jinja2, and HTMX.

## Features

### Application Management

* Create job applications
* View all applications
* View application details
* Delete applications
* Track application progress

### Dashboard

* Total applications
* Wishlist count
* Applied count
* Assessment count
* Interview count
* Offer count
* Rejected count

### Search & Filtering

* Live company search using HTMX
* Filter applications by status
* Dynamic UI updates without page reloads

### Status Workflow

* Wishlist
* Applied
* Assessment
* Interview
* Offer
* Rejected

## Tech Stack

### Backend

* FastAPI
* PostgreSQL
* SQLAlchemy (Async)
* Pydantic

### Frontend

* Jinja2
* HTMX
* Vanilla JavaScript
* CSS

## Architecture

```text
Routes
  ↓
Services
  ↓
Repositories
  ↓
Database
```

### Layers

#### Repository Layer

Responsible for database operations.

#### Service Layer

Responsible for business logic and validation.

#### Route Layer

Responsible for HTTP requests and responses.

## Project Structure

```text
project/
│
├── api/
│   ├── application_route.py
│   └── view_route.py
│
├── core/
│   ├── database.py
│   ├── template.py
│   └── static.py
│
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── applications.html
│   ├── application_detail.html
│   └── partials/
│       ├── application_list.html
│       └── application_form.html
│
├── static/
│   ├── css/
│   │   ├── style.css
│   │   └── app_style.css
│   └── js/
│       └── script.js
│
├── model.py
├── schema.py
├── application_repository.py
├── services.py
├── main.py
└── seed.py
```

## Running

```bash
uv sync
uv run main.py
```

Open:

```text
http://localhost:8000/pages/dashboard
```

## Future Improvements

* Edit applications
* Status updates from UI
* Pagination
* Resume uploads
* Dark mode
* Authentication
* User accounts
* Email reminders
* Analytics dashboard
* Kanban board view

```
```
