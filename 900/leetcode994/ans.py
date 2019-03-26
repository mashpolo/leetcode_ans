#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-03-26

"""


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        myqueue = []
        # 初始化
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    myqueue.append((i, j))

        minitue = 0;
        while True:
            count = 0
            tmp = []
            for (i, j) in myqueue:
                if i + 1 < len(grid) and grid[i + 1][j] == 1:
                    count += 1
                    tmp.append((i + 1, j))
                    grid[i + 1][j] = 2
                if i - 1 >= 0 and grid[i - 1][j] == 1:
                    count += 1
                    tmp.append((i - 1, j))
                    grid[i - 1][j] = 2
                if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
                    count += 1
                    tmp.append((i, j + 1))
                    grid[i][j + 1] = 2
                if j - 1 >= 0 and grid[i][j - 1] == 1:
                    count += 1
                    tmp.append((i, j - 1))
                    grid[i][j - 1] = 2
            # 将新一轮腐烂的橘子 添加进来
            myqueue = tmp
            # 如果这一轮没有感染其他橘子 说明感染结束 跳出
            if not count:
                break
            # 走到这里 这一轮 成功感染了橘子 分钟数加1
            minitue += 1

        # 如果grid 还有新鲜橘子 说明这个橘子不能被感染 返回-1
        for i in grid:
            for j in i:
                if j == 1:
                    return -1
        return minitue
