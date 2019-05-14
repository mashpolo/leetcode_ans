#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-05-16

"""


class Solution:
    dp = None
    mp = None

    def helper(self,m,n):
        if m<0 or n<0: return 1<<30
        if self.dp[m][n]==1<<30:
            self.dp[m][n] = min(self.helper(m-1,n),self.helper(m,n-1))+self.mp[m][n]
        return self.dp[m][n]

    def minPathSum(self, grid: List[List[int]]) -> int:
        self.mp = grid
        self.dp = []
        a = [1<<30]*len(grid[0])
        for i in range(len(grid)):
            self.dp.append(a.copy())
        self.dp[0][0] = grid[0][0]
        return self.helper(len(grid)-1,len(grid[0])-1)
