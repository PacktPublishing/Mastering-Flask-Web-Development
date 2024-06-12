from flask import Flask
import toml
from app.model.config import init_db
from flask_sock import Sock
from redis import Redis

sock = Sock()

def create_app(config_file):
    app = Flask(__name__, template_folder='../app/pages', static_folder="../app/resources")   
    app.config.from_file(config_file, toml.load)
    init_db()
    sock.init_app(app)
    
    global redis_conn
    redis_conn = Redis( db = 0, host='127.0.0.1', port=6379,
         decode_responses=True # <-- this will ensure that binary data is decoded
    )

    # Creating application context:
    # 1. Using the with statement
    with app.app_context():
        from app.views import home
        from app.views import votecount
        from app.views import election_complaint
        
    return app

