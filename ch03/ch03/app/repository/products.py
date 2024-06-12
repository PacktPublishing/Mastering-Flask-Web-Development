from typing import List, Any, Dict
from app.model.db import Category, Pizza, NonPizza, AddOns
from flask import current_app
from sqlalchemy.orm import Session

class CategoryRepository:
    def __init__(self, sess:Session):
        self.sess = sess
        current_app.logger.info('CategoryRepository instance created')
        
    def insert(self, cat:Category) -> bool:
        try:
            self.sess.add(cat)
            self.sess.commit()
            current_app.logger.info('CategoryRepository inserted record')
            return True
        except Exception as e:
            current_app.logger.error(f'CategoryRepository insert error: {e}') 
        return False
    
    def update(self, id:int, details:Dict[str, Any]) -> bool:
        try:
            self.sess.query(Category).filter(Category.id == id).update(details)     
            self.sess.commit() 
            current_app.logger.info('CategoryRepository updated record')
            return True
        except Exception as e:
            current_app.logger.error(f'CategoryRepository insert error: {e}') 
        return False  
    
    def delete(self, id:int) -> bool:
        try:
           login = self.sess.query(Category).filter(Category.id == id).delete()
           self.sess.commit()
           current_app.logger.info('CategoryRepository deleted record')
           return True
        except Exception as e:
            current_app.logger.error(f'CategoryRepository insert error: {e}') 
        return False
    
    def select_all(self) -> List[Any]:
        cats = self.sess.query(Category).all()
        return cats
         
    def select_one(self, id:int) -> Any:
        cat =  self.sess.query(Category).filter(Category.id == id).one_or_none()
        return cat
    
class PizzaRepository():
    def __init__(self, sess:Session):
        self.sess = sess
        current_app.logger.info('PizzaRepository instance created')
        
    def insert(self, piz:Pizza) -> bool:
        try:
            self.sess.add(piz)
            self.sess.commit()
            current_app.logger.info('PizzaRepository inserted record')
            return True
        except Exception as e:
            current_app.logger.error(f'PizzaRepository insert error: {e}') 
        return False
    
    def update(self, code:str, details:Dict[str, Any]) -> bool:
        try:
            self.sess.query(Pizza).filter(Pizza.code == code).update(details)     
            self.sess.commit() 
            current_app.logger.info('PizzaRepository updated record')
            return True
        except Exception as e:
            current_app.logger.error(f'PizzaRepository insert error: {e}') 
        return False  
    
    def delete(self, code:str) -> bool:
        try:
           login = self.sess.query(Pizza).filter(Pizza.code == code).delete()
           self.sess.commit()
           current_app.logger.info('PizzaRepository deleted record')
           return True
        except Exception as e:
            current_app.logger.error(f'PizzaRepository insert error: {e}') 
        return False
    
    def select_all(self) -> List[Any]:
        pizzas = self.sess.query(Pizza).all()
        return pizzas
         
    
    def select_one(self, code:str) -> Any:
        pizza =  self.sess.query(Pizza).filter(Pizza.code == code).one_or_none()
        return pizza

class NonPizzaRepository():
    def __init__(self, sess:Session):
        self.sess = sess
        current_app.logger.info('NonPizzaRepository instance created')
        
    def insert(self, npiz:NonPizza) -> bool:
        try:
            self.sess.add(npiz)
            self.sess.commit()
            current_app.logger.info('NonPizzaRepository inserted record')
            return True
        except Exception as e:
            current_app.logger.error(f'NonPizzaRepository insert error: {e}') 
        return False
    
    def update(self, code:str, details:Dict[str, Any]) -> bool:
        try:
            self.sess.query(NonPizza).filter(NonPizza.code == code).update(details)     
            self.sess.commit() 
            current_app.logger.info('NonPizzaRepository updated record')
            return True
        except Exception as e:
            current_app.logger.error(f'NonPizzaRepository insert error: {e}') 
        return False  
    
    def delete(self, code:str) -> bool:
        try:
           login = self.sess.query(NonPizza).filter(NonPizza.code == code).delete()
           self.sess.commit()
           current_app.logger.info('NonPizzaRepository deleted record')
           return True
        except Exception as e:
            current_app.logger.error(f'NonPizzaRepository insert error: {e}') 
        return False
    
    def select_all(self) -> List[Any]:
        npizzas = self.sess.query(NonPizza).all()
        return npizzas
         
    
    def select_one(self, code:str) -> Any:
        npizza =  self.sess.query(NonPizza).filter(NonPizza.code == code).one_or_none()
        return npizza
    
class AddOnsRepository():
    def __init__(self, sess:Session):
        self.sess = sess
        current_app.logger.info('AddOnsRepository instance created')
        
    def insert(self, addons:AddOns) -> bool:
        try:
            self.sess.add(addons)
            self.sess.commit()
            current_app.logger.info('AddOnsRepository inserted record')
            return True
        except Exception as e:
            current_app.logger.error(f'AddOnsRepository insert error: {e}') 
        return False
    
    def update(self, code:str, details:Dict[str, Any]) -> bool:
        try:
            self.sess.query(AddOns).filter(AddOns.code == code).update(details)     
            self.sess.commit() 
            current_app.logger.info('AddOnsRepository updated record')
            return True
        except Exception as e:
            current_app.logger.error(f'AddOnsRepository insert error: {e}') 
        return False  
    
    def delete(self, code:str) -> bool:
        try:
           login = self.sess.query(AddOns).filter(AddOns.code == code).delete()
           self.sess.commit()
           current_app.logger.info('AddOnsRepository deleted record')
           return True
        except Exception as e:
            current_app.logger.error(f'AddOnsRepository insert error: {e}') 
        return False
    
    def select_all(self) -> List[Any]:
        addons = self.sess.query(AddOns).all()
        return addons
             
    def select_one(self, code:str) -> Any:
        addon =  self.sess.query(AddOns).filter(AddOns.code == code).one_or_none()
        return addon