#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-03-26

"""


class Solution:
    def largestSumAfterKNegations(self, A, K):
        A.sort()

        for i in range(K):
            if A[i] >= 0:
                A.sort()
                if A[0] >= 0:
                    print(A, i)
                    if K - i > 2 and (K - i) % 2 == 0:
                        return sum(A)
                    else:
                        return sum(A) - 2 * A[0]
            else:
                A[i] = - A[i]
        return sum(A)


if __name__ == '__main__':
    A = Solution()
    print(A.largestSumAfterKNegations([-4,-6,9,-2,2],
4))

