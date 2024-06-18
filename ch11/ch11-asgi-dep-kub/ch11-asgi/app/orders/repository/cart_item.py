from app.models.db import CartItem
from app.models.db import database
from app import conn_mgr
from typing import Dict, Any


class CartItemRepository:
    
    async def insert_cart_item(self, details:Dict[str, Any]) -> bool: 
        try:
            async with database.atomic_async() as tx:
                await conn_mgr.create(CartItem, **details)
                await tx.commit()
                return True
        except Exception as e: 
            print(e)
        return False
    
    async def update_cart_item(self, details:Dict[str,Any]) -> bool: 
       try:
           async with database.atomic_async():
                cart_item = await conn_mgr.get(CartItem, code=details["id"])
                cart_item.orderid = details["orderid"]
                cart_item.pcode = details["pcode"]
                cart_item.qty = details["qty"]
               
                await conn_mgr.update(cart_item, only=("orderid", "pcode", "qty", ))
                return True
       except Exception as e: 
           print(e)
       return False
   
        
    async def delete_cart_item(self, id:int) -> bool: 
        try:
           async with database.atomic_async():
            cart_item = await conn_mgr.get(CartItem, id=id)
            await conn_mgr.delete(cart_item)
            return True
        except Exception as e: 
            print(e)
        return False
    
    async def select_cart_item(self, id:int): 
        cart_item = await conn_mgr.get(CartItem, id=id)
        return cart_item.to_json()
    
    async def select_cart_items_oid(self, orderid:str): 
        carts = await conn_mgr.execute(CartItem.select().where(CartItem.orderid == orderid))
        records = [log.to_json() for log in carts]
        return records
    
    async def select_all_cart_items(self): 
        carts = await conn_mgr.execute(CartItem.select())
        records = [log.to_json() for log in carts]
        return records
    
    