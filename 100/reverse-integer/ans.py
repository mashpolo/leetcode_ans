#!/usr/bin/env python
# coding=utf-8
"""
@desc:   翻转整数
@author: luluo
@date:   2018/7/23

"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = int(str(x)[::-1]) if x >= 0 else - int(str(-x)[::-1])
        return x


test_obj = Solution()
print(test_obj.reverse(12422634547))
