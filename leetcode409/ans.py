#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-10-20

"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # h = collections.Counter(s)
        h = {}
        for i in s:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
        c = 0
        sig = 0
        for i in h:
            c += h[i]//2
            if h[i] % 2 != 0:
                sig = 1
        return c * 2 + sig


if __name__ == '__main__':
    A = Solution()
    print(A.longestPalindrome("aabbbccddddd"))
