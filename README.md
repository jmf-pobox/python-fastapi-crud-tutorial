# FastAPI CRUD Application

A simple RESTful API application built with FastAPI for managing notes, featuring CRUD operations (Create, Read, Update, Delete). This is based entirely upon the testdriven.io tutorial at https://testdriven.io/blog/fastapi-crud/ which was written by Michael Herman (https://testdriven.io/authors/herman/)

## Project Architecture

This project follows a clean architecture with separation of concerns:

### Core Components:

- **API Routes (`notes.py`)**: Defines HTTP endpoints, handles requests/responses, status codes
- **Database Operations (`crud.py`)**: Contains database interaction functions for CRUD operations
- **Data Models (`models.py`)**: Defines Pydantic models for data validation
- **Database Configuration (`db.py`)**: Sets up SQLAlchemy connection, table definitions

### Component Relationships:

- `notes.py` (router) calls functions from `crud.py` to perform database operations
- `crud.py` interacts directly with the database using models defined in `models.py`
- Tests mock `crud.py` functions to test router functionality without database interactions

## Getting Started

### Prerequisites

- Docker and Docker Compose

### Setup and Running

1. Clone this repository
2. Navigate to the project directory
3. Start the application:

```bash
docker-compose up -d --build
```

This will:
- Build the FastAPI application image
- Start a PostgreSQL database container
- Connect the application to the database
- Expose the API on port 8002

### API Endpoints

- **GET /ping**: Health check endpoint
- **POST /notes/**: Create a new note
- **GET /notes/{id}/**: Get a note by ID

### Example API Requests

Using HTTPie:

```bash
# Health check
http GET http://localhost:8002/ping

# Create a note
http --json POST http://localhost:8002/notes/ title="My Note" description="Note content"

# Get a note
http GET http://localhost:8002/notes/1
```

## Development

### Project Structure

```
fastapi-crud/
├── docker-compose.yml
└── src/
    ├── Dockerfile
    ├── app/
    │   ├── __init__.py
    │   ├── api/
    │   │   ├── crud.py    # Database operations
    │   │   ├── models.py  # Pydantic models
    │   │   ├── notes.py   # API routes
    │   │   └── ping.py    # Health check
    │   ├── db.py          # Database configuration
    │   └── main.py        # Application setup
    ├── tests/             # Test files
    └── requirements.txt   # Dependencies
```

### Running Tests

```bash
# Run all tests
docker-compose exec web pytest .

# Run specific test file
docker-compose exec web pytest tests/test_notes.py
```

### Dependencies

- **FastAPI**: Modern web framework for building APIs
- **Uvicorn**: ASGI server for running FastAPI applications
- **SQLAlchemy**: SQL toolkit and ORM
- **Databases**: Async database support for Python
- **Asyncpg**: PostgreSQL client library for asyncio
- **Pytest**: Testing framework

## Environment Variables

The application uses the following environment variables:

- `DATABASE_URL`: PostgreSQL connection string (set in docker-compose.yml)

## Database Configuration

PostgreSQL database with the following settings (configured in docker-compose.yml):

- **User**: hello_fastapi
- **Password**: hello_fastapi
- **Database**: hello_fastapi_dev
- **Port**: 5432 (internal to Docker network)

## Note Schema

```json
{
  "id": 1,
  "title": "Example Note",
  "description": "This is a note description"
}
```

## Looking for some more challenges?

* Review the official tutorial. It's long but well worth a read.
* Implement async background tasks, database migrations, and auth.
* Abstract out the application configuration to a separate file.
* In a production environment, you'll probably want to stand up Gunicorn and let it manage Uvicorn. Review Running with Gunicorn and the Deployment guide for more info. Check out the official uvicorn-gunicorn-fastapi Docker image as well.
* Finally, check out the Test-Driven Development with FastAPI and Docker course as well as our other FastAPI courses for more!
Y* ou can find the source code in the fastapi-crud-async repo. Thanks for reading!
