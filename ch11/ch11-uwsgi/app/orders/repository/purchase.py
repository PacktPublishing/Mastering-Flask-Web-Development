from app.models.db import Purchase
from app.models.db import database
from typing import Dict, Any


class PurchaseRepository:
    
    def insert_purchase(self, details:Dict[str, Any]) -> bool: 
        try:
            with database.atomic() as tx:
                Purchase.create(**details)
                tx.commit()
                return True
        except Exception as e: 
            print(e)
        return False
    
    def update_purchase(self, details:Dict[str,Any]) -> bool: 
       try:
           with database.atomic() as tx:
                purchase = Purchase.get(Purchase.code==details["id"])
                purchase.orderid = details["orderid"]
                purchase.payment_date = details["payment_date"]
                purchase.received_by = details["received_by"]
               
                purchase.save()
                tx.commit()
                return True
       except Exception as e: 
           print(e)
       return False
   
    def delete_purchase(self, id:int) -> bool: 
        try:
           with database.atomic() as tx:
            purchase = Purchase.get(Purchase.id==id)
            purchase.delete_instance()
            tx.commit()
            return True
        except Exception as e: 
            print(e)
        return False
    
    def select_purchase_id(self, id:int): 
        purchase = Purchase.select(Purchase.id==id)
        return purchase.to_json()
    
    def select_all_purchase(self): 
        purchases = Purchase.select()
        records = [log.to_json() for log in purchases]
        return records
    
    