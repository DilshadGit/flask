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
    ValidationError,
)

from flaskpro.models import User


class UserRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=4, max=21)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(),
        EqualTo('password')])
    submit = SubmitField('Register')

    ''' This function check if the username is exist in the db than raise error '''

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                'This user is taken. Please try different username'
            )

    ''' This function check if the email is exist in the db than raise error '''

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                'This email is taken. Please try different email'
            )


class UserLoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
