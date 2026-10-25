# 🚀 FastAPI Blog REST API

A Blog REST API built with **Python, FastAPI, SQLAlchemy, and PostgreSQL**, featuring CRUD operations, JWT-based authentication, pagination, Pydantic validation, and interactive API documentation with Swagger UI. 📝

## ✨ Features

- **CRUD operations** — Create, read, update, and delete blog posts.
- **JWT authentication** — Protect endpoints that modify blog posts.
- **Pagination** — Retrieve blog posts in smaller pages using `skip` and `limit`.
- **PostgreSQL** — Persist blog data in a relational database.
- **SQLAlchemy ORM** — Work with database records using Python objects.
- **Pydantic validation** — Validate request data and serialize responses.
- **Swagger UI** — Explore and test API endpoints interactively.
- **FastAPI dependency injection** — Manage database sessions and authentication dependencies.

## 🛠️ Tech Stack

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- JWT (`python-jose`)
- Uvicorn
- Swagger UI

## 📁 Project Structure

```text
fastapi-blog-api/
├── main.py
├── database.py
├── models.py
├── schemas.py
├── auth.py
├── requirements.txt
├── .env                 # Local secrets; do not commit
├── .gitignore
└── README.md
```

## ⚙️ Getting Started

### 1. Clone the repository

Replace `YOUR_USERNAME` with your GitHub username.

```bash
git clone https://github.com/YOUR_USERNAME/fastapi-blog-api.git
cd fastapi-blog-api
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Windows Command Prompt:

```bat
python -m venv .venv
.venv\Scripts\activate.bat
```

### 3. Install dependencies

If `requirements.txt` is already included:

```bash
pip install -r requirements.txt
```

Or install the common dependencies directly:

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary python-jose python-multipart
```

After installing all packages your project uses, generate the dependency file:

```bash
pip freeze > requirements.txt
```

### 4. Configure PostgreSQL

Create a PostgreSQL database named `blogdb`, or update the connection string to match your database.

Your connection string should follow this format:

```text
postgresql://USERNAME:PASSWORD@localhost:5432/blogdb
```

Configure the connection string and JWT secret through environment variables or a local `.env` file, and load them in your application. Do not commit real passwords or secret keys to GitHub.

### 5. Start the server

```bash
uvicorn main:app --reload
```

Open these URLs in your browser:

- API root: http://127.0.0.1:8000/
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## 🔌 API Endpoints

| Method | Endpoint | Purpose | Authentication in the current example |
|---|---|---|---|
| `GET` | `/` | Check API status | Not required |
| `POST` | `/login` | Generate a JWT token | Not required in the demo |
| `POST` | `/blogs` | Create a blog post | Required |
| `GET` | `/blogs` | List blog posts | Not required |
| `GET` | `/blogs/{id}` | Get one blog post | Not required |
| `PUT` | `/blogs/{id}` | Update a blog post | Required |
| `DELETE` | `/blogs/{id}` | Delete a blog post | Required |

Adjust this table if your implementation differs. The demo `/login` endpoint that creates a token without checking credentials is for learning only and is not suitable for production.

## 📄 Pagination

Pagination lets clients request a smaller portion of a collection at a time.

Example requests, **if pagination is implemented** on `GET /blogs`:

```http
GET /blogs?skip=0&limit=10
GET /blogs?skip=10&limit=10
GET /blogs?skip=20&limit=10
```

- `skip`: Number of records to skip.
- `limit`: Maximum number of records to return.

If your endpoint does not yet accept these query parameters, implement pagination before advertising it as a working feature.

## 🔐 JWT Authentication Workflow

1. Call `POST /login` to receive an access token.
2. Copy the `access_token` from the response.
3. Send it to protected endpoints in the request header:

```http
Authorization: Bearer YOUR_ACCESS_TOKEN
```

4. The authentication dependency validates the token before the protected endpoint runs.

A JWT is signed, not encrypted. Do not put passwords or other secrets in its payload. For production, validate user credentials, hash passwords, store the JWT secret securely, and configure token expiration and authorization rules.

## 📬 Example Blog Request

Send this JSON body to `POST /blogs`:

```json
{
  "title": "Getting Started with FastAPI",
  "content": "FastAPI is a modern Python framework for building APIs."
}
```

Example response shape:

```json
{
  "id": 1,
  "title": "Getting Started with FastAPI",
  "content": "FastAPI is a modern Python framework for building APIs."
}
```

The returned ID and data depend on your database.

## 🎯 Learning Objectives

This project demonstrates practical use of:

- REST API development with FastAPI.
- PostgreSQL integration with SQLAlchemy.
- Request and response validation with Pydantic.
- JWT token creation and validation.
- CRUD operations and pagination.
- Interactive API testing with Swagger UI.

## 🚧 Possible Future Improvements

- User registration and credential-based login.
- User-specific blog ownership and authorization.
- Search, filtering, and sorting.
- Database migrations with Alembic.
- Automated tests with Pytest.
- Docker support and deployment.

## 📜 License

This project is licensed under the **MIT License**. You are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software, subject to the conditions in the [MIT License](LICENSE).

## 👨‍💻 Author

**Pramod Patil**

- 📧 Email: [pramodpatil0520@gmail.com](mailto:pramodpatil0520@gmail.com)
- 💼 LinkedIn: [linkedin.com/in/pramod-patil-a00309265](https://www.linkedin.com/in/pramod-patil-a00309265)

If you find this project useful, feel free to ⭐ the repository!

---

Made with ❤️ using Python and FastAPI.

