#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-02-26

"""


#入参grid[i][j]的意思是，x=i,y=j的坐标上有几个正方体，如grid=[[1,2],[3,4]],意为：x=0,y=0,有1个，x=0，y=1，有2个，x=1，y=0，有3个，x=1，y=1，有4个
class Solution:
    def projectionArea(self, grid: 'List[List[int]]') -> 'int':
        d1 = 0
        d2 = 0
        d3 = 0
        for i in grid:
            for k in i:
                if k != 0:
                    d1 += 1
            b = max(i)
            d2 += b
        print(d1,d2)
        for k in range(len(grid[0])):
            c = 0
            for i in grid:
                c = max(c, i[k])
            d3 += c
        return d1+d2+d3
