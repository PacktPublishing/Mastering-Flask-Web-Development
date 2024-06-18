
from sqlalchemy import  Column, LargeBinary ,ForeignKey, Integer, String, Date, Time, Sequence, Boolean, Float, Text, Double
from sqlalchemy.orm import relationship
from modules.models.config import Base

class Login(Base):
   __tablename__ = 'login'
   id = Column(Integer, Sequence('login_id_seq', increment=1), primary_key = True)
   username = Column(String(20), nullable=False, unique=True)
   password = Column(LargeBinary, nullable=False)  
   role = Column(Integer, nullable=False)
   
   patient = relationship('Patient', back_populates="login", uselist=False)
   administrator = relationship('Administrator', back_populates="login", uselist=False)
   doctor = relationship('Doctor', back_populates="login", uselist=False)

   def __init__(self, username, password, role, id = None):
      self.id = id
      self.username = username
      self.password = password
      self.role = role
    
   def __repr__(self):
        return f"<Login {self.id} {self.username} {self.password} {self.role} >"
     
   def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "role": self.role
        }

class Patient(Base):
   __tablename__ = 'patient'
   id = Column(Integer, Sequence('patient_id_seq', increment=1), primary_key = True)
   patientid = Column(String(20), nullable=False, unique=True)
   username = Column(String(20), ForeignKey('login.username'), nullable=False)
   firstname = Column(String(50), nullable=False)
   midname = Column(String(50), nullable=False)
   lastname = Column(String(50), nullable=False)  
   birthday = Column(Date, nullable=False)
   age = Column(Integer, nullable=False)
   address = Column(String(100), nullable=False)  
   email = Column(String(25), nullable=False)
   mobile = Column(String(15), nullable=False)
   gender = Column(String(10), nullable=False)
   
   login = relationship('Login', back_populates="patient")
   vaccard = relationship('VaccineCard', back_populates="patient")
   
   def __init__(self, patientid, gender, username, birthday, firstname, midname, lastname, age, address, email, mobile, id=None):
      self.id = id
      self.patientid = patientid
      self.username = username
      self.gender = gender
      self.firstname = firstname
      self.lastname = lastname
      self.midname = midname
      self.birthday = birthday
      self.age = age
      self.address = address
      self.email = email
      self.mobile = mobile
     
      
    
   def __repr__(self):
        return f"<Patient {self.id} {self.patientid}  {self.firstname} {self.midname} {self.lastname} {self.age} {self.gender} {self.email} {self.mobile} {self.birthday}>"

   def to_json(self):
        return {
            "id": self.id,
            "patientid": self.patientid,
            "username": self.username,
            "firstname": self.firstname,
            "midname": self.midname,
            "lastname": self.lastname,
            "gender": self.gender,
            "birthday": self.birthday,
            "age": self.age,
            "gender": self.gender,
            "address": self.address,
            "email": self.email,
            "mobile": self.mobile,
        }

class Administrator(Base):
   __tablename__ = 'administrator'
   id = Column(Integer, Sequence('administrator_id_seq', increment=1), primary_key = True)
   adminid = Column(String(12), nullable=False, unique=True)
   username = Column(String(20), ForeignKey('login.username'), nullable=False)
   firstname = Column(String(50), nullable=False)
   midname = Column(String(50), nullable=False)
   lastname = Column(String(50), nullable=False)  
   email = Column(String(25), nullable=False)
   mobile = Column(String(15), nullable=False)
   position = Column(String(100), nullable=False)  
   status = Column(Boolean, nullable=False)
   gender = Column(String(10), nullable=False)
   
   login = relationship('Login', back_populates="administrator")
   vacreg = relationship('VacRegistration', back_populates="administrator")
   
   def __init__(self, adminid, position, username,firstname, midname, lastname, gender, email, mobile,  status,  id=None):
      self.id = id
      self.adminid = adminid
      self.username = username
      self.firstname = firstname
      self.lastname = lastname
      self.midname = midname
      self.gender = gender
      self.status = status
      self.email = email
      self.mobile = mobile
      self.position = position
    
   def __repr__(self):
        return f"<Administrator {self.id} {self.adminid}  {self.firstname} {self.midname} {self.lastname} {self.position} {self.gender} {self.email} {self.mobile} {self.status}>"

   def to_json(self):
        return {
            "id": self.id,
            "adminid": self.adminid,
            "username": self.username,
            "firstname": self.firstname,
            "midname": self.midname,
            "lastname": self.lastname,
            "email": self.email,
            "mobile": self.mobile,
            "position": self.position,
            "status": self.status,
            "gender": self.gender,
          
        }

class Doctor(Base):
   __tablename__ = 'doctor'
   id = Column(Integer, Sequence('doctor_id_seq', increment=1), primary_key = True)
   docid = Column(String(12), nullable=False, unique=True)
   username = Column(String(20), ForeignKey('login.username'), nullable=False)
   firstname = Column(String(50), nullable=False)
   midname = Column(String(50), nullable=False)
   lastname = Column(String(50), nullable=False)  
   age = Column(Integer, nullable=False)
   gender = Column(String(10), nullable=False)
   email = Column(String(25), nullable=False)
   mobile = Column(String(15), nullable=False)
   status = Column(Boolean, nullable=False)
   vaccenterid = Column(String(20), ForeignKey('vaccination_center.vaccenterid'), nullable=False)  
   
   login = relationship('Login', back_populates="doctor")
   vaccenter = relationship('VacCenter', back_populates="doctor")
   vaccard = relationship('VaccineCard', back_populates="doctor")
   
   def __init__(self, docid, username,  vaccenterid, firstname, midname, lastname, age, gender, email, mobile, status, id=None):
      self.id = id
      self.docid = docid
      self.username = username
      self.firstname = firstname
      self.lastname = lastname
      self.midname = midname
      self.age = age
      self.gender = gender
      self.status = status
      self.email = email
      self.mobile = mobile
      self.status = status
      self.vaccenterid = vaccenterid
          
   def __repr__(self):
        return f"<Doctor {self.id} {self.docid}  {self.firstname} {self.midname} {self.lastname} {self.gender} {self.email} {self.mobile} {self.status}>"

   def to_json(self):
        return {
            "id": self.id,
            "docid": self.docid,
            "username": self.username,
            "firstname": self.firstname,
            "midname": self.midname,
            "lastname": self.lastname,
            "age": self.age,
            "gender": self.gender,
            "email": self.email,
            "mobile": self.mobile,
            "status": self.status
        }
        
class VacCenter(Base):
    __tablename__ = 'vaccination_center'
    id = Column(Integer, Sequence('vaccination_center_id_seq', increment=1), primary_key = True)
    vaccenterid = Column(String(20), nullable=False, unique=True)
    centername = Column(String(100), nullable=False)
    telephone = Column(String(20), nullable=False)
    address = Column(String(100), nullable=False)
    city = Column(String(50), nullable=False)
    province = Column(String(50), nullable=False)
    region = Column(String(50), nullable=False)
    
    doctor = relationship('Doctor', back_populates="vaccenter")
    inventory = relationship('Inventory', back_populates="vaccenter")
      
    
    def __init__(self, vaccenterid, centername, telephone, address, city, province, region, id = None):
      self.id = id
      self.vaccenterid = vaccenterid
      self.centername = centername
      self.telephone = telephone
      self.address = address
      self.city = city
      self.province = province
      self.region = region
          
    def __repr__(self):
        return f"<VacCenter {self.id} {self.vaccenterid} {self.centername} {self.telephone} {self.address} {self.city} {self.province} {self.region}>"

    def to_json(self):
        return {
            "id": self.id,
            "vaccenterid": self.vaccenterid,
            "centername": self.centername,
            "telephone": self.telephone,
            "address": self.address,
            "city": self.city,
            "province": self.province,
            "region": self.region,
        }


class VacRegistration(Base):
    __tablename__ = 'vaccine_registration'
    id = Column(Integer, Sequence('vaccine_registration_id_seq', increment=1), primary_key = True)
    vacid = Column(String(20), ForeignKey('vaccine.vacid'), nullable=False)
    regcode = Column(String(50), nullable=False, unique=True )
    adminid = Column(String(12), ForeignKey('administrator.adminid'), nullable=False)
    date_registration = Column(Date, nullable=False)
    
    vaccine = relationship('Vaccine', back_populates="vacreg")
    administrator = relationship('Administrator', back_populates="vacreg")
    
        
    def __init__(self, vacid, regcode, adminid, date_registration, id = None):
      self.id = id
      self.vacid = vacid
      self.regcode = regcode
      self.adminid = adminid
      self.date_registration = date_registration
     
    def __repr__(self):
        return f"<VacRegistration {self.id} {self.vacid} {self.regcode} {self.adminid} {self.date_registration}>"

    def to_json(self):
        return {
            "id": self.id,
            "vacid": self.vacid,
            "regcode": self.regcode,
            "adminid": self.adminid,
            "date_registration": self.date_registration            
        }
    
class Vaccine(Base):
    __tablename__ = 'vaccine'
    id = Column(Integer, Sequence('vaccine_id_seq', increment=1), primary_key = True)
    vacid = Column(String(20), nullable=False, unique=True)
    vacname = Column(String(50), nullable=False)
    vacdesc = Column(String(100), nullable=False)
    qty = Column(Integer, nullable=False)
    price = Column(Double, nullable=False)
    status =  Column(Boolean, nullable=False)
    
    vacreg = relationship('VacRegistration', back_populates="vaccine")
    vaccard = relationship('VaccineCard', back_populates="vaccine")
    inventory = relationship('Inventory', back_populates="vaccine")
    
    def __init__(self, vacid, vacname, vacdesc, qty, price, status, id=None):
      self.id = id
      self.vacid = vacid
      self.vacname = vacname
      self.vacdesc = vacdesc
      self.qty = qty
      self.price = price
      self.status = status  
      
    def __repr__(self):
        return f"<Vaccine {self.id} {self.vacid} {self.vacname} {self.qty} {self.price} {self.status}>"

    def to_json(self):
        return {
            "id": self.id,
            "vacid": self.vacid,
            "vacname": self.vacname,
            "qty": self.qty,
            "price": self.price,
            "status": self.status
        }
        
class VaccineCard(Base):
    __tablename__ = 'vaccine_card'
    id = Column(Integer, Sequence('vaccine_card_id_seq', increment=1), primary_key = True)
    cardid = Column(String(20), nullable=False, unique=True)
    patientid = Column(String(20), ForeignKey('patient.patientid'), nullable=False)
    docid = Column(String(100), ForeignKey('doctor.docid'), nullable=False)
    vacid = Column(String(20), ForeignKey('vaccine.vacid'), nullable=False)
    date_vaccinated = Column(Date, nullable=False)
    
    patient = relationship('Patient', back_populates="vaccard")
    doctor = relationship('Doctor', back_populates="vaccard")
    vaccine = relationship('Vaccine', back_populates="vaccard")
    
    
    def __init__(self, vacid, cardid, patientid, docid, date_vaccinated, id=None):
      self.id = id
      self.vacid = vacid
      self.patientid = patientid
      self.docid = docid
    
      self.date_vaccinated = date_vaccinated
      self.cardid = cardid
      
    def __repr__(self):
        return f"<VaccineCard {self.id} {self.vacid} {self.patientid} {self.docid}  {self.date_vaccinated}>"

    def to_json(self):
        return {
            "id": self.id,
            "vacid": self.vacid,
            "patientid": self.patientid,
            "docid": self.docid,
          
            "date_vaccinated": self.date_vaccinated,
            "cardid": self.cardid
        }


class Inventory(Base):
    __tablename__ = 'inventory'
    id = Column(Integer, Sequence('inventory_id_seq', increment=1), primary_key = True)
    vacid = Column(String(20), ForeignKey('vaccine.vacid'), nullable=False, unique=True)
    vaccenterid = Column(String(20),  ForeignKey('vaccination_center.vaccenterid'), nullable=False)
    date_delivered = Column(Date, nullable=False)
    
    vaccine = relationship('Vaccine', back_populates="inventory")
    vaccenter = relationship('VacCenter', back_populates="inventory")
         
    def __init__(self, vacid, vaccenterid, date_delivered, id=None):
      self.id = id
      self.vacid = vacid
      self.vaccenterid = vaccenterid
      self.date_delivered = date_delivered
    
    def __repr__(self):
        return f"<Inventory {self.id} {self.vacid} {self.vaccenterid} {self.date_delivered}>"

    def to_json(self):
        return {
            "id": self.id,
            "vacid": self.vacid,
            "vaccenterid": self.vaccenterid,
            "date_delivered": self.date_delivered
        }
    
