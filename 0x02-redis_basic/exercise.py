#!/usr/bin/env python3
""" exercise.py - module for the class Cache """


import redis
import uuid
from typing import Any


class Cache():
    """redis objects class"""
    def __init__(self):
        """intanstiate cache objects"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Any) -> str:
        """store data in Redis using random key and return the key"""
        _key = str(uuid.uuid4())
        self._redis.set(_key, data)
        key = self._redis.keys()
        return key[0].decode()
