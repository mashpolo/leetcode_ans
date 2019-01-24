#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-01-24

"""


class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for row in range(len(matrix) - 1):
            for col in range(len(matrix[0]) - 1):
                if matrix[row][col] != matrix[row+1][col+1]:
                    return False
        return True


if __name__ == '__main__':
    A = Solution()
    print(A.isToeplitzMatrix(matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]))


