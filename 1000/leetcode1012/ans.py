#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-03-26

"""


class Solution:
    def bitwiseComplement(self, N: int) -> int:
        a = bin(N)
        b = '0b'
        for item in a[2:]:
            if item == '1':
                b += '0'
            else:
                b += '1'
        return int(b,2)


if __name__ == '__main__':
    A = Solution()
    print(A.bitwiseComplement(5))
