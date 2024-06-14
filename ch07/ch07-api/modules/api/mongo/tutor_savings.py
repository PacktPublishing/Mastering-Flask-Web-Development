from flask import current_app, jsonify, request
from modules.repository.mongo.savings import SavingsRepository


@current_app.post('/profile/savings/add')
def add_profile_savings():
    data = request.get_json()
    repo_savings = SavingsRepository()
    result = repo_savings.add_savings(data)
    if result == False:
        return jsonify(message="error encountered in profile savings record insert"), 500
    return jsonify(message="inserted profile savings record"), 201

@current_app.patch('/profile/savings/delete')
def delete_profile_savings():
    data = request.get_json()
    repo_profile = SavingsRepository()
    result = repo_profile.delete_savings(data)
    if result == False:
        return jsonify(message="error encountered in profile savings record delete"), 500
    return jsonify(message="deleted profile savings record"), 201
