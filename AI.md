# Python Project Preferences for AI Assistance

## Project Structure Guidelines
Recommended src-layout structure for Python projects:
```
project/
├── src/
│   └── package_name/
│       ├── __init__.py
│       ├── main.py
│       ├── api/         # For web/API projects
│       ├── core/        # Core functionality
│       ├── db/          # Database related code
│       ├── models/      # Data models
│       └── schemas/     # Data validation schemas
├── tests/
│   ├── __init__.py
│   └── test_*.py
├── pyproject.toml
├── README.md
└── .gitignore
```

## Core Development Tools
- Ruff (for linting and formatting)
- MyPy (for static type checking, use --strict)
- Pytest (for testing)
- Hatch (for project management)
- Docker (for containerization when needed)

## Project Management
- Always use `pyproject.toml` for project configuration
- Use Hatch for:
  - Virtual environment management
  - Build system
  - Development scripts
  - Dependency management
- Common Hatch commands:
  - `hatch run test`: Run tests
  - `hatch run lint`: Run linting
  - `hatch run type`: Run type checking
  - `hatch run format`: Format code
  - `hatch run dev`: Start development server (if applicable)

## Python Coding Preferences

1. **Object-Oriented Programming Principles**
   - Single Responsibility Principle (SRP):
     ```python
     # Bad: Class doing too much
     class UserManager:
         def create_user(self) -> None: ...
         def send_email(self) -> None: ...
         def validate_password(self) -> None: ...
     
     # Good: Separate responsibilities
     class UserCreator:
         def create_user(self) -> None: ...
     
     class EmailService:
         def send_email(self) -> None: ...
     
     class PasswordValidator:
         def validate_password(self) -> None: ...
     ```
   - Open/Closed Principle (OCP):
     ```python
     # Bad: Modifying existing class
     class PaymentProcessor:
         def process_payment(self, payment_type: str) -> None:
             if payment_type == "credit":
                 # process credit
             elif payment_type == "paypal":
                 # process paypal
     
     # Good: Extending through inheritance
     class PaymentProcessor:
         def process_payment(self) -> None: ...
     
     class CreditCardProcessor(PaymentProcessor):
         def process_payment(self) -> None: ...
     
     class PayPalProcessor(PaymentProcessor):
         def process_payment(self) -> None: ...
     ```
   - Interface Segregation
   - Dependency Inversion
   - Composition over Inheritance

2. **Design Patterns (When Appropriate)**
   - Factory Pattern for object creation:
     ```python
     class PaymentMethodFactory:
         @staticmethod
         def create_payment_method(method_type: str) -> PaymentMethod:
             match method_type:
                 case "credit": return CreditCardPayment()
                 case "paypal": return PayPalPayment()
                 case _: raise ValueError(f"Unknown payment method: {method_type}")
     ```
   - Strategy Pattern for algorithms:
     ```python
     class SortStrategy(Protocol):
         def sort(self, data: list[int]) -> list[int]: ...
     
     class QuickSort:
         def sort(self, data: list[int]) -> list[int]: ...
     
     class MergeSort:
         def sort(self, data: list[int]) -> list[int]: ...
     ```
   - Observer Pattern for event handling
   - Repository Pattern for data access
   - Use patterns judiciously - don't over-engineer

3. **Pythonic Data Structures and Idioms**
   - Use appropriate data structures:
     ```python
     # Sets for unique items
     unique_items: set[str] = {"apple", "banana", "apple"}
     
     # Dicts for key-value pairs
     user_preferences: dict[str, Any] = {
         "theme": "dark",
         "notifications": True
     }
     
     # Lists for ordered collections
     items: list[str] = ["first", "second", "third"]
     ```
   - Leverage Python's built-in types:
     ```python
     # Use Enum for constants
     class Color(Enum):
         RED = "red"
         GREEN = "green"
         BLUE = "blue"
     
     # Use NamedTuple for simple data
     class Point(NamedTuple):
         x: float
         y: float
     ```

4. **Modern Python Features**
   - Data Classes for simple objects:
     ```python
     @dataclass(slots=True)
     class User:
         name: str
         email: str
         age: int
         is_active: bool = True
     ```
   - Type Annotations and Generics:
     ```python
     def process_items[T](items: list[T]) -> list[T]:
         return [item for item in items if item is not None]
     ```
   - Context Managers:
     ```python
     @contextmanager
     def managed_resource():
         resource = acquire_resource()
         try:
             yield resource
         finally:
             release_resource(resource)
     ```

5. **Functional Programming in Python**
   - List Comprehensions:
     ```python
     squares = [x**2 for x in range(10) if x % 2 == 0]
     ```
   - Generator Expressions:
     ```python
     large_squares = (x**2 for x in range(1000000) if x % 2 == 0)
     ```
   - Lambda Functions (sparingly):
     ```python
     # Good: Simple operations
     square = lambda x: x**2
     
     # Bad: Complex logic
     process_data = lambda x: (x**2 if x > 0 else 0) + (x if x < 10 else 10)
     ```
   - Map, Filter, Reduce:
     ```python
     # Prefer comprehensions over map/filter
     doubled = [x*2 for x in numbers]  # Better than map(lambda x: x*2, numbers)
     ```

6. **Error Handling and Resource Management**
   - Use specific exceptions
   - Context managers for resources
   - Custom exceptions for domain errors
   - Type-safe error handling

7. **Testing and Quality**
   - Unit tests for all public methods
   - Property-based testing
   - Mock external dependencies
   - Type checking in CI/CD

## Development Environment
- Python 3.11+ preferred
- Docker for containerization when needed
- VS Code with Python extensions
- Virtual environment management via Hatch or pixi

## AI Assistance Guidelines
When providing code suggestions or modifications:
1. Always include type hints
2. Use modern Python features (PEP 695 generics)
3. Follow project's linting rules
4. Maintain test coverage
5. Consider async/await patterns where appropriate
6. Follow the src-layout project structure
7. Use Hatch commands for development tasks
8. Run ruff check and mypy --strict and autocorrect
9. Document any non-obvious code decisions
10. Consider performance implications of suggestions

## Common Project Types
1. **Web/API Projects**
   - Use FastAPI for modern async APIs
   - SQLAlchemy for database ORM
   - Pydantic for data validation
   - Alembic for database migrations

2. **CLI Applications**
   - Use Click or Typer for CLI interfaces
   - Rich for terminal output
   - Proper argument parsing and validation

3. **Data Processing**
   - Use pandas for data manipulation
   - numpy for numerical operations
   - Proper error handling and logging

4. **Library Development**
   - Clear public API design
   - Comprehensive documentation
   - Version compatibility considerations
