import os

class DefaultConfig(object):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///db.sqlite')
    SECRET_KEY = os.environ.get('SECRET_KEY', 'replaceme-long-secret')

class DevelopmentConfig(DefaultConfig):
    DEBUG = True
