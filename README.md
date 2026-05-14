# User API

A small FastAPI CRUD API for managing users with SQLAlchemy and PostgreSQL.

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file from `.env.example` and set your database URL:

```bash
DATABASE_URL=postgresql://postgres:password@localhost/app
```

4. Run the API:
 
```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## Endpoints

- `GET /` - health welcome message
- `GET /users` - list users
- `GET /user/{id}` - get user by id
- `POST /user` - create user
- `PUT /user/{id}` - update user
- `DELETE /user/{id}` - delete user
