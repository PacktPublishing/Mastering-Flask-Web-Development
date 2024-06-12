from flask import current_app , jsonify, request, Response
from flask.json import  dumps,  loads
from flask.json.provider import JSONProvider
from datetime import date
from app.model.db import AddOns
from app.repository.products import AddOnsRepository
from app.model.config import db_session

@current_app.post('/addons/add')
def add_addons():
    addons_json = request.get_json()
    addons = AddOns(**addons_json)
    repo = AddOnsRepository(db_session)
    result = repo.insert(addons)
    if result:
        current_app.logger.info('insert addon menu option successful')
        return jsonify(addons_json)
    else:
        current_app.logger.error('insert addon menu option encountered a problem')
        return jsonify(message="insert addon menu option encountered a problem")
   

@current_app.get('/addons/list/all')
def list_all_addons():
    repo = AddOnsRepository(db_session)
    records = repo.select_all()
    addons_rec = [rec.to_json() for rec in records]
    current_app.logger.info('retrieved a list of addon menu options successfully')
    return jsonify(addons_rec)