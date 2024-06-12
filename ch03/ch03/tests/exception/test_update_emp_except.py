import pytest
from mock import patch, MagicMock
from main import app as flask_app
import json
from app.exceptions.db import DuplicateRecordException, NoRecordException


@pytest.fixture
def client():
   with flask_app.test_client() as client:
       yield client
       
@pytest.fixture   
def employee_data():
    order_details = {"empid": "EMP-111", "fname": "Sherwin John" , "mname": "Calleja", "lname": "Tragura", "age": 45 , "role": "clerk", "date_employed": "2011-08-11", "status": "active", "salary": 60000.99}
    return order_details

@pytest.mark.xfail(strict=True, raises=NoRecordException, reason="Negative existing record.")
def test_update_employee(client, employee_data):
    res = client.patch(f'/employee/update/{employee_data["empid"]}', json=employee_data)
    assert res.status_code == 201