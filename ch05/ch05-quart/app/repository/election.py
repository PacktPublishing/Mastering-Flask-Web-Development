
from typing import Dict, Any

from sqlalchemy import update, delete, insert
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from app.model.db import Election
from datetime import datetime

class ElectionRepository: 
    
    def __init__(self, sess:Session):
        self.sess:Session = sess
    
    async def insert(self, election: Election) -> bool: 
        try:
            sql = insert(Election).values(election_date=datetime.strptime(election.election_date, '%Y-%m-%d').date(), status=election.status, 
                                       total_voters=election.total_voters)
            await self.sess.execute(sql)
            await self.sess.commit()
            await self.sess.close()
            return True
            #self.sess.add(attendance)
            #await self.sess.flush()
        except Exception as e: 
            print(e)
        return False
    
    async def update(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
           sql = update(Election).where(Election.id == id).values(**details)
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
       except Exception as e: 
           print(e)
       return False
   
    async def delete(self, id:int) -> bool: 
        try:
           sql = delete(Election).where(Election.id == id)
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
        except Exception as e: 
            print(e)
        return False
    
    async def select_all_election(self):
        sql = select(Election)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        records = q.scalars().all()
        await self.sess.close()
        return records
    
    async def select_election(self, id:int): 
        sql = select(Election).where(Election.id == id)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        record = q.scalars().all()
        await self.sess.close()
        return record
    
