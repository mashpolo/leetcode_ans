#!/usr/bin/env python
# coding=utf-8
"""
@desc:   4的幂
@author: Luo.lu
@date:   2018-10-6

"""


class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num in [1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576,
                       4194304, 16777216, 67108864, 268435456, 1073741824, 4294967296]