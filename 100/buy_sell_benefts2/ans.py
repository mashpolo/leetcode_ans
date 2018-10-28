#!/usr/bin/env python
# coding=utf-8
"""
@desc:   尽可能多的获取更多的利润
@author: luluo
@date:   2018-8-29

"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        for i in range(1, len(prices)):
            if prices[i-1] < prices[i]:
                res += prices[i] - prices[i-1]
        return res


A = Solution()
print(A.maxProfit([1,4,3,2,5]))