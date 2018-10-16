#!/usr/bin/env python
# coding=utf-8
"""
@desc:   二进制手表
@author: Luo.lu
@date:   2018-10-16

"""


class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        ans = []
        for h in range(12):
            for m in range(60):
                if (bin(h)+ bin(m)).count('1') == num:
                    ans.append('%d:%02d' % (h, m))
        return ans