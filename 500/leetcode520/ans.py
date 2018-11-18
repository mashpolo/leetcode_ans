#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-11-18

"""


class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.upper() == word:
            return True
        if word.lower() == word:
            return True
        if len(word) > 1:
            return word[1:].lower() == word[1:] and word[0] == word[0].upper()
        else:
            return True
