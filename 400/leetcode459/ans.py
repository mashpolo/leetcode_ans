#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-11-4

"""
class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        size = len(str)
        next = [0] * size
        for i in range(1, size):
            k = next[i - 1]
            while str[i] != str[k] and k:
                k = next[k - 1]
            if str[i] == str[k]:
                next[i] = k + 1
        p = next[-1]
        return p > 0 and size % (size - p) == 0


if __name__ == '__main__':
    A = Solution()
    print(A.repeatedSubstringPattern('ababab'))
