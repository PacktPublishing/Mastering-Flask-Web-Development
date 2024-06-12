from celery import shared_task
from app.repository.vote import VoteRepository
from app.model.config import db_session
from app.model.db import Vote
from json import loads, dumps
from asyncio import run
from datetime import time, datetime

@shared_task(ignore_result=False)
def add_vote_task_wrapper(details):
    async def add_vote_task(details):
        try:
            async with db_session() as sess:
              async with sess.begin(): 
                repo = VoteRepository(sess)
                details_dict = loads(details)
                print(details_dict)
                election = Vote(**details_dict)
                result = await repo.insert(election)
                if result:
                    return str(True)
                else:
                    return str(False)
        except Exception as e:
            print(e)
            return str(False)
    return run(add_vote_task(details))

@shared_task(ignore_result=False)
def list_all_votes_task_wrapper():
    async def list_all_votes_task():
      async with db_session() as sess:
        async with sess.begin(): 
            repo = VoteRepository(sess)
            records = await repo.select_all_vote()
            vote_rec = [rec.to_json() for rec in records]
            return dumps(vote_rec, default=json_date_serializer)
    return run(list_all_votes_task())

def json_date_serializer(obj):
    if isinstance(obj, time):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))