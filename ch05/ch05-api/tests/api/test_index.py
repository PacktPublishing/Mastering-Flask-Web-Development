
import pytest
from main import app as flask_app



# ImportError: cannot import name 'app' from '__main__'


@pytest.fixture
def client():
   with flask_app.test_client() as client:
       yield client

def test_default_page(client):
    response = client.get("/ch05/index")
    assert b"Online Voting System" in response.data