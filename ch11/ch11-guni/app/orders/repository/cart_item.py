from app.models.db import CartItem
from app.models.db import database
from typing import Dict, Any


class CartItemRepository:
    
    def insert_cart_item(self, details:Dict[str, Any]) -> bool: 
        try:
            with database.atomic() as tx:
                CartItem.create(**details)
                tx.commit()
                return True
        except Exception as e: 
            print(e)
        return False
    
    def update_cart_item(self, details:Dict[str,Any]) -> bool: 
       try:
           with database.atomic() as tx:
                cart_item = CartItem.get(CartItem.code==details["id"])
                cart_item.orderid = details["orderid"]
                cart_item.pcode = details["pcode"]
                cart_item.qty = details["qty"]
               
                cart_item.save()
                tx.commit()
                return True
       except Exception as e: 
           print(e)
       return False
   
        
    def delete_cart_item(self, id:int) -> bool: 
        try:
           with database.atomic() as tx:
            cart_item = CartItem.get(CartItem.id==id)
            cart_item.delete_instance()
            tx.commit()
            return True
        except Exception as e: 
            print(e)
        return False
    
    def select_cart_item(self, id:int): 
        cart_item = CartItem.select(CartItem.id==id)
        return cart_item.to_json()
    
    def select_cart_items_oid(self, orderid:str): 
        carts = CartItem.select(CartItem.orderid == orderid)
        records = [log.to_json() for log in carts]
        return records
    
    def select_all_cart_items(self): 
        carts = CartItem.select()
        records = [log.to_json() for log in carts]
        return records
    
    