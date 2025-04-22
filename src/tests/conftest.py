import os
import sys
from typing import Generator

# Set up test database URL before any imports
os.environ["DATABASE_URL"] = "sqlite:///./test.db"

import pytest
from starlette.testclient import TestClient

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.main import app


@pytest.fixture(autouse=True)
def setup_test_database() -> None:
    """Set up test database URL before each test."""
    os.environ["DATABASE_URL"] = "sqlite:///./test.db"


@pytest.fixture(scope="module")
def test_app() -> Generator[TestClient, None, None]:
    client = TestClient(app)
    yield client  # testing happens here
