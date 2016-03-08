import os

class BaseConfig(object):
	DEBUG = True
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
	SECRET_KEY = os.environ["SECRET_KEY"]

class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    
class ProductionConfig(BaseConfig):
    DEBUG = False