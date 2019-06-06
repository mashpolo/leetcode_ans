#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-06-06

"""


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        if len(s) > 12:
            return []
        ans = []
        self.dfs([], ans, 0, s)
        return ans

    def dfs(self, stack, ans, index, s):
        # index来定位 需要的数字 的头序号
        # 回溯的答案终止条件，s里数字正好用完
        if len(stack) == 4 and index == len(s):
            ans.append('.'.join(stack))
            return
        # 回溯的非答案终止条件
        if len(stack) > 4 or index >= len(s):
            return

        for _ in range(1, 4):
            # 递归循环体，需要排除‘01’的这样的情况
            if _ != 1 and s[index] == '0':
                continue
            if int(s[index:  index + _]) <= 255:
                stack.append(s[index: index + _])
                self.dfs(stack, ans, index + _, s)
                stack.pop()
