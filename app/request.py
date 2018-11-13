from app import app
import urllib.request,json
from .models import news
# import FancyURLopener


News = news.News
Articles = news.Articles
# Getting the api key

# api_key = app.config['NEWS_API_KEY']
# base_url = app.config['NEWS_API_SOURCES_URL']
api_key='a338b8b70110423684e92c3100dc8937'
base_url='https://newsapi.org/v2/everything?q={}&apiKey={}'

def get_news():
    global api_key,base_url
    base_url='https://newsapi.org/v2/everything?q=category&apiKey=a338b8b70110423684e92c3100dc8937'
    '''
    Function that gets the json response to our url request
    '''
    # get_news_url = base_url.format(category)
    # print(get_news_url)

    with urllib.request.urlopen(base_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)


    return news_results



def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects
    Args:
        news_list: A list of dictionaries that contain news details
    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        name = news_item.get('author')
        description = news_item.get('description')
        url = news_item.get('url')
        urlToImage =news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')
        content = news_item.get('content')
        
        news_object = News(name,description,url,urlToImage,publishedAt,content)
        news_results.append(news_object)
        
    return news_results    




def get_articles():
    # get_articles_url = articles_url.format(id,api_key)
    articles_url ='https://newsapi.org/v2/sources?apiKey=a338b8b70110423684e92c3100dc8937'
    with urllib.request.urlopen(articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)
        
        articles_results = None


        if get_articles_response["sources"]:
            articles_results_list = get_articles_response["sources"]
            articles_results = process_articles(articles_results_list)


    return articles_results



def process_articles(articles_list):
   
    articles_results = []
    for articles_item in articles_list:
        name = articles_item.get('name')
        description = articles_item.get('description')
        url = articles_item.get('url')
        category = articles_item.get('category')
        
        articles_object = Articles(name,description,url,category)
        articles_results.append(articles_object)
        
    return articles_results    