#!/usr/bin/env python3
'''Redis Quickstart'''
try:
    import redis
except ModuleNotFoundError:
    print("Salam")
import uuid
import typing


class Cache:
    '''Cache class'''
    def __init__(self):
        '''Redis instance flushed'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: typing.Union[str, float, int, bytes]) -> str:
        '''Storing data in random key'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
