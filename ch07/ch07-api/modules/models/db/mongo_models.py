from mongoengine import Document, SequenceField, BooleanField, EmbeddedDocumentField, BinaryField, IntField, StringField, DateField, EmailField, EmbeddedDocumentListField, EmbeddedDocument

class GCash(EmbeddedDocument):
    acct_name = StringField(db_field='acct_name',max_length=100, required=True)
    acct_number = StringField(db_field='acct_number',max_length=11, required=True)
   
class Savings(EmbeddedDocument):
    acct_name = StringField(db_field='acct_name',max_length=100, required=True)
    acct_number = StringField(db_field='acct_number',max_length=16, required=True)
    bank =  StringField(db_field='bank', max_length=100, required=True)
    branch = StringField(db_field='branch', max_length=100, required=True)
    active = BooleanField(db_field="active", required=True)
    
class Checking(EmbeddedDocument):
    acct_name = StringField(db_field='acct_name',max_length=100, required=True)
    acct_number = StringField(db_field='acct_number',max_length=16, required=True)
    bank =  StringField(db_field='bank', max_length=100, required=True)
    branch = StringField(db_field='branch', max_length=100, required=True)
    active = BooleanField(db_field="active", required=True)
    
class PayPal(EmbeddedDocument):
    email = EmailField(db_field='email', max_length=20, required=True)
    address = StringField(db_field='address',max_length=200, required=True)
    
class Tutor(EmbeddedDocument):
    firstname = StringField(db_field='firstname',max_length=50, required=True)
    lastname = StringField(db_field='lastname',max_length=50, required=True)
    midname = StringField(db_field='middlename',max_length=50, required=True)
    position = StringField(db_field='position', max_length=50, required=True)
    email = EmailField(db_field='email', max_length=50, required=True)
    company = StringField(db_field='mobile', max_length=100)  
    savings = EmbeddedDocumentListField(Savings, required=False)
    checkings = EmbeddedDocumentListField(Checking, required=False)
    gcash = EmbeddedDocumentField(GCash, required=False)
    paypal = EmbeddedDocumentField(PayPal, required=False)
    
class TutorLogin(Document):
    id = SequenceField(required=True, primary_key=True)
    username = StringField(db_field='email',max_length=25, required=True)
    password = StringField(db_field='password',max_length=25, required=True)
    encpass = BinaryField(db_field='encpass', required=True)
    tutor = EmbeddedDocumentField(Tutor, required=False)
    
    


