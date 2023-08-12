from flask import Flask, render_template
import requests
import time

application = Flask(__name__)

NEWS_API_URL = "https://newsapi.org/v2/top-headlines"
API_KEY = "2c378a3102d04b1382e5c37c7492183b"  # Replace with your NewsAPI API key

@application.route('/')
def news():
    return render_template('news.html')

@application.route('/get_news')
def get_news():
    params = {
        'country': 'us',  # Fetch news from the US
        'apiKey': API_KEY
    }

    response = requests.get(NEWS_API_URL, params=params)
    news_data = response.json()

    articles = news_data.get('articles', [])

    return {'articles': articles}

if __name__ == '__main__':
    application.run(host='0.0.0.0')
