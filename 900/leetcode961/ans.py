#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-03-18

"""


class Solution:
    def repeatedNTimes(self, A):
        mark = []
        for key in A:
            if key in mark:
                return key
            else:
                mark.append(key)


if __name__ == '__main__':
    A = Solution()
    print(A.repeatedNTimes([2,1,2,5,3,2]))

