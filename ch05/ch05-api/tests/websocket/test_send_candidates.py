from main import app as flask_app
from app import sock
import pytest

@pytest.fixture
def client():
   with flask_app.web as client:
       yield client