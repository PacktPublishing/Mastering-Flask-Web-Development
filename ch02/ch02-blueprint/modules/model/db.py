
from sqlalchemy import Time, Column, ForeignKey, Integer, String, Float, Date, Sequence
from sqlalchemy.orm import relationship
from modules.model.config import Base

class Login(Base):
   __tablename__ = 'login'
   id = Column(Integer, Sequence('login_id_seq', increment=1), primary_key = True)
   username = Column(String(45))
   password = Column(String(45))  
   user_type = Column(Integer)
   
   admins = relationship('Admin', back_populates="login", uselist=False)
   customer = relationship('Customer', back_populates="login", uselist=False)

   def __init__(self, username, password, user_type, id = None):
      self.id = id
      self.username = username
      self.password = password
      self.user_type = user_type

def __repr__(self):
        return f"<Login {self.id} {self.username} {self.password} {self.user_type}>"
     
class Customer(Base):
   __tablename__ = 'customer'
   id = Column(Integer, ForeignKey('login.id'), primary_key = True)
   firstname = Column(String(45))
   lastname = Column(String(45))  
   middlename = Column(String(45))
   email = Column(String(45))
   mobile = Column(String(20))
   address = Column(String(100))
   status = Column(String(45))
      
   login = relationship('Login', back_populates="customer")
   orders = relationship('Orders', back_populates="customer")
   shippings = relationship('Shipping', back_populates="customer")
   
   def __init__(self, id, firstname, lastname, middlename, email, mobile, address, status):
      self.id = id
      self.firstname = firstname
      self.lastname = lastname
      self.middlename = middlename
      self.email = email
      self.mobile = mobile
      self.address = address
      self.status = status
      
   def __repr__(self):
        return f"<Customer {self.id} {self.firstname} {self.middlename} {self.lastname}>"
      

class Admin(Base):
   __tablename__ = 'admin'
   id = Column(Integer, ForeignKey('login.id'), primary_key = True)
   firstname = Column(String(45))
   lastname = Column(String(45))  
   middlename = Column(String(45))
   email = Column(String(45))
   mobile = Column(String(45))
   
   login = relationship('Login', back_populates="admins")
   
   def __init__(self, id, firstname, lastname, middlename, email, mobile):
      self.id = id
      self.firstname = firstname
      self.lastname = lastname
      self.middlename = middlename
      self.email = email
      self.mobile = mobile
      
   def __repr__(self):
        return f"<Admin {self.id} {self.firstname} {self.middlename} {self.lastname}>"

class Products(Base):
   __tablename__ = 'products'
   id = Column(Integer, Sequence('products_id_seq', increment=1), primary_key = True)
   name = Column(String(100), nullable = False)
   code = Column(String(45), nullable = False, unique = True)  
   price = Column(Float, nullable = False)  
   
   orders = relationship('Orders', back_populates="product")
   
   def __init__(self, name, code, price, id = None):
      self.id = id
      self.name = name
      self.code = code
      self.price = price
   
   def __repr__(self):
        return f"<Products {self.id} {self.name} {self.code} {self.price}>"
     
class Orders(Base):
   __tablename__ = 'orders'
   id = Column(Integer, Sequence('orders_id_seq', increment=1), primary_key = True)
   pid = Column(Integer, ForeignKey('products.id'), nullable = False)
   order_no = Column(String, nullable = False, unique = True)  
   cid = Column(Integer, ForeignKey('customer.id'), nullable = False)  
   order_date = Column(Date, nullable = False)  
   
   product = relationship('Products', back_populates="orders")
   customer = relationship('Customer', back_populates="orders")
   payment = relationship('Payment', back_populates="order", uselist=False)
   
   
   def __init__(self, pid, cid, order_no, order_date, id = None):
      self.id = id
      self.pid = pid
      self.cid = cid
      self.order_no = order_no
      self.order_date = order_date
   
   def __repr__(self):
        return f"<Orders {self.id} {self.pid} {self.cid} {self.order_no} {self.order_date}>"
     
class PaymentType(Base):
   __tablename__ = 'payment_type'
   id = Column(Integer, Sequence('payment_type_id_seq', increment=1), primary_key = True)
   name = Column(String, nullable = False)
   
   payment = relationship('Payment', back_populates="payment_types")
   
   def __init__(self, name, id=None):
      self.id = id
      self.name = name
      
   def __repr__(self):
        return f"<PaymentType {self.id} {self.name}>"
   

class Payment(Base):
   __tablename__ = 'payment'
   id = Column(Integer, Sequence('payment_id_seq', increment=1), primary_key = True)
   order_no = Column(String, ForeignKey('orders.order_no'), nullable = False)
   ref_no = Column(String, nullable = False, unique = True)  
   mode_payment = Column(Integer, ForeignKey('payment_type.id'),  nullable = False)  
   amount = Column(Float, nullable = False)  
   date_payment = Column(Date, nullable = False)  
   
   order = relationship('Orders', back_populates="payment")
   payment_types = relationship('PaymentType', back_populates="payment")
   shipping  = relationship('Shipping', back_populates="payment", uselist=False)
   
   def __init__(self, order_no, ref_no, mode_payment, amount, date_payment, id = None):
      self.id = id
      self.order_no = order_no
      self.ref_no = ref_no
      self.mode_payment = mode_payment
      self.amount = amount
      self.date_payment = date_payment
      
   def __repr__(self):
        return f"<Payment {self.id} {self.order_no} {self.ref_no} {self.date_payment}>"
     
class Shipping(Base):
   __tablename__ = 'shipping'
   id = Column(Integer, Sequence('shipping_id_seq', increment=1), primary_key = True)
   cid = Column(Integer, ForeignKey('customer.id'), nullable = False)  
   pay_id = Column(Integer, ForeignKey('payment.id'), nullable = False)  
   did = Column(Integer, ForeignKey('delivery_officer.id'), nullable = False)  
   amount = Column(Float, nullable = False) 
   status = Column(String, nullable = False)
   date_shipping = Column(Date, nullable = False)  
   
   payment = relationship('Payment', back_populates="shipping")
   shipping_details = relationship('ShippingDetails', back_populates="shipping", uselist=False)
   delivery_officer = relationship('DeliveryOfficer', back_populates="shipping", uselist=False)
   customer = relationship('Customer', back_populates="shippings")
   
   def __init__(self, cid, pay_id, did, amount, status, date_shipping, id = None):
      self.id = id
      self.cid = cid
      self.did = did
      self.pay_id = pay_id
      self.amount = amount
      self.status = status
      self.date_shipping = date_shipping
   
   def __repr__(self):
        return f"<Shipping {self.id} {self.pay_id} {self.cid} {self.did} {self.date_shipping} {self.amount}>"
     
class ShippingDetails(Base):
   __tablename__ = 'shipping_details'
   id = Column(Integer, Sequence('shipping_details_id_seq', increment=1), primary_key = True)
   sid = Column(Integer, ForeignKey('shipping.id'), nullable = False)  
   qty = Column(Integer, nullable = False)  
   amount = Column(Float, nullable = False) 
   
   shipping = relationship('Shipping', back_populates="shipping_details")
   
   def __init__(self, id, sid, qty, amount):
      self.id = id
      self.sid = sid
      self.qty = qty
      self.amount = amount
      
   def __repr__(self):
        return f"<Shipping {self.id} {self.sid} {self.qty} {self.amount}>"
   
   
class DeliveryOfficer(Base):
   __tablename__ = 'delivery_officer'
   id = Column(Integer, primary_key = True)
   firstname = Column(String(55), nullable = False)
   lastname = Column(String(55), nullable = False)  
   middlename = Column(String(55), nullable = False)
   email = Column(String(20), nullable = False)
   mobile = Column(String(15), nullable = False)
   address = Column(String(100), nullable = False)
   status = Column(String(45), nullable = False)

   shipping = relationship('Shipping', back_populates="delivery_officer")
   
   def __init__(self, id, firstname, middlename, lastname, email, mobile, address, status):
      self.id = id
      self.firstname = firstname
      self.lastname = lastname
      self.middlename = middlename
      self.email = email
      self.mobile = mobile
      self.address = address
      self.status = status
      
   def __repr__(self):
        return f"<Shipping {self.id} {self.firstname} {self.middlename} {self.lastname}>"

