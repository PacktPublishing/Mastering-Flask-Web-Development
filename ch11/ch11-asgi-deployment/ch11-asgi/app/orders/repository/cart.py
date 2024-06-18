from app.models.db import Cart
from app.models.db import database
from app import conn_mgr
from typing import Dict, Any


class CartRepository:
    
    async def insert_cart(self, details:Dict[str, Any]) -> bool: 
        try:
            async with database.atomic_async() as tx:
                await conn_mgr.create(Cart, **details)
                await tx.commit()
                return True
        except Exception as e: 
            print(e)
        return False
    
    async def update_cart(self, details:Dict[str,Any]) -> bool: 
       try:
           async with database.atomic_async():
                cart = await conn_mgr.get(Cart, code=details["orderid"])
                cart.ordered_date = details["ordered_date"]
                cart.ordered_by = details["ordered_by"]
                cart.total = details["total"]
               
                await conn_mgr.update(cart, only=("ordered_date", "ordered_by", "total", ))
                return True
       except Exception as e: 
           print(e)
       return False
   
    async def delete_cart_oid(self, orderid:str) -> bool: 
        try:
           async with database.atomic_async():
            cart = await conn_mgr.get(Cart, orderid=orderid)
            await conn_mgr.delete(cart)
            return True
        except Exception as e: 
            print(e)
        return False
    
    async def delete_cart_id(self, id:int) -> bool: 
        try:
           async with database.atomic_async():
            cart = await conn_mgr.get(Cart, id=id)
            await conn_mgr.delete(cart)
            return True
        except Exception as e: 
            print(e)
        return False
    
    async def select_cart_oid(self, orderid:str): 
        cart = await conn_mgr.get(Cart, orderid=orderid)
        return cart.to_json()
    
    async def select_cart_id(self, id:int): 
        cart = await conn_mgr.get(Cart, id=id)
        return cart.to_json()
    
    async def select_all_cart(self): 
        carts = await conn_mgr.execute(Cart.select())
        records = [log.to_json() for log in carts]
        return records
    
    