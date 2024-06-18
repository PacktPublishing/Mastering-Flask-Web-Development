
from typing import Dict, Any

from sqlalchemy import update, delete, insert
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from modules.models.db import VacRegistration
from datetime import datetime

class VacRegistrationRepository: 
    
    def __init__(self, sess:Session):
        self.sess:Session = sess
    
    async def insert_vacreg(self, vacreg: VacRegistration) -> bool: 
        try:  
            self.sess.add(vacreg)
            await self.sess.flush()
            await self.sess.commit()
            await self.sess.close()
            return True
            
        except Exception as e: 
            print(e)
        return False
    
    async def update_vacreg(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
           sql = update(VacRegistration).where(VacRegistration.id == id).values(**details)
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
       except Exception as e: 
           print(e)
       return False
   
    async def delete_vacreg(self, id:int) -> bool: 
        try:
           sql = delete(VacRegistration).where(VacRegistration.id == id)
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
        except Exception as e: 
            print(e)
        return False
    
    async def delete_vacreg_code(self, regcode:str) -> bool: 
        try:
           sql = delete(VacRegistration).where(VacRegistration.regcode == regcode)
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
        except Exception as e: 
            print(e)
        return False
    
    
    async def select_all_vacreg(self):
        sql = select(VacRegistration)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        records = q.scalars().all()
        await self.sess.close()
        return records
    
    async def select_vacreg(self, id:int): 
        sql = select(VacRegistration).where(VacRegistration.id == id)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        record = q.scalars().all()
        await self.sess.close()
        return record
    
    async def select_vacreg_regcode(self, regcode:str): 
        sql = select(VacRegistration).where(VacRegistration.regcode == regcode)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        record = q.scalars().all()
        await self.sess.close()
        return record