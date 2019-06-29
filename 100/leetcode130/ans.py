#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-06-29

"""


class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 如果是空数组，直接返回
        # Leetcode总搞这种边边角角的输入
        if not board: return
        # 计算数组长宽
        row = len(board)
        col = len(board[0])
        # 如果长度或者宽度中一个小于3的话也不用算了，直接返回
        if row < 3 or col < 3: return

        # DFS函数
        def dfs(i, j):
            # 如果i，j中有一个越界或者遇到了X则不继续扫描
            if i < 0 or j < 0 or i >= row or j >= col or board[i][j] != 'O':
                return
            # 否则把数组中的O变成#，意思是这个O和边缘是连通的
            board[i][j] = '#'
            # 之后从当前坐标开始上下左右进行递归搜索
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        for i in range(row):
            # 搜索第一行和最后一行
            dfs(i, 0)
            dfs(i, col - 1)

        for i in range(col):
            # 搜索第一列和最后一列
            dfs(0, i)
            dfs(row - 1, i)

        # 全部搜索完毕后：
        # X X X X
        # X X O X
        # X O X X
        # X O X X
        # 变为：
        # X X X X
        # X X O X
        # X # X X
        # X # X X
        # 之后再将所有的#变成O，O变成X就可以了
        for i in range(0, row):
            for j in range(0, col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'


if __name__ == '__main__':
    l = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    A = Solution()
    A.solve(l)
    print(l)
