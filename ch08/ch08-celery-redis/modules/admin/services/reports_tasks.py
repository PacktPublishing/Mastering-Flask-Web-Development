from celery import shared_task
from asyncio import run
from datetime import date

from modules.admin.repository.admin import AdminRepository
from modules.patient.repository.patient import PatientRepository
from modules.doctor.repository.doctor import DoctorRepository
from modules.models.config import db_session


@shared_task(ignore_result=False)
def generate_csv_doctor_task_wrapper(filename:str):
    async def generate_csv_doctor_task(filename:str):
        async with db_session() as sess:
          async with sess.begin(): 
            repo = DoctorRepository(sess)
            records = await repo.select_all_doc()
            doc_rec = [rec.to_json() for rec in records]
            with open(filename, 'w') as f:
                # Write all the dictionary keys in a file with commas separated.
                f.write(','.join(doc_rec[0].keys()))
                f.write('\n') # Add a new line
                for row in doc_rec:
                    # Write the values in a row.
                    f.write(','.join(str(x) for x in row.values()))
                    f.write('\n') # Add a new line
    return run(generate_csv_doctor_task(filename))

@shared_task(ignore_result=False)
def generate_csv_patient_task_wrapper(filename:str):
    async def generate_csv_patient_task(filename:str):
        async with db_session() as sess:
          async with sess.begin(): 
            repo = PatientRepository(sess)
            records = await repo.select_all_patient()
            patient_rec = [rec.to_json() for rec in records]
            with open(filename, 'w') as f:
                # Write all the dictionary keys in a file with commas separated.
                f.write(','.join(patient_rec[0].keys()))
                f.write('\n') # Add a new line
                for row in patient_rec:
                    # Write the values in a row.
                    f.write(','.join(str(x) for x in row.values()))
                    f.write('\n') # Add a new line
    return run(generate_csv_patient_task(filename))


@shared_task(ignore_result=False)
def generate_csv_admin_task_wrapper(filename:str):
    async def generate_csv_admin_task(filename:str):
        async with db_session() as sess:
          async with sess.begin(): 
            repo = AdminRepository(sess)
            records = await repo.select_all_admin()
            admin_rec = [rec.to_json() for rec in records]
            with open(filename, 'w') as f:
                # Write all the dictionary keys in a file with commas separated.
                f.write(','.join(admin_rec[0].keys()))
                f.write('\n') # Add a new line
                for row in admin_rec:
                    # Write the values in a row.
                    f.write(','.join(str(x) for x in row.values()))
                    f.write('\n') # Add a new line
    return run(generate_csv_admin_task(filename))

def json_date_serializer(obj):
    if isinstance(obj, date):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))