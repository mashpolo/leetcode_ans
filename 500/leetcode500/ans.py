#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-11-13

"""


class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        list1 = set("QWERTYUIOP")
        list2 = set("ASDFGHJKL")
        list3 = set("ZXCVBNM")
        res = []
        for x in words:
            flag = set(x.upper())
            if flag.issubset(list1) or flag.issubset(list2) or flag.issubset(list3):
                res.append(x)
        return res


if __name__ == '__main__':
    A = Solution()
    print(A.findWords(["Hello", "Alaska", "Dad", "Peace"]))
