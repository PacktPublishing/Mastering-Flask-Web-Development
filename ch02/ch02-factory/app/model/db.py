from app import db


class Login(db.Model):
   __tablename__ = 'login'
   id = db.Column(db.Integer, db.Sequence('login_id_seq', increment=1), primary_key = True)
   username = db.Column(db.String(45))
   password = db.Column(db.String(45))  
   user_type = db.Column(db.Integer)
   
   admins = db.relationship('Admin', back_populates="login", uselist=False)
   customer = db.relationship('Customer', back_populates="login", uselist=False)

   def __init__(self, username, password, user_type, id = None):
      self.id = id
      self.username = username
      self.password = password
      self.user_type = user_type

def __repr__(self):
        return f"<Login {self.id} {self.username} {self.password} {self.user_type}>"
     
class Customer(db.Model):
   __tablename__ = 'customer'
   id = db.Column(db.Integer, db.ForeignKey('login.id'), primary_key = True)
   firstname = db.Column(db.String(45))
   lastname = db.Column(db.String(45))  
   middlename = db.Column(db.String(45))
   email = db.Column(db.String(45))
   mobile = db.Column(db.String(20))
   address = db.Column(db.String(100))
   status = db.Column(db.String(45))
      
   login = db.relationship('Login', back_populates="customer")
   orders = db.relationship('Orders', back_populates="customer")
   shippings = db.relationship('Shipping', back_populates="customer")
   
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
      

class Admin(db.Model):
   __tablename__ = 'admin'
   id = db.Column(db.Integer, db.ForeignKey('login.id'), primary_key = True)
   firstname = db.Column(db.String(45))
   lastname = db.Column(db.String(45))  
   middlename = db.Column(db.String(45))
   email = db.Column(db.String(45))
   mobile = db.Column(db.String(45))
   
   login = db.relationship('Login', back_populates="admins")
   
   def __init__(self, id, firstname, lastname, middlename, email, mobile):
      self.id = id
      self.firstname = firstname
      self.lastname = lastname
      self.middlename = middlename
      self.email = email
      self.mobile = mobile
      
   def __repr__(self):
        return f"<Admin {self.id} {self.firstname} {self.middlename} {self.lastname}>"

class Products(db.Model):
   __tablename__ = 'products'
   id = db.Column(db.Integer, db.Sequence('products_id_seq', increment=1), primary_key = True)
   name = db.Column(db.String(100), nullable = False)
   code = db.Column(db.String(45), nullable = False, unique = True)  
   price = db.Column(db.Float, nullable = False)  
   
   orders = db.relationship('Orders', back_populates="product")
   
   def __init__(self, name, code, price, id = None):
      self.id = id
      self.name = name
      self.code = code
      self.price = price
   
   def __repr__(self):
        return f"<Products {self.id} {self.name} {self.code} {self.price}>"
     
class Orders(db.Model):
   __tablename__ = 'orders'
   id = db.Column(db.Integer, db.Sequence('orders_id_seq', increment=1), primary_key = True)
   pid = db.Column(db.Integer, db.ForeignKey('products.id'), nullable = False)
   order_no = db.Column(db.String, nullable = False, unique = True)  
   cid = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable = False)  
   order_date = db.Column(db.Date, nullable = False)  
   
   product = db.relationship('Products', back_populates="orders")
   customer = db.relationship('Customer', back_populates="orders")
   payment = db.relationship('Payment', back_populates="order", uselist=False)
   
   
   def __init__(self, pid, cid, order_no, order_date, id = None):
      self.id = id
      self.pid = pid
      self.cid = cid
      self.order_no = order_no
      self.order_date = order_date
   
   def __repr__(self):
        return f"<Orders {self.id} {self.pid} {self.cid} {self.order_no} {self.order_date}>"
     
class PaymentType(db.Model):
   __tablename__ = 'payment_type'
   id = db.Column(db.Integer, db.Sequence('payment_type_id_seq', increment=1), primary_key = True)
   name = db.Column(db.String, nullable = False)
   
   payment = db.relationship('Payment', back_populates="payment_types")
   
   def __init__(self, name, id=None):
      self.id = id
      self.name = name
      
   def __repr__(self):
        return f"<PaymentType {self.id} {self.name}>"
   

class Payment(db.Model):
   __tablename__ = 'payment'
   id = db.Column(db.Integer, db.Sequence('payment_id_seq', increment=1), primary_key = True)
   order_no = db.Column(db.String, db.ForeignKey('orders.order_no'), nullable = False)
   ref_no = db.Column(db.String, nullable = False, unique = True)  
   mode_payment = db.Column(db.Integer, db.ForeignKey('payment_type.id'),  nullable = False)  
   amount = db.Column(db.Float, nullable = False)  
   date_payment = db.Column(db.Date, nullable = False)  
   
   order = db.relationship('Orders', back_populates="payment")
   payment_types = db.relationship('PaymentType', back_populates="payment")
   shipping  = db.relationship('Shipping', back_populates="payment", uselist=False)
   
   def __init__(self, order_no, ref_no, mode_payment, amount, date_payment, id = None):
      self.id = id
      self.order_no = order_no
      self.ref_no = ref_no
      self.mode_payment = mode_payment
      self.amount = amount
      self.date_payment = date_payment
      
   def __repr__(self):
        return f"<Payment {self.id} {self.order_no} {self.ref_no} {self.date_payment}>"
     
class Shipping(db.Model):
   __tablename__ = 'shipping'
   id = db.Column(db.Integer, db.Sequence('shipping_id_seq', increment=1), primary_key = True)
   cid = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable = False)  
   pay_id = db.Column(db.Integer, db.ForeignKey('payment.id'), nullable = False)  
   did = db.Column(db.Integer, db.ForeignKey('delivery_officer.id'), nullable = False)  
   amount = db.Column(db.Float, nullable = False) 
   status = db.Column(db.String, nullable = False)
   date_shipping = db.Column(db.Date, nullable = False)  
   
   payment = db.relationship('Payment', back_populates="shipping")
   shipping_details = db.relationship('ShippingDetails', back_populates="shipping", uselist=False)
   delivery_officer = db.relationship('DeliveryOfficer', back_populates="shipping", uselist=False)
   customer = db.relationship('Customer', back_populates="shippings")
   
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
     
class ShippingDetails(db.Model):
   __tablename__ = 'shipping_details'
   id = db.Column(db.Integer, db.Sequence('shipping_details_id_seq', increment=1), primary_key = True)
   sid = db.Column(db.Integer, db.ForeignKey('shipping.id'), nullable = False)  
   qty = db.Column(db.Integer, nullable = False)  
   amount = db.Column(db.Float, nullable = False) 
   
   shipping = db.relationship('Shipping', back_populates="shipping_details")
   
   def __init__(self, id, sid, qty, amount):
      self.id = id
      self.sid = sid
      self.qty = qty
      self.amount = amount
      
   def __repr__(self):
        return f"<Shipping {self.id} {self.sid} {self.qty} {self.amount}>"
   
   
class DeliveryOfficer(db.Model):
   __tablename__ = 'delivery_officer'
   id = db.Column(db.Integer, primary_key = True)
   firstname = db.Column(db.String(55), nullable = False)
   lastname = db.Column(db.String(55), nullable = False)  
   middlename = db.Column(db.String(55), nullable = False)
   email = db.Column(db.String(20), nullable = False)
   mobile = db.Column(db.String(15), nullable = False)
   address = db.Column(db.String(100), nullable = False)
   status = db.Column(db.String(45), nullable = False)

   shipping = db.relationship('Shipping', back_populates="delivery_officer")
   
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
