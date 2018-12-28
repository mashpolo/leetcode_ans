#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-12-28

"""


class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s)-1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
                continue
            left, right = s[i+1: j+1], s[i: j]
            return (left == left[::-1]) or (right == right[::-1])
        return True


if __name__ == '__main__':
    A = Solution()
    print(A.validPalindrome('abba'))
