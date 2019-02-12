class Settings(object):

    """
    Common settings

    """
    DEBUG = True

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

class TestingSettings(Settings):
    """
    Testing configurations

    """
    TESTING = True


app_settings = {
    'development': DevelopmentSettings,
    'production': ProductionSettings,
    'testing' : TestingSettings
}