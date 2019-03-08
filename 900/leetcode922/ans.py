#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-03-08

"""


class Solution:
    def sortArrayByParityII(self, A):
        odd_list, even_lsit = [], []
        for (index, x) in enumerate(A):
            if index + x & 1 == 0:
                continue
            elif index & 1 == 0 and x & 1 > 0:
                odd_list.append(index)
            elif index & 1 > 0 and x & 1 == 0:
                even_lsit.append(index)

        for x in odd_list:
            y = even_lsit.pop()
            A[x], A[y] = A[y], A[x]
        return A


if __name__ == '__main__':
    A = Solution()
    print(A.sortArrayByParityII([4,2,5,7]))
