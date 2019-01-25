#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-01-25

"""
from collections import Counter


class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        gem = set(J)
        count_s = Counter(S)
        res = 0
        for x in gem:
            if x in count_s:
                res += count_s[x]

        return res


