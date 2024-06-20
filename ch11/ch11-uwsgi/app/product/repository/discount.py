from app.models.db import Discount
from app.models.db import database
from typing import Dict, Any


class DiscountRepository:
    
    def insert_discount(self, details:Dict[str, Any]) -> bool: 
        try:
            with database.atomic() as tx:
                Discount.create(**details)
                tx.commit()
                return True
        except Exception as e: 
            print(e)
        return False
    
    def update_discount(self, details:Dict[str,Any]) -> bool: 
       try:
           with database.atomic() as tx:
                discount = Discount.get(Discount.code==details["code"])
                discount.rate = details["rate"]
               
                discount.save()
                return True
       except Exception as e: 
           print(e)
       return False
   
    def delete_discount_code(self, code:str) -> bool: 
        try:
           with database.atomic() as tx:
            discount = Discount.get(Discount.code==code)
            discount.delete_instance()
            tx.commit()
            return True
        except Exception as e: 
            print(e)
        return False
    
    def delete_discount_id(self, id:int) -> bool: 
        try:
           with database.atomic() as tx:
            discount = Discount.get(Discount.id==id)
            discount.delete_instance()
            tx.commit()
            return True
        except Exception as e: 
            print(e)
        return False
    
    def select_discount_code(self, code:str): 
        discount = Discount.select(Discount.code==code)
        return discount.to_json()
    
    def select_discount_id(self, id:int): 
        discount = Discount.get(Discount.id==id)
        return discount.to_json()
    
    def select_all_discount(self): 
        discounts = Discount.select()
        records = [log.to_json() for log in discounts]
        return records
    
    