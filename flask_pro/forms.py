from flask_wtf import FlaskForm
# you need to import stringfield to create new attribut for the field
from wtforms import (
	StringField,
	PasswordField,
	SubmitField,
	BooleanField,
)
# this for validate the length of the field
from wtforms.validators import (
	DataRequired,
	Length,
	Email,
	EqualTo,
)


class UserRegistrationForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=4, max=21)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password', validators=[
																DataRequired(), 
																EqualTo('password')])
	submit = SubmitField('Register')


class UserLoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')
