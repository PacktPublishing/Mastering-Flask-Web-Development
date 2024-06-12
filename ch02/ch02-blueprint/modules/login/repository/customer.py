from typing import List, Any, Dict
from modules.model.db import Customer
from main import app
from sqlalchemy.orm import Session

class CustomerRepository:
    def __init__(self, sess:Session):
        self.sess = sess
        app.logger.info('CustomerRepository instance created')
        
    def insert(self, cust:Customer) -> bool:
        try:
            self.sess.add(cust)
            self.sess.commit()
            app.logger.info('CustomerRepository inserted record')
            return True
        except Exception as e:
            app.logger.info(f'CustomerRepository insert error: {e}') 
        return False
    
    def update(self, id:int, details:Dict[str, Any]) -> bool:
        try:
            self.sess.query(Customer).filter(Customer.id == id).update(details)     
            self.sess.commit() 
            app.logger.info('CustomerRepository updated record')
            return True
        except Exception as e:
            app.logger.info(f'CustomerRepository update error: {e}') 
        return False  
    
    def delete(self, id:int) -> bool:
        try:
           login = self.sess.query(Customer).filter(Customer.id == id).delete()
           self.sess.commit()
           app.logger.info('CustomerRepository deleted record')
           return True
        except Exception as e:
           app.logger.info(f'CustomerRepository delete error: {e}')  
        return False
    
    def select_all(self) -> List[Any]:
        users = self.sess.query(Customer).all()
        app.logger.info('CustomerRepository retrieved all record')
        return users
    
     
    def select_one(self, id:int) -> Any:
        users =  self.sess.query(Customer).filter(Customer.id == id).one_or_none()
        app.logger.info('CustomerRepository retrieved one record')
        return users
    
