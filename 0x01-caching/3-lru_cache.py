#!/usr/bin/env python3
"""
LRU Caching
"""


from typing import OrderedDict


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """" init method """
        self.lru_order = OrderedDict()
        super().__init__()

    def put(self, key, item):
        """
        Must assign self.cache_data the item value for the key
        """
        if key and item:
            self.lru_order[key] = item
            self.lru_order.move_to_end(key)
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            item_discarded = next(iter(self.lru_order))
            del self.cache_data[item_discarded]
            self.lru_order.popitem(last=False)
            print("DISCARD:", item_discarded)

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key
        """
        if key in self.cache_data:
            self.lru_order.move_to_end(key)
            return self.cache_data[key]
        return None
