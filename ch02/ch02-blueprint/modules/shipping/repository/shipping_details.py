from typing import List, Any, Dict
from modules.model.db import ShippingDetails
from sqlalchemy.orm import Session

class ShippingDetailsRepository:
    def __init__(self, sess:Session):
        self.sess = sess
        
    def insert(self, sd:ShippingDetails) -> bool:
        try:
            self.sess.add(sd)
            self.sess.commit()
            return True
        except Exception as e:
            print(e) 
        return False
    
    def update(self, id:int, details:Dict[str, Any]) -> bool:
        try:
            self.sess.query(ShippingDetails).filter(ShippingDetails.id == id).update(details)     
            self.sess.commit() 
            return True
        except Exception as e:
            print(e)
        return False  
    
    def delete(self, id:int) -> bool:
        try:
           login = self.sess.query(ShippingDetails).filter(ShippingDetails.id == id).delete()
           self.sess.commit()
           return True
        except Exception as e:
            print(e)  
        return False
    
    def select_all(self) -> List[Any]:
        users = self.sess.query(ShippingDetails).all()
        return users

    def select_one(self, id:int) -> Any:
        users =  self.sess.query(ShippingDetails).filter(ShippingDetails.id == id).one_or_none()
        return users
        
    def select_one_sid(self, sid:int) -> Any:
        users =  self.sess.query(ShippingDetails).filter(ShippingDetails.sid == sid).one_or_none()
        return users
    
