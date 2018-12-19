#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-12-19

"""


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        res = sum(nums[0:k])
        tmp = res
        n = len(nums)
        for i in range(k,n):
            tmp = tmp - nums[i -k] + nums[i]
            res = max(res, tmp)

        return res / ( k + 0.0)


if __name__ == '__main__':
    A = Solution()
    print(A.findMaxAverage([1,12,-5,-6,50,3], k=4))
