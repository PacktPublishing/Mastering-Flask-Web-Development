import pytest
from main import app as flask_app

@pytest.fixture(scope="module", autouse=True)
def client():
    with flask_app.test_client() as app:
        yield app
        
def test_home_page(client):
    res = client.get("/ch02/index")
    assert "Welcome" in res.data.decode()