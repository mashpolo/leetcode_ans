#!/usr/bin/env python
# coding=utf-8
"""
@desc:   搜索插入位置
@author: luluo
@date:   2018/8/8

"""


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        for (index, x) in enumerate(nums):
            if x == target:
                return index
            elif x > target:
                return index
            else:
                if index == len(nums) - 1:
                    return index + 1
                continue


A = Solution()
print(A.searchInsert([1,3,5,6], 7))