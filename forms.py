# imports FlaskForm class that automatically generates an html form
from flask_wtf import FlaskForm
# imports classes of various fields 
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators[DataRequired()])
    remember = BooleanFied('Remember Me')
    submit = SubmitField('Login')
  
