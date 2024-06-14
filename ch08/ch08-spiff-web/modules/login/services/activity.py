from modules.login.repository.login import LoginRepository
from modules.admin.repository.admin import AdminRepository
from modules.doctors.repository.doctor import DoctorRepository
from modules.patient.repository.patient import PatientRepository
from modules.models.config import db_session
from modules.models.db import Login

async def is_valid_user(username:str, password:str) -> bool:
    async with db_session() as sess:
        async with sess.begin(): 
            repo = LoginRepository(sess)
            login_rec = await repo.select_login_username(username)
            login_json = [rec.to_json() for rec in login_rec]
            if not len(login_json) == 0:
                if username == login_json[0]['username'] and password == login_json[0]['password']:
                    return True
                else:
                    return False
            else:
                return False

async def verify_admin_role(username:str) -> int:
    async with db_session() as sess:
        async with sess.begin(): 
            repo_admin = AdminRepository(sess)
            record_admin = await repo_admin.select_admin_username(username) 
            if not len(record_admin) == 0:
                admin_json = [rec.to_json() for rec in record_admin]
                return admin_json[0]['role']
            else:
                return -1
            
async def verify_doc_role(username:str) -> int:
    async with db_session() as sess:
        async with sess.begin(): 
            repo_doc = DoctorRepository(sess)
            record_doc = await repo_doc.select_doc_username(username) 
            if not len(record_doc) == 0:
                doc_json = [rec.to_json() for rec in record_doc]
                return doc_json[0]['role']
            else:
                return -1

async def verify_patient_role(username:str) -> int:
    async with db_session() as sess:
        async with sess.begin(): 
            repo_patient = PatientRepository(sess)
            record_patient = await repo_patient.select_patient_username(username) 
            if not len(record_patient) == 0:
                patient_json = [rec.to_json() for rec in record_patient]
                return patient_json[0]['role']
            else:
                return -1