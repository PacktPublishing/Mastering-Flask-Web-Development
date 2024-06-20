from app.models.db import Login
from app.models.db import database
from typing import Dict, Any
import asyncio

class LoginRepository:
    
    def insert_login(self, details:Dict[str, Any]) -> bool: 
        try:
            with database.atomic() as tx:
                Login.create(**details)
                tx.commit()
                return True
        except Exception as e: 
            print(e)
        return False
    
    def change_password(self, details:Dict[str,Any]) -> bool: 
       try:
           with database.atomic() as tx:
                login = Login.get(Login.username==details["username"])
                login.password = details["password"]
                login.save()
                tx.commit()
                return True
       except Exception as e: 
           print(e)
       return False
   
    def delete_login(self, username:str) -> bool: 
        try:
           with database.atomic() as tx:
            login = Login.get(Login.username==username)
            login.delete_instance()
            tx.commit()
            return True
        except Exception as e: 
            print(e)
        return False
    

    def select_login_username(self, username:str): 
        login = Login.select(Login.username==username)
        return login.to_json()
    
    def select_all_login(self): 
        logins = Login.select()
        records = [log.to_json() for log in logins]
        return records
    
    