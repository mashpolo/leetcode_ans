#!/usr/bin/env python
# coding=utf-8
"""
@desc:  两数字只和选择
@author: luluo
@date:   2018/7/30

"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, num in enumerate(nums):
            if num in dic:
                return [dic[num], i]
            else:
                dic[target - num] = i


A = Solution()
print(A.twoSum([3,3], target=6))
