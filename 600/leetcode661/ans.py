#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-12-23

"""
import math


class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(M)
        n = len(M[0])
        result = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                current = 0
                count = 0
                for a in [-1, 0, 1]:
                    for b in [-1, 0, 1]:
                        row = i + a
                        col = j + b
                        if 0 <= row < m and 0 <= col < n:
                            current += M[row][col]
                            count += 1
                result[i][j] = math.floor(current / count)
        return result
