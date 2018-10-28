#!/usr/bin/env python
# coding=utf-8
"""
@desc:   有效的字母异位词
@author: Luo.lu
@date:   2018-9-28

"""


class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)


if __name__ == '__main__':
    s = "a"
    t = "b"
    A = Solution()
    print(A.isAnagram(s, t))
