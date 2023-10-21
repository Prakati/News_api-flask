from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__)

# Move the NewsApiClient initialization outside of the route
newsapi = NewsApiClient(api_key="a62b65e7b2844798af9688f03c5a1321")

@app.route('/')
def index():
    topheadlines = newsapi.get_top_headlines(sources='bbc-news')
    articles = topheadlines['articles']

    news = []
    desc = []
    img = []

    for article in articles:
        news.append(article['title'])
        desc.append(article['description'])
        img.append(article['urlToImage'])

    # The following line should be outside of the loop
    mylist = zip(news, desc, img)

    return render_template('index.html', context=mylist)

if __name__ == '__main__':
    app.run(debug=True)