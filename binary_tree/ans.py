#!/usr/bin/env python
# coding=utf-8
"""
@desc:   判断是否是平衡二叉树
@author: luluo
@date:   2018-8-23

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        if root == None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if abs(self.maxDepth(root.left) - self.maxDepth(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

