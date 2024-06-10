import pytest
from mock import patch, MagicMock
from repository.admin import insert_admin
from repository.user import select_all_user
import time
@pytest.fixture
def admin_record():
    return ("8999", "Juan", "Luna", 76, "Manager", "2010-10-10", "active")

@patch("psycopg2.connect")
def test_mock_insert_admin(mock_connect, admin_record):
    
    mocked_conn = mock_connect.return_value
    mock_cur = mocked_conn.cursor.return_value
    
    result = insert_admin(admin_record[0], admin_record[1], admin_record[2], admin_record[3], admin_record[4], admin_record[5], admin_record[6])
   
    mock_cur.execute.assert_called_once()
    mocked_conn.commit.assert_called_once()
    #mocked_conn.rollback.assert_not_called()
    assert result is True

@patch("psycopg2.connect") 
def test_mock_select_users(mock_connect):
    expect_rec = [(222, "sjctrags", "sjctrags", "2023-02-26"), ( 567, "wewewe", "aaasa", "2023-02-26")]
    mocked_conn = mock_connect.return_value
    mock_cur = mocked_conn.cursor.return_value
    mock_cur.fetchall.return_value = expect_rec
    result = select_all_user()
    assert result is expect_rec
    
# python -m pytest -v --durations=2