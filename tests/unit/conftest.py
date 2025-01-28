import pytest

from fastapi.testclient import TestClient
from src.api.api import app

@pytest.fixture
def mock_life_span():
    app.mongodb_client = None
    app.database = None
    yield
    app.mongodb_client = None
    app.database = None

@pytest.fixture
def client():
    return TestClient(app)