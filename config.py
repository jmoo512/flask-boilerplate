import os, secrets
key=secrets.token_urlsafe(32)
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG=True
    #TESTING=False
    SECRET_KEY = key
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI = ''

class DevelopmentgConfig(Config):
    DEBUG=True
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class StagingConfig(Config):
    DEBUG=False
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class ProductionConfig(Config):
    DEBUG=False
    SQLALCHEMY_TRACK_MODIFICATIONS=False
