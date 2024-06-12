from typing import List, Any, Dict
from app.model.db import Customer
from flask import current_app
from sqlalchemy.orm import Session

class CustomerRepository:
    def __init__(self, sess:Session):
        self.sess = sess
        current_app.logger.info('CustomerRepository instance created')
        
    def insert(self, cust:Customer) -> bool:
        try:
            self.sess.add(cust)
            self.sess.commit()
            current_app.logger.info('CustomerRepository inserted record')
            return True
        except Exception as e:
            current_app.logger.error(f'CustomerRepository insert error: {e}') 
        return False
    
    def update(self, cid:int, details:Dict[str, Any]) -> bool:
        try:
            self.sess.query(Customer).filter(Customer.cid == cid).update(details)     
            self.sess.commit() 
            current_app.logger.info('CustomerRepository updated record')
            return True
        except Exception as e:
            current_app.logger.error(f'CustomerRepository update error: {e}') 
        return False  
    
    def delete(self, cid:int) -> bool:
        try:
           login = self.sess.query(Customer).filter(Customer.cid == cid).delete()
           self.sess.commit()
           current_app.logger.info('CustomerRepository deleted record')
           return True
        except Exception as e:
           current_app.logger.error(f'CustomerRepository delete error: {e}')  
        return False
    
    def select_all(self) -> List[Any]:
        users = self.sess.query(Customer).all()
        current_app.logger.info('CustomerRepository retrieved all record')
        return users
    
     
    def select_one(self, cid:int) -> Any:
        users =  self.sess.query(Customer).filter(Customer.cid == cid).one_or_none()
        current_app.logger.info('CustomerRepository retrieved one record')
        return users
    
