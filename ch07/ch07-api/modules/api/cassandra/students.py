from flask import current_app, jsonify, request
from modules.repository.cassandra.students import StudentRepository

@current_app.post('/student/add')
def add_student():
    repo = StudentRepository()
    data = request.get_json()
    result = repo.insert_student(data)
    if result == False:
        return jsonify(message="error encountered in student record insert"), 500
    return jsonify(message="inserted student record"), 201

@current_app.patch('/student/update')
def update_student():
    data = request.get_json()
    repo = StudentRepository()
    result = repo.update_student(data)
    if result == False:
        return jsonify(message="error encountered in student record update"), 500
    return jsonify(message="updated student record"), 201


@current_app.delete('/student/delete/<string:std_id>')
def delete_student(std_id:str):
    repo = StudentRepository()
    result = repo.delete_student_std_id(std_id)
    if result == False:
        return jsonify(message="error encountered in student record delete"), 500
    return jsonify(message="deleted student record"), 201

@current_app.get('/student/search/std_id/<string:std_id>')
def get_student_std_id(std_id:str):
    repo = StudentRepository()
    records = repo.search_by_std_id(std_id)
    return jsonify(records=records), 201

@current_app.post('/student/search/ids')
def list_student_ids():
    data = request.get_json()
    repo = StudentRepository()
    records = repo.search_by_ids(data['id'], data['std_id'])
    return jsonify(records=records), 201

    
@current_app.get('/student/list/all')
def list_all_students():
    repo = StudentRepository()
    records = repo.search_all_students()
    return jsonify(records=records), 201
