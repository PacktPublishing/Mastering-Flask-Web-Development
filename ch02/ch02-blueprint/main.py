from flask import Flask, session, request, redirect, url_for, make_response, render_template
import toml

import logging
import logging.config # turn off the debug to avoid windows os error 
import logging.handlers
import sys
import re

from werkzeug.exceptions import HTTPException
from exceptions.db import DuplicateRecordException

from modules.model.config import db_session, init_db

init_db()

app = Flask(__name__, template_folder='pages', static_folder="resources")   
app.config.from_file('config.toml', toml.load)

@app.errorhandler(404)
def not_found(e):
    return make_response(render_template("error/404.html", title="Page not found"), 404)

@app.errorhandler(400)
def bad_request(e):
    return make_response(render_template("error/400.html", title="Bad request"), 400)

def server_error(e):
    print(e)
    return make_response(render_template("error/500.html", title="Internal server error"), 500) 

@app.errorhandler(DuplicateRecordException)
def insert_record_exception(e):
    print(e)
    return make_response(render_template("error/insert_rec.html", title="Internal server error", ex_message=e), 500)  

app.register_error_handler(500, server_error)
#app.register_error_handler(DuplicateRecordException, insert_record_exception)


@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return e
    return render_template("error/generic.html", title="Internal server error", e=e), 500

@app.before_request
def init_request():
    if request.endpoint != None:
        static_expr = re.search('static$', request.endpoint)
    else:
        static_expr = None
    if (( request.endpoint != 'login_bp.login_db_auth' and  request.endpoint != 'home_bp.index' and static_expr == None)  and 'username' not in session):
       app.logger.info('a user is unauthenticated')
       return redirect(url_for('login_bp.login_db_auth'))
    elif (( request.endpoint == 'login_bp.login_db_auth' and  request.endpoint != 'home_bp.index' and static_expr == None)  and 'username' in session):
        app.logger.info('a user is already logged in')
        return redirect(url_for('home_bp.menu'))
    
@app.after_request
def return_response(response):
    if request.endpoint != None:
        static_expr = re.search('static$', request.endpoint)
    else:
        static_expr = None
    if ( static_expr == None):
        app.logger.info(f'{request.endpoint} done executing')
    return response

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

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

alog = configure_func_logging('log_msg.txt')
#alog = configure_logger('log_msg.txt')

 
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




if __name__ == '__main__':
    app.run()