from typing import List, Any, Dict
from modules.model.db import Shipping
from main import app
from sqlalchemy.orm import Session

class ShippingRepository:
    def __init__(self, sess:Session):
        self.sess = sess
        app.logger.info('ShippingRepository instance created')
        
    def insert(self, ship:Shipping) -> bool:
        try:
            self.sess.add(ship)
            self.sess.commit()
            app.logger.info('ShippingRepository inserted record')
            return True
        except Exception as e:
              app.logger.info(f'ShippingRepository insert error: {e}') 
        return False
    
    def update(self, id:int, details:Dict[str, Any]) -> bool:
        try:
            self.sess.query(Shipping).filter(Shipping.id == id).update(details)     
            self.sess.commit() 
            app.logger.info('ShippingRepository updated record')
            return True
        except Exception as e:
            app.logger.info(f'ShippingRepository update error: {e}') 
        return False  
    
    def delete(self, id:int) -> bool:
        try:
           login = self.sess.query(Shipping).filter(Shipping.id == id).delete()
           self.sess.commit()
           app.logger.info('ShippingRepository deleted record')
           return True
        except Exception as e:
            app.logger.info(f'ShippingRepository delete error: {e}')  
        return False
    
    def select_all(self) -> List[Any]:
        users = self.sess.query(Shipping).all()
        app.logger.info('ShippingRepository retrieved all record')
        return users

    def select_all_cid(self, cid:int) -> List[Any]:
        users =  self.sess.query(Shipping).filter(Shipping.cid == cid).all()
        app.logger.info('ShippingRepository retrieved all record by customer ID')
        return users
    
    def select_all_payment(self, pay_id:int) -> List[Any]:
        users =  self.sess.query(Shipping).filter(Shipping.pay_id == pay_id).all()
        app.logger.info('ShippingRepository retrieved all record by payment ID')
        return users
    
    def select_all_delivery(self, did:int) -> List[Any]:
        users =  self.sess.query(Shipping).filter(Shipping.did == did).all()
        app.logger.info('ShippingRepository retrieved all record by delivery officer ID')
        return users
    
    def select_one(self, id:int) -> Any:
        users =  self.sess.query(Shipping).filter(Shipping.id == id).one_or_none()
        app.logger.info('ShippingRepository retrieved one record')
        return users
    
