#!/usr/bin/env python3
"""The Least Recently Used caching module.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """This represents an object that allows storing and
    retrieving items from a dictionary with a LRU
    removal mechanism when the limit is reached.
    """
    def __init__(self):
        """This initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """This adds an item in the cache.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lru_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """This retrieves an item by key.
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
