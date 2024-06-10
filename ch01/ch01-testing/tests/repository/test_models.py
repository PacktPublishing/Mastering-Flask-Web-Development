import pytest
from model.candidates import AdminUser

@pytest.fixture(scope="module", autouse=True)
def admin_details():
    data = {"id": 101, "position": "Supervisor","age": 45, "emp_date": "1980-02-16", "emp_status": "regular",
            "username": "pedro", "password": "pedro", "utype": 0, "firstname": "Pedro", "lastname" :"Cruz"}
    yield data
    data = None

def test_admin_user_model(admin_details):
    admin = AdminUser(**admin_details)
    assert admin.firstname == "Pedro"
    assert admin.lastname == "Luz"
    assert admin.age == 45