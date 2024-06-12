from flask import current_app , jsonify, request, Response, abort
from flask.json import  dumps, loads
from flask.json.provider import JSONProvider
from datetime import date
from app.model.db import Login
from app.repository.login import LoginRepository
from app.model.config import db_session

@current_app.route('/login/add', methods = ['POST'])
def add_login():
    if request.is_json:
        login_json = loads(request.data)
        login = Login(**login_json)
        repo = LoginRepository(db_session)
        result = repo.insert(login)
        if result:
            current_app.logger.info('insert login credentials successful')
            return jsonify(login_json)
        else:
            abort(500, description="insert login encountered a problem")
    else:
        abort(500)
  

@current_app.patch('/login/password/update/<string:username>')
def update_password(username:str):
   
    login_json = request.get_json()
    repo = LoginRepository(db_session)
    result = repo.update(username, login_json)
    if result:
        current_app.logger.info('update password successful')
        return jsonify(login_json)
    else:
        abort(500, description="update password encountered a problem")
   

@current_app.route('/login/list/all', methods = ['GET'])
def list_all_login():
    repo = LoginRepository(db_session)
    records = repo.select_all()
    login_rec = [rec.to_json() for rec in records]
    current_app.logger.info('retrieved a list of login successfully')
    resp = Response(response = dumps(login_rec), status=200, mimetype="application/json" )
    return resp

    