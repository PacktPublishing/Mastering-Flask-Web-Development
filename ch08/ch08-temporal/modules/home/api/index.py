from modules.home import home_bp, get_client
from flask import jsonify, current_app

import asyncio

from flask import Flask, current_app, jsonify, make_response, request


from run_worker import SendEmailWorkflow
from modules.models.workflow import WorkflowOptions, appt_queue_id

@home_bp.route("/subscribe", methods=["POST"])
async def start_subscription():
    client = get_client()

    email: str = str(request.json.get("email"))
    data: WorkflowOptions = WorkflowOptions(email=email)
    await client.start_workflow(
        SendEmailWorkflow.run,
        data,
        id=data.email,
        task_queue=appt_queue_id,
    )

    message = jsonify({"message": "Resource created successfully"})
    response = make_response(message, 201)
    return response

@home_bp.route("/get_details", methods=["GET"])
async def get_query():
    client = get_client()
    email = request.args.get("email")
    print(email)
    handle = client.get_workflow_handle_for(SendEmailWorkflow.run, workflow_id=email)
    results = await handle.query(SendEmailWorkflow.details)
    message = jsonify(
        {
            "email": results.email,
            "message": results.message,
            "subscribed": results.subscribed,
            "numberOfEmailsSent": results.count,
        }
    )

    response = make_response(message, 200)
    return response


@home_bp.route("/unsubscribe", methods=["DELETE"])
async def end_subscription():
    client = get_client()
    email: str = str(request.json.get("email"))
    handle = client.get_workflow_handle(
        email,
    )
    await handle.cancel()
    message = jsonify({"message": "Requesting cancellation"})

    # Return 202 because this is a request to cancel and the API has accepted
    # the request but has not processed yet.
    response = make_response(message, 202)
    return response

@home_bp.route('/index', methods = ['GET'])
async def index():
    return jsonify(message="working")