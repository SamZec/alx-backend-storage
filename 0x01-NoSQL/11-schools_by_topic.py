#!/usr/bin/env python3
# 11-schools_by_topic.py
""" module for schools_by_topic(mongo_collection, topic) function """


def schools_by_topic(mongo_collection, topic):
    """
        function that returns the list of school having a specific topic

        args:
            mongo_collection - pymongo collection object
            topic (string) - topic searched
    """
    return mongo_collection.find({'topics': topic})


if __name__ == '__main__':
    schools_by_topic(mongo_collection, topic)
