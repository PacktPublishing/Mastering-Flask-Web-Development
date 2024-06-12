from typing import List, Any, Dict
from modules.model.db import Products
from main import app
from sqlalchemy.orm import Session

class ProductRepository:
    def __init__(self, sess:Session):
        self.sess = sess
        app.logger.info('ProductRepository instance created')
        
    def insert(self, prod:Products) -> bool:
        try:
            self.sess.add(prod)
            self.sess.commit()
            app.logger.info('ProductRepository inserted record')
            return True
        except Exception as e:
            print(e)
            app.logger.info(f'ProductRepository insert error: {e}')  
        return False
    
    def update(self, id:int, details:Dict[str, Any]) -> bool:
        try:
            self.sess.query(Products).filter(Products.id == id).update(details)     
            self.sess.commit() 
            app.logger.info('ProductRepository updated record')
            return True
        except Exception as e:
            app.logger.info(f'ProductRepository update error: {e}') 
        return False  
    
    def delete(self, id:int) -> bool:
        try:
           login = self.sess.query(Products).filter(Products.id == id).delete()
           self.sess.commit()
           app.logger.info('ProductRepository deleted record')
           return True
        except Exception as e:
            app.logger.info(f'ProductRepository delete error: {e}')   
        return False
    
    def select_all(self) -> List[Any]:
        users = self.sess.query(Products).all()
        app.logger.info('ProductRepository retrieved all record')
        return users
    
    def select_one(self, id:int) -> Any:
        users =  self.sess.query(Products).filter(Products.id == id).one_or_none()
        app.logger.info('ProductRepository retrieved one record')
        return users
    
    def select_one_code(self, code:str) -> Any:
        users =  self.sess.query(Products).filter(Products.code == code).one_or_none()
        app.logger.info('ProductRepository retrieved one record by product code')
        return users
    
    
