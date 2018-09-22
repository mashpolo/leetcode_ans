#!/usr/bin/env python
# coding=utf-8
"""
@desc:   存在重复元素
@author: Luo.lu
@date:   2018-9-22

"""


class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) < len(nums)