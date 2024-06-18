from app.models.db import Discount
from app.models.db import database
from app import conn_mgr
from typing import Dict, Any


class DiscountRepository:
    
    async def insert_discount(self, details:Dict[str, Any]) -> bool: 
        try:
            async with database.atomic_async() as tx:
                await conn_mgr.create(Discount, **details)
                await tx.commit()
                return True
        except Exception as e: 
            print(e)
        return False
    
    async def update_discount(self, details:Dict[str,Any]) -> bool: 
       try:
           async with database.atomic_async():
                discount = await conn_mgr.get(Discount, code=details["code"])
                discount.rate = details["rate"]
               
                await conn_mgr.update(discount, only=("rate", ))
                return True
       except Exception as e: 
           print(e)
       return False
   
    async def delete_discount_code(self, code:str) -> bool: 
        try:
           async with database.atomic_async():
            discount = await conn_mgr.get(Discount, code=code)
            await conn_mgr.delete(discount)
            return True
        except Exception as e: 
            print(e)
        return False
    
    async def delete_discount_id(self, id:int) -> bool: 
        try:
           async with database.atomic_async():
            discount = await conn_mgr.get(Discount, id=id)
            await conn_mgr.delete(discount)
            return True
        except Exception as e: 
            print(e)
        return False
    
    async def select_discount_code(self, code:str): 
        discount = await conn_mgr.get(Discount, code=code)
        return discount.to_json()
    
    async def select_discount_id(self, id:int): 
        discount = await conn_mgr.get(Discount, id=id)
        return discount.to_json()
    
    async def select_all_discount(self): 
        discounts = await conn_mgr.execute(Discount.select())
        records = [log.to_json() for log in discounts]
        return records
    
    