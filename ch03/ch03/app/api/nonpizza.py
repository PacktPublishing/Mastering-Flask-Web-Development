from flask import current_app , jsonify, request, Response, abort
from flask.json import  dumps,  loads
from flask.json.provider import JSONProvider
from datetime import date
from app.model.db import NonPizza
from app.repository.products import NonPizzaRepository
from app.model.config import db_session

@current_app.post('/nonpizza/add')
def add_nonpizza():
     content_type = request.headers.get('Content-Type')
     if content_type == 'application/json':
        nonpizza_json = request.json
        nonpizza = NonPizza(**nonpizza_json)
        repo = NonPizzaRepository(db_session)
        result = repo.insert(nonpizza)
        if result:
            current_app.logger.info('insert nonpizza menu option successful')
            return jsonify(nonpizza_json)
        else:
            current_app.logger.error('insert nonpizza menu option encountered a problem')
            return jsonify(message="insert nonpizza menu option encountered a problem")
     else:
        abort(500)
 
@current_app.get('/nonpizza/list/all')
def list_all_nonpizza():
    repo = NonPizzaRepository(db_session)
    records = repo.select_all()
    nonpizza_rec = [rec.to_json() for rec in records]
    current_app.logger.info('retrieved a list of nonpizza menu options successfully')
    return jsonify(nonpizza_rec)