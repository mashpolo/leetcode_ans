#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-03-15

"""


class Solution:
    def minDeletionSize(self, A):

        if not len(A):
            return 0
        res = 0
        for num in range(len(A[0])):
            new_list = [x[num] for x in A]
            if not new_list == sorted(new_list):
                res += 1

        return res


if __name__ == '__main__':
    A = Solution()
    print(A.minDeletionSize(["zyx", "wvu", "tsr"]))

