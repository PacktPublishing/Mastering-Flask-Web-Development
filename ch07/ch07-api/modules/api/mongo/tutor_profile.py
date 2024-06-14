from flask import current_app, jsonify, request
from modules.repository.mongo.tutor_profile import TutorProfileRepository

from typing import List, Dict, Any

@current_app.post('/login/profile/add')
def add_login_profile():
    data = request.get_json()
    repo_profile = TutorProfileRepository()
    result = repo_profile.add_tutor_profile(data)
    if result == False:
        return jsonify(message="error encountered in tutor login profile record insert"), 500
    return jsonify(message="inserted login profile record"), 201

@current_app.delete('/login/profile/del/<int:id>')
def delete_login_profile(id:int):
    repo_profile = TutorProfileRepository()
    result = repo_profile.delete_tutor_profile(id)
    if result == False:
        return jsonify(message="error encountered in tutor login profile record delete"), 500
    return jsonify(message="deleted login profile record"), 201