from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from celery import Celery, platforms
from newspaper import Article
from model import insert_url, insert_txt
from gevent import monkey
monkey.patch_all()

platforms.C_FORCE_ROOT = True

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/1'
celery = Celery(app.name)
celery.conf.update(app.config)

api = Api(app)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,session_id')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS,HEAD')
    # 这里不能使用add方法，否则会出现 The 'Access-Control-Allow-Origin' header contains multiple values 的问题
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@celery.task
def insert_article_text(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        txt = article.text
    except:
        txt = ''
    insert_txt(url, txt)

class Url(Resource):
    def get(self):
        url = request.args.get('url')
        result = insert_url(url)
        insert_article_text.delay(url)
        return jsonify(result)

api.add_resource(Url, '/api/insert')


if __name__ == '__main__':
    app.run()
