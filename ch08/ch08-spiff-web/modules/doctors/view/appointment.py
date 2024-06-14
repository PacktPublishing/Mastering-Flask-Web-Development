from modules.doctors import doc_bp
from flask import render_template, request, redirect, url_for, session
from typing import List, Any
import os

from SpiffWorkflow.bpmn.workflow import BpmnWorkflow
from SpiffWorkflow.camunda.parser.CamundaParser import CamundaParser
from SpiffWorkflow.bpmn.specs.bpmn_task_spec import TaskSpec
from SpiffWorkflow.camunda.specs.user_task import UserTask
from SpiffWorkflow.task import Task, TaskState
from SpiffWorkflow.util.deep_merge import DeepMerge

parser = CamundaParser()
filepath = os.path.join("bpmn/dams_appointment.bpmn")
parser.add_bpmn_file(filepath)
spec = parser.get_spec('Process_ApptDams01')

global workflow
workflow = None

def update_data(dct, name, value):
    path = name.split('.')
    current = dct
    for component in path[:-1]:
        if component not in current:
            current[component] = {}
        current = current[component]
    current[path[-1]] = value

def upload_login_form_data(task: UserTask, form_data):
    form = task.task_spec.form
    data = {}
    if task.data is None:
        task.data = {}
    
    for field in form.fields:
        if field.id == "specialization":
            process_data = form_data["specialization"]
        elif field.id == "docid":
            process_data = form_data["docid"]
        elif field.id == "date_scheduled":
            process_data = form_data["appt_date"]
        elif field.id == "time_scheduled":
            process_data = form_data["appt_time"]
        elif field.id == "ticketid":
            process_data = form_data["ticketid"]
        elif field.id == "patientid":
            process_data = form_data["patientid"]
        elif field.id == "priority_level":
            process_data = form_data["priority_level"]
        update_data(data, field.id,  process_data)
        DeepMerge.merge(task.data, data)

@doc_bp.route("/doctor/patient", methods = ["GET", "POST"])
async def provide_patient_details():
    if request.method == "GET":
        return render_template("doc_patient_form.html"), 201
    form_data = dict()
    form_data['specialization'] = session['specialization']
    session.pop('specialization', default=None)
    form_data['docid'] = session['docid']
    session.pop('doctor', default=None)
    form_data['appt_date'] = session['appt_date']
    session.pop('appt_date', default=None)
    form_data['appt_time'] = session['appt_time']
    session.pop('appt_time', default=None)
    form_data['ticketid'] = request.form['ticketid']
    form_data['patientid'] = request.form['patientid']
    form_data['priority_level'] = request.form['priority_level']
    print(form_data)
    workflow = BpmnWorkflow(spec)
    workflow.do_engine_steps()
    ready_tasks: List[Task] = workflow.get_tasks(TaskState.READY)
    print(ready_tasks)
    while len(ready_tasks) > 0:
        for task in ready_tasks:
            if isinstance(task.task_spec, UserTask):
                print(task.id)
                upload_login_form_data(task, form_data)
            else:
                task_details:TaskSpec = task.task_spec
                print("Complete Task ", task_details.name)
            workflow.run_task_from_id(task_id=task.id)
        workflow.do_engine_steps()
        ready_tasks = workflow.get_tasks(TaskState.READY)
    print(workflow.data)
    dashboard_page = workflow.data['finalize_sched']
    if dashboard_page:
        return render_template("doc_dashboard.html"), 201
    else:
        return redirect(url_for("doc_bp.choose_specialization"))

@doc_bp.route("/doctor/schedule", methods = ["GET", "POST"])
async def reserve_schedule():
    if request.method == "GET":
        return render_template("doc_schedule_form.html"), 201
    session['appt_date'] = request.form['appt_date']
    session['appt_time'] = request.form['appt_time']
    return redirect(url_for("doc_bp.provide_patient_details"))

@doc_bp.route("/doctor/expertise", methods = ["GET", "POST"])
async def choose_specialization():
    if request.method == "GET":
        return render_template("doc_specialization_form.html")
    session['specialization'] = request.form['specialization']
    return redirect(url_for("doc_bp.select_doctor"))


@doc_bp.route("/doctor/select", methods = ["GET", "POST"])
async def select_doctor():
    if request.method == "GET":
        return render_template("doc_doctors_form.html")
    session['docid'] = request.form['docid']
    return redirect(url_for("doc_bp.reserve_schedule") )

    
   