from modules.login import login_bp
from flask import jsonify, request
from modules.login.services.login_tasks import add_login_task_wrapper, list_all_login_task_wrapper, show_list_login_task_wrapper
from modules.login.services.workflow_tasks import add_user_login_task_wrapper, add_user_profile_task_wrapper, show_complete_login_task_wrapper

from json import dumps, loads
from celery import chain

@login_bp.post('/login/user/add')
async def add_user_workflow():
    user_json = request.get_json()
    user_str = dumps(user_json)
    task = chain(add_user_login_task_wrapper.s(user_str), add_user_profile_task_wrapper.s(), show_complete_login_task_wrapper.s())()
    result = task.get()
    records = loads(result)
    return jsonify(profile=records), 201

@login_bp.post('/login/add')
async def add_login_details():
    login_json = request.get_json()
    print(login_json)
    login_str = dumps(login_json)
    task = add_login_task_wrapper.s(login_str).apply_async()
    result = task.get()
    return jsonify(success=result), 201

@login_bp.get('/login/list/all')
async def list_all_login():
    task = list_all_login_task_wrapper.s().apply_async()
    result = task.get()
    records = loads(result)
    return jsonify(records=records), 201

@login_bp.get('/login/list/count')
async def count_login_recs():
    workflow = chain(list_all_login_task_wrapper.s(), show_list_login_task_wrapper.s())()
    count_rec = workflow.get()
    return jsonify(count=count_rec), 201