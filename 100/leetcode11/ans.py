#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-04-03

"""


class Solution:
    def maxArea(self, height: list) -> int:
        res = []
        for i in range(len(height) - 1):
            for y in range(1, len(height)):
                res.append((y - i) * min(height[y], height[i]))
        return max(res)


if __name__ == '__main__':
    A = Solution()
    print(A.maxArea([1,8,6,2,5,4,8,3,7]))

