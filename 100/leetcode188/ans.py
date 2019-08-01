#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-08-01

"""
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) <= 1: return 0
        if (k < len(prices) // 2) :
            dp = [[-prices[0], 0] for i in range(k+1)]
            for price in prices[1:]:
                for i in range(1, k+1):
                    dp[i] = [max(dp[i][0], dp[i-1][1]-price), max(dp[i][1], dp[i][0]+price)]
            return dp[k][1]
        else:
            dp = [-prices[0], 0]
            for price in prices[1:]:
                dp = [max(dp[0], dp[1]-price), max(dp[1], dp[0]+price)]
            return dp[1]
