import toml
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
import logging
import logging.config # off the debug to avoid windows os error 
import logging.handlers
import sys

db = SQLAlchemy()

def create_app(config_file):
    app = Flask(__name__, template_folder='../pages', static_folder='../resources')   
    app.config.from_file(config_file, toml.load)
    
    db.init_app(app)
    alog = configure_func_logging('log_msg.txt')
    #alog = configure_logger('log_msg.txt')
    
    with app.app_context():  
        from modules.home import home_bp
        from modules.login import login_bp
        from modules.order import order_bp
        from modules.payment import payment_bp
        from modules.shipping import shipping_bp
        from modules.product import product_bp
        
        app.register_blueprint(home_bp, url_prefix='/ch02')
        app.register_blueprint(login_bp, url_prefix='/ch02')
        app.register_blueprint(order_bp, url_prefix='/ch02')
        app.register_blueprint(payment_bp, url_prefix='/ch02')
        app.register_blueprint(shipping_bp, url_prefix='/ch02')
        app.register_blueprint(product_bp, url_prefix='/ch02')
    
    return app



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
     return logging.getLogger('default')
 
def configure_func_logging(log_path):
    logging.getLogger("werkzeug").disabled = True
    console_handler = logging.StreamHandler(stream=sys.stdout)
    console_handler.setLevel(logging.DEBUG)
    
    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(module)s %(funcName)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[logging.handlers.RotatingFileHandler(log_path, backupCount=3, maxBytes=1024  ), console_handler])
    
    return logging.getLogger('default')






