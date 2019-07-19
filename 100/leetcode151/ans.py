#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-07-19

"""


class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return s
        
        return " ".join(s.split()[::-1])
