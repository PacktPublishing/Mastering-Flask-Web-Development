from flask import request, Response, render_template, redirect
from repository.user import validate_user

def create_login_routes(app):
    @app.route('/login/params')
    def login_with_params():
        username = request.args['username']
        password = request.args['password']
        request.data
        result = validate_user(username, password)
        if result:
            resp = Response(response=render_template('/main.html'), status=200, content_type='text/html')
            return resp
        else:
            return redirect('/error')