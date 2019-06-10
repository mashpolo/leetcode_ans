#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-06-10

"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2,n3 = len(s1), len(s2), len(s3)
        if n1+n2 != n3:
            return False
        dp = [[False for _ in range(n2+1)] for _ in range(n1+1)]
        dp[0][0] = True
        for i in range(n1+1):
            for j in range(n2+1):
                if not (i ==0 and j == 0):
                    p1 = False
                    if i > 0 and s1[i-1] == s3[i+j-1]:
                        p1 = dp[i-1][j]
                    p2 = False
                    if j > 0 and s2[j-1] == s3[i+j-1]:
                        p2 = dp[i][j-1]
                    dp[i][j] = p1 or p2
        return dp[n1][n2]
