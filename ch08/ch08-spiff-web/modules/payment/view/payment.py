from modules.payment import payment_bp
from modules.login import login_bp
from modules.payment.services.payment_flow import PaymentWorkflowSpec
from flask import render_template, request, redirect, url_for, session
from typing import List, Any
import os

       
from SpiffWorkflow.workflow import Workflow
from SpiffWorkflow.task import Task, TaskState

@payment_bp.route("/payment/start", methods = ["GET", "POST"])
async def start_payment_form():
    if request.method == "GET":
        return render_template("payment_form.html"), 201
    
    ticketid = request.form["ticketid"]
    print(ticketid)
    patientid = request.form["patientid"]
    print(patientid)
    charge = float(request.form["charge"])
    print(charge)
    amount = float(request.form["amount"])
    print(amount)
    discount = float(request.form["discount"])
    print(discount)
    status = request.form["status"]
    date_released = request.form["date_released"]
    print(ticketid)
    workflow_instance = Workflow(workflow_spec=PaymentWorkflowSpec())
    workflow_instance.get_tasks()
    
    start_tasks: list[Task] = workflow_instance.get_tasks_from_spec_name(name='Start')
    for task in start_tasks:
        if task.state == TaskState.READY:
            workflow_instance.run_task_from_id(task_id=task.id)


    patient_pay_task: list[Task] = workflow_instance.get_tasks_from_spec_name(name='dams_patient_pay')
    for task in patient_pay_task:
        if task.state == TaskState.READY:
            task.set_data(ticketid=ticketid, patientid=patientid, charge=charge, amount=amount, discount=discount,
                          status=status, date_released=date_released)
            workflow_instance.run_task_from_id(task_id=task.id)

    payment_check_task: list[Task] = workflow_instance.get_tasks_from_spec_name(name='payment_check')
    for task in payment_check_task:
        if task.state == TaskState.READY:
            workflow_instance.run_task_from_id(task_id=task.id)

    for_releasing = False

    patient_release_task: list[Task] = workflow_instance.get_tasks_from_spec_name(name='dams_patient_release')
    for task in patient_release_task:
        if task.state == TaskState.READY:
            for_releasing = True
            workflow_instance.run_task_from_id(task_id=task.id)

    patient_onhold_task: list[Task] = workflow_instance.get_tasks_from_spec_name(name='dams_patient_onhold')
    for task in patient_onhold_task:
        if task.state == TaskState.READY:
            workflow_instance.run_task_from_id(task_id=task.id)
            
    if for_releasing == True:
        return redirect(url_for('payment_bp.release_patient'), code=307)
    else:
       return redirect(url_for('payment_bp.hold_patient'), code=307)


@payment_bp.route("/payment/onhold", methods = ["GET", "POST"])
async def hold_patient():
    if request.method == "POST":
        return render_template("patient_onhold.html"), 201

@payment_bp.route("/payment/onrelease", methods = ["GET", "POST"])
async def release_patient():
    if request.method == "POST":
        return render_template("patient_release.html"), 201