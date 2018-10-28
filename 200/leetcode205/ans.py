#!/usr/bin/env python
# coding=utf-8
"""
@desc:   同构字符串
@author: Luo.lu
@date:   2018-9-20

"""


class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))


if __name__ == "__main__":
    A = Solution()
    print(A.isIsomorphic('aba', 'baa'))