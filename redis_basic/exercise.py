#!/usr/bin/env python3
'''Redis Quickstart'''
import redis
import uuid


class Cache:
    '''Cache class'''
    def __init__(self, r=redis.Redis()):
        '''Redis instance flushed'''
        self._redis = r
        self._redis.flushdb()

    def store(self, data):
        key = uuid.uuid4()
        self._redis.set(key, data)
        return key
