from flask import current_app , jsonify, request, Response, abort
from flask.json import  dumps,  loads
from flask.json.provider import JSONProvider
from datetime import date
from app.model.db import Category
from app.repository.products import CategoryRepository
from app.model.config import db_session
from app.exceptions.db import NoRecordException


@current_app.post('/category/add')
def add_category():
    if request.is_json:
        cat_json = request.json
        cat = Category(**cat_json)
        repo = CategoryRepository(db_session)
        result = repo.insert(cat)
        if result:
            current_app.logger.info('insert category details successful')
            return jsonify(cat_json)
        else:
            current_app.logger.error('insert category encountered a problem')
            return jsonify(message="insert login encountered a problem")
    else:
        abort(500)
    
    
@current_app.get('/category/list/all')
def list_all_category():
    repo = CategoryRepository(db_session)
    records = repo.select_all()
    cat_rec_rec = [rec.to_json() for rec in records]
    current_app.logger.info('retrieved a list of categories successfully')
    return jsonify(cat_rec_rec)

@current_app.delete('/category/delete/<int:id>')
def delete_category(id:int):
   
    repo = CategoryRepository(db_session)
    result = repo.delete(id)
    if result:
        current_app.logger.info('delete employee record successful')
        return jsonify(message=f'category {id} deleted'), 201
    else:
        raise NoRecordException("delete employee record encountered a problem", status_code=500)
   