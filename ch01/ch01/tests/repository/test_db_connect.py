import pytest
from main import app as flask_app

from config.db import connect_db

@pytest.fixture
def client():
   with flask_app.test_client() as client:
       yield client


def test_connection():
    @connect_db
    def create_connection(conn):
        assert conn is not None
    create_connection()
       
