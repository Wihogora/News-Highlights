
class Config:
    '''
    General configuration parent class
    '''
    pass
    NEWS_API_BASE_URL ='https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=f69091f5444e473789889991c3f721cc'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True

