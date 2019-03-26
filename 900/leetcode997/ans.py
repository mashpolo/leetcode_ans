#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-03-26

"""


class Solution:
    def findJudge(self, N, trust):
        if not trust:
            return 1
        res = {}
        t = set()
        flag = []
        # 将整个二维矩阵化作一个散列表
        for item in trust:
            t.add(item[0])
            if item[1] in res:
                res[item[1]] += 1
            else:
                res[item[1]] = 1

            if res[item[1]] == N - 1:
                flag.append(item[1])
        for value in flag:
            if value not in t:
                return value

        return -1


if __name__ == '__main__':
    A = Solution()
    print(A.findJudge(3, [[1,3],[2,3], [3,1]]))



