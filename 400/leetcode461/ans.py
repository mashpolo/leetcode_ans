#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-11-5

"""


class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bin_x = bin(x)[2:]
        bin_y = bin(y)[2:]
        if len(bin_x) >= len(bin_y):
            bin_y = [0]*(len(bin_x) - len(bin_y)) + list(bin_y)
        else:
            bin_x = [0]*(len(bin_y) - len(bin_x)) + list(bin_x)
        res = 0
        print(bin_x, bin_y)
        for x in range(len(bin_x)):
            if int(bin_x[x]) != int(bin_y[x]):
                res += 1

        return res


if __name__ == '__main__':
    A = Solution()
    print(A.hammingDistance(1,4))
