#!/usr/bin/env python3
"""
    12-log_stats.py
    script that provides some stats about Nginx logs stored in MongoDB
"""


if __name__ == '__main__':
    from pymongo import MongoClient
    import pymongo
    client = MongoClient()
    db = client.logs.nginx

    print('{} logs'.format(db.estimated_document_count()))
    print('Methods:')

    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

    for item in methods:
        print('\tmethod {}: {}'.format(item,
              db.count_documents({'method': item})))

    print('{} status check'.format(db.count_documents(
          {'method': 'GET', 'path': '/status'})))

    pipe = [
            {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
            {"$sort": {"count": pymongo.DESCENDING}},
            {"$limit": 10}
            ]

    print("IPs:")

    for item in db.aggregate(pipe):
        print('\t{}: {}'.format(item['_id'], item['count']))
