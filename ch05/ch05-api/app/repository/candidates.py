
from typing import Dict, Any

from sqlalchemy import update, delete, insert
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from app.model.db import Candidate
from datetime import datetime

class CandidateRepository: 
    
    def __init__(self, sess:Session):
        self.sess:Session = sess
    
    async def insert_candidate(self, candidate: Candidate) -> bool: 
        try:
            sql = insert(Candidate).values(elect_id=candidate.elect_id, cand_id=candidate.cand_id, 
                                           firstname=candidate.firstname, lastname=candidate.lastname, middlename=candidate.middlename,
                                           address=candidate.address, tel=candidate.tel, position=candidate.position,
                                           party=candidate.party, filing_date=datetime.strptime(candidate.filing_date, '%Y-%m-%d').date())
            await self.sess.execute(sql)
            await self.sess.commit()
            await self.sess.close()
            return True
            #self.sess.add(attendance)
            #await self.sess.flush()
        except Exception as e: 
            print(e)
        return False
    
    async def update_candidate(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
           sql = update(Candidate).where(Candidate.id == id).values(**details)
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
       except Exception as e: 
           print(e)
       return False
   
    async def delete_candidate(self, id:int) -> bool: 
        try:
           sql = delete(Candidate).where(Candidate.id == id)
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
        except Exception as e: 
            print(e)
        return False
    
    async def select_all_candidate(self):
        sql = select(Candidate)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        records = q.scalars().all()
        await self.sess.close()
        return records
    
    async def select_candidate(self, id:int): 
        sql = select(Candidate).where(Candidate.id == id)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        record = q.scalars().all()
        await self.sess.close()
        return record
    
