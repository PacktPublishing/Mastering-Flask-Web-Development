import pytest
from main import app as flask_app
import base64

@pytest.fixture
def client():
    with flask_app.test_client() as app:
        yield app
        
@pytest.fixture      
def vaccine():
    vacc = {"vacid": "VAC-899", "vacname": "Narvas", "vacdesc": "For Hypertension" , "qty": 5000, "price": 1200.5, "status": True}
    return vacc

@pytest.fixture  
def auth_header():
    credentials = base64.b64encode(b'sjctrags:sjctrags').decode('utf-8')
    return credentials

def test_add_vaccine_unauth(client, vaccine, auth_header):    
        res = client.post("/vaccine/add", json=vaccine, headers={'Access-Control-Allow-Origin': "http://localhost:5000"})
        assert res.status_code == 201
    
def test_add_vaccine_auth(client, vaccine, auth_header): 
    res = client.post("/vaccine/add", json=vaccine, headers={'Authorization': 'Basic ' + auth_header, 'Access-Control-Allow-Origin': "http://localhost:5000"})
    assert res.status_code == 201