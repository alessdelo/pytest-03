# imports FlaskForm class that automatically generates an html form
from flask_wtf import FlaskForm
# imports classes of various fields 
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class RegistrationForm(FaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
  
