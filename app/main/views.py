from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news,get_article

@main.route('/', methods=[ 'GET'])
def index():




   news=get_news()

   title = "NewsUpdates"

   return render_template ('index.html', news = news )



@main.route('/source/<id>')
def article(id):
    '''
    view news page function that returns the news details  and its data
    '''
    articles = get_article(id)
    title = "NewsUpdtes"
    return render_template('article.html', articles = articles, title=title)