from modules.login import login_bp
from flask import render_template, request, redirect, url_for, session
from typing import List, Any
import os

from modules.login.services.activity import is_valid_user, verify_admin_role, verify_doc_role, verify_patient_role

from SpiffWorkflow.bpmn.workflow import BpmnWorkflow, Workflow
from SpiffWorkflow.camunda.parser.CamundaParser import CamundaParser
from SpiffWorkflow.bpmn.specs.defaults import ScriptTask
from SpiffWorkflow.camunda.specs.user_task import UserTask
from SpiffWorkflow.task import Task, TaskState
from SpiffWorkflow.util.deep_merge import DeepMerge
from datetime import datetime
parser = CamundaParser()
filepath = os.path.join("bpmn/dams_login.bpmn")
parser.add_bpmn_file(filepath)
spec = parser.get_spec('Process_LoginDams01')


def update_data(dct, name, value):
    path = name.split('.')
    current = dct
    for component in path[:-1]:
        if component not in current:
            current[component] = {}
        current = current[component]
    current[path[-1]] = value
    
def upload_login_form_data(task: UserTask, username, password, role):

    form = task.task_spec.form
    data = {}
    if task.data is None:
        task.data = {}

    for field in form.fields:
        if field.id == "username":
            process_data = username
        elif field.id == "password":
            process_data = password
        elif field.id == "role":
            process_data = role
        update_data(data, field.id,  process_data)
        DeepMerge.merge(task.data, data)
      
def callScriptTask(task):
    if(isinstance(task.task_spec, ScriptTask)):
        if (task.get_name()  == "Activity_verify02a"):
            if session['is_valid_user'] == True and session['is_admin_role'] == 0 and task.data['role'] == 'administrator':
                task.data['valid_admin'] = True
            else:
                task.data['valid_admin'] = False
            
        elif (task.get_name()  == "Activity_verify02b"):
            if session['is_valid_user'] == True and session['is_doc_role'] == 1 and task.data['role'] == 'doctor':
                task.data['valid_doc'] = True
            else:
                task.data['valid_doc'] = False
        elif (task.get_name()  == "Activity_verify02c"):
            if session['is_valid_user'] == True and session['is_patient_role'] == 2 and task.data['role'] == 'patient':
                task.data['valid_patient'] = True
            else:
                task.data['valid_patient'] = False
        elif (task.get_name()  == "Activity_proceed03a"):
            task.data['header_msg'] = f"Admin user {task.data['username'] } logged at {datetime.strftime(datetime.now(), '%d-%m-%Y (%H:%M:%S)')}"
        elif (task.get_name()  == "Activity_proceed03aerr"):
            task.data['header_msg'] = f"Admin user {task.data['username'] } is an invalid user."
        elif (task.get_name()  == "Activity_proceed03b"):
            task.data['header_msg'] = f"Doctor user {task.data['username'] } logged at {datetime.strftime(datetime.now(), '%d-%m-%Y (%H:%M:%S)')}"
        elif (task.get_name()  == "Activity_proceed03berr"):
            task.data['header_msg'] = f"Doctor user {task.data['username'] } is an invalid user."
        elif (task.get_name()  == "Activity_proceed03c"):
            task.data['header_msg'] = f"Patient user {task.data['username'] } logged at {datetime.strftime(datetime.now(), '%d-%m-%Y (%H:%M:%S)')}"
        elif (task.get_name()  == "Activity_proceed03cerr"):
            task.data['header_msg'] = f"Patient user {task.data['username'] } is an invalid user."
    
    
@login_bp.route("/login/form", methods = ["GET", "POST"])
async def show_form():
    if request.method == "GET":
        return render_template("login_form.html"), 201
    username = request.form['username']
    password = request.form['password']
    role = request.form['role']
    
    is_admin_role = await verify_admin_role(username)
    is_doc_role = await verify_doc_role(username)
    is_patient_role = await verify_patient_role(username)
    valid_user = await is_valid_user(username, password)
    session['is_admin_role'] = is_admin_role
    session['is_doc_role'] = is_doc_role
    session['is_patient_role'] = is_patient_role
    session['is_valid_user'] = valid_user
   
    
    workflow = BpmnWorkflow(spec)
    workflow.do_engine_steps()
    #ready_tasks: list[Task] = workflow.get_tasks_from_spec_name(name='Activity_Mgr01')
    
    ready_tasks: List[Task] = workflow.get_tasks(TaskState.READY)
    print(ready_tasks)
    while len(ready_tasks) > 0:
        for task in ready_tasks:
            if isinstance(task.task_spec, UserTask):
                upload_login_form_data(task, username, password, role)
            else:
                print("Complete Task ", task.task_spec.name)
            workflow.run_task_from_id(task_id=task.id)
              
        workflow.do_engine_steps(will_complete_task=callScriptTask)
        
        ready_tasks = workflow.get_tasks(TaskState.READY)
    
    dashboard_page = workflow.data['dashboard_type']
    session['header_msg'] = workflow.data['header_msg']
    if dashboard_page == "admin":
        return redirect(url_for('admin_bp.show_menu'))
    elif dashboard_page == "doc":
        return redirect(url_for('doc_bp.show_menu'))
    elif dashboard_page == "patient":
        return redirect(url_for('patient_bp.show_menu'))
    elif dashboard_page == "error":
        return render_template("bpmn_error.html")
    
    