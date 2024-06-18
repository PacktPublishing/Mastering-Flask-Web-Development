from celery import shared_task
from modules.repository.oauth2_token import TokenRepository
from modules.models.db import Token
from modules.models.config import db_session
from json import loads, dumps
from asyncio import run


@shared_task(ignore_result=False)
def add_token_task_wrapper(details):
    async def add_token_task(details):
        try:
            async with db_session() as sess:
              async with sess.begin(): 
                repo = TokenRepository(sess)
                details_dict = loads(details)
                print(details_dict)
                token = Token(**details_dict)
                result = await repo.insert_token(token)
                if result:
                    return str(True)
                else:
                    return str(False)
        except Exception as e:
            print(e)
            return str(False)
    return run(add_token_task(details))



@shared_task(ignore_result=False)
def get_token_task_wrapper(token_str):
     async def get_token_task(token_str):
        try:
            async with db_session() as sess:
               async with sess.begin(): 
                    repo = TokenRepository(sess)
                    records = await repo.select_token_access(token_str)
                    print(records[0])
                    #login_rec = [rec.to_json() for rec in records]
                    return records[0]
        except Exception as e:
            print(e)
            return None
     return run(get_token_task(token_str))
 

