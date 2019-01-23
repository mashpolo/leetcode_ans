#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-01-23

"""
from collections import Counter


class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        prime_nums = [2, 3, 5, 7, 11, 13, 17, 19]
        res = 0

        for x in range(L, R + 1):
            bin_num = bin(x)[2:]
            print(bin_num)
            count = Counter(bin_num)
            if count.get('1') in prime_nums:
                res += 1
        return res


if __name__ == '__main__':
    A = Solution()
    print(A.countPrimeSetBits(10, 15))
