#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-06-23

"""


class Solution(object):
    def maxProfit(self, prices):
        if not prices: return 0
        n = len(prices)
        h = [[0 for j in range(2)] for i in range(n)]
        f = [[0 for j in range(2)] for i in range(n)]
        min_price = prices[0]
        for i in range(1, n):
            f[i][1] = max(prices[i] - min_price, f[i - 1][1])
            min_price = min(min_price, prices[i])

        max_price = prices[n - 1]
        for i in range(n - 2, -1, -1):
            h[i][1] = max(max_price - prices[i], h[i + 1][1])
            max_price = max(max_price, prices[i])
        ans = 0
        for i in range(1, n - 1):
            ans = max(ans, h[i + 1][1] + f[i][1], f[i][1])
        ans = max(ans, f[n - 1][1])
        return ans
