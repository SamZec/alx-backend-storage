#!/usr/bin/env python3
""" exercise.py - module for the class Cache """


import redis
import uuid
from typing import Union, Callable, Optional


datatypes = Union[str, float, int, bytes]


class Cache():
    """redis objects class"""
    def __init__(self):
        """intanstiate cache objects"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: datatypes) -> str:
        """store data in Redis using random key and return the key"""
        key = str(uuid.uuid4())
        self._redis.mset({key: data})

        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> datatypes:
        """ convert the data back to the desired format """
        if fn:
            return fn(self._redis.get(key))
        data = self._redis.get(key)
        return data

    def get_int(self: bytes) -> int:
        """get a number"""
        return int.from_bytes(self, sys.byteorder)

    def get_str(self: bytes) -> str:
        """get a string"""
        return self.decode("utf-8")
