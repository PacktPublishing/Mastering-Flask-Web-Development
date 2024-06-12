from flask import current_app, request, jsonify, make_response
import json
from asyncio import gather

from app.model.db import Candidate
from app.repository.candidates import CandidateRepository
from app.model.config import db_session
from app.services.candidates import insert_candidate_task

@current_app.post('/ch05/candidates/party')
async def add_list_candidates():
    candidates = request.get_json()
    count_rec_added = 0
    results = await gather( *[insert_candidate_task(data) for data in candidates])
    for success in results:
        if success:
            count_rec_added = count_rec_added  + 1
    return jsonify(message=f'there are {count_rec_added} newly added candidates'), 201


@current_app.get("/ch05/candidate/list/all")
async def list_all_candidate():
    async with db_session() as sess:
        async with sess.begin(): 
            repo = CandidateRepository(sess)
            records = await repo.select_all_candidate()
            candidate_rec = [rec.to_json() for rec in records]
            return make_response(candidate_rec, 201)
        

