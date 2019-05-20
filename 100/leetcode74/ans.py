#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-05-20

"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        row_length = len(matrix)
        column_length = len(matrix[0])
        for row_index in range(row_length):
            if not matrix[row_index]:
                break
            if target >= matrix[row_index][0] and target <= matrix[row_index][column_length - 1]:
                start = 0
                end = column_length - 1
                while start <= end:
                    mid = int((start + end) / 2)
                    if target > matrix[row_index][mid]:
                        start = mid + 1
                    if target < matrix[row_index][mid]:
                        end = mid-1
                    if target == matrix[row_index][mid]:
                        return True
        return False


if __name__ == '__main__':
    A = Solution()
    print(A.searchMatrix(matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
],
target = 4))
