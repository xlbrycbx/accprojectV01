
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///C:/sqlite/sqlite-tools-win32-x86-3380500/accV01.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SECRET_KEY = 'sldjfkdjkfjdkfjkdf'
    DEBUG = True

class DevelopmentConfig(Config):
    ENV = 'development'


class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False