
import pytest
from main import app as flask_app

@pytest.fixture(autouse=True)
def client():
   with flask_app.test_client() as client:
       yield client
       
def test_default_page(client):
    res = client.get("/")
    assert "OPCS" in res.data.decode()
        
def test_home_page(client):
    res = client.get("/home")
    assert "Welcome" in res.data.decode()
    assert res.request.path == "/home"
    
def test_exam_page(client):
    res = client.get("/exam/assign")
    assert res.status_code == 200