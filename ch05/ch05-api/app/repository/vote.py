
from typing import Dict, Any

from sqlalchemy import update, delete, insert
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from app.model.db import Vote
from datetime import datetime
from sqlalchemy import func

class VoteRepository: 
    
    def __init__(self, sess:Session):
        self.sess:Session = sess
    
    async def insert(self, vote: Vote) -> bool: 
        try:
            sql = insert(Vote).values(voter_id=vote.voter_id, election_id=vote.election_id, cand_id=vote.cand_id,
                                      vote_time=datetime.strptime(vote.vote_time, '%H:%M:%S').time())
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
           sql = update(Vote).where(Vote.id == id).values(**details)
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
       except Exception as e: 
           print(e)
       return False
   
    async def delete(self, id:int) -> bool: 
        try:
           sql = delete(Vote).where(Vote.id == id)
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
        except Exception as e: 
            print(e)
        return False
    
    async def select_all_vote(self):
        sql = select(Vote)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        records = q.scalars().all()
        await self.sess.close()
        return records
    
    async def select_vote(self, id:int): 
        sql = select(Vote).where(Vote.id == id)
        q = await self.sess.execute(sql)
        record = q.scalars().all()
        await self.sess.close()
        return record
    
    async def count_votes_by_candidate(self, cand_id:str, election_id:int):
        sql = select(func.count()).where(Vote.cand_id == cand_id, Vote.election_id == election_id)
        q = await self.sess.execute(sql)
        count = q.scalar_one()
        await self.sess.close()
        return count
