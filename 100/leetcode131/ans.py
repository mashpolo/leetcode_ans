#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-06-30

"""


class Solution(object):
    # 本题采用回溯法
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        # 定义一列表，用来保存最终结果
        split_result = []
        # 如果给定字符串s为空，则没有分割的必要了
        if len(s) == 0:
            return split_result

        def back(start=0, res=[]):
            if start >= len(s):
                split_result.append(res)
                return
            for end in range(start+1, len(s)+1):
                split_s = s[start:end]
                # 如果当前子串为回文串，则可以继续递归
                if split_s == s[start:end][::-1]:
                    back(end, res+[split_s])

        back()
        return split_result
