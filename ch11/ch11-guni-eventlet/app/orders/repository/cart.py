from app.models.db import Cart
from app.models.db import database
from typing import Dict, Any


class CartRepository:
    
    def insert_cart(self, details:Dict[str, Any]) -> bool: 
        try:
            with database.atomic() as tx:
                Cart.create(**details)
                tx.commit()
                return True
        except Exception as e: 
            print(e)
        return False
    
    def update_cart(self, details:Dict[str,Any]) -> bool: 
       try:
           with database.atomic() as tx:
                cart = Cart.get(Cart.code==details["orderid"])
                cart.ordered_date = details["ordered_date"]
                cart.ordered_by = details["ordered_by"]
                cart.total = details["total"]
               
                cart.save()
                tx.commit()
                return True
       except Exception as e: 
           print(e)
       return False
   
    def delete_cart_oid(self, orderid:str) -> bool: 
        try:
           with database.atomic() as tx:
            cart = Cart.get(Cart.orderid==orderid)
            cart.delete_instance()
            tx.commit()
            return True
        except Exception as e: 
            print(e)
        return False
    
    def delete_cart_id(self, id:int) -> bool: 
        try:
           with database.atomic() as tx:
            cart = Cart.get(Cart.id==id)
            cart.delete_instance()
            tx.commit()
            return True
        except Exception as e: 
            print(e)
        return False
    
    def select_cart_oid(self, orderid:str): 
        cart = Cart.select(Cart.orderid==orderid)
        return cart.to_json()
    
    def select_cart_id(self, id:int): 
        cart = Cart.select(Cart.id==id)
        return cart.to_json()
    
    def select_all_cart(self): 
        carts = Cart.select()
        records = [log.to_json() for log in carts]
        return records
    
    