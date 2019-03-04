#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-03-04

"""


class Solution:
    def sortArrayByParity(self, A):
        odd_list = []
        even_list = []
        for x in A:
            if x == 1:
                odd_list.append(x)
            elif x & 1:
                odd_list.append(x)
            else:
                even_list.append(x)
        return even_list + odd_list


if __name__ == '__main__':
    A = Solution()
    print(A.sortArrayByParity([3,1,2,4]))
