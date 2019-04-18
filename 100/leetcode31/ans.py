#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-04-18

"""


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        for x in range(size - 1, -1, -1):
            if nums[x - 1] < nums[x]:
                break
        if x > 0:
            for y in range(size - 1, -1, -1):
                if nums[y] > nums[x - 1]:
                    nums[x - 1], nums[y] = nums[y], nums[x - 1]
                    break
        nums[x:] = nums[x:][::-1]
        # for z in range((size - x) // 2):
        #     nums[x + z], nums[size - z - 1] = nums[size - z - 1], nums[x + z]


if __name__ == '__main__':
    A = Solution()
    l = [1,2,4]
    A.nextPermutation(l)
    print(l)
