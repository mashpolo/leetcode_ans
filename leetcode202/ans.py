#!/usr/bin/env python
# coding=utf-8
"""
@desc:   判断一个数是否是快乐数
@author: Luo.lu
@date:   2018-9-17

"""


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        got = set()
        while n != 1 and n not in got:
            got.add(n)
            sum = 0
            while n:
                sum += (n % 10)**2
                n //= 10
            n = sum

        return n == 1


if __name__ == "__main__":
    A = Solution()
    print(A.isHappy(22))