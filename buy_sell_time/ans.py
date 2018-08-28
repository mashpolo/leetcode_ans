#!/usr/bin/env python
# coding=utf-8
"""
@desc:   计算卖股票的最佳利润
@author: luluo
@date:   2018-8-28

"""


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 时间复杂度O(n**2)
        # rest = []
        # while prices:
        #     last = prices.pop()
        #     min_list = filter(lambda x: x < last, prices)
        #     rest += list(map(lambda x: last - x, min_list))
        # return max(rest) if max(rest) > 0 else 0

        if len(prices) == 0:
            return 0
        minPrice = prices[0]
        maxProfit = 0
        for p in prices:
            if p < minPrice:
                minPrice = p
            elif p - minPrice > maxProfit:
                maxProfit = p - minPrice
        return maxProfit




A = Solution()
print(A.maxProfit([7,1,5,3,6,4]))