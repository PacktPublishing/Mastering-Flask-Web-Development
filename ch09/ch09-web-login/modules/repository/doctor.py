
from typing import Dict, Any
from sqlalchemy import update, delete, insert
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from modules.models.db import Doctor

class DoctorRepository: 
    
    def __init__(self, sess:Session):
        self.sess:Session = sess
    
    async def insert_doctor(self, doc: Doctor) -> bool: 
        try:
            
            sql = insert(Doctor).values(docid=doc.docid, username=doc.username, firstname=doc.firstname, midname=doc.midname, lastname=doc.lastname, 
                                        age=doc.age, gender=doc.gender, email=doc.email, mobile=doc.mobile, status=doc.status, vaccenterid=doc.vaccenterid)
            await self.sess.execute(sql)
            await self.sess.commit()
            await self.sess.close()
            return True
            #self.sess.add(attendance)
            #await self.sess.flush()
        except Exception as e: 
            print(e)
        return False
    
    async def update_doc(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
           sql = update(Doctor).where(Doctor.id == id).values(**details)
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
       except Exception as e: 
           print(e)
       return False
   
    async def delete_doc(self, id:int) -> bool: 
        try:
           sql = delete(Doctor).where(Doctor.id == id)
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
        except Exception as e: 
            print(e)
        return False
    
    async def delete_doc_username(self, username:str) -> bool: 
        try:
           sql = delete(Doctor).where(Doctor.username == username)
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
        except Exception as e: 
            print(e)
        return False
    
    async def select_all_doc(self):
        sql = select(Doctor)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        records = q.scalars().all()
        await self.sess.close()
        return records
    
    async def select_doc(self, id:int): 
        sql = select(Doctor).where(Doctor.id == id)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        record = q.scalars().all()
        await self.sess.close()
        return record
    
    async def select_doc_username(self, username:str): 
        sql = select(Doctor).where(Doctor.username == username)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        record = q.scalars().all()
        await self.sess.close()
        return record