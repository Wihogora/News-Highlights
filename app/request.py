from app import app
import urllib.request,json
from .models import newsArticle
News = news.News

# Getting api key
api_key = app.config['<f69091f5444e473789889991c3f721cc>']

# Getting the news base url
base_url = app.config['https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=f69091f5444e473789889991c3f721cc']