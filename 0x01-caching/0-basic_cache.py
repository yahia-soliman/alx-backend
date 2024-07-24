#!/usr/bin/env python3
"""The very basic level of caching
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Lets cache some things
    """
    def put(self, key, item):
        """cache an item with a key"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """get an item from the cache with a key"""
        return self.cache_data.get(key)
