#!/usr/bin/env python
# coding=utf-8
"""
@desc:   报数
@author: luluo
@date:   2018/8/9

"""


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return "10"

        if n == 1:
            return "1"


        i = 2
        base = "11"
        while n - i > 0:
            num = 0
            rest = ""
            for (index, x) in enumerate(base):
                if index + 1 == len(base):
                    rest += str(num + 1) + str(x)
                    break
                if x == base[index + 1]:
                    num += 1
                    continue
                else:
                    rest += str(num + 1) + str(x)
                    num = 0
            base = rest
            i += 1
        return base


A = Solution()
print(A.countAndSay(5))
