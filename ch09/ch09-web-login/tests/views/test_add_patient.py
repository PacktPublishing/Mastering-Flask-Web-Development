import pytest
from flask_login import current_user
from main import app as flask_app

@pytest.fixture
def client():
    with flask_app.test_client() as app:
        yield app

@pytest.fixture(scope="module") 
def user_credentials():
    params = dict()
    params["username"] = "sjctrags"
    params["password"] = "sjctrags"
    return params

@pytest.fixture(scope="module") 
def admin_details():
    params = dict()
    params["adminid"] = "ADM-101"
    params["username"] = "sjctrags"
    params["firstname"] = "Sherwin John"
    params["midname"] = "Calleja"
    params["lastname"] = "Tragura"
    params["email"] = "sjctrags@gmail.com"
    params["mobile"] = "092239985"
    params["position"] = "System Admin"
    params["status"] = "true"
    params["gender"] = "sjctrags"
    return params

def test_add_admin_profile(client, admin_details, user_credentials):
    res_login = client.post('/login/auth', data=user_credentials)
    assert res_login.status_code == 200
        
    with client.session_transaction() as session:
       assert current_user.username == "sjctrags"
       res = client.post("/admin/profile/add", data=admin_details)
       assert res.status_code == 200