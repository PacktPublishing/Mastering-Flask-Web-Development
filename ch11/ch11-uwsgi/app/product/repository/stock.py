from app.models.db import Stock
from app.models.db import database
from typing import Dict, Any


class StockRepository:
    
    def insert_stock(self, details:Dict[str, Any]) -> bool: 
        try:
            with database.atomic() as tx:
                Stock.create(**details)
                tx.commit()
                return True
        except Exception as e: 
            print(e)
        return False
    
    def update_stock(self, details:Dict[str,Any]) -> bool: 
       try:
           with database.atomic() as tx:
                stock = Stock.get(Stock.code==details["sid"])
                stock.invcode = details["invcode"]
                stock.qty = details["qty"]
                stock.payment_date = details["payment_date"]
                stock.received_date = details["received_date"]
                stock.recieved_by = details["recieved_by"]
                               
                stock.save()
                tx.commit()
                return True
       except Exception as e: 
           print(e)
       return False
   
    def delete_stock_sid(self, sid:str) -> bool: 
        try:
           with database.atomic() as tx:
            stock = Stock.get(Stock.sid==sid)
            stock.delete_instance()
            tx.commit()
            return True
        except Exception as e: 
            print(e)
        return False
    
    def delete_stock_id(self, id:int) -> bool: 
        try:
          with database.atomic() as tx:
            stock = Stock.get(Stock.id==id)
            stock.delete_instance()
            tx.commit()
            return True
        except Exception as e: 
            print(e)
        return False
    
    def select_stock_sid(self, sid:str): 
        stock = Stock.select(Stock.sid==sid)
        return stock.to_json()
    
    def select_stock_id(self, id:int): 
        stock = Stock.select(Stock.id==id)
        return stock.to_json()
    
    def select_all_stock(self): 
        stocks = Stock.select()
        records = [log.to_json() for log in stocks]
        return records
    
    