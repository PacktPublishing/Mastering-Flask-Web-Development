from flask import current_app, jsonify, request
from modules.repository.mongo.tutor_login import TutorLoginRepository
from typing import List, Dict, Any
from bcrypt import hashpw, gensalt

@current_app.post('/tutor/login/add')
def add_login():
   data = request.get_json()
   repo = TutorLoginRepository()
   encpass = hashpw(str(data['username']).encode(), gensalt())
   data['encpass'] = encpass
   result = repo.insert_login(data) 
   if result == False:
        return jsonify(message="error encountered in tutor login record insert"), 500
   return jsonify(message="inserted tutor login record"), 201

@current_app.get('/tutor/login/list/all')
def list_all_login():
    repo = TutorLoginRepository()
    records = repo.get_all_login()
    return jsonify(records=records), 201

@current_app.get('/tutor/login/get/<int:id>')
def get_login(id:int):
    repo = TutorLoginRepository()
    record = repo.get_login(id)
    return jsonify(record=record), 201