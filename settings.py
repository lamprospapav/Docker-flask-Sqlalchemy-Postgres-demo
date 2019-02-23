class Settings(object):

    """
    Common settings

    """
    SECRET_KEY = "testkey"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_FILE = "api.log"

    # Put any configuration here that are common across all enviroments

class DevelopmentSettings(Settings):
    """
    Developement settings

    """
    SQLALCHEMY_ECHO = True



class ProductionSettings(Settings):
    """
    Production settings

    """
    Debug = False

class DockerDevSettings(Settings):
    SQLALCHEMY_DATABASE_URI = "postgresql://testusr:password@postgres/testdb"
    DEBUG = True

class TestingSettings(Settings):
    """
    Testing configurations

    """
    TESTING = True


app_settings = {
    'development': DevelopmentSettings,
    'production': ProductionSettings,
    "docker": DockerDevSettings,
    'testing' : TestingSettings
}