from sqlalchemy import Time, Column, ForeignKey, Integer, String, Float, Date, Sequence
from sqlalchemy.orm import relationship
from app.model.config import Base

class Login(Base):
   __tablename__ = 'login'
   id = Column(Integer, Sequence('login_id_seq', increment=1), primary_key = True)
   username = Column(String(45), unique=True, nullable=False)
   password = Column(String(45), nullable=False)  
   
   employee = relationship('Employee', back_populates="login", uselist=False)
   customer = relationship('Customer', back_populates="login", uselist=False)

   def __init__(self, username, password, id = None):
      self.id = id
      self.username = username
      self.password = password
      
   def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "password" : self.password
            
        }
     

   def __repr__(self):
        return f"<Login {self.id} {self.username} {self.password}>"
     
class Customer(Base):
   __tablename__ = 'customer'
   id = Column(Integer, Sequence('customer_id_seq', increment=1), primary_key = True)
   cid = Column(String(45), ForeignKey('login.username'), unique=True, nullable=False)
   fname = Column(String(45), nullable=False)  
   mname = Column(String(45), nullable=False)
   lname = Column(String(45), nullable=False)
   age = Column(Integer, nullable=False)
   date_registered = Column(Date, nullable=False)
   status = Column(String(25), nullable=False)
   date_approved = Column(Date, nullable=False)
   
   login = relationship('Login', back_populates="customer")
   payments = relationship('Payment', back_populates="customer")
   orders = relationship('Orders', back_populates="customer")
      
   def __init__(self, cid, fname, mname, lname, age, date_registered, status, date_approved, id = None):
      self.id = id
      self.cid = cid
      self.fname = fname
      self.mname = mname
      self.lname = lname
      self.age = age
      self.date_registered = date_registered
      self.status = status
      self.date_approved = date_approved
      
   def to_json(self):
        return {
            "id": self.id,
            "cid": self.cid,
            "fname" : self.fname,
            "mname" : self.mname,
            "lname" : self.lname,
            "age": self.age,
            "date_registered": self.date_registered,
            "status": self.status,
            "date_approved":  self.date_approved
            
        }
      
   def __repr__(self):
        return f"<Customer {self.id} {self.fname} {self.mname} {self.lname} {self.status}>"

class Employee(Base):
   __tablename__ = 'employee'
   id = Column(Integer, Sequence('employee_id_seq', increment=1), primary_key = True)
   empid = Column(String(45), ForeignKey('login.username'), unique=True, nullable=False)
   fname = Column(String(45), nullable=False)  
   mname = Column(String(45), nullable=False)
   lname = Column(String(45), nullable=False)
   age = Column(Integer, nullable=False)
   salary = Column(Float, nullable=False)
   role = Column(String(45), nullable=False)
   date_employed = Column(Date, nullable=False)
   status = Column(String(25), nullable=False)
  
   
   login = relationship('Login', back_populates="employee")
   payments = relationship('Payment', back_populates="employee")
   orders = relationship('Orders', back_populates="employee")
      
   def __init__(self, fname, mname, lname, empid=None, age=None, salary=None, role=None, date_employed=None, status=None, id = None):
      self.id = id
      self.empid = empid
      self.fname = fname
      self.mname = mname
      self.lname = lname
      self.age = age
      self.salary = salary
      self.role = role
      self.date_employed = date_employed
      self.status = status
      
   def to_json(self):
        return {
            "id": self.id,
            "empid": self.empid,
            "fname" : self.fname,
            "mname" : self.mname,
            "lname" : self.lname,
            "age": self.age,
            "salary": self.salary,
            "role": self.role,
            "date_employed":  self.date_employed,
            "status": self.status
            
        }
      
   def __repr__(self):
        return f"<Employee {self.id} {self.fname} {self.mname} {self.lname} {self.status}>"
     
class Payment(Base):
    __tablename__ = 'payment'
    id = Column(Integer, Sequence('payment_id_seq', increment=1), primary_key = True)
    pid = Column(String(45), unique=True, nullable=False)
    empid = Column(String(45), ForeignKey('employee.empid'), nullable=False)  
    total = Column(Float, nullable=False)
    date_paid = Column(Date, nullable=False)
    status = Column(String(25), nullable=False)
    cid = Column(String(45), ForeignKey('customer.cid'), nullable=False)
    oid = Column(String(45), ForeignKey('orders.oid'), nullable=False)
    
    employee = relationship('Employee', back_populates="payments")
    customer = relationship('Customer', back_populates="payments")
    order = relationship('Orders', back_populates="payment")
    
    def __init__(self, pid, empid, total, date_paid, status, cid, oid, id = None):
      self.id = id
      self.pid = pid
      self.empid = empid
      self.total = total
      self.date_paid = date_paid
      self.status = status
      self.cid = cid
      self.oid = oid
      
    def to_json(self):
        return {
            "id": self.id,
            "pid": self.pid,
            "empid" : self.empid,
            "total": self.total,
            "date_paid": self.date_paid,
            "status": self.status,
            "cid":  self.cid,
            "oid":  self.oid
            
        }
        
          
    def __repr__(self):
        return f"<Payment {self.id} {self.pid} {self.empid} {self.cid} {self.oid} {self.total} {self.date_paid}>"
    
class Orders(Base):
    __tablename__ = 'orders'
    id = Column(Integer, Sequence('orders_id_seq', increment=1), primary_key = True)
    date_ordered = Column(Date, nullable=False)
    empid = Column(String(45), ForeignKey('employee.empid'), nullable=False)  
    cid = Column(String(45), ForeignKey('customer.cid'), nullable=False)
    oid = Column(String(45), unique=True, nullable=False)
    
    payment = relationship('Payment', back_populates="order")
    customer = relationship('Customer', back_populates="orders")
    employee = relationship('Employee', back_populates="orders")
    order_details = relationship('OrderDetails', back_populates="order")
    
    def __init__(self, date_ordered, empid, cid, oid, id = None):
      self.id = id
      self.date_ordered = date_ordered
      self.empid = empid
      self.cid = cid
      self.oid = oid
      
    def to_json(self):
        return {
            "id": self.id,
            "date_ordered": self.date_ordered,
            "empid" : self.empid,
            "cid" : self.cid,
            "oid" : self.oid
            
        }
                
    def __repr__(self):
        return f"<Orders {self.id} {self.date_ordered} {self.empid} {self.cid} {self.oid}>"
    

class OrderDetails(Base):
    __tablename__ = 'order_details'
    id = Column(Integer, Sequence('order_details_id_seq', increment=1), primary_key = True)
    oid = Column(String(45), ForeignKey('orders.oid'), nullable=False)
    code_pizza = Column(String(45), ForeignKey('pizza.code'), nullable=False)  
    code_nonpizza = Column(String(45), ForeignKey('nonpizza.code'), nullable=False)  
    code_addons = Column(String(45),  ForeignKey('addons.code'), nullable=False)  
    qty = Column(Integer, nullable=False)
    
    order = relationship('Orders', back_populates="order_details")
    pizza = relationship('Pizza', back_populates="order_details")
    nonpizza = relationship('NonPizza', back_populates="order_details")
    addons = relationship('AddOns', back_populates="order_details")
    
    def __init__(self, oid, code_pizza, code_nonpizza, code_addons, qty, id = None):
      self.id = id
      self.oid = oid
      self.code_pizza = code_pizza
      self.code_nonpizza = code_nonpizza
      self.code_addons = code_addons
      self.qty = qty
      
    def to_json(self):
        return {
            "id": self.id,
            "oid": self.oid,
            "code_pizza" : self.code_pizza,
            "code_nonpizza" : self.code_nonpizza,
            "code_addons" : self.code_addons,
            "qty" : self.qty
            
        }
                
    def __repr__(self):
        return f"<OrderDetails {self.id} {self.oid} >"

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, Sequence('category_id_seq', increment=1), primary_key = True)
    name = Column(String(45), nullable=False)
    description = Column(String(100), nullable=False)  
    
    pizza = relationship('Pizza', back_populates="category")
    nonpizza = relationship('NonPizza', back_populates="category")
    addons = relationship('AddOns', back_populates="category")
    
    def __init__(self, name, description, id = None):
      self.id = id
      self.name = name
      self.description = description
      
    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description" : self.description
            
        }
                   
    def __repr__(self):
        return f"<Category {self.id} {self.name} {self.description} >"


class Pizza(Base):
    __tablename__ = 'pizza'
    id = Column(Integer, Sequence('pizza_id_seq', increment=1), primary_key = True)
    code = Column(String(45), unique=True, nullable=False)
    name = Column(String(45), nullable=False)  
    price = Column(Integer, nullable=False)
    catid = Column(Integer, ForeignKey('category.id'), nullable=False)
    
    order_details = relationship('OrderDetails', back_populates="pizza")
    category = relationship('Category', back_populates="pizza")
    
    def __init__(self, code, name, price, catid, id = None):
      self.id = id
      self.code = code
      self.name = name
      self.price = price
      self.catid = catid
      
    def to_json(self):
        return {
            "id": self.id,
            "code": self.code,
            "name": self.name,
            "price" : self.price,
            "catid" : self.catid
            
        }
                   
    def __repr__(self):
        return f"<Pizza {self.id} {self.code} {self.name} {self.price} {self.catid}>"
    
    
class NonPizza(Base):
    __tablename__ = 'nonpizza'
    id = Column(Integer, Sequence('nonpizza_id_seq', increment=1), primary_key = True)
    code = Column(String(45), unique=True, nullable=False)
    name = Column(String(45), nullable=False)  
    price = Column(Integer, nullable=False)
    catid = Column(Integer, ForeignKey('category.id'), nullable=False)
    
    order_details = relationship('OrderDetails', back_populates="nonpizza")
    category = relationship('Category', back_populates="nonpizza")
    
    def __init__(self, code, name, price, catid, id = None):
      self.id = id
      self.code = code
      self.name = name
      self.price = price
      self.catid = catid
    
    def to_json(self):
        return {
            "id": self.id,
            "code": self.code,
            "name": self.name,
            "price" : self.price,
            "catid" : self.catid
            
        }
                   
    def __repr__(self):
        return f"<NonPizza {self.id} {self.code} {self.name} {self.price} {self.catid}>"
    
class AddOns(Base):
    __tablename__ = 'addons'
    id = Column(Integer, Sequence('addons_id_seq', increment=1), primary_key = True)
    code = Column(String(45), unique=True, nullable=False)
    name = Column(String(45), nullable=False)  
    price = Column(Integer, nullable=False)
    catid = Column(Integer, ForeignKey('category.id'), nullable=False)
    
    order_details = relationship('OrderDetails', back_populates="addons")
    category = relationship('Category', back_populates="addons")
    
    def __init__(self, code, name, price, catid, id = None):
      self.id = id
      self.code = code
      self.name = name
      self.price = price
      self.catid = catid
      
    def to_json(self):
        return {
            "id": self.id,
            "code": self.code,
            "name": self.name,
            "price" : self.price,
            "catid" : self.catid
            
        }
                   
    def __repr__(self):
        return f"<AddOns {self.id} {self.code} {self.name} {self.price} {self.catid}>"
    
    
    
      