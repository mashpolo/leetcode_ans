#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-03-17

"""


class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        letters = 'abcdefghijklmnopqrstuvwxyz'
        d = {v: letters[k] for k, v in enumerate(order)}
        ws = [''.join([d[j] for j in i]) for i in words]
        wss = sorted(ws)
        return ws == wss
