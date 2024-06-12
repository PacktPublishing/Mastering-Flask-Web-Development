from typing import List, Any, Dict
from app.model.db import DeliveryOfficer
from flask import current_app

class DeliveryOfficerRepository:
    def __init__(self, db):
        self.db = db
        current_app.logger.info('DeliveryOfficerRepository instance created')
        
    def insert(self, officer:DeliveryOfficer) -> bool:
        try:
            self.db.session.add(officer)
            self.db.session.commit()
            current_app.logger.info('DeliveryOfficerRepository inserted record')
            return True
        except Exception as e:
            current_app.logger.info(f'DeliveryOfficerRepository insert error: {e}') 
        return False
    
    def update(self, id:int, details:Dict[str, Any]) -> bool:
        try:
            self.db.session.query(DeliveryOfficer).filter(DeliveryOfficer.id == id).update(details)     
            self.db.session.commit() 
            current_app.logger.info('DeliveryOfficerRepository updated record')
            return True
        except Exception as e:
            current_app.logger.info(f'DeliveryOfficerRepository update error: {e}') 
        return False  
    
    def delete(self, id:int) -> bool:
        try:
           login = self.db.session.query(DeliveryOfficer).filter(DeliveryOfficer.id == id).delete()
           self.db.session.commit()
           current_app.logger.info('DeliveryOfficerRepository deleted record')
           return True
        except Exception as e:
           current_app.logger.info(f'DeliveryOfficerRepository delete error: {e}') 
        return False
    
    def select_all(self) -> List[Any]:
        users = self.db.session.query(DeliveryOfficer).all()
        current_app.logger.info('DeliveryOfficerRepository retrieved all record')
        return users

    
    def select_one(self, id:int) -> Any:
        users =  self.db.session.query(DeliveryOfficer).filter(DeliveryOfficer.id == id).one_or_none()
        current_app.logger.info('DeliveryOfficerRepository retrieved one record')
        return users
