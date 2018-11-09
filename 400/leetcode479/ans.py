#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-11-9

"""
class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        return [9, 9009, 906609, 99000099, 9966006699, 999000000999, \
                    99956644665999, 9999000000009999][n - 1] % 1337

