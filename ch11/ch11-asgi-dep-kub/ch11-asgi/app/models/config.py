from peewee_async import PostgresqlDatabase, PooledPostgresqlDatabase
import os

database = PooledPostgresqlDatabase(
        'ogs',
        user=os.environ.get('POSTGRES_DB_USER'),
        password=os.environ.get('POSTGRES_DB_PSW'),
        host=os.environ.get('SERVICE_POSTGRES_SERVICE_HOST'),
        port='5432',
        max_connections = 3,
        connect_timeout = 3
    )

    

