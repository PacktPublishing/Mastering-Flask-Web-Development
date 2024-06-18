import gevent.monkey
gevent.monkey.patch_all()

import psycogreen.gevent
psycogreen.gevent.patch_psycopg()


from app import create_app
from app.models.config import database
     
app = create_app('../config_dev.toml')

@app.before_request
def db_connect():
    database.connect()
    
@app.teardown_request
def db_close(exc):
    if not database.is_closed():
        database.close()


#run the command: gunicorn --bind 127.0.0.1:8000 main:app -w 1 -k gevent --threads 1 
