from app.models.db import Brand
from app.models.db import database
from app import conn_mgr
from typing import Dict, Any


class BrandRepository:
    
    async def insert_brand(self, details:Dict[str, Any]) -> bool: 
        try:
            async with database.atomic_async() as tx:
                await conn_mgr.create(Brand, **details)
                await tx.commit()
                return True
        except Exception as e: 
            print(e)
        return False
    
    async def update_brand(self, details:Dict[str,Any]) -> bool: 
       try:
           async with database.atomic_async():
                brand = await conn_mgr.get(Brand, code=details["code"])
                brand.name = details["name"]
                brand.description = details["description"]
               
                await conn_mgr.update(brand, only=("name", "description", ))
                return True
       except Exception as e: 
           print(e)
       return False
   
    async def delete_brand_code(self, code:str) -> bool: 
        try:
           async with database.atomic_async():
            brand = await conn_mgr.get(Brand, code=code)
            await conn_mgr.delete(brand)
            return True
        except Exception as e: 
            print(e)
        return False
    
    async def delete_brand_id(self, id:int) -> bool: 
        try:
           async with database.atomic_async():
            brand = await conn_mgr.get(Brand, id=id)
            await conn_mgr.delete(brand)
            return True
        except Exception as e: 
            print(e)
        return False
    
    async def select_brand_code(self, code:str): 
        brand = await conn_mgr.get(Brand, code=code)
        return brand.to_json()
    
    async def select_brand_id(self, id:int): 
        brand = await conn_mgr.get(Brand, id=id)
        return brand.to_json()
    
    async def select_all_brand(self): 
        brands = await conn_mgr.execute(Brand.select())
        records = [log.to_json() for log in brands]
        return records
    
    