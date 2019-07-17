#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-07-17

"""
from collections import *
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # i是需要判断点的索引
        def calc(points, i):
            # defaultdict是collections里的一个类，就是带有默认值的字典
            # 这样不用在给字典赋值时先判断key存不存在了
            hashmap = defaultdict(int)
            # 记录与需要判断点重合点的数目
            same = 0
            for j in range(len(points)):
                # 不对同一个点进行计算
                if j != i:
                    # 如果两点坐标相同same加一然后跳回循环开始
                    if points[i] == points[j]:
                        same += 1
                        continue
                    # 因为可能存在斜率无穷大的情况，提前做判断
                    if points[i][1] - points[j][1] == 0:
                        k = float('Inf')
                    else:
                        k = (points[i][0] - points[j][0]) / (points[i][1] - points[j][1])
                    # 最后更新hashmap
                    hashmap[k] += 1
            # 取hashmap中最大值加上重复的个数再加一就是该点的结果
            return 1 + same + (max(hashmap.values()) if hashmap else 0)
        res = 0
        if len(points) == 1: return 1
        # 对于每个点进行一次calc操作，取最大值作为答案
        for i in range(len(points)):
            res = max(res, calc(points, i))
        return res
