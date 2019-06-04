#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-06-04

"""
from itertools import combinations


class Solution:
    def subsetsWithDup(self, nums):
        if not nums:
            return []
        nums.sort()
        ans = []
        for i in range(len(nums)+1):
            sets = list(set(combinations(nums, i)))
            ans.extend(sets)
        return ans


if __name__ == '__main__':
    A = Solution()
    print(A.subsetsWithDup([1,4,4,4,4]))


