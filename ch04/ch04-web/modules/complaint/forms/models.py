from flask_wtf import FlaskForm
from wtforms import StringField,  TextAreaField, IntegerField, BooleanField, RadioField, SelectField, DateField, EmailField, TelField
from wtforms.validators import InputRequired, Length, Regexp, Email

class ComplaintForm(FlaskForm):
    id = SelectField('Enter user id: ', validators=[InputRequired()])
    firstname = StringField('Enter firstname:', validators=[InputRequired(),
                                            Length(max=50)])
    middlename = StringField('Enter middlename:', validators=[InputRequired(),
                                            Length(max=50)])
    lastname = StringField('Enter lastname:', validators=[InputRequired(),
                                            Length(max=50)])
    email = EmailField('Enter email:', validators=[InputRequired(),
                                            Length(max=20),
                                            Email()])
    mobile = StringField('Enter mobile:', validators=[InputRequired(),
                                            Length(max=20),
                                            Regexp(regex=r"^(\+63)[-]{1}\d{3}[-]{1}\d{3}[-]{1}\d{4}$", message="Valid phone number format is +63-xxx-xxx-xxxx")])
    address = StringField('Enter address:', validators=[InputRequired(),
                                            Length(max=100)])
    zipcode = IntegerField('Enter zip code:',  validators=[InputRequired()])
    status = SelectField('Enter status:', choices=[('active', 'ACTIVE'), ('inactive','INACTIVE'), ('blocked','BLOCKED')], validators=[InputRequired()])
    date_registered = DateField('Enter date registered', format='%Y-%m-%d', validators=[InputRequired()])
    
    def validate_zipcode(self, zipcode):
          if not len(str(zipcode.data)) == 4:
            raise ValueError('zip code must be 4 digits')
       
class EmailComplaintForm(FlaskForm):
    to = StringField('Recipient(s):', validators=[InputRequired(),
                                            Length(max=50)])
    subject = StringField('Subject:', validators=[InputRequired(),
                                            Length(max=80)])
    message = TextAreaField('Message:', render_kw={"rows": 30, "cols": 81}, validators=[InputRequired()])