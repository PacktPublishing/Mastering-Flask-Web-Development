
from asyncio import create_task
from app.model.db import Candidate
from app.repository.candidates import CandidateRepository
from app.model.config import db_session

async def insert_candidate_task(data):
    async with db_session() as sess:
        async with sess.begin(): 
            repo = CandidateRepository(sess)
            insert_task = create_task(repo.insert_candidate(Candidate(**data)))
            await insert_task
            result = insert_task.result()
            return result