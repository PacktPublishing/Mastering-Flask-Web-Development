from typing import List, Any, Dict
from modules.model.db import ShippingDetails

class ShippingDetailsRepository:
    def __init__(self, db):
        self.db = db
        
    def insert(self, sd:ShippingDetails) -> bool:
        try:
            self.db.session.add(sd)
            self.db.session.commit()
            return True
        except Exception as e:
            print(e) 
        return False
    
    def update(self, id:int, details:Dict[str, Any]) -> bool:
        try:
            self.db.session.query(ShippingDetails).filter(ShippingDetails.id == id).update(details)     
            self.db.session.commit() 
            return True
        except Exception as e:
            print(e)
        return False  
    
    def delete(self, id:int) -> bool:
        try:
           login = self.db.session.query(ShippingDetails).filter(ShippingDetails.id == id).delete()
           self.db.session.commit()
           return True
        except Exception as e:
            print(e)  
        return False
    
    def select_all(self) -> List[Any]:
        users = self.db.session.query(ShippingDetails).all()
        return users

    def select_one(self, id:int) -> Any:
        users =  self.db.session.query(ShippingDetails).filter(ShippingDetails.id == id).one_or_none()
        return users
        
    def select_one_sid(self, sid:int) -> Any:
        users =  self.db.session.query(ShippingDetails).filter(ShippingDetails.sid == sid).one_or_none()
        return users
    
