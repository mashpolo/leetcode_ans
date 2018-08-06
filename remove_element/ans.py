#!/usr/bin/env python
# coding=utf-8
"""
@desc:   在原数组基础上删除匹配的数
@author: luluo
@date:   2018/8/6

"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[length] = nums[i]
                length += 1
        return length


A = Solution()
print(A.removeElement([3,2,3,2], 3))