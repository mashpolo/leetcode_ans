#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-12-6

"""
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        res = []
        stack = [root]
        while len(stack) > 0:
            node = stack.pop(0)
            res.append(node.val)
            for i in node.children[::-1]:
                stack.insert(0, i)
        return res
