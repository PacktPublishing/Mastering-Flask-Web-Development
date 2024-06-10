import pytest
from unittest.mock import patch
from repository.admin import insert_admin
from repository.user import select_all_user


@pytest.mark.parametrize(("id", "fname", "lname", "age", "position", "date_employed", "status"),
       (("8999", "Juan", "Luna", 76, "Manager", "2010-10-10", "active"), 
        ("9999", "Maria", "Clara", 45, "Developer", "2015-08-15", "inactive")
       ))
@patch("psycopg2.connect")
def test_mock_insert_admin(mock_connect, id, fname, lname, age, position, date_employed, status):
    mocked_conn = mock_connect.return_value
    mock_cur = mocked_conn.cursor.return_value
    result = insert_admin(id, fname, lname, age, position, date_employed, status)
    mock_cur.execute.assert_called_once()
    mocked_conn.commit.assert_called_once()
    #mocked_conn.rollback.assert_not_called()
    assert result is True

@patch("psycopg2.connect") 
def test_mock_select_users(mock_connect):
    expect_rec = [(222, "sjctrags", "sjctrags", "2023-02-26"), ( 567, "owen", "owen", "2023-10-22")]
    mocked_conn = mock_connect.return_value
    mock_cur = mocked_conn.cursor.return_value
    mock_cur.fetchall.return_value = expect_rec
    result = select_all_user()
    assert result is expect_rec
    
# python -m pytest -v --durations=2