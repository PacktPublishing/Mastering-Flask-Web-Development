
import pytest
from main import app as flask_app

# ImportError: cannot import name 'app' from '__main__'

@pytest.fixture
def client():
   with flask_app.test_client() as client:
       yield client
       
def test_exam_page(client):
    response = client.get("/exam/assign")
    assert response.status_code == 200