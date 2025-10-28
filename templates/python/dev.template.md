# Development Workflow - Python

This file configures the `/dev` command workflow for Python projects.

## Environment Setup

### Virtual Environment Creation
```bash
# Using venv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Using virtualenv
virtualenv venv
source venv/bin/activate

# Using conda
conda create -n myproject python=3.11
conda activate myproject
```

### Dependency Installation
```bash
# From requirements.txt
pip install -r requirements.txt

# Development dependencies
pip install -r requirements-dev.txt

# Using poetry
poetry install

# Using pipenv
pipenv install --dev
```

### Environment Configuration
```bash
# Copy environment template
cp .env.example .env

# Edit environment variables
nano .env
```

### Database Setup (if applicable)
```bash
# Django
python manage.py migrate
python manage.py createsuperuser

# Alembic (SQLAlchemy)
alembic upgrade head

# Flask-Migrate
flask db upgrade
```

## Development Commands

### Run Development Server
```bash
# Django
python manage.py runserver
# or on specific port
python manage.py runserver 8080

# FastAPI
uvicorn main:app --reload
# or
python -m uvicorn main:app --reload --port 8000

# Flask
flask run
# or
python app.py
```

### Run Tests
```bash
# All tests
pytest

# With verbose output
pytest -v

# Specific test file
pytest tests/test_users.py

# Specific test function
pytest tests/test_users.py::test_create_user

# With coverage
pytest --cov=. --cov-report=html

# Watch mode
pytest-watch
```

### Database Operations
```bash
# Django
python manage.py makemigrations
python manage.py migrate
python manage.py shell

# Alembic
alembic revision --autogenerate -m "description"
alembic upgrade head
alembic downgrade -1

# Flask-Migrate
flask db migrate -m "description"
flask db upgrade
```

## Project Structure

### Code Organization
```
project/
├── app/               # Main application package
│   ├── __init__.py
│   ├── models.py      # Data models
│   ├── views.py       # Views/endpoints
│   ├── services.py    # Business logic
│   └── utils.py       # Utilities
├── tests/             # Test files
├── requirements.txt   # Dependencies
└── config.py          # Configuration
```

### Naming Conventions
- Files: `snake_case.py`
- Classes: `PascalCase`
- Functions/variables: `snake_case`
- Constants: `UPPER_SNAKE_CASE`
- Private: `_leading_underscore`

### Import/Module Structure
```python
# Standard library
import os
import sys
from typing import List, Optional

# Third-party
import requests
from fastapi import FastAPI, Depends

# Local imports
from app.models import User
from app.services import UserService
from .utils import format_date
```

## Best Practices

### Commit Message Format
Follow Conventional Commits:
```
feat: add user authentication endpoint
fix: resolve database connection issue
docs: update API documentation
refactor: simplify query logic
test: add unit tests for user service
chore: update dependencies
```

### Branch Naming
```
feat/issue-123-user-authentication
fix/issue-456-login-bug
refactor/issue-789-database-layer
docs/issue-012-api-docs
```

### Code Style
- Follow PEP 8 style guide
- Use type hints for function signatures
- Write docstrings for modules, classes, and functions
- Keep functions small and focused
- Use list/dict comprehensions when appropriate
- Prefer f-strings for string formatting

Example:
```python
def calculate_total(items: List[Item]) -> float:
    """Calculate the total price of items.

    Args:
        items: List of items to calculate total for

    Returns:
        Total price as float

    Raises:
        ValueError: If items list is empty
    """
    if not items:
        raise ValueError("Items list cannot be empty")
    return sum(item.price for item in items)
```

## Testing Requirements

### Unit Tests
- Test individual functions and methods
- Use fixtures for test data
- Mock external dependencies
- Follow AAA pattern (Arrange, Act, Assert)

Example:
```python
import pytest
from app.services import UserService

@pytest.fixture
def user_data():
    return {"email": "test@example.com", "name": "Test User"}

def test_create_user(user_data):
    # Arrange
    service = UserService()

    # Act
    user = service.create(user_data)

    # Assert
    assert user.email == user_data["email"]
    assert user.id is not None
```

### Integration Tests
- Test API endpoints
- Test database interactions
- Use test database or containers
- Test authentication/authorization

### Test Coverage
Minimum coverage: 80%
- Statements: > 80%
- Branches: > 75%
- Functions: > 80%
- Lines: > 80%

## Common Tasks

### Adding Dependencies
```bash
# pip
pip install <package>
pip freeze > requirements.txt

# poetry
poetry add <package>
poetry add --dev <dev-package>

# pipenv
pipenv install <package>
pipenv install --dev <dev-package>
```

### Updating Dependencies
```bash
# pip
pip install --upgrade <package>
pip list --outdated

# poetry
poetry update
poetry update <package>

# pipenv
pipenv update
pipenv update <package>
```

### Linting and Formatting
```bash
# Run linters
flake8 .
pylint app/

# Format code
black .
isort .

# Combined with ruff
ruff check . --fix
ruff format .
```

### Type Checking
```bash
# Run mypy
mypy .
mypy --strict .

# Specific directory
mypy app/
```

## Debugging

### Using pdb
```python
import pdb; pdb.set_trace()
# or in Python 3.7+
breakpoint()
```

### Using IDE
- VS Code: Add breakpoints and use F5
- PyCharm: Add breakpoints and use Debug

### Logging
```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
```

## Troubleshooting

### Import Errors
- Verify virtual environment is activated
- Check PYTHONPATH if needed
- Ensure `__init__.py` files exist

### Test Failures
- Run specific test: `pytest tests/test_file.py::test_function`
- Check test fixtures and mocks
- Verify test database state

### Type Errors
- Run `mypy .` to see all type errors
- Add type hints incrementally
- Use `# type: ignore` sparingly for unavoidable issues

### Dependency Conflicts
- Create fresh virtual environment
- Use `pip install --upgrade pip`
- Check for conflicting package versions
