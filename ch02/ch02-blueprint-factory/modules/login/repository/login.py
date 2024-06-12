from typing import List, Any, Dict
from modules.model.db import Login


class LoginRepository:
    def __init__(self, db):
        self.db = db
        
    def insert(self, login:Login) -> bool:
        try:
            self.db.session.add(login)
            self.db.session.commit()
            return True
        except Exception as e:
            print(e) 
        return False
    
    def update(self, id:int, details:Dict[str, Any]) -> bool:
        try:
            self.db.session.query(Login).filter(Login.id == id).update(details)     
            self.db.session.commit() 
            return True
        except Exception as e:
            print(e)
        return False  
    
    def delete(self, id:int) -> bool:
        try:
           login = self.db.session.query(Login).filter(Login.id == id).delete()
           self.db.session.commit()
           return True
        except Exception as e:
            print(e)  
        return False
    
    def select_all(self) -> List[Any]:
        users = self.db.session.query(Login).all()
        return users
         
    
    def select_one(self, id:int) -> Any:
        user =  self.db.session.query(Login).filter(Login.id == id).one_or_none()
        return user
    
    def select_one_username(self, username:str) -> Any:
        user =  self.db.session.query(Login).filter(Login.username == username).one_or_none()
        return user
    
    def select_login_id_name(self, utype) -> List[int]:
        ids = self.db.session.query(Login.id, Login.username).filter(Login.user_type == utype).all()
        return ids