#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-02-21

"""


class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return list(zip(*A))


if __name__ == '__main__':
    A = Solution()
    print(A.transpose([[1,4,7],[2,5,8],[3,6,9]]))
