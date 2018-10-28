#!/usr/bin/env python
# coding=utf-8
"""
@desc:   二进制求和
@author: luluo
@date:   2018-8-13

"""


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        max_num = max(len(a), len(b))
        min_num = min(len(a), len(b))

        if not a and b:
            return b
        if not b and a:
            return a

        flag = 0
        rest_list = []
        for x in range(max_num):
            print('-='*10)
            if x < min_num:
                rest = int(a[len(a) -1 -x]) + int(b[len(b) -1 -x]) + flag
                num = rest % 2
                rest_list.append(str(num))
                if rest > 1:
                    flag = 1
                else:
                    flag = 0
            elif min_num <= x < len(a):
                rest = int(a[len(a) -1 -x]) + flag
                num = rest % 2
                rest_list.append(str(num))
                if rest > 1:
                    flag = 1
                else:
                    flag = 0
            elif min_num <= x < len(b):
                rest = int(b[len(b) -x  - 1]) + flag
                num = rest % 2
                rest_list.append(str(num))
                if rest > 1:
                    flag = 1
                else:
                    flag = 0
        if flag > 0:
            rest_list.append(str(flag))
        real_list = reversed(rest_list)
        return "".join(real_list)


A = Solution()
print(A.addBinary(a="100", b="110010"))