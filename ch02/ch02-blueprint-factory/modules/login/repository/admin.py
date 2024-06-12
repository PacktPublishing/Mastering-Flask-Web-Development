from typing import List, Any, Dict
from modules.model.db import Admin
from flask import current_app


class AdminRepository:
    def __init__(self, db):
        self.db = db
        current_app.logger.info('AdminRepository instance created')
        
    def insert(self, admin:Admin) -> bool:
        try:
            self.db.session.add(admin)
            self.db.session.commit()
            current_app.logger.info('AdminRepository inserted record')
            return True
        except Exception as e:
            current_app.logger.info(f'AdminRepository insert error: {e}') 
        return False
    
    def update(self, id:int, details:Dict[str, Any]) -> bool:
        try:
            self.db.session.query(Admin).filter(Admin.id == id).update(details)     
            self.db.session.commit() 
            current_app.logger.info('AdminRepository updated record')
            return True
        except Exception as e:
            current_app.logger.info(f'AdminRepository update error: {e}') 
        return False  
    
    def delete(self, id:int) -> bool:
        try:
           admin = self.db.session.query(Admin).filter(Admin.id == id).delete()
           self.db.session.commit()
           current_app.logger.info('AdminRepository deleted record')
           return True
        except Exception as e:
           current_app.logger.info(f'AdminRepository delete error: {e}') 
        return False
    
    def select_one(self, id:int) -> Any:
        users =  self.db.session.query(Admin).filter(Admin.id == id).one_or_none()
        current_app.logger.info('AdminRepository retrieved one record')
        return users
    
    def select_all(self) -> List[Any]:
        users = self.db.session.query(Admin).all()
        current_app.logger.info('AdminRepository retrieved all record')
        return users