from modules.models.config import database

from peewee import Model, CharField,IntegerField, BigIntegerField, FloatField, DoubleField, BooleanField, TextField, PrimaryKeyField, ForeignKeyField, DateField

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
            "password": self.password,
            "role": self.role
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
    issued_date = DateField(null=False)
    
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
            "issued_date": self.issued_date
        }

class Student(Model):
    id = BigIntegerField(primary_key=True, null=False, sequence="student_id_seq")
    studid = CharField(max_length="25", null=False, unique="True")
    username = ForeignKeyField(model=Login, null=False, to_field="username", backref="login")
    firstname = CharField(max_length="100", null=False)
    lastname = CharField(max_length="100", null=False)
    course = CharField(max_length="55", null=False)
    classification = CharField(max_length="55", null=False)
    status = BooleanField(null=False)
    email = CharField(max_length="20", null=False)
    mobile = CharField(max_length="20", null=False)
    enrolled_date = DateField(null=False)
    
    class Meta:
        db_table = "student"
        database = database
        
    def to_json(self):
        return {
            "id": self.id,
            "studid": self.studid,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "course": self.course,
            "classification": self.classification,
            "status": self.status,
            "email": self.email,
            "mobile": self.mobile,
            "enrolled_date": self.enrolled_date
        }
        
class Faculty(Model):
    id = BigIntegerField(primary_key=True, null=False, sequence="faculty_id_seq")
    empid = CharField(max_length="25", null=False, unique="True")
    username = ForeignKeyField(model=Login, null=False, to_field="username", backref="login")
    firstname = CharField(max_length="100", null=False)
    lastname = CharField(max_length="100", null=False)
    department = CharField(max_length="55", null=False)
    employment_status = CharField(max_length="10", null=False)
    email = CharField(max_length="20", null=False)
    mobile = CharField(max_length="20", null=False)
    issued_date = DateField(null=False)
    
    class Meta:
        db_table = "faculty"
        database = database
        
    def to_json(self):
        return {
            "id": self.id,
            "empid": self.empid,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "department": self.department,
            "employment_status": self.employment_status,
            "status": self.status,
            "email": self.email,
            "mobile": self.mobile,
            "issued_date": self.issued_date
        }
        
class Visitor(Model):
    id = BigIntegerField(primary_key=True, null=False, sequence="visitor_id_seq")
    issuedid = CharField(max_length="25", null=False, unique="True")
    username = ForeignKeyField(model=Login, null=False, to_field="username", backref="login")
    firstname = CharField(max_length="100", null=False)
    lastname = CharField(max_length="100", null=False)
    profession = CharField(max_length="55", null=False)
    company = CharField(max_length="100", null=False)
    email = CharField(max_length="20", null=False)
    mobile = CharField(max_length="20", null=False)
    issued_date = DateField(null=False)
    
    class Meta:
        db_table = "visitor"
        database = database
        
    def to_json(self):
        return {
            "id": self.id,
            "issuedid": self.issuedid,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "profession": self.profession,
            "company": self.company,
            "email": self.email,
            "mobile": self.mobile,
            "issued_date": self.issued_date
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


class Fine(Model):
    id = BigIntegerField(primary_key=True, null=False, sequence="fine_id_seq")
    code = CharField(max_length="20", unique="True", null=False)
    amount = FloatField(null=False)
    
    class Meta:
        db_table = "fine"
        database = database
        
    def to_json(self):
        return {
            "id": self.id,
            "code": self.code,
            "amount": self.amount
        }

               
class Publisher(Model):
    id = BigIntegerField(primary_key=True, null=False, sequence="publisher_id_seq")
    code = CharField(max_length="20", unique="True", null=False)
    name = CharField(max_length="100", null=False)
        
    class Meta:
        db_table = "publisher"
        database = database
        
    def to_json(self):
        return {
            "id": self.id,
            "code": self.code,
            "name": self.name,
        }

class Book(Model):
    id = BigIntegerField(primary_key=True, null=False, sequence="book_id_seq")
    code = CharField(max_length="20", unique="True", null=False)
    title = CharField(max_length="100", null=False)
    author = CharField(max_length="100", null=False)
    isbn = CharField(max_length="100", null=False)
    published_year = IntegerField(null=False)
    edition = IntegerField(null=False)
    publisher = ForeignKeyField(model=Publisher, null=False, to_field="code", backref="publisher")
    category = ForeignKeyField(model=Category, null=False, to_field="code", backref="category")
    description = CharField(max_length="200", null=False)
    
    class Meta:
        db_table = "book"
        database = database
        
    def to_json(self):
        return {
            "id": self.id,
            "code": self.code,
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "published_year": self.published_year,
            "edition": self.edition,
            "publisher": self.publisher,
            "category": self.category,
            "description": self.description
        }
        
class Inventory(Model):
    id = BigIntegerField(primary_key=True, null=False, sequence="inventory_id_seq")
    bookcode = ForeignKeyField(model=Book, null=False, to_field="code", backref="book")
    total_count = IntegerField(null=False)
    lost_count = IntegerField(null=False)
    inventory_date = DateField(null=False)
    received_by = CharField(max_length="100")
    
    class Meta:
        db_table = "inventory"
        database = database
    
    def to_json(self):
        return {
            "id": self.id,
            "bookcode": self.bookcode,
            "total_count": self.total_count,
            "lost_count": self.lost_count,
            "inventory_date": self.inventory_date,
            "received_by": self.received_by,
        }  

class BorrowStudent(Model):
    id = BigIntegerField(primary_key=True, null=False, sequence="borrow_student_id_seq")
    bookcode = ForeignKeyField(model=Book, null=False, to_field="code", backref="book")
    studid = ForeignKeyField(model=Student, null=False, to_field="studid", backref="student")
    borrowed_date = DateField(null=False)
    duration = IntegerField(null=False)
    returned_date = DateField()
    approved_by = CharField(max_length="100")
    
    class Meta:
        db_table = "borrow_student"
        database = database
    
    def to_json(self):
        return {
            "id": self.id,
            "bookcode": self.bookcode,
            "empid": self.empid,
            "borrowed_date": self.borrowed_date,
            "duration": self.duration,
            "returned_date": self.returned_date,
            "approved_by": self.approved_by
        }  

class BorrowFaculty(Model):
    id = BigIntegerField(primary_key=True, null=False, sequence="borrow_faculty_id_seq")
    bookcode = ForeignKeyField(model=Book, null=False, to_field="code", backref="book")
    empid = ForeignKeyField(model=Faculty, null=False, to_field="empid", backref="faculty")
    borrowed_date = DateField(null=False)
    returned_date = DateField()
    duration = IntegerField(null=False)
    approved_by = CharField(max_length="100")
    
    
    class Meta:
        db_table = "borrow_faculty"
        database = database
    
    def to_json(self):
        return {
            "id": self.id,
            "bookcode": self.bookcode,
            "empid": self.empid,
            "borrowed_date": self.borrowed_date,
            "returned_date": self.returned_date,
            "duration": self.duration,
            "approved_by": self.approved_by
        }   

# pem init
# pem add app.models.db.Login
# pem watch
# pem migrate

