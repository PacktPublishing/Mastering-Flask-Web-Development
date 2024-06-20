from app.models.db import Product
from app.models.db import database
from typing import Dict, Any


class ProductRepository:
    
    def insert_product(self, details:Dict[str, Any]) -> bool: 
        try:
            with database.atomic() as tx:
                Product.create(**details)
                tx.commit()
                return True
        except Exception as e: 
            print(e)
        return False
    
    def update_product(self, details:Dict[str,Any]) -> bool: 
       try:
           with database.atomic() as tx:
                prod = Product.get(Product.code==details["code"])
                prod.rate = details["name"]
                prod.code = details["btype"]
                prod.rate = details["ctype"]
                prod.code = details["unit_type"]
                prod.rate = details["sell_price"]
                prod.code = details["purchase_price"]
                prod.rate = details["discount"]

               
                prod.save()
                tx.commit()
                return True
       except Exception as e: 
           print(e)
       return False
   
    def delete_product_code(self, code:str) -> bool: 
        try:
           with database.atomic() as tx:
            prod = Product.get(Product.code==code)
            prod.delete_instance()
            tx.commit()
            return True
        except Exception as e: 
            print(e)
        return False
    
    def delete_product_id(self, id:int) -> bool: 
        try:
           with database.atomic() as tx:
            prod = Product.get(Product.id==id)
            prod.delete_instance()
            tx.commit()
            return True
        except Exception as e: 
            print(e)
        return False
    
    def select_product_code(self, code:str): 
        prod = Product.select(Product.code==code)
        return prod.to_json()
    
    def select_product_id(self, id:int): 
        prod = Product.select(Product.id==id)
        return prod.to_json()
    
    def select_all_product(self): 
        prods = Product.select()
        records = [log.to_json() for log in prods]
        return records
    
    