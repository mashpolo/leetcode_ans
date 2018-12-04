#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-12-4

"""


class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        return min(len(candies) // 2, len(set(candies)))


if __name__ == '__main__':
    A = Solution()
    print(A.distributeCandies([1,1,2,2,3,3]))
