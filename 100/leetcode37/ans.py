#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-04-24

"""


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.helper(board)

    def helper(self, board):
        num = len(board)
        for i in range(num):
            for j in range(num):
                if board[i][j] == '.':
                    for t in range(1, 10):
                        c = str(t)
                        if self.is_valid(board, c, i, j):
                            board[i][j] = c
                            if self.helper(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False  # 当前插入1~9均无效，回溯到前一状态
        return True  # 插入最后一个数成功时需要返回True,从而将前面的状态确定下来

    def is_valid(self, board, c, row, col):
        num = len(board)
        # check row
        for m in range(num):
            if board[row][m] == c:
                return False

        # check column
        for n in range(num):
            if board[n][col] == c:
                return False

        # check block
        row_start = (row // 3) * 3
        column_start = (col // 3) * 3
        for i in range(row_start, row_start + 3):
            for j in range(column_start, column_start + 3):
                if board[i][j] == c:
                    return False
        return True
