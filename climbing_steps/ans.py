#!/usr/bin/env python
# coding=utf-8
"""
@desc:   爬楼梯算法
@author: luluo
@date:   2018-8-15

"""


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return  1
        elif n == 2:
            return 2
        else:
            while n - 2 > 0:
                return self.climbStairs(n - 2) + self.climbStairs(n - 1)


A = Solution()
print(A.climbStairs(35))