#!/usr/bin/env python
# coding=utf-8
"""
@desc:   移动零
@author: Luo.lu
@date:   2018-10-2

"""


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        x = n = 0
        while n < l - 1:
            if nums[x] == 0:
                nums.pop(x)
                nums.append(0)
            else:
                x += 1
            n += 1
        return nums


if __name__ == '__main__':
    A = Solution()
    print(A.moveZeroes([0,1,0,3,12]))