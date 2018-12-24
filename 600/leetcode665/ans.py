#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-12-24

"""


class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        chance = 1
        for x in range(len(nums)):
            if x and nums[x] < nums[x - 1]:
                if not chance:
                    return False
                chance -= 1
                if x > 1 and nums[x] <= nums[x - 2]:
                    nums[x] = nums[x - 1]
        return True


if __name__ == '__main__':
    A = Solution()
    print(A.checkPossibility([3,4,2,3]))
