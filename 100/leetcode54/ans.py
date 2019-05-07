#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-05-07

"""


class Solution:
    # 减治法 减去外框
    def spiralOrder(self, matrix):
        if matrix != []:
            return self._sprial(matrix,len(matrix),len(matrix[0]))
        else:
            return []

    def _sprial(self,matrix,m,n):
        if m < 2 or n < 2:
            return [matrix[i][j] for i in range(m) for j in range(n)]
        else:
            temp = []
            for i in range(1,m-1):
                a = []
                for j in range(1,n-1):
                    a +=[matrix[i][j]]
                temp.append(a)
            print(temp)
            return matrix[0] + [matrix[i][-1] for i in range(1,m)] + [matrix[-1][j] for j in range(n-2,-1,-1)] + [matrix[i][0] for i in range(m-2,0,-1)] + \
                   self._sprial(temp,m-2,n-2)


if __name__ == '__main__':
    A = Solution()
    print(A.spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]))
