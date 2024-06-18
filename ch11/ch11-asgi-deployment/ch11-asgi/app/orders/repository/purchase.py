from app.models.db import Purchase
from app.models.db import database
from app import conn_mgr
from typing import Dict, Any


class PurchaseRepository:
    
    async def insert_purchase(self, details:Dict[str, Any]) -> bool: 
        try:
            async with database.atomic_async() as tx:
                await conn_mgr.create(Purchase, **details)
                await tx.commit()
                return True
        except Exception as e: 
            print(e)
        return False
    
    async def update_purchase(self, details:Dict[str,Any]) -> bool: 
       try:
           async with database.atomic_async():
                purchase = await conn_mgr.get(Purchase, code=details["id"])
                purchase.orderid = details["orderid"]
                purchase.payment_date = details["payment_date"]
                purchase.received_by = details["received_by"]
               
                await conn_mgr.update(purchase, only=("orderid", "payment_date", "received_by", ))
                return True
       except Exception as e: 
           print(e)
       return False
   
    async def delete_purchase(self, id:int) -> bool: 
        try:
           async with database.atomic_async():
            purchase = await conn_mgr.get(Purchase, id=id)
            await conn_mgr.delete(purchase)
            return True
        except Exception as e: 
            print(e)
        return False
    
    async def select_purchase_id(self, id:int): 
        purchase = await conn_mgr.get(Purchase, id=id)
        return purchase.to_json()
    
    async def select_all_purchase(self): 
        purchases = await conn_mgr.execute(Purchase.select())
        records = [log.to_json() for log in purchases]
        return records
    
    