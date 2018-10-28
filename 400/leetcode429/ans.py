#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-10-25

"""
# Definition for a Node.


class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        stack_floor = [root]
        next_floor = []
        now_floor = []
        while stack_floor:
            _node = stack_floor.pop()
            now_floor.insert(0, _node.val)
            for x in  _node.children:
                next_floor.insert(0, x)

            if not stack_floor:
                stack_floor, next_floor = next_floor, stack_floor
                res.append(now_floor[::-1])
                now_floor = []
        return res
