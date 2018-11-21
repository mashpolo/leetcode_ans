#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-11-21

"""
import collections


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0: return 0
        c = collections.Counter(nums)
        return sum(c[n + k] > 1 - bool(k) for n in c.keys())


if __name__ == '__main__':
    A = Solution()
    print(A.findPairs([3,1,4,1,5]
,2))
