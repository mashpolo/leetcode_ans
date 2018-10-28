#!/usr/bin/env python
# coding=utf-8
"""
@desc:   
@author: Luo.lu
@date:   2018-10-13

"""
from collections import Counter


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = {}
        n2 = []
        for (index, x) in enumerate(s):
            if x in n2:
                continue
            if x in n:
                del n[x]
                n2.append(x)
            else:
                n[x] = index
        if n:
            return min(n.values())
        else:
            return -1


if __name__ == '__main__':
    A = Solution()
    print(A.firstUniqChar("aadadaad"))