#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-01-21

"""
from collections import Counter
import re


class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        r = re.compile("[a-zA-Z]")
        word = r.findall(licensePlate.lower())
        target_m = Counter(word)
        res = ""
        for w in words:
            print(w, res)
            if res and len(res) <= len(w):
                continue
            else:
                wn = Counter(w)
                for x in target_m:
                    print(target_m[x], wn[x])
                    if x not in w or target_m[x] > wn[x]:
                        flag = False
                        break
                    else:
                        flag = True
                if flag:
                    res = w
        return res


if __name__ == '__main__':
    A = Solution()
    print(A.shortestCompletingWord("Ah71752",
["suggest","letter","of","husband","easy","education","drug","prevent","writer","old"]))
