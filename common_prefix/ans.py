#!/usr/bin/env python
# coding=utf-8
"""
@desc:   
@author: luluo
@date:   2018/8/2

"""


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""

        sorted_strs = [len(x) for x in strs]
        str_dict = dict(zip(sorted_strs, strs))
        min_len_str = str_dict[min(str_dict.keys())]
        if len(min_len_str) == 0:
            return ""

        key_list = list(min_len_str)
        for x in range(len(key_list)):
            if x > 0:
                key_list.pop()
            key = "".join(key_list)
            rest = list(filter(lambda x: x.startswith(key), strs))
            if len(rest) == len(strs):
                break
            else:
                key = ""

        return key

A = Solution()
print(A.longestCommonPrefix(['ca', 'ca']))
