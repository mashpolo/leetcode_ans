#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-03-21

"""


class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort(reverse=True)
        if len(A) < 3:
            return 0
        for i in range(len(A) - 2):
            if A[i+1] + A[i+2] > A[i]:
                return A[i] + A[i+1] + A[i+2]
        return 0
