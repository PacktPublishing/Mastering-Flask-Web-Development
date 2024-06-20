from app import create_app
from app.models.config import database
#import eventlet
#from eventlet import wsgi
     
app = create_app('../config_dev.toml')

@app.before_request
def db_connect():
    database.connect()
    
@app.teardown_request
def db_close(exc):
    if not database.is_closed():
        database.close()
    
    
