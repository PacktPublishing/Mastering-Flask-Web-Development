from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, BooleanField, RadioField, SelectMultipleField
from wtforms.validators import InputRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Enter username: ', validators=[InputRequired(),
                                             Length(min=5, max=45)])
    password = StringField('Enter password:', validators=[InputRequired(),
                                            Length(min=5, max=45)])
    user_type = SelectMultipleField('',
                       choices={'User Types' : [('1','Administrator'), ('2', 'User')]}, validators=[InputRequired()])
    
class LoginAuthForm(FlaskForm):
    username = StringField('Enter username: ', validators=[InputRequired(),
                                             Length(min=5, max=45)])
    password = StringField('Enter password:', validators=[InputRequired(),
                                            Length(min=5, max=45)])