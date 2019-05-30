#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-05-30

"""


class Solution:
    def maximalRectangle(self, matrix) -> int:
        if not matrix or not matrix[0]:
            return 0
        new = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        new[0] = [int(i) for i in matrix[0]]
        area = self.largestRectangleArea(new[0])
        for m in range(1, len(matrix)):
            for n in range(len(matrix[0])):
                if matrix[m][n] == '0':
                    new[m][n] = 0
                else:
                    new[m][n] = int(new[m-1][n]) + int(matrix[m][n])
            print(m, new[m])
            area = max(area, self.largestRectangleArea(new[m]))
        return area

    def largestRectangleArea(self, heights):
        """单调栈"""
        heights.append(0)
        stack = [0]
        area = 0
        for i in range(1, len(heights)):
            if heights[i] >= heights[stack[-1]]: #大于栈顶元素则入栈
                stack.append(i)
            else:
                while stack and heights[i] < heights[stack[-1]]: #只要栈顶元素大于当前元素
                    x = stack.pop(-1) #弹出栈顶
                    if len(stack) != 0:
                        area = max(area, heights[x] * (i-stack[-1]-1))
                    else:
                        area = max(area, heights[x] * i)
                stack.append(i)
        return area


if __name__ == '__main__':
    A = Solution()
    print(A.maximalRectangle([["1","1","1","1"],["1","1","1","1"],["1","1","1","1"]]))
