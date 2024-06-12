from typing import List, Any, Dict
from model.db import ComplaintType
from sqlalchemy.orm import Session

class ComplaintTypeRepository:
    def __init__(self, sess:Session):
        self.sess = sess
        
    def insert(self, ctype:ComplaintType) -> bool:
        try:
            self.sess.add(ctype)
            self.sess.commit()
            return True
        except Exception as e:
            print(e) 
        return False
    
    def update(self, id:int, details:Dict[str, Any]) -> bool:
        try:
            self.sess.query(ComplaintType).filter(ComplaintType.id == id).update(details)     
            self.sess.commit() 
            return True
        except Exception as e:
            print(e)
        return False  
    
    def delete(self, id:int) -> bool:
        try:
           details = self.sess.query(ComplaintType).filter(ComplaintType.id == id).delete()
           self.sess.commit()
           return True
        except Exception as e:
            print(e)  
        return False
    
    def select_all(self) -> List[Any]:
        details = self.sess.query(ComplaintType).all()
        return details
    
    def select_one(self, id:int) -> Any:
        detail =  self.sess.query(ComplaintType).filter(ComplaintType.id == id).one_or_none()
        return detail
    
   