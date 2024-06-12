from typing import List, Any, Dict
from app.model.db import Orders
from flask import current_app

class OrderRepository:
    def __init__(self, db):
        self.db = db
        current_app.logger.info('OrderRepository instance created')
        
    def insert(self, order:Orders) -> bool:
        try:
            self.db.session.add(order)
            self.db.session.commit()
            current_app.logger.info('OrderRepository inserted record')
            return True
        except Exception as e:
            current_app.logger.info(f'OrderRepository insert error: {e}') 
        return False
    
    def update(self, id:int, details:Dict[str, Any]) -> bool:
        try:
            self.db.session.query(Orders).filter(Orders.id == id).update(details)     
            self.db.session.commit() 
            current_app.logger.info('OrderRepository updated record')
            return True
        except Exception as e:
            current_app.logger.info(f'OrderRepository update error: {e}') 
        return False  
    
    def delete(self, id:int) -> bool:
        try:
           login = self.db.session.query(Orders).filter(Orders.id == id).delete()
           self.db.session.commit()
           current_app.logger.info('OrderRepository deleted record')
           return True
        except Exception as e:
            current_app.logger.info(f'OrderRepository delete error: {e}') 
        return False
    
    def select_all(self) -> List[Any]:
        users = self.db.session.query(Orders).all()
        current_app.logger.info('OrderRepository retrieved all record')
        return users
    
    def select_one(self, id:int) -> Any:
        users =  self.db.session.query(Orders).filter(Orders.id == id).one_or_none()
        current_app.logger.info('OrderRepository retrieved one record by ID')
        return users
    
    def select_one_order(self, order_no:str) -> Any:
        users =  self.db.session.query(Orders).filter(Orders.order_no == order_no).one_or_none()
        current_app.logger.info('OrderRepository retrieved one record by order no')
        return users
    
    
