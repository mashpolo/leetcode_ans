#!/usr/bin/env python
# coding=utf-8
"""
@desc:   验证一个字符串是否是回文，只计算字符和数字
@author: luluo
@date:   2018-8-30

"""


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        new_s = [x.upper() for x in s if x.isalpha() or x.isdigit()]
        return new_s[::-1] == new_s

A = Solution()
print(A.isPalindrome("A man, a plan, a canal: Panama"))