from typing import List, Any, Dict
from modules.model.db import Login
from sqlalchemy.orm import Session

class LoginRepository:
    def __init__(self, sess:Session):
        self.sess = sess
        
    def insert(self, login:Login) -> bool:
        try:
            self.sess.add(login)
            self.sess.commit()
            return True
        except Exception as e:
            print(e) 
        return False
    
    def update(self, id:int, details:Dict[str, Any]) -> bool:
        try:
            self.sess.query(Login).filter(Login.id == id).update(details)     
            self.sess.commit() 
            return True
        except Exception as e:
            print(e)
        return False  
    
    def delete(self, id:int) -> bool:
        try:
           login = self.sess.query(Login).filter(Login.id == id).delete()
           self.sess.commit()
           return True
        except Exception as e:
            print(e)  
        return False
    
    def select_all(self) -> List[Any]:
        users = self.sess.query(Login).all()
        return users
         
    
    def select_one(self, id:int) -> Any:
        user =  self.sess.query(Login).filter(Login.id == id).one_or_none()
        return user
    
    def select_one_username(self, username:str) -> Any:
        user =  self.sess.query(Login).filter(Login.username == username).one_or_none()
        return user
    
    def select_login_id_name(self, utype) -> List[int]:
        ids = self.sess.query(Login.id, Login.username).filter(Login.user_type == utype).all()
        return ids