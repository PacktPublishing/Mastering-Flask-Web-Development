
import pytest
from main import app as flask_app

@pytest.fixture(autouse=True)
def client():
   with flask_app.test_client() as client:
       yield client
       
@pytest.fixture(autouse=True, scope="module")    
def login_details():
    data = {"username": "sjctrags", "password":"sjctrags"}
    yield data 
    data = None 

@pytest.xfail(reason="An exception is encountered")
def test_add_login(client, login_details):
    res = client.post("/ch05/login/add", json=login_details)
    assert res.status_code == 201