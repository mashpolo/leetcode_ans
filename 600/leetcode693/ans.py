#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-1-2

"""


class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        b_n = bin(n)[2:]
        if len(b_n) == 1:
            return True
        odd_num = list(set(b_n[::2]))
        even_num = list(set(b_n[1::2]))
        if len(odd_num) == 1 and len(even_num) == 1 and odd_num != even_num:
            return True
        else:
            return False


if __name__ == '__main__':
    A = Solution()
    print(A.hasAlternatingBits(5))
