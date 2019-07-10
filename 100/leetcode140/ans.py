#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-07-10

"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        # 借助139，判断是否存在可分的情况，否则特例可能会超时
        if not s:
            return True
        res = [0] * (len(s) + 1)
        # 开始位置查找：
        for word in wordDict:
            if s.startswith(word):
                res[len(word)] = 1
        for i in range(len(s)):
            if res[i]:
                for word in wordDict:
                    if s[i:].startswith(word):
                        res[i + len(word)] = 1
        new_res = []
        if bool(res[-1]):
            self.DFS(s, wordDict, new_res, "")
        return new_res

    # DFS遍历
    def DFS(self, s, wordDict, res, tmp):
        if not s:
            res.append(tmp.strip())
        for word in wordDict:
            if s.startswith(word):
                self.DFS(s[len(word):], wordDict, res, tmp + word + " ")
            else:
                continue
