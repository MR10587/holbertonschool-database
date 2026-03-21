#!/usr/bin/env python3
'''Redis Quickstart'''
import redis
import uuid


class Cache:
    '''Cache class'''
    def __init__(self):
        '''Redis instance flushed'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data):
        key = uuid.uuid4()
        self._redis.set(key, data)
        return key
