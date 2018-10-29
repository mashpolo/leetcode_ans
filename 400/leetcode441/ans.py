#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-10-29

"""


class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n ==0:
            return 0
        return max(int(pow(2 * n + 0.25, 1/2) - 0.5), int(pow(2*n-1, 1/2) - 1))


if __name__ == '__main__':
    A = Solution()
    print(A.arrangeCoins(1))
