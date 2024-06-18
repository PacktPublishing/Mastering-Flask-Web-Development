from app.models.config import database

from peewee import Model, CharField, IntegerField, BigIntegerField, FloatField, DoubleField, BooleanField, TextField, PrimaryKeyField, ForeignKeyField, DateField

class Login(Model):
    id = BigIntegerField(primary_key=True, null=False, sequence="login_id_seq")
    username = CharField(max_length=50, unique=True, null=False)
    password = CharField(max_length=250, null=False)
    role = IntegerField(null=False)
        
    class Meta:
        db_table = 'login'
        database = database
        
    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password
        }
        
class Administrator(Model):
    id = BigIntegerField(primary_key=True, null=False, sequence="administrator_id_seq")
    empid = CharField(max_length="25", unique="True", null=False)
    username = ForeignKeyField(model=Login, null=False, to_field="username", backref="login")
    firstname = CharField(max_length="100", null=False)
    lastname = CharField(max_length="100", null=False)
    position = CharField(max_length="100", null=False)
    email = CharField(max_length="20", null=False)
    mobile = CharField(max_length="20", null=False)
    enrolled_date = DateField(null=False)
    
    class Meta:
        db_table = 'administrator'
        database = database
        
    def to_json(self):
        return {
            "id": self.id,
            "empid": self.empid,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "position": self.position,
            "username": self.username,
            "email": self.email,
            "mobile": self.mobile,
            "enrolled_date": self.enrolled_date
        }

class Customer(Model):
    id = BigIntegerField(primary_key=True, null=False, sequence="customer_id_seq")
    custid = CharField(max_length="25", null=False, unique="True")
    type = CharField(max_length="25", null=False)
    username = ForeignKeyField(model=Login, null=False, to_field="username", backref="login")
    firstname = CharField(max_length="100", null=False)
    lastname = CharField(max_length="100", null=False)
    position = CharField(max_length="100", null=False)
    email = CharField(max_length="20", null=False)
    mobile = CharField(max_length="20", null=False)
    enrolled_date = DateField(null=False)
    
    class Meta:
        db_table = "customer"
        database = database
        
    def to_json(self):
        return {
            "id": self.id,
            "custid": self.custid,
            "type": self.type,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "position": self.position,
            "username": self.username,
            "email": self.email,
            "mobile": self.mobile,
            "enrolled_date": self.enrolled_date
        }


class Brand(Model):
    id = BigIntegerField(primary_key=True, null=False, sequence="brand_id_seq")
    code = CharField(max_length="20", unique="True", null=False)
    name = CharField(max_length="100", null=False)
    description = CharField(max_length="200", null=False)
    
    class Meta:
        db_table = "brand"
        database = database
        
    def to_json(self):
        return {
            "id": self.id,
            "code": self.code,
            "name": self.name,
            "description": self.description
        }

class Category(Model):
    id = BigIntegerField(primary_key=True, null=False, sequence="category_id_seq")
    code = CharField(max_length="20", unique="True", null=False)
    name = CharField(max_length="100", null=False)
    description = CharField(max_length="200", null=False)
    
    class Meta:
        db_table = "category"
        database = database
        
    def to_json(self):
        return {
            "id": self.id,
            "code": self.code,
            "name": self.name,
            "description": self.description
        }


class Discount(Model):
    id = BigIntegerField(primary_key=True, null=False, sequence="discount_id_seq")
    code = CharField(max_length="20", unique="True", null=False)
    rate = FloatField(null=False)
    
    class Meta:
        db_table = "discount"
        database = database
        
    def to_json(self):
        return {
            "id": self.id,
            "code": self.code,
            "rate": self.rate
        }

               
class Product(Model):
    id = BigIntegerField(primary_key=True, null=False, sequence="product_id_seq")
    code = CharField(max_length="20", unique="True", null=False)
    name = CharField(max_length="100", null=False)
    btype = ForeignKeyField(model=Brand, null=False, to_field="code", backref="brand")
    ctype = ForeignKeyField(model=Category, null=False, to_field="code", backref="category")
    unit_type = CharField(max_length="100", null=False)
    sell_price = FloatField(unique="True")
    purchase_price = FloatField(unique="True")
    discount = ForeignKeyField(model=Discount, null=False, to_field="code", backref="discount")
    
    class Meta:
        db_table = "product"
        database = database
        
    def to_json(self):
        return {
            "id": self.id,
            "code": self.code,
            "name": self.name,
            "btype": self.btype,
            "ctype": self.ctype,
            "unit_type": self.unit_type,
            "sell_price": self.sell_price,
            "purchase_price": self.purchase_price,
            "discount": self.discount
        }

class Supplier(Model):
    id = BigIntegerField(primary_key=True, null=False, sequence="supplier_id_seq")
    sid = CharField(max_length="20", unique="True", null=False)
    company = CharField(max_length="100", null=False)
    email = CharField(max_length="20", null=False)
    bank_name = CharField(max_length="50", null=False)
    bank_account = CharField(max_length="50", null=False)
    mobile = CharField(max_length="20", null=False)
    approved_date = DateField(null=False)
    
    class Meta:
        db_table = "supplier"
        database = database   
        
    def to_json(self):
        return {
            "id": self.id,
            "sid": self.sid,
            "company": self.company,
            "email": self.email,
            "bank_name": self.bank_name,
            "bank_account": self.bank_account,
            "mobile": self.mobile,
            "approved_date": self.approved_date
        }   

class InvoiceRequest(Model):
    id = BigIntegerField(primary_key=True, null=False, sequence="invoice_request_id_seq")
    code = CharField(max_length="50", unique="True", null=False)
    pcode = ForeignKeyField(model=Product, null=False, to_field="code", backref="product")
    purchase_date = DateField(null=False)
    
    class Meta:
        db_table = "invoice_request"
        database = database    
        
    def to_json(self):
        return {
            "id": self.id,
            "code": self.code,
            "pcode": self.pcode,
            "purchase_date": self.purchase_date
        }

class Stock(Model):
    id = BigIntegerField(primary_key=True, null=False, sequence="stock_id_seq")
    sid = ForeignKeyField(model=Supplier, null=False, to_field="sid", backref="supplier")
    invcode = ForeignKeyField(model=InvoiceRequest, null=False, to_field="code", backref="invoice")
    qty = IntegerField(null=False)
    payment_date = DateField(null=True)
    received_date = DateField(null=False)
    recieved_by = CharField(max_length="100")
    
    class Meta:
        db_table = "stock"
        database = database
    
    def to_json(self):
        return {
            "id": self.id,
            "sid": self.sid,
            "invcode": self.invcode,
            "qty": self.qty,
            "payment_date": self.payment_date,
            "received_date": self.received_date,
            "recieved_by": self.recieved_by
        }  

class Cart(Model):
    id = BigIntegerField(primary_key=True, null=False, sequence="cart_id_seq")
    orderid = CharField(max_length="50", unique=True, null=False)
    ordered_date = DateField(null=False)
    ordered_by = ForeignKeyField(model=Login, null=False, to_field="username", backref="login")
    total = FloatField(null=True, default=0.0)
    
    class Meta:
        db_table = "cart"
        database = database
        
    def to_json(self):
        return {
            "id": self.id,
            "orderid": self.orderid,
            "ordered_date": self.ordered_date,
            "ordered_by": self.ordered_by,
            "total": self.total
        }
        
class CartItem(Model):
    id = BigIntegerField(primary_key=True, null=False, sequence="cart_item_id_seq")
    orderid = ForeignKeyField(model=Cart, null=False, to_field="orderid", backref="cart")
    pcode = ForeignKeyField(model=Product, null=False, to_field="code", backref="product")
    qty = IntegerField(null=False)
     
    class Meta:
        db_table = "cart_item"
        database = database
        
    def to_json(self):
        return {
            "id": self.id,
            "orderid": self.orderid,
            "pcode": self.pcode,
            "qty": self.qty,
        }
                    
class Purchase(Model):
    id = BigIntegerField(primary_key=True, null=False, sequence="purchase_id_seq")
    orderid = ForeignKeyField(model=Cart, null=False, to_field="orderid", backref="order")
    payment_date = DateField(null=False)
    received_by = CharField(max_length="100")
        
    class Meta:
        db_table = "purchase"
        database = database 
        
    def to_json(self):
        return {
            "id": self.id,
            "orderid": self.orderid,
            "payment_date": self.payment_date,
            "received_by": self.received_by,
        }
        


