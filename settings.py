
class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://mofinscmadmin:NAMAt67oCEgu@47.98.143.6:6301/mofin-scmsys'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SECRET_KEY = 'sldjfkdjkfjdkfjkdf'
    DEBUG = True

class DevelopmentConfig(Config):
    ENV = 'development'


class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False