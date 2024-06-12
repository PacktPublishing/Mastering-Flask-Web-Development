
from typing import Dict, Any

from sqlalchemy import update, delete, insert
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from app.model.db import Login


class LoginRepository: 
    
    def __init__(self, sess:Session):
        self.sess:Session = sess
    
    async def insert_login(self, login: Login) -> bool: 
        try:
            sql = insert(Login).values(username=login.username, password=login.password)
            #sql.execution_options(synchronize_session="fetch")
            await self.sess.execute(sql)
            await self.sess.commit()
            await self.sess.close()
            return True
            #self.sess.add(attendance)
            #await self.sess.flush()
        except Exception as e: 
            print(e)
        return False
    
    async def update_login(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
           sql = update(Login).where(Login.id == id).values(**details)
          
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
       except Exception as e: 
           print(e)
       return False
   
    async def delete_login(self, id:int) -> bool: 
        try:
           sql = delete(Login).where(Login.id == id)
           sql.execution_options(synchronize_session="fetch")
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
        except Exception as e: 
            print(e)
        return False
    
    async def select_all_login(self):
        sql = select(Login)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        records = q.scalars().all()
        await self.sess.close()
        return records
    
    async def select_login(self, id:int): 
        sql = select(Login).where(Login.id == id)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        record = q.scalars().all()
        await self.sess.close()
        return record
