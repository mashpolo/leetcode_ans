#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-05-24

"""


class Solution:
    def subsets(self, nums):
        d = []
        d.append([])
        for x in nums:
            le = len(d)
            for i in range(le):
                print(d[i])
                t = [x]
                d.append(t+d[i])
        return d


if __name__ == '__main__':
    A = Solution()
    print(A.subsets(nums=[1,2,3]))
