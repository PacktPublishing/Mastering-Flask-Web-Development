from typing import List, Any, Dict
from modules.model.db import Shipping
from flask import current_app

class ShippingRepository:
    def __init__(self, db):
        self.db = db
        current_app.logger.info('ShippingRepository instance created')
        
    def insert(self, ship:Shipping) -> bool:
        try:
            self.db.session.add(ship)
            self.db.session.commit()
            current_app.logger.info('ShippingRepository inserted record')
            return True
        except Exception as e:
              current_app.logger.info(f'ShippingRepository insert error: {e}') 
        return False
    
    def update(self, id:int, details:Dict[str, Any]) -> bool:
        try:
            self.db.session.query(Shipping).filter(Shipping.id == id).update(details)     
            self.db.session.commit() 
            current_app.logger.info('ShippingRepository updated record')
            return True
        except Exception as e:
            current_app.logger.info(f'ShippingRepository update error: {e}') 
        return False  
    
    def delete(self, id:int) -> bool:
        try:
           login = self.db.session.query(Shipping).filter(Shipping.id == id).delete()
           self.db.session.commit()
           current_app.logger.info('ShippingRepository deleted record')
           return True
        except Exception as e:
            current_app.logger.info(f'ShippingRepository delete error: {e}')  
        return False
    
    def select_all(self) -> List[Any]:
        users = self.db.session.query(Shipping).all()
        current_app.logger.info('ShippingRepository retrieved all record')
        return users

    def select_all_cid(self, cid:int) -> List[Any]:
        users =  self.db.session.query(Shipping).filter(Shipping.cid == cid).all()
        current_app.logger.info('ShippingRepository retrieved all record by customer ID')
        return users
    
    def select_all_payment(self, pay_id:int) -> List[Any]:
        users =  self.db.session.query(Shipping).filter(Shipping.pay_id == pay_id).all()
        current_app.logger.info('ShippingRepository retrieved all record by payment ID')
        return users
    
    def select_all_delivery(self, did:int) -> List[Any]:
        users =  self.db.session.query(Shipping).filter(Shipping.did == did).all()
        current_app.logger.info('ShippingRepository retrieved all record by delivery officer ID')
        return users
    
    def select_one(self, id:int) -> Any:
        users =  self.db.session.query(Shipping).filter(Shipping.id == id).one_or_none()
        current_app.logger.info('ShippingRepository retrieved one record')
        return users
    
