#!/usr/bin/env python
# coding=utf-8
"""
@desc:   
@author: Luo.lu
@date:   2018-10-17

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nodes = [root]
        left_arr = []
        while nodes:
            node = nodes.pop()
            if node.left:
                nodes.append(node.left)
                if not node.left.left and not node.left.right:
                    left_arr.append(node.left.val)
            if node.right:
                nodes.append(node.right)
        return sum(left_arr)