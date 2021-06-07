import os

class Config:

    NEWS_API_BASE_URL ='https://newsapi.org/v2/sources?language=en&apiKey=fb1128aaea20470f9f96d54e431ab90c'
    NEWS_ARTICLE_URL =  'https://newsapi.org/v2/everything?q=apple&from=2021-06-06&to=2021-06-06&sortBy=popularity&apiKey=fb1128aaea20470f9f96d54e431ab90c'
    
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    # SECRET_KEY = os.environ.get('SECRET_KEY')



class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
