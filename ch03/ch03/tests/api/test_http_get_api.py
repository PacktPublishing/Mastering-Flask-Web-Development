import pytest
from mock import patch, MagicMock
from main import app as flask_app
import json

@pytest.fixture
def client():
   with flask_app.test_client() as client:
       yield client
       
def test_index(client):
    res = client.get('/index')
    data = json.loads(res.get_data(as_text=True))
    assert data["message"] == "This is an Online Pizza Ordering System."


    
    