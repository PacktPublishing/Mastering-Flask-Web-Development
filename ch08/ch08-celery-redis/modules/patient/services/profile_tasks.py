from celery import shared_task
from modules.patient.repository.patient import PatientRepository
from modules.models.config import db_session
from modules.models.db import Patient
from json import loads, dumps
from asyncio import run
from datetime import date


@shared_task(ignore_result=False)
def add_patient_task_wrapper(details):
    async def add_patient_task(details):
        try:
            async with db_session() as sess:
              async with sess.begin(): 
                repo = PatientRepository(sess)
                details_dict = loads(details)
                print(details_dict)
                patient = Patient(**details_dict)
                result = await repo.insert_patient(patient)
                if result:
                    return str(True)
                else:
                    return str(False)
        except Exception as e:
            print(e)
            return str(False)
    return run(add_patient_task(details))

@shared_task(ignore_result=False)
def list_all_patient_task_wrapper():
    async def list_all_patient_task():
      async with db_session() as sess:
        async with sess.begin(): 
            repo = PatientRepository(sess)
            records = await repo.select_all_patient()
            doc_rec = [rec.to_json() for rec in records]
            return dumps(doc_rec, default=json_date_serializer)
    return run(list_all_patient_task())

def json_date_serializer(obj):
    if isinstance(obj, date):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))
