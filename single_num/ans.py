#!/usr/bin/env python
# coding=utf-8
"""
@desc:   判断一个非空整数数组的不重复数字
@author: luluo
@date:   2018-8-31

"""


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in nums:
            res^=i
        return res


A = Solution()
A.singleNumber([1,2,4,2,1])

