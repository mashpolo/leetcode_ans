#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-05-29

"""


class Solution(object):
    def largestRectangleArea(self, heights):
        """单调栈"""
        heights.append(0)
        stack = [0]
        area = 0
        for i in range(1, len(heights)):
            print(stack, heights[i])
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
    print(A.largestRectangleArea([2,1,5,6,2,3]))


