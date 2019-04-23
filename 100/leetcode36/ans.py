#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-04-23

"""


class Solution:
    def isValidSudoku(self, board):
        l = [list() for _ in range(9)]
        for (index, x) in enumerate(board):
            row = []
            if index % 3 == 0:
                col = [[], [], []]
            # else:
            #     print(col, index)

            for (index2, y) in enumerate(x):
                if y == '.':
                    continue
                if y in row:
                    return False
                else:
                    row.append(y)
                flag = index2 // 3
                if y in l[index2]:
                    return False
                else:
                    l[index2].append(y)

                if y in col[flag]:
                    return False
                else:
                    col[flag].append(y)

        return True


if __name__ == '__main__':
    A = Solution()
    print(A.isValidSudoku([[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]))

