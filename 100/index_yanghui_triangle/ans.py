#!/usr/bin/env python
# coding=utf-8
"""
@desc:   返回杨辉三角的第n行
@author: luluo
@date:   2018-8-27

"""


class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rest = [1]
        while rowIndex > 0:
            rest = list(map(lambda x, y: x+y, rest + [0], [0] + rest))
            rowIndex -= 1
        return rest


A = Solution()
print(A.getRow(1))
