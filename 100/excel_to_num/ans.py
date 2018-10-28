#!/usr/bin/env python
# coding=utf-8
"""
@desc:   求Excel表列序号
@author: Luo.lu
@date:   2018-9-7

"""


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        rest = 0
        for c in s:
            rest = rest*26 + ord(c) - 64
        return rest


A = Solution()
print(A.titleToNumber('ZY'))