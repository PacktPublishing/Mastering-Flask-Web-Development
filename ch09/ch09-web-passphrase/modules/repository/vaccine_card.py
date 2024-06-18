
from typing import Dict, Any

from sqlalchemy import update, delete, insert
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from modules.models.db import VaccineCard
from datetime import datetime

class VacCardRepository: 
    
    def __init__(self, sess:Session):
        self.sess:Session = sess
    
    async def insert_vaccard(self, card: VaccineCard) -> bool: 
        try:  
            self.sess.add(card)
            await self.sess.flush()
            await self.sess.commit()
            await self.sess.close()
            return True
            
        except Exception as e: 
            print(e)
        return False
    
    async def update_vaccard(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
           sql = update(VaccineCard).where(VaccineCard.id == id).values(**details)
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
       except Exception as e: 
           print(e)
       return False
   
    async def delete_vaccard_cardid(self, cardid:str) -> bool: 
        try:
           sql = delete(VaccineCard).where(VaccineCard.cardid == cardid)
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
        except Exception as e: 
            print(e)
        return False
    
    async def delete_vaccard(self, id:int) -> bool: 
        try:
           sql = delete(VaccineCard).where(VaccineCard.id == id)
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
        except Exception as e: 
            print(e)
        return False
        
    async def select_all_vaccard(self):
        sql = select(VaccineCard)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        records = q.scalars().all()
        await self.sess.close()
        return records
    
    async def select_vaccard_cardid(self, cardid:str): 
        sql = select(VaccineCard).where(VaccineCard.cardid == cardid)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        record = q.scalars().all()
        await self.sess.close()
        return record
    
    async def select_vaccard(self, id:int): 
        sql = select(VaccineCard).where(VaccineCard.id == id)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        record = q.scalars().all()
        await self.sess.close()
        return record