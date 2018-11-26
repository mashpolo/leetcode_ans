#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-11-26

"""


class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join([x[::-1] for x in s.split()])


if __name__ == '__main__':
    A = Solution()
    print(A.reverseWords("Let's take LeetCode contest"))
