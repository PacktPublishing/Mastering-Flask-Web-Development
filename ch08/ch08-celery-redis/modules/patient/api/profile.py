from modules.admin import admin_bp
from flask import jsonify, request
from modules.patient.services.profile_tasks import add_patient_task_wrapper, list_all_patient_task_wrapper
from json import dumps, loads


@admin_bp.post('/patient/profile/add')
async def add_patient_profile():
    patient_json = request.get_json()
    print(patient_json)
    patient_str = dumps(patient_json)
    task = add_patient_task_wrapper.apply_async(args=[patient_str])
    result = task.get()
    return jsonify(message=result), 201

@admin_bp.get('/patient/profile/list/all')
async def list_all_patient_profile():
    task = list_all_patient_task_wrapper.apply_async(args=[])
    result = task.get()
    records = loads(result)
    return jsonify(records=records), 201
