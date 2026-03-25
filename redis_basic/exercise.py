#!/usr/bin/env python3
'''Redis Quickstart'''

import uuid
from typing import Union, Callable, Optional, Any
import redis
from functools import wraps


def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__

        self._redis.incr(key)
        return method(self, *args, **kwargs)
    
    return wrapper


class Cache:
    '''Cache class'''
    def __init__(self) -> None:
        '''Redis instance flushed'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, float, int, bytes]) -> str:
        '''Storing data in random key'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable[[bytes], Any]] = None) -> Any:
        '''Getting value in desired format'''
        value = self._redis.get(key)

        if value is None:
            return None

        if fn is None:
            return value

        return fn(value)

    def get_str(self, key: str) -> Optional[str]:
        '''Getting value in str'''
        return self.get(key=key, fn=lambda v: v.decode('utf-8'))
    
    def get_int(self, key: str) -> Optional[int]:
        '''Getting value in integer'''
        return self.get(key=key, fn=lambda v: int(v.decode('utf-8')))
