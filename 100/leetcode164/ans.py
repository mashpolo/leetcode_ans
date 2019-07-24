#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-07-24

"""


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()
        ans = 0
        pre = nums[0]
        for i in nums:
            ans = max(ans, i - pre)
            pre = i
        return ans
