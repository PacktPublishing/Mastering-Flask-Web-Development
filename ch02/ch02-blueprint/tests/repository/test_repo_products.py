import pytest
from mock import patch
from main import app as flask_app
from modules.product.repository.product import ProductRepository
from modules.model.db import Products

@pytest.fixture(autouse=True)
def form_data():
    params = dict()
    params["name"] = "eraser"
    params["code"] = "SCH-8977"
    params["price"] = "125.00"
    yield params
    params = None
    
@patch("modules.model.config.db_session")
def test_mock_add_products(mocked_sess, form_data):
    db_sess = mocked_sess.return_value
    with flask_app.app_context() as context:
        repo = ProductRepository(db_sess)
        prod = Products(price=form_data["price"], code=form_data["code"], name=form_data["name"])
        res = repo.insert(prod)
        db_sess.add.assert_called_once()
        db_sess.commit.assert_called_once()
        assert res is True



