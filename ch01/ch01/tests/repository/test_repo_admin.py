import pytest
from repository.admin import insert_admin

@pytest.fixture
def admin_record():
    return ("8999", "Juan", "Luna", 76, "Manager", "2010-10-10", "active")

def test_insert_admin(admin_record):
    result = insert_admin(admin_record[0], admin_record[1], admin_record[2], admin_record[3], admin_record[4], admin_record[5], admin_record[6])
    assert result is True