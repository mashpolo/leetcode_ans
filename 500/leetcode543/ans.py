#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-11-24

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0

        def max_depth(node):
            if not node:
                return 0
            left = max_depth(node.left)
            right = max_depth(node.right)
            self.res = max(self.res, left + right)
            return max(left, right) + 1

        max_depth(root)
        return self.res


