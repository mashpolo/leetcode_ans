#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-05-09

"""


class Solution:
    def merge(self, intervals):
        ans = [[float('-inf'),float('-inf')]]
        i = 0
        j = 0
        intervals = sorted(intervals,key = lambda x:x[0])
        while(i < len(intervals)):
            if ans[j][-1] >= intervals[i][0]:
                temp = ans.pop()
                ans.append([temp[0], max(temp[-1],intervals[i][-1])])
            else:
                ans.append(intervals[i])
                j += 1
            i += 1
        return ans[1:]
