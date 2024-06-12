import pytest
from main import app as flask_app

@pytest.fixture(scope="module", autouse=True)
def client():
    with flask_app.test_client() as app:
        yield app

def test_add_vote_ws_client(client):
    res = client.get('/ch05/votecount/add')
    assert res.status_code == 200 