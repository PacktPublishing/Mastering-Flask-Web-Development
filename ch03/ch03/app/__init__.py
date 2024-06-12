from flask import Flask
import logging
import logging.config
import toml

from app.model.config import init_db

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
     

def create_app(config_file):
    app = Flask(__name__)   
    app.config.from_file(config_file, toml.load)
    init_db()
    configure_logger('log_msg.txt')
    with app.app_context():
        from app.api import index
        from app.api import login
        from app.api import employee
        from app.api import customer
        from app.api import pizza
        from app.api import nonpizza
        from app.api import addons
        from app.api import category
        from app.api import orders
     
    return app