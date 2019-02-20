from flask import render_template
from app import app
from .request import get_news,get_articles

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
 # Getting popular news
    title = 'News Highlight'
    general_news = get_news('general')
    business_news = get_news('business')
    sports_news = get_news('sports')
    technology_news = get_news('technology')
    return render_template('index.html', title = title, general = general_news, business = business_news, sports = sports_news, technology = technology_news)
    

@app.route('/news/<news_id>')
def news(id):

    '''
    View news page function that returns the news details page and its data
def get_articles(id):

    '''
    news=get_articles(id)
    title= f'{id}'
    return render_template('news.html',news = news)

