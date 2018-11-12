# imports FlaskForm class that automatically generates an html form
from flask_wtf import FlaskForm
# imports classes of various fields 
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email

class RegistrationForm(FaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password'), validators[DataRequired(), ]
  
