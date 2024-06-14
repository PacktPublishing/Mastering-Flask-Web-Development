
from typing import Dict, Any

from sqlalchemy import update, delete, insert
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from modules.models.db import Request
from datetime import datetime
import time

class RequestRepository: 
    
    def __init__(self, sess:Session):
        self.sess:Session = sess
    
    async def insert_request(self, req: Request) -> bool: 
        try:
            
            sql = insert(Request).values(docid=req.docid, adminid=req.adminid, details=req.details, status=req.status, date_approved=datetime.strptime(req.date_approved, '%Y-%m-%d').date())
            await self.sess.execute(sql)
            await self.sess.commit()
            await self.sess.close()
            return True
            #self.sess.add(attendance)
            #await self.sess.flush()
        except Exception as e: 
            print(e)
        return False
    
    async def update_request(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
           sql = update(Request).where(Request.id == id).values(**details)
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
       except Exception as e: 
           print(e)
       return False
   
    async def delete_request(self, id:int) -> bool: 
        try:
           sql = delete(Request).where(Request.id == id)
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
        except Exception as e: 
            print(e)
        return False
    
    async def select_all_request(self):
        sql = select(Request)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        records = q.scalars().all()
        await self.sess.close()
        return records
    
    async def select_request(self, id:int): 
        sql = select(Request).where(Request.id == id)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        record = q.scalars().all()
        await self.sess.close()
        return record
    
