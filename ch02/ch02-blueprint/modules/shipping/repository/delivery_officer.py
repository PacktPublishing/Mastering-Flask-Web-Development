from typing import List, Any, Dict
from modules.model.db import DeliveryOfficer
from main import app
from sqlalchemy.orm import Session

class DeliveryOfficerRepository:
    def __init__(self, sess:Session):
        self.sess = sess
        app.logger.info('DeliveryOfficerRepository instance created')
        
    def insert(self, officer:DeliveryOfficer) -> bool:
        try:
            self.sess.add(officer)
            self.sess.commit()
            app.logger.info('DeliveryOfficerRepository inserted record')
            return True
        except Exception as e:
            app.logger.info(f'DeliveryOfficerRepository insert error: {e}') 
        return False
    
    def update(self, id:int, details:Dict[str, Any]) -> bool:
        try:
            self.sess.query(DeliveryOfficer).filter(DeliveryOfficer.id == id).update(details)     
            self.sess.commit() 
            app.logger.info('DeliveryOfficerRepository updated record')
            return True
        except Exception as e:
            app.logger.info(f'DeliveryOfficerRepository update error: {e}') 
        return False  
    
    def delete(self, id:int) -> bool:
        try:
           login = self.sess.query(DeliveryOfficer).filter(DeliveryOfficer.id == id).delete()
           self.sess.commit()
           app.logger.info('DeliveryOfficerRepository deleted record')
           return True
        except Exception as e:
           app.logger.info(f'DeliveryOfficerRepository delete error: {e}') 
        return False
    
    def select_all(self) -> List[Any]:
        users = self.sess.query(DeliveryOfficer).all()
        app.logger.info('DeliveryOfficerRepository retrieved all record')
        return users

    
    def select_one(self, id:int) -> Any:
        users =  self.sess.query(DeliveryOfficer).filter(DeliveryOfficer.id == id).one_or_none()
        app.logger.info('DeliveryOfficerRepository retrieved one record')
        return users
