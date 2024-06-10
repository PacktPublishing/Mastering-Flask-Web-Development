from config.db import connect_db

def test_connection():
    @connect_db
    def create_connection(conn):
        assert conn is not None
    create_connection()
       
