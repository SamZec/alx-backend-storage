#!/usr/bin/env python3
"""
9-insert_school.py
module for the function insert_school(mongo_collection, **kwargs)
"""


def insert_school(mongo_collection, **kwargs):
    """
        function that inserts a new document in a collection based on kwargs
        Returns the new _id
    """
    res = mongo_collection.insert_one(kwargs)

    return res.inserted_id


if __name__ == '__main__':
    insert_school(mongo_collection, **kwargs)
