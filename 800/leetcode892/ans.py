#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-03-01

"""


class Solution:
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    res += 4*grid[i][j] + 2
                if i :
                    res -= min(grid[i][j],grid[i-1][j]) * 2
                if j :
                    res -= min(grid[i][j],grid[i][j-1]) * 2
        return res
