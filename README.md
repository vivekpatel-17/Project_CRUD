# FastAPI User Task Manager

A clean FastAPI backend for managing users, tasks, and the mapping between them. This project supports full CRUD operations for users and tasks, plus APIs to assign tasks to users, list all assignments, fetch tasks for a user, and delete an assignment.

## Features

- User CRUD: create, read, update, and delete users
- Task CRUD: create, read, update, and delete tasks
- User-task mapping: assign tasks to users
- PostgreSQL database connection with SQLAlchemy
- Pydantic request schemas
- Alembic migration setup
- Consistent API response format
- Interactive API docs from FastAPI

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- Uvicorn
- Pydantic

## Project Structure

```text
app/
|-- alembic/                 # Database migrations
|-- core/
|   `-- database.py          # Database engine, session, and Base setup
|-- models/
|   |-- user_model.py        # User table model
|   |-- tasks_model.py       # Task table model
|   `-- user_task.py         # User-task mapping table model
|-- routes/
|   |-- user_routes.py       # User CRUD endpoints
|   |-- task_routes.py       # Task CRUD endpoints
|   `-- user_task_routes.py  # Task assignment endpoints
|-- schemas/
|   |-- user_schemas.py      # User request/response schemas
|   |-- schemas_taks.py      # Task request/response schemas
|   `-- user_task_schemas.py # User-task mapping schemas
|-- services/
|   |-- user_services.py     # User business logic
|   |-- tasks_services.py    # Task business logic
|   `-- user_task_services.py# Mapping business logic
|-- utils/
|   `-- response.py          # Common API response helper
|-- main.py                  # FastAPI app entry point
|-- requirements.txt
`-- README.md
```

## Getting Started

### 1. Clone the Project

```bash
git clone <your-repository-url>
cd app
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Activate it on macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/your_database_name
```

Example:

```env
DATABASE_URL=postgresql://postgres:admin@localhost:5432/user_task_db
```

### 5. Run Database Migrations

If you are using Alembic migrations:

```bash
alembic upgrade head
```

The app also calls `Base.metadata.create_all(bind=engine)` in `main.py`, which can create tables directly when the application starts.

### 6. Start the Server

```bash
uvicorn main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

Interactive documentation:

```text
http://127.0.0.1:8000/docs
```

Alternative documentation:

```text
http://127.0.0.1:8000/redoc
```

## API Response Format

Most endpoints return data using this format:

```json
{
  "status_code": 200,
  "message": "Operation message",
  "data": {},
  "success": true
}
```

## Root Endpoint

### Check API Status

```http
GET /
```

Response:

```json
{
  "message": "Welcome to the User API!"
}
```

## User CRUD APIs

### Create User

```http
POST /user
```

Request body:

```json
{
  "username": "Virat",
  "email": "virat@example.com",
  "password": "securepassword"
}
```

cURL:

```bash
curl -X POST http://127.0.0.1:8000/user \
  -H "Content-Type: application/json" \
  -d "{\"username\":\"Virat\",\"email\":\"virat@example.com\",\"password\":\"securepassword\"}"
```

### Get All Users

```http
GET /users
```

cURL:

```bash
curl http://127.0.0.1:8000/users
```

### Get User By ID

```http
GET /user/{id}
```

Example:

```bash
curl http://127.0.0.1:8000/user/1
```

### Update User

```http
PUT /user/{id}
```

Request body:

```json
{
  "username": "Virat Updated",
  "email": "virat.updated@example.com",
  "password": "newpassword"
}
```

cURL:

```bash
curl -X PUT http://127.0.0.1:8000/user/1 \
  -H "Content-Type: application/json" \
  -d "{\"username\":\"Virat Updated\",\"email\":\"virat.updated@example.com\",\"password\":\"newpassword\"}"
```

### Delete User

```http
DELETE /user/{id}
```

Example:

```bash
curl -X DELETE http://127.0.0.1:8000/user/1
```

## Task CRUD APIs

### Create Task

```http
POST /tasks
```

Request body:

```json
{
  "title": "Complete FastAPI project",
  "description": "Build CRUD APIs and user-task mapping"
}
```

cURL:

```bash
curl -X POST http://127.0.0.1:8000/tasks \
  -H "Content-Type: application/json" \
  -d "{\"title\":\"Complete FastAPI project\",\"description\":\"Build CRUD APIs and user-task mapping\"}"
```

### Get All Tasks

```http
GET /tasks
```

cURL:

```bash
curl http://127.0.0.1:8000/tasks
```

### Get Task By ID

```http
GET /tasks/{id}
```

Example:

```bash
curl http://127.0.0.1:8000/tasks/1
```

### Update Task

```http
PUT /tasks/{id}
```

Request body:

```json
{
  "title": "Complete FastAPI project updated",
  "description": "Update CRUD APIs and README documentation"
}
```

cURL:

```bash
curl -X PUT http://127.0.0.1:8000/tasks/1 \
  -H "Content-Type: application/json" \
  -d "{\"title\":\"Complete FastAPI project updated\",\"description\":\"Update CRUD APIs and README documentation\"}"
```

### Delete Task

```http
DELETE /task/{id}
```

Example:

```bash
curl -X DELETE http://127.0.0.1:8000/task/1
```

Note: the delete route uses `/task/{id}` while the other task routes use `/tasks`.

## User Task Mapping APIs

Use these endpoints to connect users with tasks.

### Assign Task To User

```http
POST /assign-task
```

Request body:

```json
{
  "user_id": 1,
  "task_id": 1
}
```

cURL:

```bash
curl -X POST http://127.0.0.1:8000/assign-task \
  -H "Content-Type: application/json" \
  -d "{\"user_id\":1,\"task_id\":1}"
```

### Get All User-Task Mappings

```http
GET /task-mappings
```

cURL:

```bash
curl http://127.0.0.1:8000/task-mappings
```

### Get Tasks Assigned To A User

```http
GET /users/{user_id}/tasks
```

Example:

```bash
curl http://127.0.0.1:8000/users/1/tasks
```

### Delete User-Task Mapping

```http
DELETE /task-mapping/{mapping_id}
```

Example:

```bash
curl -X DELETE http://127.0.0.1:8000/task-mapping/1
```

## Complete Flow Example

### 1. Create a User

```bash
curl -X POST http://127.0.0.1:8000/user \
  -H "Content-Type: application/json" \
  -d "{\"username\":\"Aman\",\"email\":\"aman@example.com\",\"password\":\"pass123\"}"
```

### 2. Create a Task

```bash
curl -X POST http://127.0.0.1:8000/tasks \
  -H "Content-Type: application/json" \
  -d "{\"title\":\"Learn FastAPI\",\"description\":\"Practice routes, schemas, services, and database models\"}"
```

### 3. Assign The Task To The User

```bash
curl -X POST http://127.0.0.1:8000/assign-task \
  -H "Content-Type: application/json" \
  -d "{\"user_id\":1,\"task_id\":1}"
```

### 4. Check Tasks For The User

```bash
curl http://127.0.0.1:8000/users/1/tasks
```

## Database Tables

### `users`

| Column | Type | Description |
| --- | --- | --- |
| `id` | Integer | Primary key |
| `username` | String | User name |
| `email` | String | Unique email address |
| `hashed_password` | String | Stored password field |
| `created_at` | DateTime | Creation timestamp |
| `updated_at` | DateTime | Last update timestamp |

### `tasks`

| Column | Type | Description |
| --- | --- | --- |
| `id` | Integer | Primary key |
| `title` | String | Task title |
| `description` | String | Task details |
| `completed` | Boolean | Task completion status |
| `created_at` | DateTime | Creation timestamp |
| `updated_at` | DateTime | Last update timestamp |

### `user_task_mapping`

| Column | Type | Description |
| --- | --- | --- |
| `id` | Integer | Primary key |
| `user_id` | Integer | Foreign key connected to `users.id` |
| `task_id` | Integer | Foreign key connected to `tasks.id` |
| `created_at` | DateTime | Assignment timestamp |

## Development Notes

- Keep route functions inside `routes/`.
- Keep database models inside `models/`.
- Keep request and response schemas inside `schemas/`.
- Keep business logic inside `services/`.
- Use `/docs` while testing because FastAPI generates a complete Swagger UI automatically.
- Run migrations after changing database models.

## Useful Commands

```bash
uvicorn main:app --reload
```

```bash
alembic revision --autogenerate -m "your migration message"
```

```bash
alembic upgrade head
```

## License

This project is open for learning, practice, and improvement.
    