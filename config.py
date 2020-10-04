import os
from uuid import uuid4
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    """ Parent Configuration Object """
    DEBUG=False
    TESTING=False
    SQLALCHEMY_TRACK_MODIFICATIONS=False


class DevelopmentConfig(BaseConfig):
    """Development configuration options

    Args:
        BaseConfig (object): Base configuration object to inherit from
    """
    DEBUG=True
    SQLALCHEMY_DATABASE_URI="sqlite:///" + os.path.join(BASE_DIR, 'db/dev.sqlite3')
    SECRET_KEY=str(uuid4())


class TestingConfig(BaseConfig):
    """Testing configuration options

    Args:
        BaseConfig (object): Base configuration object to inherit from
    """
    DEBUG=True
    TESTING=True
    SECRET_KEY=str(uuid4())


config_factory = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
