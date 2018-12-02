#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-12-2

"""


class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        lens = 0
        total = []
        for x in nums:
            lens += len(x)
            total.extend(x)

        if lens != r*c:
            return nums
        else:
            res = []
            start = 0
            while start < lens:
                res.append(total[start:start+c])
                start += c

        return res


if __name__ == '__main__':
    A = Solution()
    print(A.matrixReshape(nums =[[1,2],[3,4]], r=4, c=1))
