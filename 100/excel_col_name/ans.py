#!/usr/bin/env python
# coding=utf-8
"""
@desc:   获取excel表的列名称
@author: Luo.lu
@date:   2018-9-5

"""


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        while n:
            res = chr((n - 1) % 26 + 65) + res
            n = (n - 1) // 26
        return res


A = Solution()
print(A.convertToTitle(701))
