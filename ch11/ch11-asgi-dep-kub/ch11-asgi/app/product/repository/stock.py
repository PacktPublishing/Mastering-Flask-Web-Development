from app.models.db import Stock
from app.models.db import database
from app import conn_mgr
from typing import Dict, Any


class StockRepository:
    
    async def insert_stock(self, details:Dict[str, Any]) -> bool: 
        try:
            async with database.atomic_async() as tx:
                await conn_mgr.create(Stock, **details)
                await tx.commit()
                return True
        except Exception as e: 
            print(e)
        return False
    
    async def update_stock(self, details:Dict[str,Any]) -> bool: 
       try:
           async with database.atomic_async():
                stock = await conn_mgr.get(Stock, code=details["sid"])
                stock.invcode = details["invcode"]
                stock.qty = details["qty"]
                stock.payment_date = details["payment_date"]
                stock.received_date = details["received_date"]
                stock.recieved_by = details["recieved_by"]
                               
                await conn_mgr.update(stock, only=("invcode", "qty", "payment_date", "received_date", "recieved_by",))
                return True
       except Exception as e: 
           print(e)
       return False
   
    async def delete_stock_sid(self, sid:str) -> bool: 
        try:
           async with database.atomic_async():
            stock = await conn_mgr.get(Stock, sid=sid)
            await conn_mgr.delete(stock)
            return True
        except Exception as e: 
            print(e)
        return False
    
    async def delete_stock_id(self, id:int) -> bool: 
        try:
           async with database.atomic_async():
            stock = await conn_mgr.get(Stock, id=id)
            await conn_mgr.delete(stock)
            return True
        except Exception as e: 
            print(e)
        return False
    
    async def select_stock_sid(self, sid:str): 
        stock = await conn_mgr.get(Stock, sid=sid)
        return stock.to_json()
    
    async def select_stock_id(self, id:int): 
        stock = await conn_mgr.get(Stock, id=id)
        return stock.to_json()
    
    async def select_all_stock(self): 
        stocks = await conn_mgr.execute(Stock.select())
        records = [log.to_json() for log in stocks]
        return records
    
    