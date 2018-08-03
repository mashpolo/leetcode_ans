#!/usr/bin/env python
# coding=utf-8
"""
@desc:   判断括号是否是正确的使用
@author: luluo
@date:   2018/8/3

"""


class Solution:
    def isValid(self, s):
        # 步骤1
        rules = {k: v for k, v in zip('([{', ')]}')}
        stack = []

        for char in s:
            if char in rules:
                stack.append(char)
            else:
                print(stack)
                if not stack or rules[stack.pop()] != char:
                    return False

        return not stack


A = Solution()
print(A.isValid("([]){}"))