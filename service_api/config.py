import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SERVICE_NAME = "wordcount"
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://wdcnt:wdcnt@localhost/wordcount_dev')


class ProdConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SERVICE_HOST = 'localhost'
    SERVICE_PORT = 5000


class TestingConfig(Config):
    TESTING = True
