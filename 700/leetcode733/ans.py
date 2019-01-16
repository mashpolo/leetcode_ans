#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-01-16

"""
import collections


class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        que = collections.deque()
        que.append((sr, sc))
        start = image[sr][sc]
        if start == newColor:
            return image
        M, N = len(image), len(image[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while que:
            pos = que.popleft()
            image[pos[0]][pos[1]] = newColor
            for d in directions:
                newx, newy = pos[0] + d[0], pos[1] + d[1]
                if 0 <= newx < M and 0 <= newy < N and image[newx][newy] == start:
                    que.append((newx, newy))
        return image
