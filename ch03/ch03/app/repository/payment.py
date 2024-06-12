from typing import List, Any, Dict
from app.model.db import Payment
from flask import current_app
from sqlalchemy.orm import Session

class PaymentRepository:
    def __init__(self, sess:Session):
        self.sess = sess
        current_app.logger.info('PaymentRepository instance created')
        
    def insert(self, pay:Payment) -> bool:
        try:
            self.sess.add(pay)
            self.sess.commit()
            current_app.logger.info('PaymentRepository inserted record')
            return True
        except Exception as e:
            current_app.logger.error(f'PaymentRepository insert error: {e}') 
        return False
    
    def update(self, pid:int, details:Dict[str, Any]) -> bool:
        try:
            self.sess.query(Payment).filter(Payment.pid == pid).update(details)     
            self.sess.commit() 
            current_app.logger.info('PaymentRepository updated record')
            return True
        except Exception as e:
            current_app.logger.error(f'PaymentRepository update error: {e}') 
        return False  
    
    def delete(self, pid:int) -> bool:
        try:
           login = self.sess.query(Payment).filter(Payment.pid == pid).delete()
           self.sess.commit()
           current_app.logger.info('PaymentRepository deleted record')
           return True
        except Exception as e:
           current_app.logger.error(f'PaymentRepository delete error: {e}')  
        return False
    
    def select_all(self) -> List[Any]:
        pays = self.sess.query(Payment).all()
        current_app.logger.info('PaymentRepository retrieved all record')
        return pays
    
     
    def select_one(self, pid:int) -> Any:
        pay =  self.sess.query(Payment).filter(Payment.pid == pid).one_or_none()
        current_app.logger.info('PaymentRepository retrieved one record')
        return pay
    