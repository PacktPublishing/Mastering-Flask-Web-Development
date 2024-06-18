
from typing import Dict, Any

from sqlalchemy import update, delete, insert
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from modules.models.db import Vaccine
from datetime import datetime

class VaccineRepository: 
    
    def __init__(self, sess:Session):
        self.sess:Session = sess
    
    async def insert_vaccine(self, vac: Vaccine) -> bool: 
        try:
            
            sql = insert(Vaccine).values(vacid=vac.vacid, vacname=vac.vacname, vacdesc=vac.vacdesc, qty=vac.qty, price=vac.price, 
                                               status=vac.status)
            await self.sess.execute(sql)
            await self.sess.commit()
            await self.sess.close()
            return True
            #self.sess.add(attendance)
            #await self.sess.flush()
        except Exception as e: 
            print(e)
        return False
    
    async def update_vaccine(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
           sql = update(Vaccine).where(Vaccine.id == id).values(**details)
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
       except Exception as e: 
           print(e)
       return False
   
    async def delete_vaccine(self, id:int) -> bool: 
        try:
           sql = delete(Vaccine).where(Vaccine.id == id)
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
        except Exception as e: 
            print(e)
        return False
    
    async def delete_vaccine_vacid(self, vacid:str) -> bool: 
        try:
           sql = delete(Vaccine).where(Vaccine.vacid == vacid)
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
        except Exception as e: 
            print(e)
        return False
        
    async def select_all_vaccine(self):
        sql = select(Vaccine)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        records = q.scalars().all()
        await self.sess.close()
        return records
    
    async def select_vaccine(self, id:int): 
        sql = select(Vaccine).where(Vaccine.id == id)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        record = q.scalars().all()
        await self.sess.close()
        return record
    
    async def select_vaccine_vacid(self, vacid:str): 
        sql = select(Vaccine).where(Vaccine.vacid == vacid)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        record = q.scalars().all()
        await self.sess.close()
        return record