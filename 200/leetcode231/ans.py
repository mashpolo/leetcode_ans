#!/usr/bin/env python
# coding=utf-8
"""
@desc:   2的幂
@author: Luo.lu
@date:   2018-9-24

"""


class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 0:
            return False

        last = n // 2
        remain = n % 2
        if remain > 0:
            return False
        if n == 1:
            return True
        while last > 2:
            remain = last % 2
            last = last // 2
            print(remain)
            if remain > 0:
                return False
        return True


if __name__ == "__main__":
    A = Solution()
    print(A.isPowerOfTwo(10))