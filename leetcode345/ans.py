#!/usr/bin/env python
# coding=utf-8
"""
@desc:   反转字符串中的元音字母
@author: Luo.lu
@date:   2018-10-6

"""


class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        main_num = ['a', 'e', 'i', 'o', 'u']
        l_s = list(s)
        reverse_l = []
        position_l = []
        for index, x in enumerate(l_s):
            if x.lower() in main_num:
                reverse_l.append(x)
                position_l.append(index)

        rl = reverse_l[::-1] if reverse_l else reverse_l
        r_dict = dict(zip(position_l, rl))
        for x in r_dict:
            l_s[x] = r_dict[x]

        return "".join(l_s)