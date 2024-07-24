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


my_cache = BasicCache()
my_cache.print_cache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
print(my_cache.get("D"))
my_cache.print_cache()
my_cache.put("D", "School")
my_cache.put("E", "Battery")
my_cache.put("A", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
