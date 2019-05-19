#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-05-19

"""


class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        cols = []
        for index0, row in enumerate(matrix):
            flag = False
            for index, i in enumerate(row):
                if i == 0:
                    cols.append(index)
                    flag = True
            if flag:
                matrix[index0] = [0] * len(row)
        print(cols)
        for y in set(cols):
            for x in range(len(matrix)):
                matrix[x][y] = 0
        print(matrix)


if __name__ == '__main__':
    A = Solution()
    mar = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
    aa = A.setZeroes(mar)
    print(aa)

