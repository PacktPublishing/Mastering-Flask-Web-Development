from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, BooleanField, RadioField, SelectField, DateField, EmailField, TelField
from wtforms.validators import InputRequired, Length, Regexp, Email

class AdminForm(FlaskForm):
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
    date_registered = DateField('Enter date registered', format='%Y-%m-%d', validators=[InputRequired()])
    
    