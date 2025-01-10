import pytest

from fastapi.testclient import TestClient
from src.api.api import app

@pytest.fixture
def client():
    return TestClient(app)