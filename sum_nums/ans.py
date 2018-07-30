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
        for (index, select_num) in enumerate(nums):
            need_num = target - select_num
            if need_num in nums:
                need_index = nums.index(need_num)
                if need_index != index:
                    return [index, need_index]


A = Solution()
print(A.twoSum([3,3], target=6))
