from typing import Dict, Any
from modules.models.db.mongo_models import TutorLogin
import json


class TutorLoginRepository: 
    def insert_login(self, details:Dict[str, Any]) -> bool: 
        try:
            login = TutorLogin(**details)
            login.save()
            return True
        except Exception as e:
            print(e)
        return False
    
    def update_login(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
          login = TutorLogin.objects(id=id).get()
          login.update(**details)
       except: 
           return False 
       return True
   
    def delete_login(self, id:int) -> bool: 
        try:
            login = TutorLogin.objects(id=id).get()
            login.delete()
        except: 
            return False 
        return True
    
        
    def get_all_login(self):
        login = TutorLogin.objects()
        #records = [rec.to_json() for rec in login]
        return json.loads(login.to_json())
    
    def get_login(self, id:int): 
        login = TutorLogin.objects(id=id).get()
        return login.to_json()
    
    def get_login_username(self, username:str, password:str): 
        login = TutorLogin.objects(username=username, password=password).get()
        return login.to_json()