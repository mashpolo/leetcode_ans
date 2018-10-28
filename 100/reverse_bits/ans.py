#!/usr/bin/env python
# coding=utf-8
"""
@desc:   颠倒二进制位
@author: Luo.lu
@date:   2018-9-12

"""


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        b_n = bin(n)[2:]
        return int(b_n[::-1] + (32-len(b_n))*'0', 2)


if __name__ == '__main__':
    A = Solution()
    print(A.reverseBits(20))