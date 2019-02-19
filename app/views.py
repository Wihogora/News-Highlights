from flask import render_template
from app import app
from .request import get_news
# Views
# @app.route('/')
# def index():

#     '''
#     View root page function that returns the index page and its data
#     '''
#     message="hello world"
#     return render_template('index.html',message = message)


@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('news.html',id = news_id)

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular news
    popular_news = get_news('popular')
    print(popular_news)
    title = 'Home - Welcome to The best News Review Website'
    return render_template('index.html', title = title,popular = popular_news)