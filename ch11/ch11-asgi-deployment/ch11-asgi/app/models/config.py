from peewee_async import PooledPostgresqlDatabase


database = PooledPostgresqlDatabase(
        'ogs',
        user='postgres',
        password='admin2255',
        host='ch11-asgi-deployment-postgres-1',
        port='5432',
        max_connections = 3,
        connect_timeout = 3
    )

    

