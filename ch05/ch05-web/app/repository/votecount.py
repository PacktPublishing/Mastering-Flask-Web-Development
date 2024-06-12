
from typing import Dict, Any

from sqlalchemy import update, delete, insert
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from app.model.db import VoteCount
from datetime import datetime

class VoteCountRepository: 
    
    def __init__(self, sess:Session):
        self.sess:Session = sess
    
    async def insert(self, vote_count: VoteCount) -> bool: 
        try:
            sql = insert(VoteCount).values(election_id=int(vote_count.election_id), precinct=vote_count.precinct, 
                                           final_tally=int(vote_count.final_tally), approved_date=datetime.strptime(vote_count.approved_date, '%Y-%m-%d').date())
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
           sql = update(VoteCount).where(VoteCount.id == id).values(**details)
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
       except Exception as e: 
           print(e)
       return False
   
    async def delete(self, id:int) -> bool: 
        try:
           sql = delete(VoteCount).where(VoteCount.id == id)
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
        except Exception as e: 
            print(e)
        return False
    
    async def select_all_votecount(self):
        sql = select(VoteCount)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        records = q.scalars().all()
        await self.sess.close()
        return records
    
    async def select_votecount(self, id:int): 
        sql = select(VoteCount).where(VoteCount.id == id)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        record = q.scalars().all()
        await self.sess.close()
        return record
