from celery import shared_task
from modules.repository.login import LoginRepository
from modules.models.config import db_session
from json import loads, dumps
from asyncio import run
from datetime import time, datetime, date

@shared_task(ignore_result=False)
def get_user_task_wrapper(username):
     async def get_user_task(username):
        try:
            async with db_session() as sess:
               async with sess.begin(): 
                    repo = LoginRepository(sess)
                    records = await repo.select_login_username(username)
                    print(records[0])
                    #login_rec = [rec.to_json() for rec in records]
                    return records[0]
        except Exception as e:
            print(e)
            return None
     return run(get_user_task(username))
