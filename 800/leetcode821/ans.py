#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-02-10

"""


class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        pos = []
        for (index, x) in enumerate(S):
            if x == C:
                pos.append(index)
        res = []
        for x in range(len(S)):
            length = map(lambda y: abs(x - y), pos)
            res.append(min(length))
        return res


if __name__ == '__main__':
    A = Solution()
    print(A.shortestToChar(S="loveleetcode", C='e'))
