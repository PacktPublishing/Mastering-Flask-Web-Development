import pytest
from repository.admin import insert_admin

@pytest.mark.parametrize(("id", "fname", "lname", "age", "position", "date_employed", "status"),
       (("8999", "Juan", "Luna", 76, "Manager", "2010-10-10", "active"), 
        ("9999", "Maria", "Clara", 45, "Developer", "2015-08-15", "inactive")
       ))

def test_insert_admin(id, fname, lname, age, position, date_employed, status):
    result = insert_admin(id, fname, lname, age, position, date_employed, status)
    assert result is True