#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-03-26

"""


class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        # 找出R所在位置
        # 从R位置开始上下左右寻找符合条件的p
        for i in range(len(board)):
            if 'R' in board[i]:
                R = (i, board[i].index('R'))
                break

        k = 0
        for i in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            j = R
            while True:
                j = [sum(s) for s in zip(j, i)]
                if sorted(j)[0] < 0 or sorted(j)[-1] > 7:
                    break
                tmp = board[j[0]][j[1]]
                if tmp == 'p':
                    k += 1
                    break
                if tmp == 'B':
                    break
        return k
