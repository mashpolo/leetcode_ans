#!/usr/bin/env python
# coding=utf-8
"""
@desc:   赎金信
@author: Luo.lu
@date:   2018-10-12

"""
from collections import Counter


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        n1 = Counter(ransomNote)
        n2 = Counter(magazine)
        for key in n1:
            if n1.get(key) > n2.get(key, 0):
                return False

        return True