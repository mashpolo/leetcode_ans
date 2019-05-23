#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-05-23

"""


class Solution(object):
    def combine(self, n, k):
        tmp, ret = [], []
        self.dfs(n, k, 1, tmp, ret)
        return ret

    def dfs(self, n, k, index, tmp, ret):
        if len(tmp) == k:
            ret.append(tmp[:])
            return
        for i in range(index, n + 1):
            tmp.append(i)
            self.dfs(n, k, i + 1, tmp, ret)
            tmp.pop()


if __name__ == '__main__':
    A = Solution()
    print(A.combine(3, 2))
