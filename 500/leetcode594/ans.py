#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-12-8

"""
import collections


class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        count = collections.Counter(nums)

        indep = sorted(list(set(nums)))
        total = 0
        root = indep.pop()
        while indep:
            n = indep.pop()
            if abs(root - n) == 1:
                total = count.get(n) + count.get(root) if count.get(n) + count.get(root) > total else total
            root = n
        return total


if __name__ == '__main__':
    A = Solution()
    print(A.findLHS([1,3,2,2,5,2,3,7]))

