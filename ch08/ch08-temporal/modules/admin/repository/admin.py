
from typing import Dict, Any

from sqlalchemy import update, delete, insert
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from modules.models.db import Administrator
from datetime import datetime

class AdminRepository: 
    
    def __init__(self, sess:Session):
        self.sess:Session = sess
    
    async def insert_admin(self, admin: Administrator) -> bool: 
        try:
            
            sql = insert(Administrator).values(empid=admin.empid, username=admin.username, role=admin.role, firstname=admin.firstname, midname=admin.midname, lastname=admin.lastname, 
                                               email=admin.email, mobile=admin.mobile, position=admin.position, status=admin.status, date_started=datetime.strptime(admin.date_started, '%Y-%m-%d').date())
            await self.sess.execute(sql)
            await self.sess.commit()
            await self.sess.close()
            return True
            #self.sess.add(attendance)
            #await self.sess.flush()
        except Exception as e: 
            print(e)
        return False
    
    async def update_admin(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
           sql = update(Administrator).where(Administrator.id == id).values(**details)
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
       except Exception as e: 
           print(e)
       return False
   
    async def delete_admin(self, id:int) -> bool: 
        try:
           sql = delete(Administrator).where(Administrator.id == id)
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
        except Exception as e: 
            print(e)
        return False
    
    async def select_all_admin(self):
        sql = select(Administrator)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        records = q.scalars().all()
        await self.sess.close()
        return records
    
    async def select_admin(self, id:int): 
        sql = select(Administrator).where(Administrator.id == id)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        record = q.scalars().all()
        await self.sess.close()
        return record
    
