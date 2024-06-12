from typing import List, Any, Dict
from model.db import Complainant
from sqlalchemy.orm import Session

class ComplainantRepository:
    def __init__(self, sess:Session):
        self.sess = sess
        
    def insert(self, complainant:Complainant) -> bool:
        try:
            self.sess.add(complainant)
            self.sess.commit()
            return True
        except Exception as e:
            print(e) 
        return False
    
    def update(self, id:int, details:Dict[str, Any]) -> bool:
        try:
            self.sess.query(Complainant).filter(Complainant.id == id).update(details)     
            self.sess.commit() 
            return True
        except Exception as e:
            print(e)
        return False  
    
    def delete(self, id:int) -> bool:
        try:
           complainant = self.sess.query(Complainant).filter(Complainant.id == id).delete()
           self.sess.commit()
           return True
        except Exception as e:
            print(e)  
        return False
    
    def select_all(self) -> List[Any]:
        complainants = self.sess.query(Complainant).all()
        return complainants
         
    
    def select_one(self, id:int) -> Any:
        complainant =  self.sess.query(Complainant).filter(Complainant.id == id).one_or_none()
        return complainant
    
   