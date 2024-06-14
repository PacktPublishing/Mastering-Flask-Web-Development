from modules.admin import admin_bp
from flask import jsonify, request
from celery import group, chord
import os

from modules.admin.services.reports_tasks import generate_csv_admin_task_wrapper, generate_csv_doctor_task_wrapper, generate_csv_patient_task_wrapper
from modules.admin.services.doctor_stats_tasks import count_patients_doctor_task_wrapper, count_request_doctor_task_wrapper, create_doctor_stats_task_wrapper


@admin_bp.get('/admin/reports/create')
async def create_reports():
    admin_csv_filename = os.getcwd() + "/files/dams_admin.csv"
    patient_csv_filename = os.getcwd() + "/files/dams_patient.csv"
    doctor_csv_filename = os.getcwd() + "/files/dams_doc.csv"
    workflow = group(generate_csv_admin_task_wrapper.s(admin_csv_filename), generate_csv_doctor_task_wrapper.s(doctor_csv_filename), generate_csv_patient_task_wrapper.s(patient_csv_filename))()
    workflow.get()
    return jsonify(message="done backup"), 201

@admin_bp.get('/admin/doc/stats')
async def derive_doctor_stats():
    docid = request.args.get("docid")
    workflow = chord((count_patients_doctor_task_wrapper.s(docid), count_request_doctor_task_wrapper.s(docid)), create_doctor_stats_task_wrapper.s(docid))()
    result = workflow.get()
    return jsonify(message=result), 201