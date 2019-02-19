
class Config:
    '''
    General configuration parent class
    '''
    pass
    NEWS_API_BASE_URL ='https://newsapi.org/v2/{}?q=bitcoin&from=2019-01-19&sortBy=publishedAt&apiKey={}'
    NEWS_SOURCES_BASE_URL = 'https://newsapi.org/v2/sources?category{}apiKey={}'
    NEWS_ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?category{}apiKey={}'


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

