#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-02-15

"""


class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r = 0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                if set((grid[i][j],grid[i][j+2],grid[i+2][j],grid[i+2][j+2])) == set((2,4,6,8)) and grid[i+1][j+1] == 5:
                    if sum(grid[i][j:j+3]) == sum(grid[i+2][j:j+3])==grid[i][j]+grid[i+1][j]+grid[i+2][j] == 15:
                        r += 1
        return r


if __name__ == '__main__':
    A = Solution()
    print(A.numMagicSquaresInside([[4,3,8,4],
      [9,5,1,9],
      [2,7,6,2]]))

