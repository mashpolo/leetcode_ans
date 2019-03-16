#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-03-17

"""


class Solution:
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        A.sort()
        A = A[::-1]
        # 排列组合，且小于23:59
        from itertools import permutations
        for i in permutations(A, 4):
            part1 = int(str(i[0]) + str(i[1]))
            part2 = int(str(i[2]) + str(i[3]))
            if part1 < 24 and part2 < 60:
                return str(i[0]) + str(i[1]) + ':' + str(i[2]) + str(i[3])
        return ""
