from flask import current_app, jsonify, request
from modules.models.db.redis_models import SearchCourse
from modules.repository.redis.course_search import SearchCourseRepository

@current_app.post('/saved/search/add')
def save_course():
    data = request.get_json()
    repo = SearchCourseRepository()
    result = repo.add_course(data)
    if result == False:
        return jsonify(message="error encountered in course record insert"), 500
    return jsonify(message="inserted course record"), 201

@current_app.patch('/saved/search/update')
def update_saved_course():
    data = request.get_json()
    repo = SearchCourseRepository()
    result = repo.update_course(data)
    if result == False:
        return jsonify(message="error encountered in course record update"), 500
    return jsonify(message="updated course record"), 201

@current_app.delete('/saved/search/delete/<string:pk>')
def delete_saved_course(pk:str):
    repo = SearchCourseRepository()
    result = repo.delete_course(pk)
    if result == False:
        return jsonify(message="error encountered in course record delete"), 500
    return jsonify(message="deleted course record"), 201

@current_app.get('/saved/search/course_code/<string:code>')
def search_course_code(code:str):
    repo = SearchCourseRepository()
    records = repo.select_course_code(code)
    return jsonify(records=records), 201

@current_app.get('/saved/search/course_pk/<string:pk>')
def search_course(pk:str):
    repo = SearchCourseRepository()
    record = repo.select_course(pk)
    return jsonify(record=record), 201

@current_app.get('/saved/search/course/all')
def search_saved_courses():
    repo = SearchCourseRepository()
    records = repo.select_all_course()
    return jsonify(records=records), 201