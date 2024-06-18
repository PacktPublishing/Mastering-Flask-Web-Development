
from typing import Dict, Any

from sqlalchemy import update, delete, insert
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from modules.models.db import Inventory
from datetime import datetime

class InventoryRepository: 
    
    def __init__(self, sess:Session):
        self.sess:Session = sess
    
    async def insert_inventory(self, inventory: Inventory) -> bool: 
        try:  
            self.sess.add(inventory)
            await self.sess.flush()
            await self.sess.commit()
            await self.sess.close()
            return True
            
        except Exception as e: 
            print(e)
        return False
    
    async def update_inventory(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
           sql = update(Inventory).where(Inventory.id == id).values(**details)
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
       except Exception as e: 
           print(e)
       return False
   
    async def delete_inventory(self, id:int) -> bool: 
        try:
           sql = delete(Inventory).where(Inventory.id == id)
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
        except Exception as e: 
            print(e)
        return False
     
    
    async def select_all_inventory(self):
        sql = select(Inventory)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        records = q.scalars().all()
        await self.sess.close()
        return records
    
    async def select_inventory(self, id:int): 
        sql = select(Inventory).where(Inventory.id == id)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        record = q.scalars().all()
        await self.sess.close()
        return record
    
    