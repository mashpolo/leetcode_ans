#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-04-16

"""
class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0:
            return []
        word_len, s_len, res, words_dict = len(words[0]), len(s), [], {}
        for v in words:
            words_dict[v] = 1 if v not in words_dict.keys() else words_dict[v] + 1
        for i in range(s_len - len(words)*word_len + 1):
            j, tmp_dict = i, words_dict.copy()
            while len(tmp_dict.keys()) != 0:
                is_res, tmp = False, s[j:j + word_len]
                if tmp in tmp_dict.keys():
                    is_res = True
                    if tmp_dict[tmp] != 1:
                        tmp_dict[tmp] -= 1
                    else:
                        tmp_dict.pop(tmp)
                    j += word_len
                else:
                    break
            if is_res:
                res.append(i)
        return res
