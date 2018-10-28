#!/usr/bin/env python
# coding=utf-8
"""
@desc:   求阶乘后的零个数
@author: Luo.lu
@date:   2018-9-8

"""


class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        rest = n // 5
        res = rest
        while rest > 0:
            res += rest // 5
            rest = rest // 5
        return res


A = Solution()
print(A.trailingZeroes(26))
