from modules.admin import admin_bp, get_client
from flask import jsonify, current_app

import asyncio

from flask import Flask, current_app, jsonify, make_response, request


from modules.workflows.transactions import ReserveAppointmentWorkflow
from modules.models.workflow import appt_queue_id, ReqAppointment

@admin_bp.route("/appointment/doctor", methods=["POST"])
async def request_appointment():
    client = get_client()
    appt_json = request.get_json()
    appointment = ReqAppointment(**appt_json)
    await client.start_workflow(
        ReserveAppointmentWorkflow.run,
        appointment,
        id=appointment.ticketid,
        task_queue=appt_queue_id,
    )

    message = jsonify({"message": "Appointment for doctor requested...."})
    response = make_response(message, 201)
    return response

@admin_bp.route("/appointment/details", methods=["GET"])
async def get_appointment_details():
    client = get_client()
    ticketid = request.args.get("ticketid")
    print(ticketid)
    handle = client.get_workflow_handle_for(ReserveAppointmentWorkflow.run, ticketid)
    results = await handle.query(ReserveAppointmentWorkflow.details)
    message = jsonify(
        {
            "ticketid": results.ticketid,
            "patientid": results.patientid,
            "docid": results.docid,
            "date_scheduled": results.date_scheduled,
            "time_scheduled": results.time_scheduled,
        }
    )

    response = make_response(message, 200)
    return response


@admin_bp.route("/appointment/close", methods=["DELETE"])
async def end_subscription():
    client = get_client()
    ticketid = request.args.get("ticketid")
    print(ticketid)
    handle = client.get_workflow_handle(
        ticketid,
    )
    await handle.cancel()
    message = jsonify({"message": "Requesting cancellation"})
    response = make_response(message, 202)
    return response




