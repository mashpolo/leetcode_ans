#!/usr/bin/env python
# coding=utf-8
"""
@desc:   实现strstr方法
@author: luluo
@date:   2018/8/7

"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1




A = Solution()
print(A.strStr("mississippi", "issip"))