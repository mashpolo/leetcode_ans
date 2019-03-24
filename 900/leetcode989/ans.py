#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-03-24

"""


class Solution:
    def addToArrayForm(self, A, K):
        whole = int("".join([str(x) for x in A]))
        total = whole + K
        return [int(x) for x in str(total)]


if __name__ == '__main__':
    A = Solution()
    print(A.addToArrayForm(A = [1], K = 33))
