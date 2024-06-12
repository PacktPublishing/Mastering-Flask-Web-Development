
from app import create_app, db
#from app.exceptions.db import DuplicateRecordException
from werkzeug.exceptions import HTTPException
from flask import g, session, request, redirect, make_response, render_template
from datetime import datetime
app = create_app('../config_dev.toml')

def get_database():
    if 'db' not in g:
        g.db = db
        app.logger.info('storing the db connection as context data')

@app.teardown_appcontext
def teardown_database(exception):
    db = g.pop('db', None)
    if not db == None:
        app.logger.info('removing the db connection as context data')

@app.context_processor
def show_date():
    template_details = dict()
    template_details['webmaster'] = 'sjctrags'
    template_details['date_accessed'] = datetime.now()
    template_details['copyright_year'] = '2003'
    template_details['company'] = 'Packt Publishing'
    return template_details

@app.before_request
def init_request():
    get_database()
    if (( request.endpoint != 'login_db_auth' and  request.endpoint != 'index' and request.endpoint != 'static')  and 'username' not in session):
       app.logger.info('a user is unauthenticated')
       return redirect('/login/auth')
    elif (( request.endpoint == 'login_db_auth' and  request.endpoint != 'index' and request.endpoint != 'static')  and 'username' in session):
        app.logger.info('a user is already logged in')
        return redirect('/menu')
    
@app.after_request
def return_response(response):
    if ( request.endpoint != 'static'):
        app.logger.info(f'{request.endpoint} done executing')
    return response
       
@app.errorhandler(404)
def not_found(e):
    return make_response(render_template("error/404.html", title="Page not found"), 404)

@app.errorhandler(400)
def bad_request(e):
    return make_response(render_template("error/400.html", title="Bad request"), 400)

def server_error(e):
    print(e)
    return make_response(render_template("error/500.html", title="Internal server error"), 500) 

#@app.errorhandler(DuplicateRecordException)
#def insert_record_exception(e):
#    print(e)
#    return make_response(render_template("error/insert_rec.html", title="Internal server error", ex_message=e), 500)  

app.register_error_handler(500, server_error)
#app.register_error_handler(DuplicateRecordException, insert_record_exception)


@app.errorhandler(Exception)
def handle_built_exception(e):
    if isinstance(e, HTTPException):
        return e
    return render_template("error/generic.html", title="Internal server error", e=e), 500



if __name__ == '__main__':
    app.run()
    