from app.models.db import Category
from app.models.db import database
from app import conn_mgr
from typing import Dict, Any


class CategoryRepository:
    
    async def insert_category(self, details:Dict[str, Any]) -> bool: 
        try:
            async with database.atomic_async() as tx:
                await conn_mgr.create(Category, **details)
                await tx.commit()
                return True
        except Exception as e: 
            print(e)
        return False
    
    async def update_category(self, details:Dict[str,Any]) -> bool: 
       try:
           async with database.atomic_async():
                category = await conn_mgr.get(Category, code=details["code"])
                category.name = details["name"]
                category.description = details["description"]
               
                await conn_mgr.update(category, only=("name", "description", ))
                return True
       except Exception as e: 
           print(e)
       return False
   
    async def delete_category_code(self, code:str) -> bool: 
        try:
           async with database.atomic_async():
            category = await conn_mgr.get(Category, code=code)
            await conn_mgr.delete(category)
            return True
        except Exception as e: 
            print(e)
        return False
    
    async def delete_category_id(self, id:int) -> bool: 
        try:
           async with database.atomic_async():
            category = await conn_mgr.get(Category, id=id)
            await conn_mgr.delete(category)
            return True
        except Exception as e: 
            print(e)
        return False
    
    async def select_category_code(self, code:str): 
        category = await conn_mgr.get(Category, code=code)
        return category.to_json()
    
    async def select_category_id(self, id:int): 
        category = await conn_mgr.get(Category, id=id)
        return category.to_json()
    
    async def select_all_category(self): 
        cats = await conn_mgr.execute(Category.select())
        records = [log.to_json() for log in cats]
        return records
    
    