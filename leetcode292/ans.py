#!/usr/bin/env python
# coding=utf-8
"""
@desc:   Nim游戏
@author: Luo.lu
@date:   2018-10-4

"""


class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0

