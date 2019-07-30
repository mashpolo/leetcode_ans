#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-07-30

"""


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n=len(s)-9
        d={}
        for i in range(n):
            if s[i:i+10] in d:
                d[s[i:i+10]]=True
            else:
                d[s[i:i+10]]=False
        return [i for i in d if d[i]]
