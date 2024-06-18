
from typing import Dict, Any

from sqlalchemy import update, delete, insert, and_, or_
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from modules.models.db import Token
from datetime import datetime
from werkzeug.security import gen_salt

class TokenRepository: 
    
    def __init__(self, sess:Session):
        self.sess:Session = sess
    
    async def insert_token(self, token: Token) -> bool: 
        try:
            sql = insert(Token).values(user_id=token.user_id, client_id=token.client_id, token_type=token.token_type, access_token=token.access_token, 
                                       refresh_token=token.refresh_token, expires_in=token.expires_in, scope=token.scope, issued_at=token.issued_at,
                                       access_token_revoked_at=token.access_token_revoked_at, refresh_token_revoked_at=token.refresh_token_revoked_at)
            await self.sess.execute(sql)
            await self.sess.commit()
            await self.sess.close()
            return True
            #self.sess.add(attendance)
            #await self.sess.flush()
        except Exception as e: 
            print(e)
        return False
    
    async def delete_token(self, client_id:str) -> bool: 
        try:
           sql = delete(Token).where(Token.client_id == client_id)
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
        except Exception as e: 
            print(e)
        return False
    
    async def select_all_client(self):
        sql = select(Token)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        records = q.scalars().all()
        await self.sess.close()
        return records
    
    async def select_token_access(self, access_token:str): 
        sql = select(Token).where(Token.access_token == access_token)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        record = q.scalars().all()
        await self.sess.close()
        return record
    
    