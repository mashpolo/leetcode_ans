#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-07-14

"""

class LRUCache:

    def __init__(self, capacity):
        self.dict = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.dict.keys():
            return -1
        else:
            self.dict.move_to_end(key)
            return self.dict[key]

    def put(self, key, value):
        if key in self.dict.keys():
            self.dict[key] = value
            self.dict.move_to_end(key)
        else:
            if len(self.dict) == self.capacity:
                self.dict.popitem(0)
            self.dict[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
