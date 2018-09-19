#!/usr/bin/env python
# coding=utf-8
"""
@desc:   计数质数
@author: Luo.lu
@date:   2018-9-19

"""


class Solution():
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n is None or n <= 1:
            return 0
        tmp = [True] * n
        tmp[0] = False
        tmp[1] = False

        i = 2
        while i * i < n:
            if tmp[i]:
                j = i
                while j * i < n:
                    tmp[i * j] = False
                    j += 1
            i += 1

        res = 0
        for k in tmp:
            if k:
                res += 1
        return res


if __name__ == "__main__":
    A = Solution()
    print(A.countPrimes(12))