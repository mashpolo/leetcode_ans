#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-10-19

"""


class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        dict = {10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}
        if num == 0:
            return '0'
        if num < 0:
            num += 2**32
        s = ''
        s1 = []
        if num > 0 and num < 10:
            return str(num)
        elif num >=10 and num < 16:
            return dict[num]
        while num >= 16:
            num, res =divmod(num, 16)
            s1.append(res)
        s1.append(num)
        for i in s1:
            if i < 10:
                s = str(i) + s
            else:
                s = dict[i] + s
        return s
