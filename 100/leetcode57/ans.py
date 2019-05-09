#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-05-09

"""


class Solution:
    def insert(self, intervals, newInterval):
        start, end = newInterval[0], newInterval[-1]
        res = []
        flag = False
        if not intervals or not newInterval:
            return [intervals + newInterval]

        for index, interval in enumerate(intervals):
            if interval[1] < start:
                res.append(interval)
                if intervals[index + 1][0] > end:
                    res.append(newInterval)
            elif interval[0] > end:
                if flag:
                    res.append([start, end])
                    flag = False
                res.append(interval)
            else:
                start = min(interval[0], start)
                end = max(interval[1], end)
                flag = True
        if flag:
            res.append([start, end])
        else:
            if intervals[0][0] > end:
                res.insert(0, newInterval)
            elif intervals[-1][1] < start:
                res.append(newInterval)
        return res


if __name__ == '__main__':
    A = Solution()
    print(A.insert([[3,5],[12,15]],
[6,6]))
