from peewee import PostgresqlDatabase, MySQLDatabase, SqliteDatabase

database = PostgresqlDatabase(
        'ogs',
        user='postgres',
        password='admin2255',
        host='localhost',
        autocommit=False,
        port=5433
    )

    

