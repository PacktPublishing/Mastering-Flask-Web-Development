import pytest
from flask import url_for
from main import app as flask_app

@pytest.fixture
def client():
    flask_app.config["WTF_CSRF_ENABLED"] = False
    with flask_app.test_client() as app:
        yield app

@pytest.fixture(scope="module") 
def user_credentials():
    params = dict()
    params["username"] = "sjctrags"
    params["password"] = "sjctrags"
    return params
        
def test_patient_profile_add_invalid_access(client):
    res = client.get("/patient/profile/add", base_url='https://localhost')
    assert res.status_code == 302
    assert res.location.split('?')[0] == url_for('login_user')

def test_patient_profile_add_valid_access(client, user_credentials):
  
        res_login = client.post('/login/auth', data=user_credentials, base_url='https://localhost')
        assert res_login.status_code == 302
        assert res_login.location.split('?')[0] == url_for('view_signup')
        
        res = client.get("/patient/profile/add", base_url='https://localhost:5000')
        assert res.status_code == 200
    
        with client.session_transaction() as session:
            assert session["user"] == "sjctrags"