from sqlalchemy import Time, Column, ForeignKey, Integer, String, Float, Date, Sequence
from sqlalchemy.orm import relationship
from modules_fastapi.models.config import Base


class FacultyBorrower(Base):
    __tablename__ = 'faculty_borrower'
    id = Column(Integer, Sequence('faculty_borrower_id_seq', increment=1), primary_key = True)
    empid = Column(String(55), nullable=False, unique=True)
    firstname = Column(String(55), nullable=False)
    lastname = Column(String(55), nullable=False)
    
    faculty = relationship('BorrowedHist', back_populates="history")
   
    def __init__(self, empid, firstname, lastname, id=None):
      self.id = id
      self.empid = empid
      self.firstname = firstname
      self.lastname = lastname
    
    def __repr__(self):
        return f"<FacultyBorrower {self.id} {self.empid} {self.firstname} {self.lastname}>"

    def to_json(self):
        return {
            "id": self.id,
            "empid": self.empid,
            "firstname": self.firstname,
            "lastname": self.lastname
        }  
        
class BorrowedHist(Base):
    __tablename__ = 'borrowed_hist'
    id = Column(Integer, Sequence('borrowed_hist_id_seq', increment=1), primary_key = True)
    empid = Column(String, ForeignKey('faculty_borrower.empid'), nullable = False)
    borrowed_date = Column(Date, nullable=False)
    
    history = relationship('FacultyBorrower', back_populates="faculty")
    
    def __init__(self, empid, borrowed_date, id=None):
      self.id = id
      self.empid = empid
      self.borrowed_date = borrowed_date
      
    def to_json(self):
        return {
            "id": self.id,
            "empid": self.empid,
            "borrowed_date": self.borrowed_date
        }  
     
    def __repr__(self):
        return f"<BorrowedHist {self.id} {self.empid} {self.borrowed_date} >"