#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-11-8

"""


class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        bin_num = bin(num)[2:]
        bin_r = len(bin_num)
        reverse_num = int("0b"+'1'*bin_r, 2)
        return num ^ reverse_num


if __name__ == '__main__':
    A = Solution()
    print(A.findComplement(1))

