from typing import List, Any, Dict
from modules.model.db import Payment, PaymentType
from flask import current_app

class PaymentRepository:
    def __init__(self, db):
        self.db = db
        current_app.logger.info('PaymentRepository instance created')
        
    def insert(self, payment:Payment) -> bool:
        try:
            self.db.session.add(payment)
            self.db.session.commit()
            current_app.logger.info('PaymentRepository inserted record')
            return True
        except Exception as e:
            current_app.logger.info(f'PaymentRepository insert error: {e}') 
        return False
    
    def update(self, id:int, details:Dict[str, Any]) -> bool:
        try:
            self.db.session.query(Payment).filter(Payment.id == id).update(details)     
            self.db.session.commit()
            current_app.logger.info('PaymentRepository updated record') 
            return True
        except Exception as e:
            current_app.logger.info(f'PaymentRepository update error: {e}') 
        return False  
    
    def delete(self, id:int) -> bool:
        try:
           login = self.db.session.query(Payment).filter(Payment.id == id).delete()
           self.db.session.commit()
           current_app.logger.info('PaymentRepository deleted record')
           return True
        except Exception as e:
            current_app.logger.info(f'PaymentRepository delete error: {e}')  
        return False
    
    def select_all(self) -> List[Any]:
        users = self.db.session.query(Payment).all()
        current_app.logger.info('OrderRepository retrieved all record')
        return users
    
    def select_one(self, id:int) -> Any:
        users =  self.db.session.query(Payment).filter(Payment.id == id).one_or_none()
        current_app.logger.info('OrderRepository retrieved one record by ID')
        return users
    
    def select_one_reference(self, ref_no:str) -> Any:
        users =  self.db.session.query(Payment).filter(Payment.ref_no == ref_no).one_or_none()
        current_app.logger.info('OrderRepository retrieved one record by reference no')
        return users
    
    
class PaymentTypeRepository:
    def __init__(self, db):
        self.db = db
        
    def insert(self, type:PaymentType) -> bool:
        try:
            self.db.session.add(type)
            self.db.session.commit()
            return True
        except Exception as e:
            print(e) 
        return False
    
    def update(self, id:int, details:Dict[str, Any]) -> bool:
        try:
            self.db.session.query(PaymentType).filter(PaymentType.id == id).update(details)     
            self.db.session.commit() 
            return True
        except Exception as e:
            print(e)
        return False  
    
    def delete(self, id:int) -> bool:
        try:
           login = self.db.session.query(PaymentType).filter(PaymentType.id == id).delete()
           self.db.session.commit()
           return True
        except Exception as e:
            print(e)  
        return False
    
    def select_all(self) -> List[Any]:
        users = self.db.session.query(PaymentType).all()
        return users
    
    def select_one(self, id:int) -> Any:
        users =  self.db.session.query(PaymentType).filter(PaymentType.id == id).one_or_none()
        return users
