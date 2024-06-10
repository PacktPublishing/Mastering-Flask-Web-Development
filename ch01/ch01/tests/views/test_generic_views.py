
import pytest
from main import app as flask_app

# ImportError: cannot import name 'app' from '__main__'
print("main __name__ is set to: {}" .format(__name__))
@pytest.fixture
def client():
   
   with flask_app.test_client() as client:
       yield client

def test_default_page(client):
    response = client.get("/")
    assert b"OPCS" in response.data
        
def test_home_page(client):
    response = client.get("/home")
    assert b"Hello" in response.data
    
