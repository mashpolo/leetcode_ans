#!/usr/bin/env python
# coding=utf-8
"""
@desc:   有序数组求指定和的两个数
@author: luluo
@date:   2018-9-4

"""


class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for (index, x) in enumerate(numbers):
        #     rest = target - x
        #     if rest in numbers[index + 1:]:
        #         return [index + 1, numbers[index + 1:].index(rest) + index + 2]
        #     else:
        #         continue

        map_dict = {}
        for (index, x) in enumerate(numbers):
            rest = target - x
            if rest in map_dict:
                return [map_dict[rest], index + 1]
            else:
                map_dict[x] = index + 1


A = Solution()
print(A.twoSum([2,3,4], 6))