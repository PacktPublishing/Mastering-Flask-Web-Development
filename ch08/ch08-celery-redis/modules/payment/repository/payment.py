
from typing import Dict, Any

from sqlalchemy import update, delete, insert
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from modules.models.db import Payment
from datetime import datetime

class PaymentRepository: 
    
    def __init__(self, sess:Session):
        self.sess:Session = sess
    
    async def insert_payment(self, payment: Payment) -> bool: 
        try:
            
            sql = insert(Payment).values(paymentid=payment.paymentid, patientid=payment.patientid, amount=payment.amount, discount=payment.discount, status=payment.status, date_released=datetime.strptime(payment.date_released, '%Y-%m-%d').date())
            await self.sess.execute(sql)
            await self.sess.commit()
            await self.sess.close()
            return True
            #self.sess.add(attendance)
            #await self.sess.flush()
        except Exception as e: 
            print(e)
        return False
    
    async def update_payment(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
           sql = update(Payment).where(Payment.id == id).values(**details)
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
       except Exception as e: 
           print(e)
       return False
   
    async def delete_payment(self, id:int) -> bool: 
        try:
           sql = delete(Payment).where(Payment.id == id)
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
        except Exception as e: 
            print(e)
        return False
    
    async def select_all_payment(self):
        sql = select(Payment)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        records = q.scalars().all()
        await self.sess.close()
        return records
    
    async def select_payment(self, id:int): 
        sql = select(Payment).where(Payment.id == id)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        record = q.scalars().all()
        await self.sess.close()
        return record
    
