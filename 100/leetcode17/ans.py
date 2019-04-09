#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-04-09

"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        len_s = len(digits)

        def dfs(n, s):
            if n == len_s:
                res.append(s)
                return
            for ch in dic[digits[n]]:
                dfs(n + 1, s + ch)

        if len_s == 0:
            return []
        dfs(0, '')
        return res
