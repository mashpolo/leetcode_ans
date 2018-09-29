#!/usr/bin/env python
# coding=utf-8
"""
@desc:   各位相加
@author: Luo.lu
@date:   2018-9-29

"""


class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        n = sum([int(x) for x in str(num)])
        while n > 9:
            n = sum([int(x)  for x in str(n)])
        return n


if __name__ == '__main__':
    A = Solution()
    print(A.addDigits(19))
