#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-11-3

"""


class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        tests = minutesToTest / minutesToDie + 1
        pigs = 0
        while tests ** pigs < buckets:
            pigs += 1
        return pigs
