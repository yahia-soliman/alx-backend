#!/usr/bin/env python3
"""The very basic level of caching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """First in first out
    """
    def __init__(self):
        self.q = []
        super().__init__()

    def put(self, key, item):
        """cache an item with a key"""
        if key is None or item is None:
            return
        if key in self.q:
            self.q.remove(key)
        self.cache_data[key] = item
        self.q.append(key)
        if len(self.q) > self.MAX_ITEMS:
            key = self.q.pop(0)
            del self.cache_data[key]
            print(f"DISCARD: {key}")

    def get(self, key):
        """get an item from the cache with a key"""
        return self.cache_data.get(key)
