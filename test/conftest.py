import pytest
from fastapi.testclient import TestClient

from semana_da_fisica.app import app


@pytest.fixture
def client():
    return TestClient(app)
