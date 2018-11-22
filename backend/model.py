# -*- coding: utf-8 -*-
from pymongo import MongoClient
from utils import get_article_text

client = MongoClient()
db = client.articles
collection = db.articles
collection.create_index('url', unique=True)

def insert_url(url):
    try:
        result = collection.update_one(
            {'url': url},
            # {'$set': {'txt': url}},
            upsert=True
        )
        if result.matched_count > 0:
            return {'type': 'warning', 'msg': 'url already exists!'}
        return {'type': 'success', 'msg': 'url add successfully!'}
    except:
        return {'type': 'error', 'msg': 'faild to add url'}

def insert_txt(url, txt):
    try:
        collection.update_one(
            {'url': url},
            {'$set': {'txt': txt}},
            upsert=True
        )
    except:
        pass
