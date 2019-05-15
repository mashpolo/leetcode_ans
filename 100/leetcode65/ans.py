#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-05-16

"""


class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s: return False

        # 首先检测一个 +/- 以及尽可能多个 0-9
        numeric, s = self.scanInt(s)

        # 检测小数位
        if not s: return numeric
        if s[0] == '.':
            b, s = self.scanUint(s[1:])
            numeric = numeric or b  # 整数/小数有其一即可，所以用 or

        # 检测指数
        if not s: return numeric
        if s[0] == 'e':
            b, s = self.scanInt(s[1:])
            numeric = numeric and b  # 如果出现 e 字符，则 C 部分一定要有数字，所以用 and
        return numeric and not s  # not s 表示尾部不能含有非0-9的其他字符

    def scanUint(self, s: str) -> (bool, str):
        if not s: return (False, s)
        temp = s
        while True:
            if not s or s[0] < '0' or s[0] > '9':
                return (s != temp, s)
            s = s[1:]

    def scanInt(self, s: str) -> (bool, str):
        if not s: return (False, s)  # 空字符串
        if s[0] in ['+', '-']: s = s[1:]  # +/-开头
        return self.scanUint(s)


