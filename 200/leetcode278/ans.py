#!/usr/bin/env python
# coding=utf-8
"""
@desc:   第一个错误的版本
@author: Luo.lu
@date:   2018-10-1

"""


def isBadVersion(n):
    return n >= 3


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while True:
            mid = (left + right) // 2
            if isBadVersion(mid):
                if mid == 1 or not isBadVersion(mid - 1):
                    return mid
                right = mid - 1
            else:
                left = mid + 1


if __name__ == '__main__':
    A = Solution()
    print(A.firstBadVersion(9))