#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-07-08

"""
class Solution(object):
    # 本题回溯法超出时间限制，采用动态回归法
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # 初始化标记列表
        flag = [True]+[False]*len(s)

        for start in range(len(s)):
            if flag[start]:
                for end in range(start+1, len(s)+1):
                    if s[start:end] in wordDict:
                        flag[end] = True
        return flag[-1]
