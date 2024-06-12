from flask import jsonify, current_app, request, make_response
from app.services.vote_tasks import add_vote_task_wrapper, list_all_votes_task_wrapper
from json import dumps, loads
from datetime import time, datetime

@current_app.post('/ch05/vote/add')
async def add_vote():
    vote_json = request.get_json()
    print(vote_json)
    vote_str = dumps(vote_json)
    task = add_vote_task_wrapper.apply_async(args=[vote_str])
    result = task.get()
    return jsonify(message=result), 201

@current_app.get('/ch05/vote/list/all')
async def list_all_vote():
    task = list_all_votes_task_wrapper.apply_async(args=[])
    result = task.get()
    records = loads(result)
    return jsonify(records=records), 201

