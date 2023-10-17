#!/usr/bin/env python3
""" 8-all.py - a module for list_all(mongo_collection) function"""


def list_all(mongo_collection):
    """
        a function that lists all documents in a collection.
        Return an empty list if no document in the collection.
    """
    res = list(mongo_collection.find())

    return res


if __name__ == '__main__':
    list_all(mongo_collection)
