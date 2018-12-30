#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-12-30

"""

class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        na, nb = len(A), len(B)
        times = nb / na + 3
        for i in range(1, times):
            if B in A * i:
                return i
        return -1



