#!/usr/bin/env python
# coding=utf-8
"""
@desc:   旋转数组
@author: Luo.lu
@date:   2018-9-11

"""


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        while k > 0:
            nums.insert(0,nums.pop())
            k -= 1


A = Solution()
print(A.rotate([1,2,3,4], 2))

