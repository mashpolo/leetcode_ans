#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-07-23

"""


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def binarySearch(nums, start, end):
            while start < end:
                mid = (start + end) // 2
                if nums[mid] > nums[mid + 1]:
                    end = mid
                else:
                    start = mid + 1
            return start
        
        return binarySearch(nums, 0, len(nums) - 1)

        
