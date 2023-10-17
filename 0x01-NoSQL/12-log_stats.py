#!/usr/bin/env python3
"""
    12-log_stats.py
    script that provides some stats about Nginx logs stored in MongoDB
"""


if __name__ == '__main__':
    from pymongo import MongoClient


    client = MongoClient()
    db = client.logs.nginx

    print('{} logs'.format(db.estimated_document_count()))
    print('Methods:')
    print('\tmethod GET: {}'.format(db.count_documents({'method': 'GET'})))
    print('\tmethod POST: {}'.format(db.count_documents({'method': 'POST'})))
    print('\tmethod PUT: {}'.format(db.count_documents({'method': 'PUT'})))
    print('\tmethod PATCH: {}'.format(db.count_documents({'method': 'PATCH'})))
    print('\tmethod DELETE: {}'.format(db.count_documents(
          {'method': 'DELETE'})))
    print('{} status check'.format(db.count_documents(
          {'method': 'GET', 'path': '/status'})))
