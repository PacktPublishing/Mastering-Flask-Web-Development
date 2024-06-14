
from typing import Dict, Any

from sqlalchemy import update, delete, insert
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from modules.models.db import Appointment
from datetime import datetime
import time

class AppointmentRepository: 
    
    def __init__(self, sess:Session):
        self.sess:Session = sess
    
    async def insert_appt(self, appt: Appointment) -> bool: 
        try:
            
            sql = insert(Appointment).values(ticketid= appt.ticketid, patientid=appt.patientid, docid=appt.docid, priority_level=appt.priority_level, date_scheduled=datetime.strptime(appt.date_scheduled, '%Y-%m-%d').date(), time_scheduled=datetime.strptime(appt.time_scheduled, '%H:%M'),
                                             consult_hrs=appt.consult_hrs)
            await self.sess.execute(sql)
            await self.sess.commit()
            await self.sess.close()
            return True
            #self.sess.add(attendance)
            #await self.sess.flush()
        except Exception as e: 
            print(e)
        return False
    
    async def update_appt(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
           sql = update(Appointment).where(Appointment.id == id).values(**details)
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
       except Exception as e: 
           print(e)
       return False
   
    async def delete_appt(self, id:int) -> bool: 
        try:
           sql = delete(Appointment).where(Appointment.id == id)
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
        except Exception as e: 
            print(e)
        return False
    
    async def delete_appt_ticket(self, tid:int) -> bool: 
        try:
           sql = delete(Appointment).where(Appointment.ticketid == tid)
           await self.sess.execute(sql)
           await self.sess.commit()
           await self.sess.close()
           return True
        except Exception as e: 
            print(e)
        return False
    
    async def select_all_appt(self):
        sql = select(Appointment)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        records = q.scalars().all()
        await self.sess.close()
        return records
    
    async def select_appt(self, id:int): 
        sql = select(Appointment).where(Appointment.id == id)
        sql.execution_options(synchronize_session="fetch")
        q = await self.sess.execute(sql)
        record = q.scalars().all()
        await self.sess.close()
        return record
    
