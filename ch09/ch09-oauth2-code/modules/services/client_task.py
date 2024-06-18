from celery import shared_task
from modules.repository.oauth2_client import ClientRepository
from modules.models.db import Client
from modules.models.config import db_session
from json import loads, dumps
from asyncio import run
from datetime import time, datetime, date
from werkzeug.security import generate_password_hash, gen_salt

@shared_task(ignore_result=False)
def get_client_task_wrapper(client_id):
     async def get_client_task(client_id):
        try:
            async with db_session() as sess:
               async with sess.begin(): 
                    repo = ClientRepository(sess)
                    records = await repo.select_client(client_id)
                    print(records[0])
                    #login_rec = [rec.to_json() for rec in records]
                    return records[0]
        except Exception as e:
            print(e)
            return None
     return run(get_client_task(client_id))
 
def get_client_user_task_wrapper(user_id):
     async def get_client_user_task(user_id):
        try:
            async with db_session() as sess:
               async with sess.begin(): 
                    repo = ClientRepository(sess)
                    records = await repo.select_client_user(user_id)
                    print(records[0])
                    #login_rec = [rec.to_json() for rec in records]
                    return records[0]
        except Exception as e:
            print(e)
            return None
     return run(get_client_user_task(user_id))
 
@shared_task(ignore_result=False)
def add_client_task_wrapper(details, details_meta):
    async def add_client_task(details, details_meta):
        details_dict = loads(details)
        details_meta_dict = loads(details_meta)
       
        client_secret = ''
        if details_meta_dict['token_endpoint_auth_method'] == 'none':
            client_secret = ''
        else:
            client_secret = gen_salt(48)
            
        client:Client = Client(
            client_id=details_dict["client_id"],
            client_id_issued_at=details_dict["client_id_issued_at"],
            user_id=details_dict["user_id"],
            client_secret=client_secret
        )
        
        client.set_client_metadata(details_meta_dict)
        print(client.client_metadata)
        try:
            async with db_session() as sess:
              async with sess.begin(): 
                repo = ClientRepository(sess)
                result = await repo.insert_client(client)
                if result:
                    return str(True)
                else:
                    return str(False)
        except Exception as e:
            print(e)
            return str(False)
    return run(add_client_task(details, details_meta))