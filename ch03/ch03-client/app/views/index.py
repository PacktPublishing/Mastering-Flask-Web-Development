from flask import current_app


@current_app.route('/client/app', methods = ['GET'])
def index():
    return "client"