from ariadne import QueryType, MutationType
from typing import List, Any, Dict
from modules_sub_flask.models.db import Category
from sqlalchemy.orm import Session


query = QueryType()
mutation = MutationType()

class CategoryResolver:
    def __init__(self, sess:Session):
        self.sess = sess
    

    def insert_category(self, obj, info, name) -> bool:
        try:
            category = Category(name)
            self.sess.add(category)
            self.sess.commit()
            payload = {
                "success": True,
                "model": category
            }
        except Exception as e:
            print(e) 
            payload = {
                "success": False,
                "errors": [f"Category matching  not found"]
            }
        return payload
    
    def update_category(self, obj, info, id:int, details:Dict[str, Any]) -> bool:
        try:
            self.sess.query(Category).filter(Category.id == id).update(details)     
            self.sess.commit() 
            payload = {
                "success": True,
                "message": [f"Update Category succeeded."]
            }
           
        except Exception as e:
            print(e)
            payload = {
                "success": False,
                "errors": [f"Update Complainant found errors."]
            }
        return payload  
    
    def delete_category(self, obj, info, id:int) -> bool:
        try:
           self.sess.query(Category).filter(Category.id == id).delete()
           self.sess.commit()
           payload = {
                "success": True,
                "message": [f"Delete Category succeeded."]
            }
        except Exception as e:
            print(e)  
            payload = {
                "success": False,
                "errors": [f"Delete Category found errors."]
            }
        return payload
    
    def select_all_category(self, obj, info) -> List[Any]:
        categories = self.sess.query(Category).all()
    
        try:
            records = [todo.to_json() for todo in categories]
            print(records)
            payload = {
                "success": True,
                "categories": records
            }
        except Exception as e:
            print(e)
            payload = {
                "success": False,
                "errors": [str("Empty records")]
            }
        return payload
        
    
    def select_category(self, obj, info, id:int) -> Any:
        cat =  self.sess.query(Category).filter(Category.id == id).one_or_none()
        return cat