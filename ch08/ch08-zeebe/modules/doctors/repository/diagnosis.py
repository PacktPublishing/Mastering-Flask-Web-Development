
from typing import Dict, Any

from sqlalchemy import update, delete, insert
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from modules.models.db import Diagnosis
from datetime import datetime

class DiagnosisRepository: 
    
    def __init__(self, sess:Session):
        self.sess:Session = sess
    
    async def insert_diag(self, diag: Diagnosis) -> bool: 
        try:
            
            sql = insert(Diagnosis).values(docid=diag.docid, patientid=diag.patientid, narrative=diag.narrative, resolution=diag.resolution, date_submitted=datetime.strptime(diag.date_submitted, '%Y-%m-%d').date())
            await self.sess.execute(sql)
            await self.sess.commit()
            await self.sess.close()
            return True
            #self.sess.add(attendance)
            #await self.sess.flush()
        except Exception as e: 
            print(e)
        return False
    
    async def update_diag(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
           sql = update(Diagnosis).where(Diagnosis.id == id).values(**details)
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
       except Exception as e: 
           print(e)
       return False
   
    async def delete_diag(self, id:int) -> bool: 
        try:
           sql = delete(Diagnosis).where(Diagnosis.id == id)
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
        except Exception as e: 
            print(e)
        return False
    
    async def select_all_diag(self):
        sql = select(Diagnosis)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        records = q.scalars().all()
        await self.sess.close()
        return records
    
    async def select_diag(self, id:int): 
        sql = select(Diagnosis).where(Diagnosis.id == id)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        record = q.scalars().all()
        await self.sess.close()
        return record
    
    async def select_diag_doc_patient(self, docid:str, patientid:int): 
        sql = select(Diagnosis).where(Diagnosis.docid == docid)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        record = q.scalars().all()
        await self.sess.close()
        return record
    
