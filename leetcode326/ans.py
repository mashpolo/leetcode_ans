#!/usr/bin/env python
# coding=utf-8
"""
@desc:   3的幂
@author: Luo.lu
@date:   2018-10-5

"""


class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 2:
            rest = n % 3
            if rest != 0:
                return False
            else:
                n = n // 3
        if n == 1:
            return True
        else:
            return False


if __name__ == '__main__':
    A = Solution()
    print(A.isPowerOfThree(32))