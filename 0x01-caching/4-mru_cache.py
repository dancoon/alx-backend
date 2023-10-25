#!/usr/bin/env python3
"""
MRU Caching
"""


from collections import OrderedDict


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        self.mru_order = OrderedDict()
        super().__init__()

    def put(self, key, item):
        """
        Must assign self.cache_data the item value for the key key
        """
        if key and item:
            self.cache_data[key] = item
            self.mru_order[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                item_discarded = next(iter(self.mru_order))
                del self.cache_data[item_discarded]
                self.mru_order.popitem(last=False)
                print("DISCARD:", item_discarded)

            self.mru_order.move_to_end(key, False)

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key.
        """
        if key in self.cache_data:
            self.mru_order.move_to_end(key, False)
            return self.cache_data[key]
        return None
