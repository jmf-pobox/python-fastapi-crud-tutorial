# Project Structure TODOs

1. Directory Structure Alignment
   - [✓] Move `tests` directory from `src/tests` to root level `/tests`
   - [✓] Rename `app` directory to match package name (should be under src/package_name)
   - [✓] Create missing recommended directories:
     - [✓] `core/` for core functionality
     - [✓] `models/` for data models
     - [✓] `schemas/` for data validation schemas
     - [✓] `db/` directory (move db.py into this)

2. Development Tools
   - [✓] Ruff is properly configured
   - [✓] MyPy is properly configured with --strict
   - [✓] Pytest is properly configured
   - [✓] Docker is set up
   - [ ] Consider migrating from direct pip/venv to Hatch for environment management

3. Code Organization
   - [ ] Review and implement Single Responsibility Principle across modules
   - [ ] Add type hints to all functions (need to check current coverage)
   - [ ] Consider implementing proper dependency injection patterns
   - [ ] Move database models to `models/` directory
   - [ ] Create Pydantic schemas in `schemas/` directory

4. Project Configuration
   - [✓] pyproject.toml exists and is well configured
   - [✓] Dependencies are properly specified
   - [✓] Build system is configured (using hatchling)
   - [✓] Development scripts are defined
   - [ ] Consider adding more Hatch environments (e.g., dev, prod)

5. Testing
   - [ ] Ensure test coverage for all public methods
   - [ ] Add property-based testing where appropriate
   - [ ] Implement proper mocking for external dependencies

6. Documentation
   - [ ] Add docstrings to all public functions and classes
   - [ ] Enhance README.md with setup and development instructions
   - [ ] Document API endpoints (if using FastAPI, consider adding OpenAPI docs)

7. Database
   - [ ] Consider adding Alembic for database migrations
   - [ ] Move database configuration to separate config file
   - [ ] Implement proper repository pattern for data access

8. Code Quality
   - [ ] Run full ruff check and address any issues
   - [ ] Run mypy --strict and fix any type issues
   - [ ] Implement proper error handling with custom exceptions
   - [ ] Review async/await patterns usage
