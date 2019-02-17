#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-02-18

"""

class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        res = -1
        d = 0
        for i in seats:
            if i == 1:
                if res == -1:
                    res = max(res, d)
                else:
                    res = max(res, d//2)
                d = 1
            else:
                d += 1
        return max(res, d-1)
