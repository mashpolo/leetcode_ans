#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-01-08

"""


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l = []

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.l.append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        while key in self.l:
            self.l.remove(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return key in self.l



