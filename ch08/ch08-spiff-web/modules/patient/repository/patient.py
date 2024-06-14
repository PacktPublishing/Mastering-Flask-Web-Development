
from typing import Dict, Any

from sqlalchemy import update, delete, insert
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from modules.models.db import Patient
from datetime import datetime

class PatientRepository: 
    
    def __init__(self, sess:Session):
        self.sess:Session = sess
    
    async def insert_patient(self, patient: Patient) -> bool: 
        try:
            
            sql = insert(Patient).values(patientid=patient.patientid, username=patient.username, role=patient.role, firstname=patient.firstname, midname=patient.midname, lastname=patient.lastname, 
                                        birthday=datetime.strptime(patient.birthday, '%Y-%m-%d').date(), age=patient.age, profession=patient.profession, address=patient.address, email=patient.email, mobile=patient.mobile, date_registered=datetime.strptime(patient.date_registered, '%Y-%m-%d').date())
            await self.sess.execute(sql)
            await self.sess.commit()
            await self.sess.close()
            return True
            #self.sess.add(attendance)
            #await self.sess.flush()
        except Exception as e: 
            print(e)
        return False
    
    async def update_patient(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
           sql = update(Patient).where(Patient.id == id).values(**details)
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
       except Exception as e: 
           print(e)
       return False
   
    async def delete_patient(self, id:int) -> bool: 
        try:
           sql = delete(Patient).where(Patient.id == id)
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
        except Exception as e: 
            print(e)
        return False
    
    async def select_all_patient(self):
        sql = select(Patient)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        records = q.scalars().all()
        await self.sess.close()
        return records
    
       
    async def select_patient(self, id:int): 
        sql = select(Patient).where(Patient.id == id)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        record = q.scalars().all()
        await self.sess.close()
        return record
    
    async def select_patient_username(self, username:str): 
        sql = select(Patient).where(Patient.username == username)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        record = q.scalars().all()
        await self.sess.close()
        return record
    
