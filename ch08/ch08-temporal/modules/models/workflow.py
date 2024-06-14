from dataclasses import dataclass, field
from datetime import date, time, datetime

appt_queue_id = "dams_appointment_queue"


@dataclass
class WorkflowOptions:
    email: str


@dataclass
class EmailDetails:
    email: str = ""
    message: str = ""
    subscribed:bool= False
    count:int = 0
    
@dataclass   
class ReqAppointment:
    ticketid:str
    patientid:int
    docid:str
    priority_level: int
    date_scheduled:str 
    time_scheduled:str 
    consult_hrs:float

@dataclass
class AppointmentWf:
    ticketid:str = ""
    patientid:int = 0
    docid:str = ""
    #date_scheduled:date = field(default_factory=date.today())
    #time_scheduled:time = field(default_factory=datetime.time(datetime.now()))
    date_scheduled:str = ""
    time_scheduled:str = ""
    priority_level:int = 0
    status:bool = False
    remarks:str = ""
    