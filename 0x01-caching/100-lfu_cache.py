#!/usr/bin/env python3
"""The very basic level of caching
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Least Frequentely Used is OUT
    This one is the best, but LRU is ok
    """
    def __init__(self):
        self.lfu = []
        super().__init__()

    def put(self, key, item):
        """cache an item with a key"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            self.pop()
        self.key_used(key)

    def get(self, key):
        """get an item from the cache with a key"""
        val = self.cache_data.get(key)
        if val:
            self.key_used(key)
        return val

    def pop(self):
        """Get the least used element in cache"""
        lru = self.lfu[0]
        for tup in self.lfu:
            if tup[1] < lru[1]:
                lru = tup
        print(f"DISCARD: {lru[0]}")
        del self.cache_data[lru[0]]
        self.lfu.remove(lru)
        del lru

    def key_used(self, key):
        """Update the usage data"""
        for tup in self.lfu:
            if tup[0] == key:
                self.lfu.append((tup[0], tup[1] + 1))
                self.lfu.remove(tup)
                break
        else:
            self.lfu.append((key, 0))
