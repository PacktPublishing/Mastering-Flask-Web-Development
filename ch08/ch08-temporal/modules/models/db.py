
from sqlalchemy import  Column, ForeignKey, Integer, String, Date, Time, Sequence, Boolean, Float, Text, Double
from sqlalchemy.orm import relationship
from modules.models.config import Base

class Login(Base):
   __tablename__ = 'login'
   id = Column(Integer, Sequence('login_id_seq', increment=1), primary_key = True)
   username = Column(String(20), nullable=False, unique=True)
   password = Column(String(50), nullable=False)  
   
   patient = relationship('Patient', back_populates="login", uselist=False)
   administrator = relationship('Administrator', back_populates="login", uselist=False)
   doctor = relationship('Doctor', back_populates="login", uselist=False)

   def __init__(self, username, password, id = None):
      self.id = id
      self.username = username
      self.password = password
    
   def __repr__(self):
        return f"<Login {self.id} {self.username} {self.password} >"
     
   def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password
        }

class Patient(Base):
   __tablename__ = 'patient'
   id = Column(Integer, Sequence('patient_id_seq', increment=1), primary_key = True)
   patientid = Column(Integer, nullable=False, unique=True)
   username = Column(String(20), ForeignKey('login.username'), nullable=False)
   role = Column(Integer, nullable=False)
   firstname = Column(String(50), nullable=False)
   midname = Column(String(50), nullable=False)
   lastname = Column(String(50), nullable=False)  
   birthday = Column(Date, nullable=False)
   age = Column(Integer, nullable=False)
   profession = Column(String(100), nullable=False)  
   address = Column(String(100), nullable=False)  
   email = Column(String(25), nullable=False)
   mobile = Column(String(15), nullable=False)
   date_registered = Column(Date, nullable=False)
   
   login = relationship('Login', back_populates="patient")
   appointment = relationship('Appointment', back_populates="patient")
   diagnosis = relationship('Diagnosis', back_populates="patient")
   payment = relationship('Payment', back_populates="patient")
   
   def __init__(self, patientid, username, role, firstname, midname, lastname, birthday, age, profession, address, email, mobile, date_registered, id=None):
      self.id = id
      self.patientid = patientid
      self.username = username
      self.role = role
      self.firstname = firstname
      self.lastname = lastname
      self.midname = midname
      self.birthday = birthday
      self.age = age
      self.profession = profession
      self.address = address
      self.email = email
      self.mobile = mobile
      self.date_registered = date_registered
      
    
   def __repr__(self):
        return f"<Patient {self.id} {self.patientid}  {self.firstname} {self.midname} {self.lastname} {self.age} {self.email} {self.mobile} {self.birthday}>"

   def to_json(self):
        return {
            "id": self.id,
            "patientid": self.patientid,
            "username": self.username,
            "firstname": self.firstname,
            "midname": self.midname,
            "lastname": self.lastname,
            "birthday": self.birthday,
            "age": self.age,
            "address": self.address,
            "email": self.email,
            "mobile": self.mobile,
            "date_registered": self.date_registered,
            "role": self.role
        }

class Administrator(Base):
   __tablename__ = 'administrator'
   id = Column(Integer, Sequence('administrator_id_seq', increment=1), primary_key = True)
   empid = Column(String(12), nullable=False, unique=True)
   username = Column(String(20), ForeignKey('login.username'), nullable=False)
   role = Column(Integer, nullable=False)
   firstname = Column(String(50), nullable=False)
   midname = Column(String(50), nullable=False)
   lastname = Column(String(50), nullable=False)  
   email = Column(String(25), nullable=False)
   mobile = Column(String(15), nullable=False)
   position = Column(String(100), nullable=False)  
   status = Column(Boolean, nullable=False)
   date_started = Column(Date, nullable=False)
   
   login = relationship('Login', back_populates="administrator")
   request = relationship('Request', back_populates="administrator")
   
   
   def __init__(self, empid, username, role, firstname, midname, lastname, email, mobile, position, status, date_started, id=None):
      self.id = id
      self.empid = empid
      self.username = username
      self.role = role
      self.firstname = firstname
      self.lastname = lastname
      self.midname = midname
      self.position = position
      self.status = status
      self.email = email
      self.mobile = mobile
      self.date_started = date_started
      
    
   def __repr__(self):
        return f"<Administrator {self.id} {self.empid}  {self.firstname} {self.midname} {self.lastname} {self.position} {self.email} {self.mobile} {self.status}>"

   def to_json(self):
        return {
            "id": self.id,
            "empid": self.empid,
            "username": self.username,
            "firstname": self.firstname,
            "midname": self.midname,
            "lastname": self.lastname,
            "email": self.email,
            "mobile": self.mobile,
            "position": self.position,
            "status": self.status,
            "date_started": self.date_started,
            "role": self.role
        }

class Doctor(Base):
   __tablename__ = 'doctor'
   id = Column(Integer, Sequence('doctor_id_seq', increment=1), primary_key = True)
   empid = Column(String(12), nullable=False, unique=True)
   username = Column(String(20), ForeignKey('login.username'), nullable=False)
   role = Column(Integer, nullable=False)
   firstname = Column(String(50), nullable=False)
   midname = Column(String(50), nullable=False)
   lastname = Column(String(50), nullable=False)  
   age = Column(Integer, nullable=False)
   email = Column(String(25), nullable=False)
   mobile = Column(String(15), nullable=False)
   position = Column(String(100), nullable=False)  
   specialization = Column(String(100), nullable=False) 
   status = Column(Boolean, nullable=False)
   date_started = Column(Date, nullable=False)
   
   login = relationship('Login', back_populates="doctor")
   appointment = relationship('Appointment', back_populates="doctor")
   diagnosis = relationship('Diagnosis', back_populates="doctor")
   request = relationship('Request', back_populates="doctor")
      
   def __init__(self, empid, username, role, firstname, midname, lastname, age, email, mobile, position, specialization, status, date_started, id=None):
      self.id = id
      self.empid = empid
      self.username = username
      self.role = role
      self.firstname = firstname
      self.lastname = lastname
      self.midname = midname
      self.age = age
      self.position = position
      self.specialization = specialization
      self.status = status
      self.email = email
      self.mobile = mobile
      self.status = status
      self.date_started = date_started
          
   def __repr__(self):
        return f"<Doctor {self.id} {self.empid}  {self.firstname} {self.midname} {self.lastname} {self.position} {self.specialization} {self.email} {self.mobile} {self.status}>"

   def to_json(self):
        return {
            "id": self.id,
            "empid": self.empid,
            "username": self.username,
            "firstname": self.firstname,
            "midname": self.midname,
            "lastname": self.lastname,
            "email": self.email,
            "mobile": self.mobile,
            "position": self.position,
            "status": self.status,
            "date_started": self.date_started,
            "specialization": self.specialization,
            "role": self.role
        }
        
class Appointment(Base):
    __tablename__ = 'appointment'
    id = Column(Integer, Sequence('appointment_id_seq', increment=1), primary_key = True)
    ticketid = Column(String(20), nullable=False)
    patientid = Column(Integer, ForeignKey('patient.patientid'), nullable=False)
    docid = Column(String(12), ForeignKey('doctor.empid'), nullable=False)
    priority_level = Column(Integer, nullable=False)
    date_scheduled = Column(Date, nullable=False)
    time_scheduled = Column(Time, nullable=False)
    consult_hrs = Column(Float, nullable=False)
    
    patient = relationship('Patient', back_populates="appointment")
    doctor = relationship('Doctor', back_populates="appointment")
    
    
    def __init__(self, ticketid, patientid, docid, priority_level, date_scheduled, time_scheduled, consult_hrs, id = None):
      self.id = id
      self.ticketid = ticketid
      self.patientid = patientid
      self.docid = docid
      self.priority_level = priority_level
      self.date_scheduled = date_scheduled
      self.time_scheduled = time_scheduled
      self.consult_hrs = consult_hrs
          
    def __repr__(self):
        return f"<Appointment {self.id} {self.ticketid} {self.patientid} {self.docid} {self.priority_level} {self.date_scheduled} {self.time_scheduled}>"

    def to_json(self):
        return {
            "id": self.id,
            "ticketid": self.ticketid,
            "patientid": self.patientid,
            "docid": self.docid,
            "priority_level": self.priority_level,
            "date_scheduled": self.date_scheduled,
            "time_scheduled": self.time_scheduled,
            "consult_hrs": self.consult_hrs,
        }
    
class Diagnosis(Base):
    __tablename__ = 'diagnosis'
    id = Column(Integer, Sequence('diagnosis_id_seq', increment=1), primary_key = True)
    docid = Column(String(12), ForeignKey('doctor.empid'), nullable=False)
    patientid = Column(Integer, ForeignKey('patient.patientid'), nullable=False)
    narrative = Column(String(500), nullable=False)
    resolution = Column(String(500), nullable=False)
    date_submitted = Column(Date, nullable=False)
    
    
    patient = relationship('Patient', back_populates="diagnosis")
    doctor = relationship('Doctor', back_populates="diagnosis")
    
    def __init__(self, docid, patientid, narrative, resolution, date_submitted, id = None):
      self.id = id
      self.docid = docid
      self.patientid = patientid
      self.narrative = narrative
      self.resolution = resolution
      self.date_submitted = date_submitted
     
    def __repr__(self):
        return f"<Diagnosis {self.id} {self.docid} {self.patientid} {self.date_submitted}>"

    def to_json(self):
        return {
            "id": self.id,
            "docid": self.docid,
            "patientid": self.patientid,
            "narrative": self.narrative,
            "resolution": self.resolution,
            "date_submitted": self.date_submitted,
        }
    
class Payment(Base):
    __tablename__ = 'payment'
    id = Column(Integer, Sequence('payment_id_seq', increment=1), primary_key = True)
    paymentid = Column(String(50), nullable=False)
    patientid = Column(Integer, ForeignKey('patient.patientid'), nullable=False)
    amount = Column(Double, nullable=False)
    discount = Column(Double, nullable=False)
    status = Column(Boolean, nullable=False)
    date_released = Column(Date, nullable=False)
    
    patient = relationship('Patient', back_populates="payment")
    
    
    def __init__(self, paymentid, patientid, amount, discount, status, date_released, id=None):
      self.id = id
      self.paymentid = paymentid
      self.patientid = patientid
      self.amount = amount
      self.discount = discount
      self.status = status
      self.date_released = date_released
     
      
    def __repr__(self):
        return f"<Payment {self.id} {self.paymentid} {self.patientid} {self.amount} {self.discount} {self.status} {self.date_released}>"

    def to_json(self):
        return {
            "id": self.id,
            "paymentid": self.paymentid,
            "patientid": self.patientid,
            "amount": self.amount,
            "discount": self.discount,
            "status": self.status,
            "date_released": self.date_released
        }

class Request(Base):
    __tablename__ = 'request'
    id = Column(Integer, Sequence('request_id_seq', increment=1), primary_key = True)
    docid = Column(String(12), ForeignKey('doctor.empid'), nullable=False)
    adminid = Column(String(12), ForeignKey('administrator.empid'), nullable=False)
    details = Column(String(500), nullable=False)
    date_approved = Column(Date, nullable=False)
    status = Column(Boolean, nullable=False)
    
    administrator = relationship('Administrator', back_populates="request")
    doctor = relationship('Doctor', back_populates="request")
        
    def __init__(self, docid, adminid, details, date_approved, status, id=None):
      self.id = id
      self.docid = docid
      self.adminid = adminid
      self.details = details
      self.date_approved = date_approved
      self.status = status
            
    def __repr__(self):
        return f"<Request {self.id} {self.docid} {self.adminid} {self.date_approved} {self.status} >"

    def to_json(self):
        return {
            "id": self.id,
            "docid": self.docid,
            "adminid": self.adminid,
            "details": self.details,
            "date_approved": self.date_approved,
            "status": self.status,
        }
    
