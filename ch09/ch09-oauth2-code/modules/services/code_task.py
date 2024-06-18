from celery import shared_task
from modules.repository.oauth2_code import AuthCodeRepository
from modules.models.db import AuthorizationCode
from modules.models.config import db_session
from json import loads, dumps
from asyncio import run
from datetime import time, datetime, date

@shared_task(ignore_result=False)
def add_authcode_task_wrapper(details):
    async def add_authcode_task(details):
        try:
            async with db_session() as sess:
              async with sess.begin(): 
                repo = AuthCodeRepository(sess)
                details_dict = loads(details)
                print(details_dict)
                auth_code = AuthorizationCode(**details_dict)
                result = await repo.insert_code(auth_code)
                if result:
                    return str(True)
                else:
                    return str(False)
        except Exception as e:
            print(e)
            return str(False)
    return run(add_authcode_task(details))

@shared_task(ignore_result=False)
def delete_authcode_task_wrapper(code):
    async def delete_authcode_task(code):
        try:
            async with db_session() as sess:
              async with sess.begin(): 
                repo = AuthCodeRepository(sess)
                result = await repo.delete_code(code)
                if result:
                    return str(True)
                else:
                    return str(False)
        except Exception as e:
            print(e)
            return str(False)
    return run(delete_authcode_task(code))


@shared_task(ignore_result=False)
def get_authcode_task_wrapper(code, client_id):
     async def get_authcode_task(code, client_id):
        try:
            async with db_session() as sess:
               async with sess.begin(): 
                    repo = AuthCodeRepository(sess)
                    records = await repo.select_code(code, client_id)
                    print(records[0])
                    #login_rec = [rec.to_json() for rec in records]
                    return records[0]
        except Exception as e:
            print(e)
            return None
     return run(get_authcode_task(code, client_id))
 

