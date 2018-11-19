from pymongo import MongoClient

client = MongoClient()
db = client.articles
collection = db.articles
collection.ensure_index('url', unique=True)


def insert(url):
    try:
        collection.update_one(
            {'url': url},
            {'$set': {'url': url}},
            upsert=True
        )
        return True
    except:
        return False


