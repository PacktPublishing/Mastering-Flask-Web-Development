from modules.admin import admin_bp
from flask import jsonify, request
from modules.admin.services.profile_tasks import add_admin_task_wrapper, list_all_admin_task_wrapper
from json import dumps, loads

@admin_bp.post('/admin/profile/add')
async def add_admin_profile():
    admin_json = request.get_json()
    print(admin_json)
    admin_str = dumps(admin_json)
    task = add_admin_task_wrapper.apply_async(args=[admin_str])
    result = task.get()
    return jsonify(message=result), 201

@admin_bp.get('/admin/profile/list/all')
async def list_all_admin_profile():
    task = list_all_admin_task_wrapper.apply_async(args=[])
    result = task.get()
    records = loads(result)
    return jsonify(records=records), 201

