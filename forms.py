# from flask_wtf import Form
from flask_wtf import FlaskForm as BaseForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(BaseForm):
    first_name = StringField('First name', validators=[DataRequired("Please enter your first name.")])
    last_name = StringField('Last name', validators=[DataRequired("Please enter your last name.")])
    email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter your email address.")])
    password = PasswordField('Password', validators=[DataRequired("Please enter a password."), Length(min=6, message="Passwords must be 6 characters or more.")])
    submit = SubmitField('Sign up')

class LoginForm(BaseForm):
    email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter your email address.")])
    password = PasswordField('Password', validators =[DataRequired("Please enter a password.")])
    submit = SubmitField("Sign in")

class AddressForm(BaseForm):
	address = StringField('Address', validators=[DataRequired("Please enter an address.")])
	submit = SubmitField("Search")
	