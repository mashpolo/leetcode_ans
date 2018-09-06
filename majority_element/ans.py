#!/usr/bin/env python
# coding=utf-8
"""
@desc:   求一个数组中的众数
@author: Luo.lu
@date:   2018-9-6

"""


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return

        num_dict = {}
        flag = len(nums) // 2
        for x in nums:
            num_dict[x] = num_dict.get(x, 0) + 1
            if num_dict[x] > flag:
                return x


A = Solution()
print(A.majorityElement([2,2,1,1,1,2,2]))