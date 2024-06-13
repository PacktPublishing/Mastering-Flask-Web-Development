import pytest
from main import app as flask_app
import os


@pytest.fixture
def client():
   with flask_app.test_client() as client:
       yield client
       
       
def test_upload_file(client):
    
    test_file = os.getcwd() + "/tests/files/2011Q2.xlsx"
    data = {
        'data_file': (open(test_file, 'rb'), test_file)
    }
    response = client.post("/ch06/upload/xlsx/analysis", buffered=True, content_type='multipart/form-data', data=data)
    assert response.status_code == 200
    assert response.mimetype == "text/html"