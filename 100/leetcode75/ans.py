#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-05-21

"""


class Solution:
    def sortColors(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        lt = -1
        gt = n
        i = 0
        while i < gt :
            if nums[i] == 0:
                lt += 1
                nums[lt], nums[i] = nums[i], nums[lt]
                i += 1
            elif nums[i] == 2:
                gt -= 1
                nums[gt], nums[i] = nums[i], nums[gt]
            else:
                i += 1


if __name__ == '__main__':
    nums = [2,0,2,1,1,0]
    A = Solution()
    A.sortColors([2,0,2,1,1,0])
    print(nums)
