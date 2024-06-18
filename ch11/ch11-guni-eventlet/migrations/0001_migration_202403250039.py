# auto-generated snapshot
from peewee import *
import datetime
import peewee


snapshot = Snapshot()


@snapshot.append
class Login(peewee.Model):
    id = BigIntegerField(primary_key=True, sequence='login_id_seq')
    username = CharField(max_length=50, unique=True)
    password = CharField(max_length=250)
    role = IntegerField()
    class Meta:
        table_name = "login"


@snapshot.append
class Administrator(peewee.Model):
    id = BigIntegerField(primary_key=True, sequence='administrator_id_seq')
    empid = CharField(max_length='25', unique='True')
    username = snapshot.ForeignKeyField(backref='login', field='username', index=True, model='login')
    firstname = CharField(max_length='100')
    lastname = CharField(max_length='100')
    position = CharField(max_length='100')
    email = CharField(max_length='20')
    mobile = CharField(max_length='20')
    enrolled_date = DateField()
    class Meta:
        table_name = "administrator"


@snapshot.append
class Brand(peewee.Model):
    id = BigIntegerField(primary_key=True, sequence='brand_id_seq')
    code = CharField(max_length='20', unique='True')
    name = CharField(max_length='100')
    description = CharField(max_length='200')
    class Meta:
        table_name = "brand"


@snapshot.append
class Cart(peewee.Model):
    id = BigIntegerField(primary_key=True, sequence='cart_id_seq')
    orderid = CharField(max_length='50', unique=True)
    ordered_date = DateField()
    ordered_by = snapshot.ForeignKeyField(backref='login', field='username', index=True, model='login')
    total = FloatField(default=0.0, null=True)
    class Meta:
        table_name = "cart"


@snapshot.append
class Category(peewee.Model):
    id = BigIntegerField(primary_key=True, sequence='category_id_seq')
    code = CharField(max_length='20', unique='True')
    name = CharField(max_length='100')
    description = CharField(max_length='200')
    class Meta:
        table_name = "category"


@snapshot.append
class Discount(peewee.Model):
    id = BigIntegerField(primary_key=True, sequence='discount_id_seq')
    code = CharField(max_length='20', unique='True')
    rate = FloatField()
    class Meta:
        table_name = "discount"


@snapshot.append
class Product(peewee.Model):
    id = BigIntegerField(primary_key=True, sequence='product_id_seq')
    code = CharField(max_length='20', unique='True')
    name = CharField(max_length='100')
    btype = snapshot.ForeignKeyField(backref='brand', field='code', index=True, model='brand')
    ctype = snapshot.ForeignKeyField(backref='category', field='code', index=True, model='category')
    unit_type = CharField(max_length='100')
    sell_price = FloatField(unique='True')
    purchase_price = FloatField(unique='True')
    discount = snapshot.ForeignKeyField(backref='discount', field='code', index=True, model='discount')
    class Meta:
        table_name = "product"


@snapshot.append
class CartItem(peewee.Model):
    id = BigIntegerField(primary_key=True, sequence='cart_item_id_seq')
    orderid = snapshot.ForeignKeyField(backref='cart', field='orderid', index=True, model='cart')
    pcode = snapshot.ForeignKeyField(backref='product', field='code', index=True, model='product')
    qty = IntegerField()
    class Meta:
        table_name = "cart_item"


@snapshot.append
class Customer(peewee.Model):
    id = BigIntegerField(primary_key=True, sequence='customer_id_seq')
    custid = CharField(max_length='25', unique='True')
    type = CharField(max_length='25')
    username = snapshot.ForeignKeyField(backref='login', field='username', index=True, model='login')
    firstname = CharField(max_length='100')
    lastname = CharField(max_length='100')
    position = CharField(max_length='100')
    email = CharField(max_length='20')
    mobile = CharField(max_length='20')
    enrolled_date = DateField()
    class Meta:
        table_name = "customer"


@snapshot.append
class InvoiceRequest(peewee.Model):
    id = BigIntegerField(primary_key=True, sequence='invoice_request_id_seq')
    code = CharField(max_length='50', unique='True')
    pcode = snapshot.ForeignKeyField(backref='product', field='code', index=True, model='product')
    purchase_date = DateField()
    class Meta:
        table_name = "invoice_request"


@snapshot.append
class Purchase(peewee.Model):
    id = BigIntegerField(primary_key=True, sequence='purchase_id_seq')
    orderid = snapshot.ForeignKeyField(backref='order', field='orderid', index=True, model='cart')
    payment_date = DateField()
    received_by = CharField(max_length='100')
    class Meta:
        table_name = "purchase"


@snapshot.append
class Supplier(peewee.Model):
    id = BigIntegerField(primary_key=True, sequence='supplier_id_seq')
    sid = CharField(max_length='20', unique='True')
    company = CharField(max_length='100')
    email = CharField(max_length='20')
    bank_name = CharField(max_length='50')
    bank_account = CharField(max_length='50')
    mobile = CharField(max_length='20')
    approved_date = DateField()
    class Meta:
        table_name = "supplier"


@snapshot.append
class Stock(peewee.Model):
    id = BigIntegerField(primary_key=True, sequence='stock_id_seq')
    sid = snapshot.ForeignKeyField(backref='supplier', field='sid', index=True, model='supplier')
    invcode = snapshot.ForeignKeyField(backref='invoice', field='code', index=True, model='invoicerequest')
    qty = IntegerField()
    payment_date = DateField(null=True)
    received_date = DateField()
    recieved_by = CharField(max_length='100')
    class Meta:
        table_name = "stock"


