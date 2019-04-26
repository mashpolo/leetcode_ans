#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-04-26

"""


class Solution:
    def firstMissingPositive(self, nums: list) -> int:
        if not nums:
            return 1

        for x in range(1, len(nums) + 1):
            if x not in nums:
                return x

        return max(nums) + 1


if __name__ == '__main__':
    A = Solution()
    print(A.firstMissingPositive([7,8,9,11,12]))
