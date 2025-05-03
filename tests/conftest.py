import os
import sys
from collections.abc import Generator

import pytest
import pytest_asyncio
from starlette.testclient import TestClient

# Set up test database URL before any imports
os.environ["DATABASE_URL"] = "sqlite:///./test.db"

# Add src directory to Python path
src_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src"
)
sys.path.append(src_path)

from fastapi_crud_tutorial.main import app


@pytest.fixture(autouse=True)
def setup_test_database() -> None:
    """Set up test database URL before each test."""
    os.environ["DATABASE_URL"] = "sqlite:///./test.db"


@pytest.fixture(scope="module")
def test_app() -> Generator[TestClient, None, None]:
    client = TestClient(app)
    yield client  # testing happens here
