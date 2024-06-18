from peewee import PostgresqlDatabase, MySQLDatabase, SqliteDatabase

database = PostgresqlDatabase(
        'olms',
        user='postgres',
        password='admin2255',
        host='localhost',
        port=5433,
        autocommit=False,
       
    )

    

