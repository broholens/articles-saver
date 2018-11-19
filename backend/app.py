from gevent import monkey
monkey.patch_all()
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from model import insert


app = Flask(__name__)
api = Api(app)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,session_id')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS,HEAD')
    # 这里不能使用add方法，否则会出现 The 'Access-Control-Allow-Origin' header contains multiple values 的问题
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

class Url(Resource):
    def get(self):
        url = request.args.get('url')
        result = insert(url)
        return jsonify({'result': result})

api.add_resource(Url, '/api/insert')


if __name__ == '__main__':
    app.run()
