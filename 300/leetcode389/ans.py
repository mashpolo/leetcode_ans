#!/usr/bin/env python
# coding=utf-8
"""
@desc:   
@author: Luo.lu
@date:   2018-10-14

"""
from functools import reduce
import operator


class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return chr(reduce(operator.xor, map(ord, s + t)))


if __name__ == '__main__':
    A = Solution()
    print(A.findTheDifference('abc', 'abcd'))