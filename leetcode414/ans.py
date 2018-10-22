#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-10-22

"""


class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(set(nums)) < 3:
            return max(nums)
        nums.sort()
        n1 = nums.pop()
        n2 = nums.pop()
        n3 = nums.pop()
        while n1 == n2 or n2 == n3:
            n2 = n3
            if nums:
                n3 = nums.pop()
            else:
                break
        return n3


if __name__ == '__main__':
    A = Solution()
    print(A.thirdMax([1, 2, 1]))
