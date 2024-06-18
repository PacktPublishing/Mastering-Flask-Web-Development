from app.models.db import Brand
from app.models.db import database
from typing import Dict, Any


class BrandRepository:
    
    def insert_brand(self, details:Dict[str, Any]) -> bool: 
        try:
            with database.atomic() as tx:
                Brand.create(**details)
                tx.commit()
                return True
        except Exception as e: 
            print(e)
        return False
    
    def update_brand(self, details:Dict[str,Any]) -> bool: 
       try:
           with database.atomic() as tx:
                brand = Brand.get(Brand.code==details["code"])
                brand.name = details["name"]
                brand.description = details["description"]
               
                brand.save()
                tx.commit()
                return True
       except Exception as e: 
           print(e)
       return False
   
    def delete_brand_code(self, code:str) -> bool: 
        try:
          with database.atomic() as tx:
            brand = Brand.get(Brand.code==code)
            brand.delete_instance()
            tx.commit()
            return True
        except Exception as e: 
            print(e)
        return False
    
    def delete_brand_id(self, id:int) -> bool: 
        try:
           with database.atomic() as tx:
            brand = Brand.get(Brand.id==id)
            brand.delete_instance()
            tx.commit()
            return True
        except Exception as e: 
            print(e)
        return False
    
    def select_brand_code(self, code:str): 
        brand = Brand.select(Brand.code==code)
        return brand.to_json()
    
    def select_brand_id(self, id:int): 
        brand = Brand.select(Brand.id==id)
        return brand.to_json()
    
    def select_all_brand(self): 
        brands = Brand.select()
        records = [log.to_json() for log in brands]
        return records
    
    