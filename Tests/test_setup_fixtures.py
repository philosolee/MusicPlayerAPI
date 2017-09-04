import pytest
from run import app


@pytest.fixture(scope="session")
def client():
    test_client = app.test_client()
    test_client.testing = True
    return test_client