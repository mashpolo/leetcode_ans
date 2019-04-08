#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-04-08

"""


import sys


class Solution:  # O(N^2),O(1)
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        dist = sys.maxsize
        for i, num in enumerate(nums[:-2]):
            a = i + 1
            b = len(nums) - 1
            while a < b:
                delta = target - (num + nums[a] + nums[b])
                if abs(delta) < dist:  # 距离比较记得加上绝对值
                    res = num + nums[a] + nums[b]
                    dist = abs(delta)
                if delta > 0:
                    a += 1
                else:
                    b -= 1

        return res
