from flask import Flask
import toml
from app.model.config import init_db
from celery_config import celery_init_app
from flask_sock import Sock

import logging
import logging.config
import logging.handlers
import sys

sock = Sock()

def configure_func_logging(log_path):
    logging.getLogger("werkzeug").disabled = True
    console_handler = logging.StreamHandler(stream=sys.stdout)
    console_handler.setLevel(logging.DEBUG)
    
    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(module)s %(funcName)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[logging.handlers.RotatingFileHandler(log_path, backupCount=3, maxBytes=1024  ), console_handler])

def create_app(config_file):
    app = Flask(__name__)   
    app.config.from_file(config_file, toml.load)
    #configure_func_logging('log_msg.txt')
    init_db()
    
    app.config.from_prefixed_env()
    celery_app = celery_init_app(app)
    sock.init_app(app)
    
    
      
    # Creating application context:
    # 1. Using the with statement
    with app.app_context():
        from app.api import home
        from app.api import login
        from app.api import member
        from app.api import voter
        from app.api import election
        from app.api import candidates
        from app.api import votecount_websocket
        from app.api import vote
        from app.api import votecount
        
    
            
    return app, celery_app

