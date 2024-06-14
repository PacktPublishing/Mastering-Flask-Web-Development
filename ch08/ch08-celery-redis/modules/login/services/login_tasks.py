from celery import shared_task
from modules.login.repository.login import LoginRepository
from modules.models.config import db_session
from modules.models.db import Login
from json import loads, dumps
from asyncio import run
from datetime import time

@shared_task(ignore_result=False)
def add_login_task_wrapper(details):
    async def add_login_task(details):
        try:
            async with db_session() as sess:
              async with sess.begin(): 
                repo = LoginRepository(sess)
                details_dict = loads(details)
                print(details_dict)
                login = Login(**details_dict)
                result = await repo.insert_login(login)
                if result:
                    return str(True)
                else:
                    return str(False)
        except Exception as e:
            print(e)
            return str(False)
    return run(add_login_task(details))

@shared_task(ignore_result=False)
def list_all_login_task_wrapper():
    async def list_all_login_task():
      async with db_session() as sess:
        async with sess.begin(): 
            repo = LoginRepository(sess)
            records = await repo.select_all_login()
            vote_rec = [rec.to_json() for rec in records]
            return dumps(vote_rec, default=json_date_serializer)
    return run(list_all_login_task())

@shared_task(ignore_result=False)
def show_list_login_task_wrapper(records):
    async def show_list_login_task(records):
       data = loads(records)
       count = len(data)
       return count
    return run(show_list_login_task(records))

def json_date_serializer(obj):
    if isinstance(obj, time):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))