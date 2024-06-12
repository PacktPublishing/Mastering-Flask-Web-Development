from typing import List, Any, Dict
from modules.model.db import Admin
from main import app
from sqlalchemy.orm import Session


class AdminRepository:
    def __init__(self, sess:Session):
        self.sess = sess
        app.logger.info('AdminRepository instance created')
        
    def insert(self, admin:Admin) -> bool:
        try:
            self.sess.add(admin)
            self.sess.commit()
            app.logger.info('AdminRepository inserted record')
            return True
        except Exception as e:
            app.logger.info(f'AdminRepository insert error: {e}') 
        return False
    
    def update(self, id:int, details:Dict[str, Any]) -> bool:
        try:
            self.sess.query(Admin).filter(Admin.id == id).update(details)     
            self.sess.commit() 
            app.logger.info('AdminRepository updated record')
            return True
        except Exception as e:
            app.logger.info(f'AdminRepository update error: {e}') 
        return False  
    
    def delete(self, id:int) -> bool:
        try:
           admin = self.sess.query(Admin).filter(Admin.id == id).delete()
           self.sess.commit()
           app.logger.info('AdminRepository deleted record')
           return True
        except Exception as e:
           app.logger.info(f'AdminRepository delete error: {e}') 
        return False
    
    def select_one(self, id:int) -> Any:
        users =  self.sess.query(Admin).filter(Admin.id == id).one_or_none()
        app.logger.info('AdminRepository retrieved one record')
        return users
    
    def select_all(self) -> List[Any]:
        users = self.sess.query(Admin).all()
        app.logger.info('AdminRepository retrieved all record')
        return users