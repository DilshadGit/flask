import os


class Config:
	# added securit key for csrf request and secure login detail
	SECRET_KEY = '8ba7aa2eea1ddbf6c024bea56ac6c804198b535a1fe5616cced1d0c61f21ddb2'
	''' configurate the db and location '''
	SQLALCHEMY_DATABASE_URI = 'sqlite:///flask_db.db'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	MAIL_SERVER = 'smtp.google.com'
	MAIL_PORT = 587
	MAIL_USE_LTF = True
	MAIL_USERNAME = os.environ.get('MAIL_USER')
	MAIL_PASSWORD = os.environ.get('MAIL_PASS')
