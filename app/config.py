class Config:
    '''
    General config class
    '''

    NEWS_API_SOURCES_URL ='https://newsapi.org/v2/everything?q={}&apiKey={}'

    HEADLINES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    pass

class ProdConfig(Config):
    '''
     Production config child class
     Args:
         The parent configuration class with General configuration settings
    '''  
    pass   

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True     