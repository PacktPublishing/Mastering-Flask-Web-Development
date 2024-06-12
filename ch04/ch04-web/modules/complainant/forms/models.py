from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, DateField, EmailField
from wtforms.validators import InputRequired, Length, Regexp, Email, ValidationError
from datetime import datetime
class ComplainantForm(FlaskForm):
  
    def disallow_invalid_dates(date_after):
       message = 'Must be after the date %s.' % (date_after)

       def _disallow_invalid_dates(form, field):
          base_date = datetime.strptime(date_after, '%Y-%m-%d').date()
          if field.data < base_date:
             raise ValidationError(message)

       return _disallow_invalid_dates
     
    id = SelectField('Choose Login ID: ', validators=[InputRequired()])
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
    date_registered = DateField('Enter date registered', format='%Y-%m-%d', validators=[InputRequired(), disallow_invalid_dates('2000-01-01')])
    
    def validate_zipcode(self, zipcode):
          if not len(str(zipcode.data)) == 4:
            raise ValueError('zip code must be 4 digits')
          
    
       
