# 💼 Job Application Tracker

A modern full-stack job application tracking system built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, **Jinja2**, and **HTMX**.

The application helps users organize and manage their job search by tracking applications through different hiring stages. It demonstrates RESTful backend development, layered architecture, asynchronous database operations, and dynamic frontend interactions using HTMX.

---

## ✨ Features

### 📋 Job Application Management

- Create job applications
- View all applications
- View detailed application information
- Delete applications
- Track application progress across hiring stages

### 📊 Interactive Dashboard

- Total applications
- Wishlist count
- Applied count
- Assessment count
- Interview count
- Offer count
- Rejected count

### 🔍 Search & Filtering

- Live company search with HTMX
- Filter applications by status
- Dynamic page updates without full page reloads

### 🔄 Application Workflow

- Wishlist
- Applied
- Assessment
- Interview
- Offer
- Rejected

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| FastAPI | Backend Framework |
| PostgreSQL | Database |
| SQLAlchemy (Async) | ORM |
| Pydantic | Data Validation |
| Jinja2 | Server-side Templates |
| HTMX | Dynamic UI |
| JavaScript | Client-side Interactions |
| CSS | Styling |

---

## 🏗 Architecture

```text
Client
    │
    ▼
Routes
    │
    ▼
Services
    │
    ▼
Repositories
    │
    ▼
PostgreSQL
```

### Layer Responsibilities

### Repository Layer

Handles all database queries and persistence logic.

### Service Layer

Implements business logic, validation, and application workflows.

### Route Layer

Processes HTTP requests, returns responses, and coordinates with services.

---

## 📂 Project Structure

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
│
├── static/
│   ├── css/
│   └── js/
│
├── model.py
├── schema.py
├── application_repository.py
├── services.py
├── seed.py
└── main.py
```

---

## ⚙️ Getting Started

### Clone Repository

```bash
git clone https://github.com/yashG0/job-application-tracker.git

cd job-application-tracker
```

### Install Dependencies

```bash
uv sync
```

### Configure Environment

Create a `.env` file.

```env
DATABASE_URL=postgresql://username:password@localhost/job_tracker
```

### Run the Application

```bash
uv run main.py
```

Open

```
http://localhost:8000/pages/dashboard
```

---

## 📡 Main Features

| Feature | Description |
|---------|-------------|
| Dashboard | View application statistics |
| CRUD Operations | Create, Read, Delete applications |
| Live Search | HTMX-powered company search |
| Status Workflow | Track hiring progress |
| Responsive UI | Server-rendered pages with HTMX |

---

## 🗄 Database

### applications

| Column | Type |
|---------|------|
| id | INTEGER |
| company | TEXT |
| role | TEXT |
| status | TEXT |
| location | TEXT |
| applied_date | DATE |
| notes | TEXT |

---

## 📸 Screenshots

### Dashboard

> Add dashboard screenshot

### Application List

> Add application management screenshot

### Search & Filtering

> Add HTMX live search screenshot

---

## 🎯 Why I Built This

I built this project to gain practical experience with backend application architecture using FastAPI and PostgreSQL. The project focuses on asynchronous database operations, layered architecture, RESTful application design, and improving user experience with HTMX-powered dynamic interfaces.

---

## 🚀 Future Improvements

- Update existing applications
- Authentication & Authorization
- Multi-user support
- Resume uploads
- Email reminders
- Pagination
- Kanban board
- Analytics dashboard
- Dark mode
- Docker support
- Unit & Integration Tests

---

## 👨‍💻 Author

**Yash Gaurkar**

- GitHub: https://github.com/yashG0
- LinkedIn: https://linkedin.com/in/yash-gaurkar-a897b3228
- Portfolio: https://yash-portfolio-app.vercel.app

---

⭐ If you found this project helpful, consider giving it a **Star**.
