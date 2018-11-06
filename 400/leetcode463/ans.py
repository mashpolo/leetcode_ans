#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-11-6

"""


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        h = len(grid)
        w = len(grid[0]) if h else 0
        ans = 0
        for x in range(h):
            for y in range(w):
                if grid[x][y] == 1:
                    ans += 4
                    if x > 0 and grid[x - 1][y]:
                        ans -= 2
                    if y > 0 and grid[x][y - 1]:
                        ans -= 2
        return ans


if __name__ == '__main__':
    A = Solution()
    print(A.islandPerimeter([[0,1,0,0],
                             [1,1,1,0],
                             [0,1,0,0],
                             [1,1,0,0]]))
