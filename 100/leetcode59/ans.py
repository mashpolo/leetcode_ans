#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-05-10

"""


class Solution:
    def generateMatrix(self, n: int):
        ans = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for x in range(n * n):
            if ans[(i + di) % n][(j + dj) % n] != 0:
                # 0 1 变 1 0, 1 0 变 0 -1, 0 -1 变 -1, 0, -1 0 变 0 1
                di, dj = dj, -di

            ans[i][j] = x + 1
            i += di
            j += dj

        return ans


if __name__ == '__main__':
    A = Solution()
    print(A.generateMatrix(5))
