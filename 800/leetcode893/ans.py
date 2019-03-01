#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-03-01

"""


class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        se = set()
        total = []
        for s in A:
            i1 = []
            i2 = []
            for i in range(len(s)):
                if i % 2 == 1:
                    i1.append(s[i])
                else:
                    i2.append(s[i])
            i1.sort()
            i2.sort()
            ii = ''.join(i1+i2)
            total.append(ii)
        se = set(total)
        return len(se)
