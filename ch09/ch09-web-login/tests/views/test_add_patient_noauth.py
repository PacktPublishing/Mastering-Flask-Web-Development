import pytest
from main import app as flask_app

@pytest.fixture
def client():
    flask_app.config["LOGIN_DISABLED"] = True
    with flask_app.test_client() as app:
        yield app

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

def test_add_admin_profile(client, admin_details):
    res = client.post("/admin/profile/add", data=admin_details)
    assert res.status_code == 200