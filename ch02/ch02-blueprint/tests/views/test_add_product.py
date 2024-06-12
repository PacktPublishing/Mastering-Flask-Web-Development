import pytest
from unittest.mock import patch
from main import app as flask_app
from modules.model.config import init_db
from flask import url_for, session
@pytest.fixture(autouse=True)
def client():
    with flask_app.test_client() as app:
        yield app

@pytest.fixture(autouse=True)
def form_data():
    params = dict()
    params["name"] = "eraser"
    params["code"] = "SCH-8977"
    params["price"] = "125.00"
    yield params
    params = None
    
@pytest.fixture(autouse=True)
def login_data():
    params = dict()
    params["username"] = "admin"
    params["password"] = "admin"
    
    yield params
    params = None
    
    
def test_add_product_no_login(form_data, client):
    res = client.post("/ch02/products/add", data=form_data)
    assert res.status_code == 302
    assert res.status == "302 FOUND"
    assert res.location.split('?')[0] == "/ch02/login/auth"
    
def test_add_product_with_login(form_data, login_data, client):
        res_login = client.post("/ch02/login/auth", data=login_data)
        with client.session_transaction() as session:
            assert 'admin' == session["username"]
            assert res_login.location.split('?')[0] == url_for('home_bp.menu')
            res = client.post("/ch02/products/add", data=form_data)
            assert res.status_code == 200

