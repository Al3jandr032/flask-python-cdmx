import os


class BaseConfig:
    """Base configuration class"""

    SECRET_KEY = os.getenv("SECRET_KEY", "dev key")

    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    QUERY_THRESHOLD = 1


class DevelopmentConfig(BaseConfig):
    """Development configuration class"""

    name = "app.db"

    SQLALCHEMY_DATABASE_URI = f"sqlite:///{name}"
    DEBUG = True
    print("DEvlop")


class TestingConfig(BaseConfig):
    """Testing configuration class"""

    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"  # in-memory database
    os.environ["SECRET_KEY_TIME"] = "TestingSecretKey"


class ProductionConfig(BaseConfig):
    """Production configuration class"""

    name = "postgres"
    passwrd = "password"
    db = "app_db"
    host = "db"
    if os.environ.get("DATABASE_URL"):
        _database = os.environ.get("DATABASE_URL")
    else:
        _database = f"postgresql+pg8000://{name}:{passwrd}@{host}/{db}"
    SQLALCHEMY_DATABASE_URI = _database
    # print("Prod: ",SQLALCHEMY_DATABASE_URI)
    os.environ["SECRET_KEY_TIME"] = "ProdSecretKey"


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}
