import pytest
from mock import patch
from main import app as flask_app
from app.repository.orders import OrdersRepository
from app.model.db import Orders

@pytest.fixture
def client():
   with flask_app.test_client() as client:
       yield client

@pytest.fixture
def order():
    order_details = {"date_ordered": "2020-12-10", "empid": "EMP-101" , "cid": "CUST-101", "oid": "ORD-910"}
    order = Orders(**order_details)
    return order

@pytest.fixture
def list_orders():
    order1 = {"id": 4, "date_ordered": "2020-12-10", "empid": "EMP-101" , "cid": "CUST-101", "oid": "ORD-910"}
    order2 = {"id": 1, "date_ordered": "2023-06-03", "empid": "EMP-101" , "cid": "CUST-101", "oid": "ORD-908"}
    orders = [Orders(**order1), Orders(**order1)]
    return orders

@patch("app.model.config.db_session")
def test_mock_add_order(mocked_sess, order):
    db_sess = mocked_sess.return_value
    with flask_app.app_context() as context:
        repo = OrdersRepository(db_sess)
        res = repo.insert(order)
        db_sess.add.assert_called_once()
        db_sess.commit.assert_called_once()
        assert res is True
        
@patch("app.model.config.db_session")
def test_mock_list_order(mocked_sess, list_orders):
    db_sess = mocked_sess.return_value
    mock_query = db_sess.query.return_value 
    mock_query.all.return_value = list_orders
    with flask_app.app_context() as context:
        repo = OrdersRepository(db_sess)
        res = repo.select_all()
        db_sess.query.assert_called_once()
        assert len(res) == 2
        