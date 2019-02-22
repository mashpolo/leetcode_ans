#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-02-22

"""


class Solution:
    def binaryGap(self, N: 'int') -> 'int':
        b_num = bin(N)[2:]
        res = 0
        first = None
        for (index, x) in enumerate(b_num):
            if x == '1' and first is None:
                first = index
            elif x == '1' and first is not None:
                print(index, first)
                res = index - first if index - first > res else res
                first = index
        return res


if __name__ == '__main__':
    A = Solution()
    print(A.binaryGap(22))


