#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-05-15

"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        dp=[[0 for j in range(n+2)]for i in range(m+2)]
        if obstacleGrid[0][0]==1:
            return 0    #排除起点障碍的特殊情况
        for i in range(1,m+1):
            for j in range (1,n+1):
                if i==1 and j==1:
                    dp[1][1]=1
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
                if obstacleGrid[i-1][j-1]==1:
                    dp[i][j]=0
        return dp[m][n]
