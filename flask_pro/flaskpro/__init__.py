from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskpro.config import Config


''' create the database '''
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'accounts.user_login'
login_manager.login_message_category = 'info'

mail = Mail()


def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(Config)
	from flaskpro.accounts.routes import accounts
	from flaskpro.posts.routes import posts
	from flaskpro.settings.routes import settings
	from flaskpro.errors.handlers import errors

	db.init_app(app)
	bcrypt.init_app(app)
	login_manager.init_app(app)
	mail.init_app(app)

	app.register_blueprint(accounts)
	app.register_blueprint(posts)
	app.register_blueprint(settings)
	app.register_blueprint(errors)

	return app
