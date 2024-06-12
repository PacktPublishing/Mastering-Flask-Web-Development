from flask import Flask
import logging
import logging.config
import toml


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
    app = Flask(__name__, template_folder='../app/pages', static_folder='../app/resources')   
    app.config.from_file(config_file, toml.load)
    configure_logger('log_msg.txt')
    
    with app.app_context():
        from app.views import index
        from app.views import pizza_client
        from app.views import orders_client
     
    return app