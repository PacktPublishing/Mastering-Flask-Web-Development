from peewee_async import PostgresqlDatabase, PooledPostgresqlDatabase
from peewee_async import Manager
import asyncio

database = PooledPostgresqlDatabase(
        'ogs',
        user='postgres',
        password='admin2255',
        host='ch11-asgi-dep-nginx-postgres-1',
        port='5432',
        max_connections = 3,
        connect_timeout = 3
    )

    

