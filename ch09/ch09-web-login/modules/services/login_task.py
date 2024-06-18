from celery import shared_task
from modules.repository.login import LoginRepository
from modules.models.config import db_session
from asyncio import run


@shared_task(ignore_result=False)
def get_user_task_wrapper(id):
     async def get_user_task(id):
        try:
            async with db_session() as sess:
               async with sess.begin(): 
                    repo = LoginRepository(sess)
                    records = await repo.select_login(int(id))
                    print(records[0])
                    #login_rec = [rec.to_json() for rec in records]
                    return records[0]
        except Exception as e:
            print(e)
            return None
     return run(get_user_task(id))
