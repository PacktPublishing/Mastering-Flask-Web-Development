from flask import current_app , jsonify, request, Response, abort
from flask.json import  dumps,  loads
from flask.json.provider import JSONProvider
from datetime import date
from app.model.db import Pizza
from app.repository.products import PizzaRepository
from app.model.config import db_session
from app.exceptions.db import NoRecordException



@current_app.post('/pizza/add')
def add_pizza():
    if request.is_json:
        pizza_json = request.get_json(force=True)

        pizza = Pizza(**pizza_json)
        repo = PizzaRepository(db_session)
        result = repo.insert(pizza)
        if result:
            current_app.logger.info('insert pizza menu option successful')
            return jsonify(pizza_json)
        else:
            current_app.logger.error('insert pizza menu option encountered a problem')
            return jsonify(message="insert pizza menu option encountered a problem")
    else:
        abort(500)
   

@current_app.get('/pizza/list/all')
def list_all_pizza():
    repo = PizzaRepository(db_session)
    records = repo.select_all()
    pizza_rec = [rec.to_json() for rec in records]
    current_app.logger.info('retrieved a list of pizza menu options successfully')
    return jsonify(pizza_rec)

@current_app.delete('/pizza/delete/<string:code>')
def delete_pizza(code:str):
   
    repo = PizzaRepository(db_session)
    result = repo.delete(code)
    if result:
        current_app.logger.info('delete pizza record successful')
        return jsonify(message=f'pizza {code} deleted'), 201
    else:
        raise NoRecordException("delete employee record encountered a problem", status_code=500)
   