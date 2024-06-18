from app.models.db import Category
from app.models.db import database
from typing import Dict, Any


class CategoryRepository:
    
    def insert_category(self, details:Dict[str, Any]) -> bool: 
        try:
            with database.atomic() as tx:
                Category.create(**details)
                tx.commit()
                return True
        except Exception as e: 
            print(e)
        return False
    
    def update_category(self, details:Dict[str,Any]) -> bool: 
       try:
           with database.atomic() as tx:
                category = Category.get(Category.code==details["code"])
                category.name = details["name"]
                category.description = details["description"]
               
                category.save()
                tx.commit()
                return True
       except Exception as e: 
           print(e)
       return False
   
    def delete_category_code(self, code:str) -> bool: 
        try:
           with database.atomic() as tx:
            category = Category.get(Category.code==code)
            category.delete_instance()
            tx.commit()
            return True
        except Exception as e: 
            print(e)
        return False
    
    def delete_category_id(self, id:int) -> bool: 
        try:
           with database.atomic() as tx:
            category = Category.get(Category.id==id)
            category.delete_instance()
            tx.commit()
            return True
        except Exception as e: 
            print(e)
        return False
    
    def select_category_code(self, code:str): 
        category = Category.select(Category.code==code)
        return category.to_json()
    
    def select_category_id(self, id:int): 
        category = Category.get(Category.id==id)
        return category.to_json()
    
    def select_all_category(self): 
        cats = Category.select()
        records = [log.to_json() for log in cats]
        return records
    
    