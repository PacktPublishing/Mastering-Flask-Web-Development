
from typing import Dict, Any

from sqlalchemy import update, delete, insert, and_, or_
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from modules.models.db import Client
from datetime import datetime
from werkzeug.security import gen_salt

class ClientRepository: 
    
    def __init__(self, sess:Session):
        self.sess:Session = sess
    
    async def insert_client(self, client: Client) -> bool: 
        try:
            #sql = insert(Client).values(user_id=client.user_id, client_id=client.client_id, client_secret=client.client_secret, client_id_issued_at=client.client_id_issued_at)
            #await self.sess.execute(sql)
            #await self.sess.commit()
            #await self.sess.close()
            
            await self.sess.add(client)
            await self.sess.flush()
            await self.sess.commit()
            await self.sess.close()
            return True
        except Exception as e: 
            print(e)
        return False
    
    
    async def delete_client(self, client_id:str) -> bool: 
        try:
           sql = delete(Client).where(Client.client_id == client_id)
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
        except Exception as e: 
            print(e)
        return False
    
    
    
    async def select_all_client(self):
        sql = select(Client)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        records = q.scalars().all()
        await self.sess.close()
        return records
    
    async def select_client(self, client_id:str): 
        sql = select(Client).where(Client.client_id == client_id)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        record = q.scalars().all()
        await self.sess.close()
        return record
    
    async def select_client_user(self, user_id:str): 
        sql = select(Client).where(Client.user_id == user_id)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        record = q.scalars().all()
        await self.sess.close()
        return record
    