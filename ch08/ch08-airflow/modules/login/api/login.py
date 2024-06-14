from modules.login import login_bp
from modules.models.config import db_session
from modules.models.db import Login
from modules.login.repository.login import LoginRepository
from flask import jsonify, request
from datetime import datetime
import requests
import json

@login_bp.post("/login/add")
async def add_login():
     async with db_session() as sess:
        async with sess.begin(): 
            login_json = request.get_json()
            login = Login(**login_json)
            repo = LoginRepository(sess)
            result = await repo.insert_login(login)
            if result: 
                return jsonify(record=login_json), 201
            else:
                return jsonify(record={}), 500

@login_bp.get("/login/list/all")
async def retrieve_all_login():
    async with db_session() as sess:
        async with sess.begin(): 
            repo = LoginRepository(sess)
            result = await repo.select_all_login()
            result_rec = [rec.to_json()for rec in result]
            print(result_rec)
            return jsonify(records=result_rec), 201

@login_bp.get("/login/report/count")
async def count_login_accounts():
    login_count = request.args.get("login_count")
    print(login_count)
    message = f'There are {login_count} users as of {datetime.now()}.'
    return jsonify(message=message), 201

@login_bp.get("/login/dag/report/login/count")
async def trigger_report_login_count():
    token = "cGFja3RhZG1pbjpwYWNrdGFkbWlu"
    dag_id = "report_login_count"
    deployment_url = "localhost:8080"
    response = requests.post(
        url=f"http://{deployment_url}/api/v1/dags/{dag_id}/dagRuns",
        headers={
            "Authorization": f"Basic {token}",
            "Content-Type": "application/json",
            "Accept": "*/*",
            "Connection": "keep-alive",
            "Accept-Encoding": "gzip, deflate, br"
        },
        data = '{"dag_run_id": "d08a62c6-ed71-49fc-81a4-47991221aea5"}'
    )
    result = response.content.decode(encoding="utf-8")
    return jsonify(message=result), 201
    

@login_bp.get("/login/dag/xcom/values")
async def extract_xcom_count():
    try:
        token = "cGFja3RhZG1pbjpwYWNrdGFkbWlu"
        dag_id = "report_login_count"
        task_id = "return_report"
        dag_run_id = "d08a62c6-ed71-49fc-81a4-47991221aea5"
        deployment_url = "localhost:8080"
        response = requests.get(
            url=f"http://{deployment_url}/api/v1/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/xcomEntries/{'report_msg'}",
            headers={
                "Authorization": f"Basic {token}",
                "Content-Type": "application/json",
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Accept-Encoding": "gzip, deflate, br"
            }
        )
        result = response.json()
        message = result['value']
        return jsonify(message=message)
    except Exception as e:
        print(e)
    return jsonify(message="")