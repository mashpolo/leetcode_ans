#!/usr/bin/env python
# coding=utf-8
"""
@desc:   判断是否从左向右读和正常整数完全一样
@author: luluo
@date:   2018/7/31

"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        div = 1
        while x / div >= 10:
            div *= 10
        while x > 0:
            l = x // div
            r = x % 10

            if l != r:
                return False
            x %= div
            x //= 10
            div /= 100
        return True


A = Solution()
print(A.isPalindrome(123))
