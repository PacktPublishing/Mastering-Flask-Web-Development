from celery import shared_task
from modules.login.repository.login import LoginRepository
from modules.admin.repository.admin import AdminRepository
from modules.patient.repository.patient import PatientRepository
from modules.doctor.repository.doctor import DoctorRepository
from modules.models.config import db_session
from modules.models.db import Login, Administrator, Doctor, Patient
from json import loads, dumps
from asyncio import run
from datetime import date

# chained tasks
@shared_task(ignore_result=False)
def add_user_login_task_wrapper(details):
    async def add_user_task(details):
        try:
            async with db_session() as sess:
              async with sess.begin(): 
                repo = LoginRepository(sess)
                details_dict = loads(details)
                user_dict = dict()
                user_dict['username'] = details_dict['username']
                user_dict['password'] = details_dict['password']
                del details_dict['password']
               
                login = Login(**user_dict)
                result = await repo.insert_login(login)
                
                if result:
                    profile_details = dumps(details_dict)
                    return profile_details
                else:
                    return ""
        except Exception as e:
            print(e)
            return ""
    return run(add_user_task(details))

@shared_task(ignore_result=False)
def add_user_profile_task_wrapper(details):
    async def add_user_profile_task(details):
        try:
            async with db_session() as sess:
              async with sess.begin(): 
                print(details)
                if len(details) == 0:
                    return dumps({})
                profile_dict = loads(details)
                role = profile_dict['role']
                print(role)
                result = False
                if role == 0:
                    repo = AdminRepository(sess) 
                    admin = Administrator(**profile_dict)
                    result = await repo.insert_admin(admin)
                elif role == 1:
                    repo = DoctorRepository(sess) 
                    doc = Doctor(**profile_dict)
                    result = await repo.insert_doctor(doc) 
                elif role == 2:
                    repo = PatientRepository(sess) 
                    patient = Patient(**profile_dict)
                    result = await repo.insert_patient(patient) 
                
                if result:
                    return profile_dict['username']
                else:
                    return ""
        except Exception as e:
            print(e)
            return ""
    return run(add_user_profile_task(details))


@shared_task(ignore_result=False)
def show_complete_login_task_wrapper(username):
    async def show_complete_login_task(username):
        try:
            async with db_session() as sess:
              async with sess.begin(): 
                if len(username) == 0:
                    return dumps({}) 
                repo = LoginRepository(sess)
                records = await repo.select_login_username(username)
                login_rec = [rec.to_json() for rec in records]
                return dumps(login_rec, default=json_date_serializer)
        except Exception as e:
            print(e)
            return dumps({}) 
    return run(show_complete_login_task(username))

def json_date_serializer(obj):
    if isinstance(obj, date):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))