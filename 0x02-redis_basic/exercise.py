#!/usr/bin/env python3
""" exercise.py - module for the class Cache """


import redis
import uuid
from typing import Union


class Cache():
    """redis objects class"""
    def __init__(self):
        """intanstiate cache objects"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, float, int, bytes]) -> str:
        """store data in Redis using random key and return the key"""
        key = str(uuid.uuid4())
        self._redis.mset({key: data})

        return key
