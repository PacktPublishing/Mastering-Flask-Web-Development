
import pytest
from main import app as flask_app
from flask import request, url_for
from datetime import date
from config.db import connect_db

# ImportError: cannot import name 'app' from '__main__'
@pytest.fixture(autouse=True)   
def form_data():
    params = dict()
    params["id"] = "2255"
    params["cid"] = "HJNB6778"
    params["pid"] = "1111"
    params["exam_date"] = "2020-10-10"
    params["duration"] = "3"
    yield params
    params = None

@pytest.fixture
def client():
   with flask_app.test_client() as client:
       yield client
       
def test_assign_exam_redirect(client, form_data):
    res = client.post('/exam/assign', data=form_data, follow_redirects=True)
    assert res.status == '200 OK'
    assert res.request.path == url_for('redirect_success_exam')
    
def test_assign_exam_redirect_302(client, form_data):
    res = client.post('/exam/assign', data=form_data)
    assert res.status_code == 302
    assert res.location.split('?')[0] == url_for('redirect_success_exam')

@connect_db
def insert_question_details(conn, id:int, cid:str, pid:int, exam_date:date, duration:int):
        return True

@pytest.fixture
def insert_question_patched(monkeypatch):
    monkeypatch.setattr("views.examination.insert_question_details", insert_question_details)
    
def test_assign_mock_exam(insert_question_patched, client, form_data):    
    res = client.post('/exam/assign', data=form_data, follow_redirects=True)
    assert res.status == '200 OK'
    assert res.request.path == url_for('redirect_success_exam')
    
def test_assign_mock_302_exam(insert_question_patched, client, form_data):    
    res = client.post('/exam/assign', data=form_data)
    assert res.status_code == 302
    assert res.location.split('?')[0] == url_for('redirect_success_exam')
    
    