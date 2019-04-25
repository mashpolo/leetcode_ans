#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-04-25

"""


class Solution(object):
    def combinationSum(self, candidates, target):
        tmp, ret = [], []
        self.dfs(0, candidates, tmp, ret, target)
        return ret

    def dfs(self, index, candidates, tmp, ret, target):
        if target == 0:
            ret.append(tmp[:])
            return
        if target < 0:
            return
        for i in range(index, len(candidates)):
            tmp.append(candidates[i])
            self.dfs(i, candidates, tmp, ret, target - candidates[i])
            tmp.pop()
        return


if __name__ == '__main__':
    A = Solution()
    print(A.combinationSum(candidates = [2,3,6,7], target = 7,))


