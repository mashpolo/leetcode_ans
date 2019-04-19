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
        new_can = candidates[:]
        if target == 0:
            if sorted(tmp[:]) not in ret:
                ret.append(sorted(tmp[:]))
            return
        if target < 0:
            return
        for i in range(index, len(candidates)):
            tmp.append(candidates[i])
            del new_can[i]
            self.dfs(i, new_can, tmp, ret, target - candidates[i])
            tmp.pop()
            new_can.insert(i, candidates[i])
        return


if __name__ == '__main__':
    A = Solution()
    print(A.combinationSum(candidates = [10,1,2,7,6,1,5], target = 8,))
