from typing import List, Any, Dict
from modules.model.db import Orders
from main import app
from sqlalchemy.orm import Session

class OrderRepository:
    def __init__(self, sess:Session):
        self.sess = sess
        app.logger.info('OrderRepository instance created')
        
    def insert(self, order:Orders) -> bool:
        try:
            self.sess.add(order)
            self.sess.commit()
            app.logger.info('OrderRepository inserted record')
            return True
        except Exception as e:
            app.logger.info(f'OrderRepository insert error: {e}') 
        return False
    
    def update(self, id:int, details:Dict[str, Any]) -> bool:
        try:
            self.sess.query(Orders).filter(Orders.id == id).update(details)     
            self.sess.commit() 
            app.logger.info('OrderRepository updated record')
            return True
        except Exception as e:
            app.logger.info(f'OrderRepository update error: {e}') 
        return False  
    
    def delete(self, id:int) -> bool:
        try:
           login = self.sess.query(Orders).filter(Orders.id == id).delete()
           self.sess.commit()
           app.logger.info('OrderRepository deleted record')
           return True
        except Exception as e:
            app.logger.info(f'OrderRepository delete error: {e}') 
        return False
    
    def select_all(self) -> List[Any]:
        users = self.sess.query(Orders).all()
        app.logger.info('OrderRepository retrieved all record')
        return users
    
    def select_one(self, id:int) -> Any:
        users =  self.sess.query(Orders).filter(Orders.id == id).one_or_none()
        app.logger.info('OrderRepository retrieved one record by ID')
        return users
    
    def select_one_order(self, order_no:str) -> Any:
        users =  self.sess.query(Orders).filter(Orders.order_no == order_no).one_or_none()
        app.logger.info('OrderRepository retrieved one record by order no')
        return users
    
    
