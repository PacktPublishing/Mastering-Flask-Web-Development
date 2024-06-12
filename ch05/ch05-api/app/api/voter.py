from flask import jsonify, current_app, request, make_response

from app.repository.voters import VoterRepository
from app.model.config import db_session
from app.model.db import Voter
from asyncio import InvalidStateError, get_running_loop

@current_app.post("/ch05/voter/add")
async def add_voter():
    async with db_session() as sess:
        async with sess.begin(): 
            repo = VoterRepository(sess)
            voter_json = request.get_json()
            voter = Voter(**voter_json)
            try:
                loop = get_running_loop()
                insert_task = loop.create_task(repo.insert_voter(voter))
                await insert_task
                result = insert_task.result()
                if result:
                    content = jsonify(voter_json)
                    return make_response(content, 201)
                else:
                    content = jsonify(message="insert voter details encountered a problem")
                    return make_response(content, 500)
            except InvalidStateError:
                content = jsonify(message="insert voter task failed with exceptions")
                return make_response(content, 500)
            
@current_app.get("/ch05/voter/list/all")
async def list_all_voter():
     async with db_session() as sess:
        async with sess.begin(): 
            repo = VoterRepository(sess)
            loop = get_running_loop()
            list_voter_task = loop.create_task(repo.select_all_voter())
            await list_voter_task
            records = list_voter_task.result()
            voter_rec = [rec.to_json() for rec in records]
            return make_response(voter_rec, 201)
            
