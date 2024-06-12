from typing import List, Any, Dict
from app.model.db import Orders, OrderDetails
from flask import current_app
from sqlalchemy.orm import Session

class OrdersRepository:
    def __init__(self, sess:Session):
        self.sess = sess
        current_app.logger.info('OrdersRepository instance created')
        
    def insert(self, ord:Orders) -> bool:
        try:
            self.sess.add(ord)
            self.sess.commit()
            current_app.logger.info('OrdersRepository inserted record')
            return True
        except Exception as e:
            print(e)
            current_app.logger.error(f'OrdersRepository insert error: {e}') 
        return False
    
    def update(self, oid:int, details:Dict[str, Any]) -> bool:
        try:
            self.sess.query(Orders).filter(Orders.oid == oid).update(details)     
            self.sess.commit() 
            current_app.logger.info('OrdersRepository updated record')
            return True
        except Exception as e:
            current_app.logger.error(f'OrdersRepository update error: {e}') 
        return False  
    
    def delete(self, oid:int) -> bool:
        try:
           login = self.sess.query(Orders).filter(Orders.oid == oid).delete()
           self.sess.commit()
           current_app.logger.info('OrdersRepository deleted record')
           return True
        except Exception as e:
           current_app.logger.error(f'OrdersRepository delete error: {e}')  
        return False
    
    def select_all(self) -> List[Any]:
        orders = self.sess.query(Orders).all()
        current_app.logger.info('OrdersRepository retrieved all record')
        return orders
    
     
    def select_one(self, oid:int) -> Any:
        order =  self.sess.query(Orders).filter(Orders.oid == oid).one_or_none()
        current_app.logger.info('CustomerRepository retrieved one record')
        return order

class OrderDetailsRepository:
    def __init__(self, sess:Session):
        self.sess = sess
        current_app.logger.info('OrderDetailsRepository instance created')
        
    def insert(self, ordetails:OrderDetails) -> bool:
        try:
            self.sess.add(ordetails)
            self.sess.commit()
            current_app.logger.info('OrderDetailsRepository inserted record')
            return True
        except Exception as e:
            current_app.logger.error(f'OrderDetailsRepository insert error: {e}') 
        return False
    
    def update(self, id:int, details:Dict[str, Any]) -> bool:
        try:
            self.sess.query(OrderDetails).filter(OrderDetails.id == id).update(details)     
            self.sess.commit() 
            current_app.logger.info('OrderDetailsRepository updated record')
            return True
        except Exception as e:
            current_app.logger.error(f'OrderDetailsRepository update error: {e}') 
        return False  
    
    def delete(self, id:int) -> bool:
        try:
           login = self.sess.query(OrderDetails).filter(OrderDetails.id == id).delete()
           self.sess.commit()
           current_app.logger.info('OrderDetailsRepository deleted record')
           return True
        except Exception as e:
           current_app.logger.error(f'OrderDetailsRepository delete error: {e}')  
        return False
    
    def select_all(self) -> List[Any]:
        details = self.sess.query(OrderDetails).all()
        current_app.logger.info('OrderDetailsRepository retrieved all record')
        return details
    
     
    def select_one(self, id:int) -> Any:
        detail =  self.sess.query(OrderDetails).filter(OrderDetails.id == id).one_or_none()
        current_app.logger.info('OrderDetailsRepository retrieved one record')
        return detail