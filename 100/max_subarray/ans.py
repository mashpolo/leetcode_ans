#!/usr/bin/env python
# coding=utf-8
"""
@desc:   求最大和的子序列
@author: luluo
@date:   2018/8/10

"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        current = nums[0]
        m = current
        for i in range(1, len(nums)):
            if current < 0:
                current = 0
            current += nums[i]
            m = max(current, m)
        return m



A = Solution()
print(A.maxSubArray([31,-41,59,26,-53,58,97,-93,-23,84]))
