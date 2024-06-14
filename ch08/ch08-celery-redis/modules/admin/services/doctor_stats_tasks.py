from celery import shared_task
from json import loads, dumps
from asyncio import run
from typing import List, Any

from modules.admin.repository.appointment import AppointmentRepository
from modules.admin.repository.request import RequestRepository

from modules.models.config import db_session


@shared_task(ignore_result=False)
def count_patients_doctor_task_wrapper(docid:str):
    async def count_patients_doctor_task(docid:str):
        async with db_session() as sess:
          async with sess.begin(): 
            repo = AppointmentRepository(sess)
            records = await repo.select_all_appt_doc(docid)
            patient_rec = [rec.to_json() for rec in records]
            count_patients = len(patient_rec)
        return count_patients
    return run(count_patients_doctor_task(docid))


@shared_task(ignore_result=False)
def count_request_doctor_task_wrapper(docid:str):
    async def ount_request_doctor_task(docid:str):
        async with db_session() as sess:
          async with sess.begin(): 
            repo = RequestRepository(sess)
            records = await repo.select_all_request_doc(docid)
            request_rec = [rec.to_json() for rec in records]
            count_request = len(request_rec)
        return count_request
    return run(ount_request_doctor_task(docid))


@shared_task(ignore_result=False)
def create_doctor_stats_task_wrapper(details:List[Any], docid:str):
    async def ount_request_doctor_task(details:List[Any]):
        return f"Doctor {docid} has {details[0]} patients and {details[1]} lab requests."
    return run(ount_request_doctor_task(details))