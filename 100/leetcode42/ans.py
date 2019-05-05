#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-05-05

"""


class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 2:
            return 0
        res = 0
        i,j = 0,len(height)-1
        h0 = 0
        while i < j:
            if height[i] > h0 and height[j] > h0:
                if height[i] <= height[j]:
                    h1 = height[i]
                    i += 1
                else:
                    h1 = height[j]
                    j -= 1
                res += (j-i+2)*(h1-h0)
                h0 = h1
            if height[i] <= h0:
                i += 1
            if height[j] <= h0:
                j -= 1
        return res - sum(height)+max(height)-h0
