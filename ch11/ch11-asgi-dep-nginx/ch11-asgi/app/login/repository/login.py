from app.models.db import Login
from app.models.db import database
from app import conn_mgr
from typing import Dict, Any
import asyncio

class LoginRepository:
    
    async def insert_login(self, details:Dict[str, Any]) -> bool: 
        try:
            async with database.atomic_async() as tx:
                await conn_mgr.create(Login, **details)
                await tx.commit()
                return True
        except Exception as e: 
            print(e)
        return False
    
    async def change_password(self, details:Dict[str,Any]) -> bool: 
       try:
           async with database.atomic_async():
                login = await conn_mgr.get(Login, username=details["username"])
                login.password = details["password"]
                await conn_mgr.update(login, only=("password",))
                return True
       except Exception as e: 
           print(e)
       return False
   
    async def delete_login(self, username:str) -> bool: 
        try:
           async with database.atomic_async():
            login = await conn_mgr.get(Login, username=username)
            await conn_mgr.delete(login)
            return True
        except Exception as e: 
            print(e)
        return False
    

    async def select_login_username(self, username:str): 
        login = await conn_mgr.get(Login, username=username)
        return login.to_json()
    
    async def select_all_login(self): 
        logins = await conn_mgr.execute(Login.select())
        records = [log.to_json() for log in logins]
        return records
    
    