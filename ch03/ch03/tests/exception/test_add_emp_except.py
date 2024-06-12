import pytest
from main import app as flask_app
from app.exceptions.db import DuplicateRecordException

@pytest.fixture
def client():
   with flask_app.test_client() as client:
       yield client
       
@pytest.fixture   
def employee_data():
    order_details = {"empid": "EMP-101", "fname": "Sherwin John" , "mname": "Calleja", "lname": "Tragura", "age": 45 , "role": "clerk", "date_employed": "2011-08-11", "status": "active", "salary": 60000.99}
    return order_details
       
def test_add_employee(client, employee_data):
    with pytest.raises(DuplicateRecordException) as ex:
        res = client.post('/employee/add', json=employee_data)
        assert res.status_code == 200
    assert str(ex.value) == "insert employee record encountered a problem"
   