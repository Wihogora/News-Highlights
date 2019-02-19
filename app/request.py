from app import app
import urllib.request,json
from .models import news
News = news.News

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config['NEWS_API_BASE_URL']

# Getting the source base url
source_base_url = app.config['NEWS_SOURCES_BASE_URL']

# Getting the article base url
articles_base_url = app.config['NEWS_ARTICLES_BASE_URL']


def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = source_base_url.format(api_key)
    print(get_news_url)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
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
        id = news_item.get('id')
        name = news_item.get('name')
        url = news_item.get('url')
        print(news_results)

    return news_results

def get_articles(id):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = articles_base_url.format(id,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)

    return articles_results


def process_articles(articles_list):
    '''
    Function that processes the articles result and transforms them to a list of objects
    Args:
        articles_list: a list of dictionaries that contain articles
    Returns:
        articles_results: a list of articles objects
    '''
    articles_results = []
    for articles_item in articles_list:
        id = articles_item.get('id')
        title = articles_item.get('title')
        name = articles_item.get('name')
        url = articles_item.get('url')
        urlToImage = articles_item.get('urlToImage')
        publishedAt = articles_item.get('publishedAt')

        if urlToImage:
            articles_object = Articles(id,title,name,url,urlToImage,publishedAt)
            articles_results.append(articles_object)

    return articles_results

def get_newss(id):
    get_news_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None
        if news_details_response:
            id = news_details_response.get('id')
            title = news_details_response.get('title')
            name = news_details_response.get('name')
            url = news_details_response.get('url')
            urlToImage = news_details_response.get('urlToImage')
            publishedAt = news_details_response.get('publishedAt')

            news_object = News(id,title,name,url,urlToImage,publishedAt)

    return news_object