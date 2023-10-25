#!/usr/bin/env python3
"""
FIFO Caching
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    a class FIFOCache that inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """ Init method """
        self.key_indices = []
        super().__init__()

    def put(self, key, item):
        """
        assign self.cache_data the item value for the key
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                return

            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                item_discarded = self.key_indices.pop(0)
                del self.cache_data[item_discarded]
                print("DISCARD:", item_discarded)

            self.cache_data[key] = item
            self.key_indices.append(key)

    def get(self, key):
        """
        return the value in self.cache_data linked to key.
        """
        return self.cache_data[key] if key in self.cache_data else None
