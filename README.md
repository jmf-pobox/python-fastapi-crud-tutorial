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

## Database Configuration

The application supports multiple database configurations:

1. **Development Database**: 
   - Default SQLite database at `dev.db`
   - Created automatically when no `DATABASE_URL` is set
   - Used for local development and testing
   - Not committed to version control

2. **Test Database**:
   - SQLite database at `test.db`
   - Used exclusively for running tests
   - Created and managed by pytest

3. **Production Database**:
   - Configured via `DATABASE_URL` environment variable
   - Typically PostgreSQL in production
   - Managed through Docker Compose in development

To use a different database, set the `DATABASE_URL` environment variable:
```bash
# PostgreSQL example
export DATABASE_URL=postgresql://user:password@localhost:5432/dbname

# SQLite example
export DATABASE_URL=sqlite:///./custom.db
```

## Getting Started

### Prerequisites

- Python 3.11 or higher
- Docker and Docker Compose
- Hatch (Python package manager)

### Setup and Running

1. Clone this repository
2. Navigate to the project directory
3. Install Hatch:
```bash
pip install hatch
```

4. Create and activate the development environment:
```bash
hatch env create
hatch shell
```

5. Start the application:
```bash
hatch run docker-up
hatch run dev
```

This will:
- Build the FastAPI application image
- Start a PostgreSQL database container
- Connect the application to the database
- Expose the API on port 8002

### Development Tools

The project uses Hatch for managing development tasks:

```bash
# Run tests
hatch run test

# Run linter (Ruff)
hatch run lint

# Format code (Ruff)
hatch run format

# Type checking (MyPy)
hatch run type

# Docker commands
hatch run docker-up     # Start containers
hatch run docker-down   # Stop containers
hatch run docker-logs   # View logs
hatch run docker-build  # Build images

# Development server
hatch run dev          # Start server with Docker
```

### API Endpoints

#### Health Check
- **GET /ping**: Health check endpoint
  ```bash
  # Check API health
  http --follow GET http://localhost:8002/ping
  ```

#### Notes Operations
- **GET /notes/**: Get all notes
  ```bash
  # Retrieve all notes
  http --follow GET http://localhost:8002/notes/
  ```

- **POST /notes/**: Create a new note
  ```bash
  # Create a new note
  http --follow --json POST http://localhost:8002/notes/ \
      title="Shopping List" \
      description="Milk, bread, eggs"
  ```

- **GET /notes/{id}/**: Get a specific note by ID
  ```bash
  # Retrieve note with ID 1
  http --follow GET http://localhost:8002/notes/1
  ```

- **PUT /notes/{id}/**: Update a specific note
  ```bash
  # Update note with ID 1
  http --follow --json PUT http://localhost:8002/notes/1 \
      title="Updated Shopping List" \
      description="Milk, bread, eggs, cheese"
  ```

- **DELETE /notes/{id}/**: Delete a specific note
  ```bash
  # Delete note with ID 1
  http --follow DELETE http://localhost:8002/notes/1
  ```

Each endpoint expects and returns JSON data in the following format:
```json
{
  "id": 1,              // Returned by GET, not required for POST/PUT
  "title": "string",    // Required, 3-50 characters
  "description": "string" // Required, 3-50 characters
}
```

Response Status Codes:
- `200`: Successful operation (GET, PUT, DELETE)
- `201`: Note created successfully (POST)
- `404`: Note not found
- `422`: Validation error (invalid input data)

### API Documentation

FastAPI automatically generates interactive API documentation for all endpoints. Once the application is running, you can access:

- **Swagger UI**: Interactive API documentation and testing interface
  - URL: [http://localhost:8002/docs](http://localhost:8002/docs)
  - Features:
    - Interactive endpoint testing
    - Request/response schema examples
    - Authentication support
    - Real-time API exploration

- **ReDoc**: Alternative documentation interface
  - URL: [http://localhost:8002/redoc](http://localhost:8002/redoc)
  - Features:
    - Clean, responsive interface
    - Searchable documentation
    - Schema references
    - Method and model descriptions

Both interfaces automatically update when API endpoints are modified and include:
- Detailed request/response schemas
- Input validation rules
- Example requests and responses
- Error responses and status codes
- Authentication requirements (when configured)
