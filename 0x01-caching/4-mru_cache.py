#!/usr/bin/env python3
"""The very basic level of caching
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Least Recently used is OUT
    """
    def __init__(self):
        self.mru = []
        super().__init__()

    def put(self, key, item):
        """cache an item with a key"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            mru = self.mru.pop()
            print(f"DISCARD: {mru}")
            del self.cache_data[mru]
        self.key_used(key)

    def get(self, key):
        """get an item from the cache with a key"""
        val = self.cache_data.get(key)
        if val:
            self.key_used(key)
        return val

    def key_used(self, key):
        """Update the usage data"""
        if key in self.mru:
            self.mru.remove(key)
        self.mru.append(key)
