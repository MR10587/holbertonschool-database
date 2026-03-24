#!/usr/bin/env python3
'''Redis Quickstart'''

import uuid
from typing import Union, Callable, Optional, Any
import redis


class Cache:
    '''Cache class'''
    def __init__(self) -> None:
        '''Redis instance flushed'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, float, int, bytes]) -> str:
        '''Storing data in random key'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable[bytes, any]] = None) -> Any:
        value = self._redis.get(key)
        if fn:
            return fn(value)
        return value
