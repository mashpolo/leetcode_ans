#!/usr/bin/env python
# coding=utf-8
"""
@desc:   使用牛顿迭代来求平方根
@author: luluo
@date:   2018-8-14

"""


class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 1.0
        while abs(result * result - x) > 0.1:
            result = (result + x / result) / 2
        return int(result)


A = Solution()
print(A.mySqrt(191))
