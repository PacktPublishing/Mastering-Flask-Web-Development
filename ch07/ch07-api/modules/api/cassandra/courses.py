from flask import current_app, jsonify, request
from modules.repository.cassandra.courses import CourseRepository


@current_app.post('/course/add')
def add_course():
    repo = CourseRepository()
    data = request.get_json()
    result = repo.insert_course(data)
    if result == False:
        return jsonify(message="error encountered in course record insert"), 500
    return jsonify(message="inserted course record"), 201

@current_app.patch('/course/update/code')
def update_course():
    data = request.get_json()
    repo = CourseRepository()
    result = repo.update_course(data)
    if result == False:
        return jsonify(message="error encountered in course record update"), 500
    return jsonify(message="updated course record"), 201

@current_app.delete('/course/delete/code/<string:code>')
def delete_course_code(code:str):
    repo = CourseRepository()
    result = repo.delete_course_code(code)
    if result == False:
        return jsonify(message="error encountered in course record delete"), 500
    return jsonify(message="deleted course record"), 201

@current_app.get('/course/search/code/<string:code>')
def get_course_code(code:str):
    repo = CourseRepository()
    records = repo.search_by_code(code)
    return jsonify(records=records), 201

@current_app.get('/course/list/all')
def list_all_course():
    repo = CourseRepository()
    records = repo.search_all_courses()
    return jsonify(records=records), 201
