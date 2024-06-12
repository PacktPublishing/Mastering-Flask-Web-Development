from modules import create_app
from werkzeug.exceptions import HTTPException
from exceptions.db import DuplicateRecordException
import re

from flask import session, request, redirect, url_for, abort, make_response, render_template

app = create_app('../config_dev.toml')

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
if __name__ == '__main__':
    app.run()
    
    