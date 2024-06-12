from typing import List, Any, Dict
from model.db import Complaint
from sqlalchemy.orm import Session

class ComplaintRepository:
    def __init__(self, sess:Session):
        self.sess = sess
        
    def insert(self, complaint:Complaint) -> bool:
        try:
            self.sess.add(complaint)
            self.sess.commit()
            return True
        except Exception as e:
            print(e) 
        return False
    
    def update(self, id:int, details:Dict[str, Any]) -> bool:
        try:
            self.sess.query(Complaint).filter(Complaint.id == id).update(details)     
            self.sess.commit() 
            return True
        except Exception as e:
            print(e)
        return False  
    
    def delete(self, id:int) -> bool:
        try:
           complaint = self.sess.query(Complaint).filter(Complaint.id == id).delete()
           self.sess.commit()
           return True
        except Exception as e:
            print(e)  
        return False
    
    def select_all(self) -> List[Any]:
        complaint = self.sess.query(Complaint).all()
        return complaint
    
    def select_one(self, id:int) -> Any:
        complaint =  self.sess.query(Complaint).filter(Complaint.id == id).one_or_none()
        return complaint
    
   