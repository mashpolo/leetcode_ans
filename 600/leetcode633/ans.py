#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-12-17

"""


class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for i in range(0,int(c**0.5)+1):
            j=c-i**2
            if((int(j**0.5)**2)==j):
                return True
        return False
