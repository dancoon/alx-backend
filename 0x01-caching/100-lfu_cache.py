#!/usr/bin/env python3
"""
caching System
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    inherits from BaseCaching and is a caching system
    """

    def __init__(self) -> None:
        """ initialize of class """
        self.temp_list = {}
        super().__init__()

    def put(self, key, item):
        """
        Must assign self.cache_data the item value for the key
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                _key = min(self.temp_list, key=self.temp_list.get)
                self.temp_list.pop(_key)
                self.cache_data.pop(_key)
                print(f"DISCARD:", _key)
            if not (key in self.temp_list):
                self.temp_list[key] = 0
            else:
                self.temp_list[key] += 1

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key
        """
        if key and key in self.cache_data:
            self.temp_list[key] += 1
            return self.cache_data.get(key)
        return None
