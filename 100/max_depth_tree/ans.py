#!/usr/bin/env python
# coding=utf-8
"""
@desc:   最二叉树的最大深度
@author: luluo
@date:   2018-8-20

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))