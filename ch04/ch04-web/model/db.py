
from sqlalchemy import  Column, ForeignKey, Integer, String, Date, Sequence
from sqlalchemy.orm import relationship
from model.config import Base

class Login(Base):
   __tablename__ = 'login'
   id = Column(Integer, Sequence('login_id_seq', increment=1), primary_key = True)
   username = Column(String(45))
   password = Column(String(45))  
   user_type = Column(Integer)

   complainant = relationship('Complainant', back_populates="login", uselist=False)
   admin = relationship('Administrator', back_populates="login", uselist=False)

   def __init__(self, username, password, user_type, id = None):
      self.id = id
      self.username = username
      self.password = password
      self.user_type = user_type

   def __repr__(self):
        return f"<Login {self.id} {self.username} {self.password} {self.user_type}>"
     
   def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "user_type": self.user_type
        }
     
class Complainant(Base):
   __tablename__ = 'complainant'
   id = Column(Integer, ForeignKey('login.id'), primary_key = True)
   firstname = Column(String(45))
   lastname = Column(String(45))  
   middlename = Column(String(45))
   email = Column(String(45))
   mobile = Column(String(20))
   address = Column(String(100))
   zipcode = Column(Integer)
   status = Column(String(45))
   date_registered = Column(Date)
      
   login = relationship('Login', back_populates="complainant")
   complaints = relationship('Complaint', back_populates="complainants")
   
   def __init__(self, id, firstname, lastname, middlename, email, mobile, address, status, zipcode, date_registered):
      self.id = id
      self.firstname = firstname
      self.lastname = lastname
      self.middlename = middlename
      self.email = email
      self.mobile = mobile
      self.address = address
      self.status = status
      self.zipcode = zipcode
      self.date_registered = date_registered
      
   def __repr__(self):
        return f"<Customer {self.id} {self.firstname} {self.middlename} {self.lastname}>"
   
   def to_json(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "middlename": self.middlename,
            "lastname": self.lastname,
            "email": self.email,
            "mobile": self.mobile,
            "address": self.address,
            "status": self.status,
            "zipcode": self.zipcode,
            "date_registered": self.date_registered
        }
        
class Administrator(Base):
   __tablename__ = 'admin'
   id = Column(Integer, ForeignKey('login.id'), primary_key = True)
   firstname = Column(String(45))
   lastname = Column(String(45))  
   middlename = Column(String(45))
   email = Column(String(45))
   mobile = Column(String(45))
   date_registered = Column(Date)
   
   login = relationship('Login', back_populates="admin")
   
   def __init__(self, id, firstname, lastname, middlename, email, mobile, date_registered):
      self.id = id
      self.firstname = firstname
      self.lastname = lastname
      self.middlename = middlename
      self.email = email
      self.mobile = mobile
      self.date_registered = date_registered
      
   def __repr__(self):
        return f"<Admin {self.id} {self.firstname} {self.middlename} {self.lastname}>"

   def to_json(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "middlename": self.middlename,
            "lastname": self.lastname,
            "email": self.email,
            "mobile": self.mobile,
            "date_registered": self.date_registered
        }

class Complaint(Base):
   __tablename__ = 'complaint'
   id = Column(Integer, Sequence('complaint_id_seq', increment=1), primary_key = True)
   cid = Column(Integer, ForeignKey('complainant.id'), nullable = False)
   catid = Column(Integer, ForeignKey('category.id'), nullable = False)  
   ctype = Column(Integer, ForeignKey('complaint_type.id'), nullable = False)  
   
   category = relationship('Category', back_populates="complaints")
   complainants = relationship('Complainant', back_populates="complaints")
   complaint_type = relationship('ComplaintType', back_populates="complaints")
   complaint_details = relationship('ComplaintDetails', back_populates="complaint", uselist=False)
   
   def __init__(self, cid, catid, ctype, id = None):
      self.id = id
      self.cid = cid
      self.catid = catid
      self.ctype = ctype
   
   def __repr__(self):
        return f"<Products {self.id} {self.cid} {self.catid} {self.ctype}>"
   
   def to_json(self):
        return {
            "id": self.id,
            "cid": self.cid,
            "catid": self.catid,
            "ctype": self.ctype,
        }

class Category(Base):
   __tablename__ = 'category'
   id = Column(Integer, Sequence('category_id_seq', increment=1), primary_key = True)
   name = Column(String(45), nullable = False)
   
   complaints = relationship('Complaint', back_populates="category")
   
   def __init__(self, name, id=None):
      self.id = id
      self.name = name
      
   def __repr__(self):
        return f"<Category {self.id} {self.name}>"
     
   def to_json(self):
        return {
            "id": self.id,
            "name": self.name
        }
     
class ComplaintType(Base):
   __tablename__ = 'complaint_type'
   id = Column(Integer, Sequence('complaint_type_id_seq', increment=1), primary_key = True)
   name = Column(String(45), nullable = False)
   
   complaints = relationship('Complaint', back_populates="complaint_type")
   
   def __init__(self, name, id=None):
      self.id = id
      self.name = name
      
   def __repr__(self):
        return f"<ComplaintType {self.id} {self.name}>"
   
   def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
        }
         
class ComplaintDetails(Base):
   __tablename__ = 'complaint_details'
   id = Column(Integer, Sequence('complaint_details_id_seq', increment=1), primary_key = True)
   compid = Column(Integer, ForeignKey('complaint.id'), nullable = False, unique=True)
   statement = Column(String(100), nullable = False)  
   status = Column(String(50))  
   resolution = Column(String(100))  
   date_resolved = Column(Date)
   
   complaint = relationship('Complaint', back_populates="complaint_details")
  
   
   
   def __init__(self, compid, statement, status=None, resolution=None, date_resolved = None, id = None):
      self.id = id
      self.compid = compid
      self.statement = statement
      self.status = status
      self.resolution = resolution
      self.date_resolved = date_resolved
   
   def __repr__(self):
        return f"<Orders {self.id} {self.compid} {self.statement} {self.status} {self.resolution}>"
     
   def to_json(self):
        return {
            "id": self.id,
            "compid": self.compid,
            "statement": self.statement,
            "status": self.status,
            "resolution": self.resolution
           
        }