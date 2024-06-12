from typing import List, Any, Dict
from modules.model.db import Products
from flask import current_app

class ProductRepository:
    def __init__(self, db):
        self.db = db
        current_app.logger.info('ProductRepository instance created')
        
    def insert(self, prod:Products) -> bool:
        try:
            self.db.session.add(prod)
            self.db.session.commit()
            current_app.logger.info('ProductRepository inserted record')
            return True
        except Exception as e:
            current_app.logger.info(f'ProductRepository insert error: {e}')  
        return False
    
    def update(self, id:int, details:Dict[str, Any]) -> bool:
        try:
            self.db.session.query(Products).filter(Products.id == id).update(details)     
            self.db.session.commit() 
            current_app.logger.info('ProductRepository updated record')
            return True
        except Exception as e:
            current_app.logger.info(f'ProductRepository update error: {e}') 
        return False  
    
    def delete(self, id:int) -> bool:
        try:
           login = self.db.session.query(Products).filter(Products.id == id).delete()
           self.db.session.commit()
           current_app.logger.info('ProductRepository deleted record')
           return True
        except Exception as e:
            current_app.logger.info(f'ProductRepository delete error: {e}')   
        return False
    
    def select_all(self) -> List[Any]:
        users = self.db.session.query(Products).all()
        current_app.logger.info('ProductRepository retrieved all record')
        return users
    
    def select_one(self, id:int) -> Any:
        users =  self.db.session.query(Products).filter(Products.id == id).one_or_none()
        current_app.logger.info('ProductRepository retrieved one record')
        return users
    
    def select_one_code(self, code:str) -> Any:
        users =  self.db.session.query(Products).filter(Products.code == code).one_or_none()
        current_app.logger.info('ProductRepository retrieved one record by product code')
        return users
    
    
