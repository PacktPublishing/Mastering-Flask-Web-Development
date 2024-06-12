from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
import logging
import logging.config
import logging.handlers
import sys
import toml

# Extension module setup
db = SQLAlchemy()

def configure_logger(log_path):
     logging.config.dictConfig({
        'version': 1,
        'formatters': {
            'default': {'format': '%(asctime)s %(levelname)s %(module)s %(funcName)s %(message)s', 'datefmt': '%Y-%m-%d %H:%M:%S'}
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'default',
                'stream': 'ext://sys.stdout'
            },
            'file': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'default',
                'filename': log_path,
                'maxBytes': 1024,
                'backupCount': 3
            }
        },
        'loggers': {
            'default': {
                'level': 'DEBUG',
                'handlers': ['console', 'file']
            }
        },
        'disable_existing_loggers': False
    })
     
 
def configure_func_logging(log_path):
    logging.getLogger("werkzeug").disabled = True
    console_handler = logging.StreamHandler(stream=sys.stdout)
    console_handler.setLevel(logging.DEBUG)
    
    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(module)s %(funcName)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[logging.handlers.RotatingFileHandler(log_path, backupCount=3, maxBytes=1024  ), console_handler])
    
    

def create_app(config_file):
    app = Flask(__name__, template_folder='../app/pages', static_folder='../app/resources')   
    app.config.from_file(config_file, toml.load)
    db.init_app(app)
    configure_func_logging('log_msg.txt')
    
    # Creating application context:
    # 1. Using the with statement
    with app.app_context():
        from app.views import login
        from app.views import menu
        from app.views import customer
        from app.views import admin
        from app.views import product
        from app.views import order
        from app.views import payment
        from app.views import shipping
          
    # 2. Manually calling and pushing the context
    #app_ctx = app.app_context()
    #app_ctx.push()
      
    return app




