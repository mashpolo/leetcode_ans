#!/usr/bin/env python
# coding=utf-8
"""
@desc:   求二进制数中的1的个数
@author: Luo.lu
@date:   2018-9-13

"""
from collections import Counter


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return Counter(bin(n)[2:])['1']


if __name__ == "__main__":
    A = Solution()
    print(A.hammingWeight(11))