from modules.home import home_bp
from flask import Flask, render_template, request, url_for, redirect
import os
from typing import List

from SpiffWorkflow.bpmn.workflow import BpmnWorkflow, Workflow
from SpiffWorkflow.camunda.parser.CamundaParser import CamundaParser
from SpiffWorkflow.camunda.specs.user_task import EnumFormField, UserTask
from SpiffWorkflow.util.deep_merge import DeepMerge
from node import ServiceTask, Node
from SpiffWorkflow.specs.Simple import Simple
from SpiffWorkflow.camunda.specs.business_rule_task import BusinessRuleTask
from SpiffWorkflow.bpmn.specs.defaults import ServiceTask, ScriptTask
from SpiffWorkflow.bpmn.PythonScriptEngine import PythonScriptEngine
from SpiffWorkflow.bpmn.PythonScriptEngineEnvironment import TaskDataEnvironment
from RestrictedPython import safe_globals
import json
from SpiffWorkflow.workflow import Workflow
from SpiffWorkflow.task import Task, TaskState

parser = CamundaParser()
filepath = os.path.join("bpmn/deployment_bpmn.bpmn")
parser.add_bpmn_file(filepath)
spec = parser.get_spec('Process_12knidk')

def update_data(dct, name, value):
    path = name.split('.')
    current = dct
    for component in path[:-1]:
        if component not in current:
            current[component] = {}
        current = current[component]
    current[path[-1]] = value

def pass_form_data(task: UserTask, age):
    
    form = task.task_spec.form
    data = {}
    if task.data is None:
        task.data = {}

    for field in form.fields:
        if field.type == "long":
            answer = age
        update_data(data, field.id, answer)
        DeepMerge.merge(task.data, data)

def callScriptTask(task):
    print(task.get_name(), task.data)
    if (task.get_name() == "Activity_1s1r3h3"):
        task.data['age'] = 10
  
@home_bp.route('/index', methods=["GET", "POST"])
async def index():
    if request.method == "GET":
        return render_template("age.html")
    
    age = int(request.form['age'])
    
    
    workflow = BpmnWorkflow(spec)
    workflow.do_engine_steps()
    #ready_tasks: list[Task] = workflow.get_tasks_from_spec_name(name='Activity_Mgr01')
    
    ready_tasks: List[Task] = workflow.get_tasks(TaskState.READY)
    print(ready_tasks)
    while len(ready_tasks) > 0:
        for task in ready_tasks:
            if isinstance(task.task_spec, UserTask):
                pass_form_data(task, age)
                print(task.data)
            elif isinstance(task.task_spec, ScriptTask):
                print(task.id, task.data)
            else:
                print("Complete Task ", task.task_spec.name)
            workflow.run_task_from_id(task_id=task.id)
        #workflow.refresh_waiting_tasks()
       
        workflow.do_engine_steps(will_complete_task=callScriptTask)
        print(workflow.data)
        ready_tasks = workflow.get_tasks(TaskState.READY)
    return render_template("form_order.html"), 201