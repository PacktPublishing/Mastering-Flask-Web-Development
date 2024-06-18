from app.models.db import Administrator
from app.models.db import database
from app import conn_mgr
from typing import Dict, Any


class AdminRepository:
    
    async def insert_admin(self, details:Dict[str, Any]) -> bool: 
        try:
            async with database.atomic_async() as tx:
                await conn_mgr.create(Administrator, **details)
                await tx.commit()
                return True
        except Exception as e: 
            print(e)
        return False
    
    async def update_admin(self, details:Dict[str,Any]) -> bool: 
       try:
           async with database.atomic_async():
                admin = await conn_mgr.get(AdminRepository, username=details["username"])
                admin.empid = details["empid"]
                admin.firstname = details["firstname"]
                admin.lastname = details["lastname"]
                admin.position = details["position"]
                admin.email = details["email"]
                admin.mobile = details["mobile"]
                admin.enrolled_date = details["enrolled_date"]
                
                await conn_mgr.update(admin, only=("empid", "firstname", "lastname", "position", "email", "mobile", "enrolled_date"))
                return True
       except Exception as e: 
           print(e)
       return False
   
    async def delete_admin_username(self, username:str) -> bool: 
        try:
           async with database.atomic_async():
            admin = await conn_mgr.get(Administrator, username=username)
            await conn_mgr.delete(admin)
            return True
        except Exception as e: 
            print(e)
        return False
    
    async def delete_admin_id(self, empid:str) -> bool: 
        try:
           async with database.atomic_async():
            admin = await conn_mgr.get(Administrator, empid=empid)
            await conn_mgr.delete(admin)
            return True
        except Exception as e: 
            print(e)
        return False
    
    async def select_admin_username(self, username:str): 
        admin = await conn_mgr.get(Administrator, username=username)
        return admin.to_json()
    
    async def select_admin_empid(self, empid:str): 
        admin = await conn_mgr.get(Administrator, empid=empid)
        return admin.to_json()
    
    async def select_all_admin(self): 
        admins = await conn_mgr.execute(Administrator.select())
        records = [log.to_json() for log in admins]
        return records
    
    