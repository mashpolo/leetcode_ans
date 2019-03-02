#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-03-02

"""


class Solution:
    def isMonotonic(self, A):
        return A == sorted(A) or A == sorted(A)[::-1]


if __name__ == '__main__':
    A = Solution()
    print(A.isMonotonic([1,2,3,3]))
