#!/usr/bin/env python
# coding=utf-8
"""
@desc:   两整数相加
@author: Luo.lu
@date:   2018-10-10

"""


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b != 0:
            carry = a & b
            a = (a ^ b) % 0x100000000
            b = (carry << 1) % 0x100000000
        return a if a <= 0x7FFFFFFF else a | (~0x100000000+1)

