
from typing import Dict, Any

from sqlalchemy import update, delete, insert
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from modules.models.db import VacCenter
from datetime import datetime

class VacCenterRepository: 
    
    def __init__(self, sess:Session):
        self.sess:Session = sess
    
    async def insert_vaccenter(self, vaccenter: VacCenter) -> bool: 
        try:  
            self.sess.add(vaccenter)
            await self.sess.flush()
            await self.sess.commit()
            await self.sess.close()
            return True
            
        except Exception as e: 
            print(e)
        return False
    
    async def update_vaccenter(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
           sql = update(VacCenter).where(VacCenter.id == id).values(**details)
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
       except Exception as e: 
           print(e)
       return False
   
    async def delete_vaccenter_vcenterid(self, vaccenterid:str) -> bool: 
        try:
           sql = delete(VacCenter).where(VacCenter.vaccenterid == vaccenterid)
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
        except Exception as e: 
            print(e)
        return False
    
    async def delete_vaccenter(self, id:int) -> bool: 
        try:
           sql = delete(VacCenter).where(VacCenter.id == id)
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
        except Exception as e: 
            print(e)
        return False
        
    async def select_all_vaccenter(self):
        sql = select(VacCenter)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        records = q.scalars().all()
        await self.sess.close()
        return records
    
    async def select_vaccenter_vcenterid(self, vaccenterid:str): 
        sql = select(VacCenter).where(VacCenter.vaccenterid == vaccenterid)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        record = q.scalars().all()
        await self.sess.close()
        return record
    
    async def select_vaccine(self, id:int): 
        sql = select(VacCenter).where(VacCenter.id == id)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        record = q.scalars().all()
        await self.sess.close()
        return record