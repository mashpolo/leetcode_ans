#!/usr/bin/env python
# coding=utf-8
"""
@desc:   丑数
@author: Luo.lu
@date:   2018-9-30

"""


class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        while num:
            if not num % 5:
                num = num // 5
            if not num % 3:
                num = num // 3
            if not num % 2:
                num = num // 2
            if num in [1, 2,3,5]:
                return True
            if num % 2 > 0 and num % 3 > 0 and num % 5>0:
                return False


if __name__ == '__main__':
    A = Solution()
    print(A.isUgly(6))