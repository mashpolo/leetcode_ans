#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-01-29

"""


class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        l1 = {'2', '5', '6', '9'}
        l2 = {'0', '1', '2', '5', '6', '8', '9'}

        count = 0

        for i in range(1, N+1):
            if set(str(i)) < l2:
                for j in str(i):
                    if set(j) < l1:
                        count += 1
                        break

        return count


if __name__ == '__main__':
    A = Solution()
    print(A.rotatedDigits(1000 ))
