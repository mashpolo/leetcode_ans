#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-05-10

"""
from itertools import permutations


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = permutations(range(1, n + 1))
        i = 1
        for s in res:
            if i == k:
                return "".join(str(n) for n in s)
            i += 1


if __name__ == '__main__':
    A = Solution()
    print(A.getPermutation(9, 2890))
