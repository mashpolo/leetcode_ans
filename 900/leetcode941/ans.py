#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-03-13

"""


class Solution:
    def validMountainArray(self, A):
        if len(A) <= 2:
            return False
        flag = None
        for (index, x) in enumerate(A):
            if index == 0:
                continue
            elif index == 1:
                if A[index] <= A[0]:
                    return False
            else:
                if x == A[index - 1]:
                    return False
                elif x < A[index - 1]:
                    flag = index

                else:
                    continue
        return A[flag:] == sorted(set(A[flag:]), reverse=True)


if __name__ == '__main__':
    A = Solution()
    print(A.validMountainArray([14,82,89,84,79,70,70,68,67,66,63,60,58,54,44,43,32,28,26,25,22,15,13,12,10,8,7,5,4,3]))

