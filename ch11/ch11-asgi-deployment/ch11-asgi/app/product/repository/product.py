from app.models.db import Product
from app.models.db import database
from app import conn_mgr
from typing import Dict, Any


class ProductRepository:
    
    async def insert_product(self, details:Dict[str, Any]) -> bool: 
        try:
            async with database.atomic_async() as tx:
                await conn_mgr.create(Product, **details)
                await tx.commit()
                return True
        except Exception as e: 
            print(e)
        return False
    
    async def update_product(self, details:Dict[str,Any]) -> bool: 
       try:
           async with database.atomic_async():
                prod = await conn_mgr.get(Product, code=details["code"])
                prod.rate = details["name"]
                prod.code = details["btype"]
                prod.rate = details["ctype"]
                prod.code = details["unit_type"]
                prod.rate = details["sell_price"]
                prod.code = details["purchase_price"]
                prod.rate = details["discount"]

               
                await conn_mgr.update(prod, only=("name", "btype", "ctype", "unit_type", "sell_price", "purchase_price", "discount"))
                return True
       except Exception as e: 
           print(e)
       return False
   
    async def delete_product_code(self, code:str) -> bool: 
        try:
           async with database.atomic_async():
            prod = await conn_mgr.get(Product, code=code)
            await conn_mgr.delete(prod)
            return True
        except Exception as e: 
            print(e)
        return False
    
    async def delete_product_id(self, id:int) -> bool: 
        try:
           async with database.atomic_async():
            prod = await conn_mgr.get(Product, id=id)
            await conn_mgr.delete(prod)
            return True
        except Exception as e: 
            print(e)
        return False
    
    async def select_product_code(self, code:str): 
        prod = await conn_mgr.get(Product, code=code)
        return prod.to_json()
    
    async def select_product_id(self, id:int): 
        prod = await conn_mgr.get(Product, id=id)
        return prod.to_json()
    
    async def select_all_product(self): 
        prods = await conn_mgr.execute(Product.select())
        records = [log.to_json() for log in prods]
        return records
    
    