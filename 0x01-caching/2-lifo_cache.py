#!/usr/bin/env python3
"""The very basic level of caching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Last in first out
    CRAZY, only the last cached item will be deleted
    """
    def __init__(self):
        self.last = None
        super().__init__()

    def put(self, key, item):
        """cache an item with a key"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if self.last and len(self.cache_data) > self.MAX_ITEMS:
            del self.cache_data[self.last]
            print(f"DISCARD: {self.last}")
        self.last = key

    def get(self, key):
        """get an item from the cache with a key"""
        return self.cache_data.get(key)
