# pip install pytest-celery
import pytest
from app.services.vote_tasks import add_vote_task_wrapper
import json
from main import app as flask_app

pytest_plugins = ('pytest_celery',)

@pytest.fixture(scope='session')
def celery_config():
    yield {
        'broker_url': 'redis://localhost:6379/1',
        'result_backend': 'redis://localhost:6379/1'
    }

@pytest.fixture
def vote():
  
    login_details = {"voter_id": "BCH-111-789", "election_id": 1, "cand_id": "PHL-102" , "vote_time": "09:11:19" }
    login_str = json.dumps(login_details)
    return login_str

def test_add_votes(vote, celery_config):
    #with flask_app.app_context() as context:
        login_task = add_vote_task_wrapper.apply_async(args=[vote])
        result = login_task.get()
        assert bool(result) is True