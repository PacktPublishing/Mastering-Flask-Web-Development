from sqlalchemy import  Column, ForeignKey, Integer, String, Date, Sequence
from sqlalchemy.orm import relationship
from modules_sub_flask.models.config import Base


class Complainant(Base):
   __tablename__ = 'complainant'
   id = Column(Integer, Sequence('complainant_id_seq', increment=1), primary_key = True)
   firstname = Column(String(45), nullable=False)
   lastname = Column(String(45), nullable=False)  
   middlename = Column(String(45), nullable=False)
   email = Column(String(45), nullable=False)
   date_registered = Column(Date, nullable=False)
   
   complaints = relationship('Complaint', back_populates="complainants")
   
   def __init__(self, firstname, lastname, middlename, email, date_registered, id=None):
      self.id = id
      self.firstname = firstname
      self.lastname = lastname
      self.middlename = middlename
      self.email = email
    
      self.date_registered = date_registered
     
   def __repr__(self):
        return f"<Complainant {self.id} {self.firstname} {self.middlename} {self.lastname}>"
   
   def to_json(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "middlename": self.middlename,
            "lastname": self.lastname,
            "email": self.email,
        
            "date_registered": self.date_registered
        }


class Complaint(Base):
   __tablename__ = 'complaint'
   id = Column(Integer, Sequence('complaint_id_seq', increment=1), primary_key = True)
   ticketId = Column(String, nullable = False, unique=True)
   catid = Column(Integer, ForeignKey('category.id'), nullable = False)  
   ctype = Column(Integer, ForeignKey('complaint_type.id'), nullable = False) 
   complainantId =  Column(Integer, ForeignKey('complainant.id'), nullable = False) 
 
   category = relationship('Category', back_populates="complaints")
   complainants = relationship('Complainant', back_populates="complaints")
   complaint_type = relationship('ComplaintType', back_populates="complaints")
   complaint_details = relationship('ComplaintDetails', back_populates="complaint", uselist=False)
   
   def __init__(self, catid, complainantId, ticketId, ctype, id = None):
      self.id = id
      self.ticket_id = ticketId
      self.complainant_id = complainantId
      self.catid = catid
      self.ctype = ctype
   
   def __repr__(self):
        return f"<Complaint {self.id} {self.complainantId} {self.catid} {self.ctype}>"
   
   def to_json(self):
        return {
            "id": self.id,
            "ticketId": self.ticketId,
            "complainantId": self.complainantId,
            "catid": self.catid,
            "ctype": self.ctype
            
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