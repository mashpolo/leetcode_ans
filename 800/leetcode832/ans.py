#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-02-13

"""


class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        for a in A:
            a.reverse()
            b = list(map(lambda x: x ^ 1, a))
            res.append(b)
        return res


if __name__ == '__main__':
    A = Solution()
    print(A.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
