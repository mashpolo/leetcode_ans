#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-01-14

"""


class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return -1
        if len(nums) > 2:
            begin = 0
            left = 0
            right = sum(nums[begin+1:])
            while begin + 1 <= len(nums):
                print(left, right)
                if left == right:
                    return begin

                else:
                    begin += 1
                    left = sum(nums[:begin])
                    right = sum(nums[begin + 1:])

            return -1


if __name__ == '__main__':
    A = Solution()
    print(A.pivotIndex([-1,-1,-1,0,1,1]))
