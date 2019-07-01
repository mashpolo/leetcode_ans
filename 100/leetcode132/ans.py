#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-07-01

"""


class Solution:
    
    def minCut(self, s: str) -> int:
        if not s:
            return 0
        len1 = len(s)
        record = [[False for _ in range(len1)] for _ in range(len1)]
        path = [float('inf') for _ in range(len1)]
        for i in range(len1):
            path[i] = i
            for j in range(i, -1, -1):
                if s[j] == s[i] and ((i - j < 3) or record[j + 1][i - 1]):
                    record[j][i] = True
                    if j == 0:
                        path[i] = 0
                    else:
                        path[i] = min(path[i], path[j - 1] + 1)
        return path[-1]
