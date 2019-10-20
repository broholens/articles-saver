import os
from concurrent.futures import ThreadPoolExecutor
from .save_article import Article
from .config.config import IMG_DIR
from flask import Flask, request
from flask_restful import Api, Resource

if not os.path.exists(IMG_DIR):
    os.makedirs(IMG_DIR)

app = Flask(__name__)
api = Api(app)

executor = ThreadPoolExecutor()
article = Article()


class ArticleSaver(Resource):
    def post(self):
        url = request.args.get('url')
        executor.submit(Article().save(url))
        return 'OK', 200


if __name__ == '__main__':
    app.run()
