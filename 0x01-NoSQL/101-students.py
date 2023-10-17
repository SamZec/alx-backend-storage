#!/usr/bin/env python3
""" 101-students.py - module for top_students(mongo_collection) function"""


import pymongo


def top_students(mongo_collection):
    """
        function that returns all students sorted by average score:

        args:
            mongo_collection - pymongo collection object
    """

    pipe = [
            {"$project":
                {"name": "$name",
                    "averageScore": {"$avg": "$topics.score"}}},
            {"$sort": {"averageScore": pymongo.DESCENDING}}
            ]

    res = mongo_collection.aggregate(pipe)

    return res


if __name__ == '__main__':
    top_students(mongo_collection)
