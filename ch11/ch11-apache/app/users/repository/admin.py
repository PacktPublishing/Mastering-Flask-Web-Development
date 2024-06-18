from app.models.db import Administrator
from app.models.db import database
from typing import Dict, Any


class AdminRepository:
    
    def insert_admin(self, details:Dict[str, Any]) -> bool: 
        try:
            with database.atomic() as tx:
                Administrator.create(**details)
                tx.commit()
                return True
        except Exception as e: 
            print(e)
        return False
    
    def update_admin(self, details:Dict[str,Any]) -> bool: 
       try:
           with database.atomic() as tx:
                admin = Administrator.get(Administrator.username==details["username"])
                admin.empid = details["empid"]
                admin.firstname = details["firstname"]
                admin.lastname = details["lastname"]
                admin.position = details["position"]
                admin.email = details["email"]
                admin.mobile = details["mobile"]
                admin.enrolled_date = details["enrolled_date"]
                
                admin.save()
                tx.commit()
                return True
       except Exception as e: 
           print(e)
       return False
   
    def delete_admin_username(self, username:str) -> bool: 
        try:
           with database.atomic() as tx:
            admin = Administrator.get(Administrator.username==username)
            admin.delete_instance()
            tx.commit()
            return True
        except Exception as e: 
            print(e)
        return False
    
    def delete_admin_id(self, empid:str) -> bool: 
        try:
           with database.atomic() as tx:
            admin = Administrator.select(Administrator.empid==empid)
            admin.delete_instance()
        except Exception as e: 
            print(e)
        return False
    
    def select_admin_username(self, username:str): 
        admin = Administrator.select(Administrator.username==username)
        return admin.to_json()
    
    def select_admin_empid(self, empid:str): 
        admin = Administrator.select(Administrator.empid==empid)
        return admin.to_json()
    
    def select_all_admin(self): 
        admins = Administrator.select()
        records = [log.to_json() for log in admins]
        return records
    
    