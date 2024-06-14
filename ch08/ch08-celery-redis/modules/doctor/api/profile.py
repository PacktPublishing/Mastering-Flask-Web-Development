from modules.admin import admin_bp
from flask import jsonify,  request
from modules.doctor.services.profile_tasks import add_doctor_task_wrapper, list_all_doc_task_wrapper
from json import dumps, loads

@admin_bp.post('/doc/profile/add')
async def add_doc_profile():
    doc_json = request.get_json()
    print(doc_json)
    doc_str = dumps(doc_json)
    task = add_doctor_task_wrapper.apply_async(args=[doc_str])
    result = task.get()
    return jsonify(message=result), 201

@admin_bp.get('/doc/profile/list/all')
async def list_all_doc_profile():
    task = list_all_doc_task_wrapper.apply_async(args=[])
    result = task.get()
    records = loads(result)
    return jsonify(records=records), 201
