import os
from collections.abc import Generator

import pytest
from starlette.testclient import TestClient

from fastapi_crud_tutorial.main import app

# Set up test database URL before any imports
os.environ["DATABASE_URL"] = "sqlite:///./test.db"


@pytest.fixture(autouse=True)
def setup_test_database() -> None:
    """Set up test database URL before each test."""
    os.environ["DATABASE_URL"] = "sqlite:///./test.db"


@pytest.fixture(scope="module")
def test_app() -> Generator[TestClient, None, None]:
    client = TestClient(app)
    yield client  # testing happens here
