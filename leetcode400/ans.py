#!/usr/bin/env python
# coding=utf-8
"""
@desc:   第N个数字
@author: Luo.lu
@date:   2018-10-15

"""


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit=1
        base=9
        ith=1
        while n>base*digit:
            n=n-base*digit
            digit=digit+1
            ith=ith+base
            base=base*10
        return ord(str(ith+(n-1)//digit)[(n-1)%digit])-ord('0')
