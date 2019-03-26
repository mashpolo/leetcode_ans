#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-03-26

"""


class Solution:
    def commonChars(self, A):
        res = []
        s0 = set(A[0])
        for x in A:
            y = set(x)
            s0 = s0 & y
        if not len(s0):
            return res
        res = list(s0)
        for x in s0:
            num = min(map(lambda word: word.count(x), A))
            res += [x] * (num - 1)
        return res


if __name__ == '__main__':
    A = Solution()
    print(A.commonChars(["bella","label","roller"]))

