
import pytest
from app.model.config import db_session

from app.model.db import Login
from app.repository.login import LoginRepository

pytest_plugins = ('pytest_asyncio',)

# ImportError: cannot import name 'app' from '__main__'

# You need to install a suitable plugin for your async framework, for example:
#    - anyio
#    - pytest-asyncio
#    - pytest-tornasync
#    - pytest-trio
#    - pytest-twisted
#    warnings.warn(PytestUnhandledCoroutineWarning(msg.format(nodeid)))
@pytest.fixture
def login_details():
    login_details = {"username": "user-1908", "password": "pass9087" }
    login_model = Login(**login_details)
    return login_model

@pytest.mark.asyncio
async def test_add_login(login_details):
     async with db_session() as sess:
        async with sess.begin(): 
            repo = LoginRepository(sess)
            res = await repo.insert_login(login_details)
            assert res is True