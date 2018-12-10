#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-12-10

"""


class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return m * n
        l_max = min([x[0] for x in ops])
        r_max = min([y[1] for y in ops])
        return min(l_max, m) * min(r_max, n)


if __name__ == '__main__':
    A = Solution()
    print(A.maxCount(3,3,[[2,2],[3,3]]))
