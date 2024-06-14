from temporalio import activity

from modules.models.workflow import AppointmentWf
from modules.models.db import Appointment
from modules.admin.repository.appointment import AppointmentRepository
from modules.models.config import db_session
from datetime import datetime
import time

    
@activity.defn
async def reserve_schedule(appointmentwf: AppointmentWf) -> str:
    try:
        async with db_session() as sess:
              async with sess.begin(): 
                repo = AppointmentRepository(sess)
                appt = Appointment(ticketid = appointmentwf.ticketid, patientid = appointmentwf.patientid,
                                   docid = appointmentwf.docid, priority_level = appointmentwf.priority_level,
                                  date_scheduled = appointmentwf.date_scheduled,
                                  time_scheduled = appointmentwf.time_scheduled,
                                    consult_hrs = 0.0                )

                result = await repo.insert_appt(appt)
                if result == False:
                    print(f"Appointment by {appointmentwf.patientid} for {appointmentwf.docid} on {appointmentwf.date_scheduled} at {appointmentwf.time_scheduled} not successful.")
                    return "failure"
                print(f"Appointment by {appointmentwf.patientid} for {appointmentwf.docid}  with {appointmentwf.ticketid} and message priority {appointmentwf.priority_level} on {appointmentwf.date_scheduled} at {appointmentwf.time_scheduled} is successfully reserved.")
                return "success"
    except Exception as e:
        print(e)
    print(f"Appointment by {appointmentwf.patientid} for {appointmentwf.docid} on {appointmentwf.date_scheduled} at {appointmentwf.time_scheduled} not successful.")
    return "failure"
    

@activity.defn
async def close_schedule(appointmentwf: AppointmentWf) -> str:
    try:
        async with db_session() as sess:
              async with sess.begin(): 
                repo = AppointmentRepository(sess)
                result = await repo.delete_appt_ticket(appointmentwf.ticketid)
                if result == False:
                    print(f"Appointment by {appointmentwf.patientid} for {appointmentwf.docid} on {appointmentwf.date_scheduled} at {appointmentwf.time_scheduled} not closed yet.")
                    return "failure"
                print(f"Appointment reserved by {appointmentwf.patientid} for {appointmentwf.docid}  with {appointmentwf.ticketid} and message priority {appointmentwf.priority_level} on: {appointmentwf.date_scheduled} at {appointmentwf.time_scheduled} is successfully closed.")
                return "success"
    except Exception as e:
        print(e)
    print(f"Appointment by {appointmentwf.patientid} for {appointmentwf.docid} on {appointmentwf.date_scheduled} at {appointmentwf.time_scheduled} not closed yet.")
    return "failure"