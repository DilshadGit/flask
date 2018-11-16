import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


app = Flask(__name__)

# added securit key for csrf request and secure login detail
app.config[
    'SECRET_KEY'] = '8ba7aa2eea1ddbf6c024bea56ac6c804198b535a1fe5616cced1d0c61f21ddb2'
''' configurate the db and location '''
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


''' create the database '''
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'user_login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.google.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_LTF'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASS')
mail = Mail(app)

from flaskpro import routes
