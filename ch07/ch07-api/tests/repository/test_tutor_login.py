import pytest
import mongomock
from mongoengine import connect, get_connection, disconnect
from main import app as flask_app
from modules.repository.mongo.tutor_login import TutorLoginRepository
from bcrypt import hashpw, gensalt

@pytest.fixture
def login_details():
    login = dict()
    login["username"] = "sjctrags"
    login["password"] = "sjctrags"
    login["encpass"] = hashpw(str(login['username']).encode(), gensalt())
    return login


@pytest.fixture
def client():
   disconnect()
   with flask_app.test_client() as client:
       yield client

@pytest.fixture
def connect_db():
    connect(host='localhost', port=27017, db='tfs_test', uuidRepresentation='standard', mongo_client_class=mongomock.MongoClient)
    conn = get_connection()
    return conn

def test_add_login(client, connect_db, login_details):
    repo = TutorLoginRepository()
    res = repo.insert_login(login_details)
    assert res is True