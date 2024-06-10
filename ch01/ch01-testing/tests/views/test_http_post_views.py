
import pytest 
from main import app as flask_app

@pytest.fixture
def client():
   with flask_app.test_client() as client:
       yield client

@pytest.fixture   
def form_data():
    params = dict()
    params["username"] = "owen"
    params["password"] = "owen"
    params["utype"] = 2
    params["firstname"] = "Owen Salvador"
    params["lastname"] = "Estabillo"
    params["cid"] = "CGFCDS"
    return params
         
       
def test_signup_get(client):
    response = client.get("/signup/submit")
    assert response.status_code == 405
    
def test_signup_post(client, form_data):
    response = client.post("/signup/submit", data=form_data)
    assert response.status_code == 200