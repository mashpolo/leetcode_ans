#!/usr/bin/env python
# coding=utf-8
"""
@desc:   
@author: Luo.lu
@date:   2018-10-4

"""


class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.add = [0]
        for i in nums:
            self.add.append(self.add[-1] + i)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.add[j+1] - self.add[i]

