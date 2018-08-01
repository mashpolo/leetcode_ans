#!/usr/bin/env python
# coding=utf-8
"""
@desc:   translate roma num to num
@author: luluo
@date:   2018/8/1

"""


roma_nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
roma_high_nums = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roma_keys = roma_nums.keys()
        roma_high_keys = roma_high_nums.keys()
        result = 0
        for x in roma_high_keys:
            if x in s:
                result += roma_high_nums[x]
                s = s.replace(x, '', 1)

        for y in s:
            if y in roma_keys:
                result += roma_nums[y]
                s = s.replace(y, '', 1)
                print(result, s, y)

        return result


A = Solution()
print(A.romanToInt("DCXXI"))