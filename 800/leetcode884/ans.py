#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-02-27

"""
from collections import Counter


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        whole =  A + " " + B
        count = Counter(whole.split())
        res = []
        for x in count:
            if count[x] == 1:
                res.append(x)

        return res
