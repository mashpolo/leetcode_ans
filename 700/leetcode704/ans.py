#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-01-07

"""


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        l = len(nums)
        res = 0
        while l // 2 > 0:
            key = len(nums) // 2

            if target == nums[key]:
                return res + key
            elif target < nums[key]:
                nums = nums[:key]
                l = len(nums)
            else:
                res += key
                nums = nums[key:]
                l = len(nums)
        return -1 if nums[0] != target else res


if __name__ == '__main__':
    A = Solution()
    print(A.search(nums=[-1,0,3], target=3))
