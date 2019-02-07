class Settings(object):

    """
    Common settings

    """
    # Put any configuration here that are common across all enviroments

class DevelopmentSettings(Settings):
    """
    Developement settings

    """
    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionSettings(Settings):
    """
    Production settings

    """
    Debug = False

app_settings = {
    'development': DevelopmentSettings,
    'production': ProductionSettings
}